# Platform Tool Reference

> **Load when:** Needing to export output (PPTX/PDF/inline HTML), mapping the current host's preview/screenshot tools, or verifying the preview workflow
> **Skip when:** Only building and previewing designs — no export needed
> **Why it matters:** Tool names are non-obvious and export scripts require specific setup; wrong tool names break the verification flow
> **Typical failure it prevents:** Using the wrong preview path, missing `npm install` for export scripts, or skipping console/screenshot verification

## Tool Mapping

Different hosts expose different names for preview, browser automation, and screenshot capture. Treat the table below as a capability map, not a hardcoded API contract.

| Need | Generic path | Typical implementation |
|---|---|---|
| Copy a starter scaffold | Shell copy | `cp skills/cc-design/assets/templates/...` or host scaffold-copy tool |
| Open preview | Browser preview | Playwright, host HTML preview, or system browser |
| Check console output | Browser console logs | Playwright console API or host log tool |
| Capture screenshots | Browser screenshot | Playwright screenshot or host screenshot tool |
| Export PPTX / PDF / self-contained HTML | Local scripts in `scripts/` | Equivalent built-in export tools, or the local scripts |

## Preview & Screenshots

| Need | Capability | Notes |
|---|---|---|
| Open HTML for preview | Browser navigate/open | Prefer `file:///absolute/path/to/file.html` |
| Take screenshot | Browser screenshot | Full-page or region screenshot both work |
| Check console errors | Browser console logs | Read errors and warnings before delivery |
| Execute JS in page | Browser evaluate | Useful for structure checks and layout state |
| Get page snapshot | DOM / accessibility snapshot | Better than screenshot for understanding structure |
| Run multi-step browser code | Browser automation | Use only when simple preview tools are insufficient |
| Open in system browser | Shell | macOS: `open <file>`, Linux: `xdg-open <file>` |

### Typical verification flow

```
1. Open the HTML file in a browser preview
2. Read console logs for errors/warnings
3. Take a screenshot and visually verify
4. Fix any issues, repeat
```

## Export Scripts

Scripts live in the skill's `scripts/` directory. First run requires `npm install`:

```bash
cd skills/cc-design/scripts && npm install && cd -
```

For Playwright-backed export flows, also install the browser binary:

```bash
npx playwright install chromium
```

### PPTX export

```bash
node skills/cc-design/scripts/gen_pptx.js --input slides.html --output deck.pptx --mode screenshots
# --mode editable   → native text & shapes
# --mode screenshots → flat images, pixel-perfect (requires Playwright)
```

### Inline HTML

```bash
node skills/cc-design/scripts/super_inline_html.js --input page.html --output page-inline.html
# Bundles HTML + all linked CSS/JS/images into a single self-contained file
```

### Print to PDF

```bash
node skills/cc-design/scripts/open_for_print.js --input page.html --output page.pdf
# Uses Playwright to render and export as PDF
```
