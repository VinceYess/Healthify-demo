# Healthify prototype: developer source code
Latest handoff: 28 October 2026. Based on the public prototype at https://healthify-mobile-test.vercel.app/ (the centered-pagination version).

## Files
- `index.html`: entry point, loading `styles.css` and `app.js`.
- `styles.css`: complete responsive CSS.
- `app.js`: complete interaction and product data logic, including embedded product photography.
- `original-combined.html`: original working HTML with inline CSS/JS, for reference.
- `assets-manifest.json`: expected 10 original Figma media files with verified SHA-1 hashes and byte sizes.
- `download_assets.py`: retrieves GIF and 9 SVG assets from the public live prototype and verifies them.
- `run_local.py`: downloads missing assets, checks integrity, then serves the app locally.
- `vercel.json`: static Vercel configuration.

## Run locally
With Python 3 installed and internet access, from this folder:

```bash
python3 run_local.py
```

Then open http://localhost:8000/ on the same machine. To test from another device, change the server bind address in `run_local.py` to `0.0.0.0` and use the host's local IP, with due care for network access.

Alternatively:
```bash
python3 download_assets.py
python3 -m http.server 8000
```

## Deployment
Fetch assets first using `python3 download_assets.py`, then deploy the contents of this folder to a static web host or Vercel. Keep `styles.css`, `app.js`, and all 10 downloaded assets in the same web root as `index.html`. The prototype uses absolute `/asset.svg` paths and expects deployment at the domain root.

## Behaviour
- Animated analysis screen with progress text changing at ~3, 6 and 9 seconds; scan completes at ~10 seconds.
- Moving forward without a choice records `Behouden`.
- `Toon alle` is disabled until one product is recorded, then opens the summary screen.
- Original and alternative product images each show the matching Nutri-Score A–E SVG badge.
- Group of dots and `1/3` pagination label centered horizontally. `Toon alle` aligns independently to the right.
- Final success screen has confetti, basket entrance, Figma result illustration, summary cards, and fixed CTA.
- Demo reset and responsive UI for mobile and desktop preview.

## Implementation notes
This is a standalone HTML/CSS/JavaScript demo. It is not a Rive export or a native iOS app. The scan timing, products, prices, scores, and success screen are demo state/content. Before adding it to a production app, connect data, navigation, and ARIA accessibility to your own system.

Media are not embedded in this ZIP. This handoff includes a verified one-command downloader for the 10 original Figma files. A developer with internet access should run that command once and commit the downloaded media files to their internal code repository, so the working app no longer depends on the prototype URL.
