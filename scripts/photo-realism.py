#!/usr/bin/env python3
"""Take the machine-generated sheen off an image.

Generated images give themselves away less through content than through physics:
every plane is equally sharp, highlights clip flat, there is no sensor noise and
no lens error. This adds back the artefacts a real camera cannot avoid - shallow
depth of field, lateral chromatic aberration, grain that follows luminance,
highlight rolloff and a little vignette.

It cannot fix a structural tell. Invented chart text, garbled signage and wrong
hands survive this untouched; those images need replacing, not filtering.

    python scripts/photo-realism.py in.png out.webp
    python scripts/photo-realism.py --strength 0.6 in.png out.webp
"""
import argparse
import numpy as np
from PIL import Image, ImageFilter


def _radial(h, w, power=2.0):
    y, x = np.mgrid[0:h, 0:w].astype(np.float32)
    cy, cx = (h - 1) / 2, (w - 1) / 2
    r = np.sqrt(((x - cx) / cx) ** 2 + ((y - cy) / cy) ** 2) / np.sqrt(2)
    return np.clip(r, 0, 1) ** power


def realism(img, strength=1.0, dof=1.9, grain=3.4, ca=1.0018,
            vign=0.10, roll=0.90, focus=0.42, seed=7):
    """Return a filtered copy. strength scales every effect together."""
    s = max(0.0, float(strength))
    dof, grain, vign = dof * s, grain * s, vign * s
    ca = 1.0 + (ca - 1.0) * s
    roll = 1.0 - (1.0 - roll) * s
    rng = np.random.default_rng(seed)
    w, h = img.size
    base = np.asarray(img.convert("RGB"), dtype=np.float32) / 255.0

    # lateral chromatic aberration: red scaled out, blue in, about the centre
    if abs(ca - 1.0) > 1e-6:
        chans = []
        for c, sc in zip(range(3), (ca, 1.0, 1.0 / ca)):
            layer = Image.fromarray((base[..., c] * 255).astype(np.uint8))
            nw, nh = max(1, int(round(w * sc))), max(1, int(round(h * sc)))
            layer = layer.resize((nw, nh), Image.LANCZOS)
            ox, oy = (nw - w) // 2, (nh - h) // 2
            chans.append(np.asarray(layer.crop((ox, oy, ox + w, oy + h)),
                                    dtype=np.float32) / 255.0)
        base = np.stack(chans, axis=-1)

    # depth of field: sharp through the middle, softening outward
    if dof > 0.01:
        blurred = np.asarray(
            Image.fromarray((np.clip(base, 0, 1) * 255).astype(np.uint8)
                            ).filter(ImageFilter.GaussianBlur(dof)),
            dtype=np.float32) / 255.0
        m = np.clip((_radial(h, w, 2.2) - focus) / (1 - focus), 0, 1)[..., None]
        base = base * (1 - m) + blurred * m

    # highlight rolloff: a sensor does not clip to a flat plate
    if roll < 0.999:
        base = np.where(base > roll, roll + (base - roll) / (1 + (base - roll) * 6), base)

    # grain: strongest in the midtones, barely there in the highlights
    if grain > 0.01:
        lum = base @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
        weight = (1 - np.abs(lum - 0.45) / 0.75).clip(0.25, 1)[..., None]
        n = rng.normal(0, 1.0, base.shape).astype(np.float32)
        n = np.asarray(Image.fromarray(
            ((n - n.min()) / (np.ptp(n) + 1e-9) * 255).astype(np.uint8)
        ).filter(ImageFilter.GaussianBlur(0.35)), dtype=np.float32)
        base = base + ((n / 255.0 - 0.5) * (grain / 255.0) * 3.2) * weight

    # vignette
    if vign > 0.001:
        base = base * (1 - vign * _radial(h, w, 2.6)[..., None])

    return Image.fromarray((np.clip(base, 0, 1) * 255).astype(np.uint8))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("src"); p.add_argument("dst")
    p.add_argument("--strength", type=float, default=1.0)
    a = p.parse_args()
    out = realism(Image.open(a.src), strength=a.strength)
    out.save(a.dst, quality=88, method=6)
    print("wrote", a.dst, out.size)
