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
 */

const CRM_ENDPOINT = "https://jyni.io/api/inbound/website";

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
    return Response.json({ ok: false, error: "Upstream unavailable" }, { status: 504 });
  }

  // Upstream detail is logged, not returned: this endpoint is public, and the CRM's
  // error text is for us. The site only needs to know whether the lead landed.
  const text = await res.text();
  if (!res.ok) console.error(`[apply] CRM ${res.status}: ${text.slice(0, 500)}`);

  return Response.json({ ok: res.ok }, { status: res.status });
};
