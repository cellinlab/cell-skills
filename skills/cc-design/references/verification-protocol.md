# Verification Protocol

> **Load when:** Reaching the Verify step (step 5) in the workflow, or preparing to deliver a final artifact
> **Skip when:** Still in the Build step iterating on intermediate changes
> **Why it matters:** Platform-native design tools run two-phase verification automatically. Without this protocol, defects slip through to delivery.
> **Typical failure it prevents:** Delivering artifacts with console errors, broken scaling, invisible text, or misaligned elements

If the current host exposes different tool names, use the equivalent browser preview, console-log, screenshot, and page-evaluate capabilities.

## Phase 1: Structural Verification

Run these checks first. Any failure = stop and fix before proceeding to Phase 2.

| Check | Method | Pass criteria | Fix if fail |
|-------|--------|---------------|-------------|
| Console errors | `browser_console_messages` (level: error) | 0 errors | Read error message, fix source, re-verify |
| Console warnings | `browser_console_messages` (level: warning) | 0 warnings about missing resources | Fix asset paths or missing imports |
| Layout structure | `browser_snapshot` | All expected elements present in accessibility tree | Check rendering conditions (display:none, conditional logic) |
| Fixed-size scaling | `browser_evaluate` — check deck_stage or stage transform | Content fills intended viewport without overflow | Verify transform:scale calculation, check container dimensions |
| Asset loading | `browser_evaluate` — check `document.querySelectorAll('[src],[href]')` | No broken links (404) | Fix relative paths, ensure assets exist |

### Console check command

```
browser_console_messages → level: error
browser_console_messages → level: warning
```

If Phase 1 has any failure: fix the issue, re-navigate the page, re-run Phase 1. Do not proceed to Phase 2 until Phase 1 passes clean.

## Phase 2: Visual Verification

Run these after Phase 1 passes. Requires human judgment via screenshot review.

| Check | Method | Pass criteria |
|-------|--------|---------------|
| Screenshot taken | `browser_take_screenshot` | Screenshot captured successfully |
| Typography | Visual check on screenshot | Headings distinct from body, no text < 12pt (print) or < 24px (1080p slides) |
| Alignment | Visual check on screenshot | Elements aligned to grid, no drift, consistent margins |
| Contrast | Visual check on screenshot | Text readable against background, no low-contrast pairs |
| Spacing | Visual check on screenshot | Consistent use of spacing tokens, no arbitrary gaps |
| Tweaks panel | Visual check (if applicable) | Tweaks toggle visible, panel functional, no UI artifacts when hidden |
| Content | Visual check on screenshot | No placeholder text left in, no filler content |

### Visual review flow

```
1. browser_take_screenshot → capture full page
2. Review screenshot against criteria above
3. If any criterion fails → fix in Build step, re-verify from Phase 1
4. If all pass → proceed to Deliver step
```

## Phase 3: Task-Specific Verification

After structural and visual checks, add the checks that match the artifact type:

| Artifact | Extra checks |
|---|---|
| Mobile / interactive prototype | Click through the core path once; verify state switches, navigation, and no dead buttons on the main route |
| Multi-option design board | Verify labels are visible and each option is genuinely different |
| Slide deck | Check first slide, one middle slide, and last slide; confirm scaling and readable type on all three |
| Exported asset | Verify the target file actually exists and matches the expected format |

For prototypes, do not stop at a static screenshot if the main value is interaction.

## Fix Loop

The verification loop is strict:

```
Phase 1 fail → fix → re-navigate → Phase 1 again
Phase 2 fail → fix → re-navigate → Phase 1 + Phase 2 again
```

Never skip Phase 1 to "just check visuals." Structural errors cause visual defects that are symptoms, not root causes.
