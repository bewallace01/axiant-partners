/**
 * POST /.netlify/functions/apply  →  https://jyni.io/api/inbound/website
 *
 * The CRM's intake route authenticates with `x-intake-key: $CRM_INTAKE_SHARED_KEY`.
 * This site is static, so it has nowhere to keep that secret — in client-side JS
 * it would be published, and anyone could then write leads into the CRM. The route
 * also sets no CORS headers, so a direct browser POST from axiantpartners.com would
 * be blocked regardless.
 *
 * Hence this proxy: browser → here → CRM. The key stays in a Netlify env var, the
 * hop to the CRM is server-to-server so CORS never arises, and the CRM is untouched.
 *
 * .mjs, not .js, deliberately: package.json has no "type": "module", so a .js file
 * using ESM syntax would be loaded as CommonJS and fail at parse time.
 *
 * ── SERVER-SIDE CONVERSIONS ────────────────────────────────────────────────────
 * This function is also where the Meta and OpenAI conversion events are reported
 * server-side, because it is the one place that sees every completed application
 * from a server. Browser pixels lose events to ad blockers and Safari's ITP; these
 * calls never touch the browser.
 *
 * Both vendors deduplicate against the browser pixel by event id, and BOTH SIDES
 * USE THE APPLICATION'S REFERENCE NUMBER as that id (`AXP-…`, generated in
 * script.js). So one application counts once no matter how many of the paths
 * survive, and the same string appears in the CRM, in Meta and in OpenAI — which is
 * what makes a disputed conversion traceable months later.
 *
 * Nothing here can break the lead: every vendor call is wrapped, time-limited, and
 * its outcome is logged rather than returned. If a vendor's key is unset the call
 * is skipped, so this file is safe to deploy before the keys exist.
 */

const CRM_ENDPOINT = "https://jyni.io/api/inbound/website";

// Not secrets — both ids already appear in the page source of every page.
const META_PIXEL_ID = "1269109058680441";
const META_API_VERSION = "v25.0";
const OPENAI_PIXEL_ID = "F5EEdLVA6WthrKjN3WYkKc";

// Well under the CRM's own budget, so a slow vendor can never be the thing that
// makes this function time out.
const VENDOR_TIMEOUT_MS = 4_000;

/**
 * Hashed email / phone / name are what let a vendor match a conversion for someone
 * who arrived without a click cookie. The site's privacy policy covers this: it
 * permits disclosure to third parties for "marketing and advertising" and for
 * "creating user profiles". Set AX_CONVERSIONS_SHARE_IDENTITY=0 to send only the
 * click identifiers (fbc/fbp/oppref/obref) and drop every personal field — click
 * attribution still works, match rate drops.
 */
function shareIdentity() {
  return Netlify.env.get("AX_CONVERSIONS_SHARE_IDENTITY") !== "0";
}

/* ── hashing and normalisation ─────────────────────────────────────────────────
   Meta and OpenAI specify the same rules, so one set of helpers serves both.
   Web Crypto rather than node:crypto — it needs no import and would still work if
   this ever moved to an edge runtime. */

const encoder = new TextEncoder();

async function sha256Hex(value) {
  const digest = await crypto.subtle.digest("SHA-256", encoder.encode(value));
  return Array.from(new Uint8Array(digest), (b) => b.toString(16).padStart(2, "0")).join("");
}

/** Trim, lowercase. Null for anything not plausibly an address: a hash of junk is
 *  worse than no field, because it counts against the vendor's match quality. */
function normaliseEmail(value) {
  const email = String(value || "").trim().toLowerCase();
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) ? email : null;
}

/**
 * Digits only, country code kept, leading zeroes dropped, 8-15 digits.
 * The form collects US numbers without a country code, so a bare 10-digit number
 * gets a "1" — without it the hash matches nothing at either vendor.
 */
function normalisePhone(value) {
  let digits = String(value || "").replace(/\D/g, "").replace(/^0+/, "");
  if (digits.length === 10) digits = `1${digits}`;
  return digits.length >= 8 && digits.length <= 15 ? digits : null;
}

/** Lowercase, strip punctuation and spacing, keep accented letters. */
function normaliseName(value) {
  const name = String(value || "").toLowerCase().replace(/[^\p{L}\p{N}]/gu, "");
  return name || null;
}

/** First and last token of a full name. A one-word name gives nothing to match on. */
function splitName(fullName) {
  const parts = String(fullName || "").trim().split(/\s+/).filter(Boolean);
  if (parts.length < 2) return { first: null, last: null };
  return { first: parts[0], last: parts[parts.length - 1] };
}

function parseCookies(header) {
  const jar = {};
  for (const part of String(header || "").split(";")) {
    const eq = part.indexOf("=");
    if (eq > 0) jar[part.slice(0, eq).trim()] = part.slice(eq + 1).trim();
  }
  return jar;
}

/**
 * Meta's click identifier. The `_fbc` cookie is authoritative; when it is missing
 * (cookies blocked, or the click landed before the pixel ran) Meta's documented
 * fallback is to build it from the fbclid, which script.js forwards in the body.
 */
function resolveFbc(cookies, fbclid) {
  if (cookies._fbc) return cookies._fbc;
  if (fbclid) return `fb.1.${Date.now()}.${fbclid}`;
  return null;
}

/** SHA-256 every non-null input, in parallel. */
function hashAll(values) {
  return Promise.all(values.map((v) => (v == null ? null : sha256Hex(v))));
}

/* ── vendor dispatch ───────────────────────────────────────────────────────── */

async function sendMetaConversion(ctx) {
  const token = Netlify.env.get("META_CAPI_TOKEN");
  if (!token) return "skipped (META_CAPI_TOKEN unset)";

  const user_data = {};
  if (ctx.ip) user_data.client_ip_address = ctx.ip;
  if (ctx.userAgent) user_data.client_user_agent = ctx.userAgent;

  const fbc = resolveFbc(ctx.cookies, ctx.body.fbclid);
  if (fbc) user_data.fbc = fbc;
  if (ctx.cookies._fbp) user_data.fbp = ctx.cookies._fbp;

  if (shareIdentity()) {
    const { first, last } = splitName(ctx.body.name);
    const [em, ph, fn, ln] = await hashAll([
      normaliseEmail(ctx.body.email),
      normalisePhone(ctx.body.phone),
      normaliseName(first),
      normaliseName(last),
    ]);
    if (em) user_data.em = [em];
    if (ph) user_data.ph = [ph];
    if (fn) user_data.fn = [fn];
    if (ln) user_data.ln = [ln];
  }

  // No custom_data. An individual's requested loan amount and credit band are
  // exactly the "financial information" Meta's Business Tools Terms restrict, and
  // the Lead event optimises perfectly well without them.
  const payload = {
    data: [
      {
        event_name: "Lead",
        event_time: ctx.eventTimeSeconds,
        event_id: ctx.eventId,
        action_source: "website",
        event_source_url: ctx.body.page_url || undefined,
        user_data,
      },
    ],
  };

  const testCode = Netlify.env.get("META_CAPI_TEST_EVENT_CODE");
  if (testCode) payload.test_event_code = testCode;

  const res = await fetch(
    `https://graph.facebook.com/${META_API_VERSION}/${META_PIXEL_ID}/events` +
      `?access_token=${encodeURIComponent(token)}`,
    {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(payload),
      signal: AbortSignal.timeout(VENDOR_TIMEOUT_MS),
    },
  );
  const text = await res.text();
  if (!res.ok) throw new Error(`${res.status} ${text.slice(0, 300)}`);
  return `ok ${text.slice(0, 200)}`;
}

async function sendOpenAiConversion(ctx) {
  const apiKey = Netlify.env.get("OPENAI_ADS_API_KEY");
  if (!apiKey) return "skipped (OPENAI_ADS_API_KEY unset)";

  const user = {};
  if (ctx.ip) user.ip_address = ctx.ip;
  if (ctx.userAgent) user.user_agent = ctx.userAgent;
  if (ctx.cookies.__obref) user.obref = ctx.cookies.__obref;

  if (shareIdentity()) {
    const { first, last } = splitName(ctx.body.name);
    const [em, ph, fn, ln] = await hashAll([
      normaliseEmail(ctx.body.email),
      normalisePhone(ctx.body.phone),
      normaliseName(first),
      normaliseName(last),
    ]);
    if (em) user.emails_sha256 = [em];
    if (ph) user.phone_numbers_sha256 = [ph];
    if (fn) user.first_names_sha256 = [fn];
    if (ln) user.last_names_sha256 = [ln];
  }

  const event = {
    id: ctx.eventId,
    type: "lead_created",
    timestamp_ms: ctx.eventTimeSeconds * 1000,
    action_source: "web",
    data: { type: "customer_action" },
    user,
  };
  if (ctx.body.page_url) event.source_url = ctx.body.page_url;
  if (ctx.cookies.__oppref) event.oppref = ctx.cookies.__oppref;

  // One bad event rejects the whole batch, so AX_CONVERSIONS_VALIDATE_ONLY=1 gives
  // a way to prove the payload is accepted without writing a conversion.
  const payload = {
    events: [event],
    validate_only: Netlify.env.get("AX_CONVERSIONS_VALIDATE_ONLY") === "1",
  };

  const res = await fetch(
    `https://bzr.openai.com/v1/events?pid=${encodeURIComponent(OPENAI_PIXEL_ID)}`,
    {
      method: "POST",
      headers: { authorization: `Bearer ${apiKey}`, "content-type": "application/json" },
      body: JSON.stringify(payload),
      signal: AbortSignal.timeout(VENDOR_TIMEOUT_MS),
    },
  );
  const text = await res.text();
  if (!res.ok) throw new Error(`${res.status} ${text.slice(0, 300)}`);
  return `ok ${text.slice(0, 200)}`;
}

/* ── handler ───────────────────────────────────────────────────────────────── */

export default async (req) => {
  if (req.method !== "POST") {
    return Response.json({ ok: false, error: "Method not allowed" }, { status: 405 });
  }

  const key = Netlify.env.get("CRM_INTAKE_SHARED_KEY");
  if (!key) {
    // The CRM answers 503 for the same reason; say so here rather than sending an
    // unauthenticated request that comes back as an opaque 401.
    console.error("[apply] CRM_INTAKE_SHARED_KEY is not set on this site");
    return Response.json({ ok: false, error: "Intake not configured" }, { status: 503 });
  }

  let body;
  try {
    body = await req.json();
  } catch {
    return Response.json({ ok: false, error: "Invalid JSON" }, { status: 400 });
  }

  /* Conversions are reported for completed applications only. Partial captures are
     people who typed a name and left; counting them would teach both optimisers to
     buy abandoners. The reference number doubles as the dedup key, so without one
     there is nothing to deduplicate against and the browser pixel must stand alone
     rather than risk double-counting. */
  const eventId = typeof body.referenceNumber === "string" ? body.referenceNumber : null;
  const reportConversion =
    Boolean(eventId) && body.partial !== true && body.lead_type !== "partial";

  // Started before the CRM call and awaited after it, so the hops overlap rather
  // than add up.
  let conversions = null;
  if (reportConversion) {
    const ctx = {
      body,
      eventId,
      eventTimeSeconds: Math.floor(Date.now() / 1000),
      cookies: parseCookies(req.headers.get("cookie")),
      ip:
        req.headers.get("x-nf-client-connection-ip") ||
        (req.headers.get("x-forwarded-for") || "").split(",")[0].trim() ||
        null,
      userAgent: req.headers.get("user-agent") || null,
    };
    conversions = Promise.allSettled([sendMetaConversion(ctx), sendOpenAiConversion(ctx)]);
  }

  /** Never throws. Vendor outcomes belong in the logs, not the public response. */
  const settleConversions = async () => {
    if (!conversions) return;
    try {
      const [meta, openai] = await conversions;
      for (const [name, result] of [["meta", meta], ["openai", openai]]) {
        if (result.status === "fulfilled") console.log(`[apply] ${name} capi ${result.value}`);
        else console.error(`[apply] ${name} capi failed:`, result.reason?.message || result.reason);
      }
    } catch (err) {
      console.error("[apply] conversion reporting threw:", err?.message || err);
    }
  };

  let res;
  try {
    res = await fetch(CRM_ENDPOINT, {
      method: "POST",
      headers: { "content-type": "application/json", "x-intake-key": key },
      body: JSON.stringify(body),
      // The CRM route declares maxDuration 30; give up before the function does so
      // a hung upstream returns a clean 504 rather than a platform timeout page.
      signal: AbortSignal.timeout(25_000),
    });
  } catch (err) {
    console.error("[apply] CRM unreachable:", err?.name || err);
    // The application still happened, so the conversions are still real. Awaited
    // here too, or this early return would abandon them mid-flight.
    await settleConversions();
    return Response.json({ ok: false, error: "Upstream unavailable" }, { status: 504 });
  }

  // Upstream detail is logged, not returned: this endpoint is public, and the CRM's
  // error text is for us. The site only needs to know whether the lead landed.
  const text = await res.text();
  if (!res.ok) console.error(`[apply] CRM ${res.status}: ${text.slice(0, 500)}`);

  await settleConversions();

  return Response.json({ ok: res.ok }, { status: res.status });
};
