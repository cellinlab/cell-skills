#!/usr/bin/env node
/**
 * gen_pptx.js — Export HTML slide deck to PPTX
 *
 * Modes:
 *   --mode editable    → Parse HTML for text/shapes, create native PPTX elements
 *   --mode screenshots → Headless browser screenshots per slide, embed as images
 *
 * Usage:
 *   node gen_pptx.js --input slides.html --output deck.pptx
 *   node gen_pptx.js --input slides.html --output deck.pptx --mode screenshots
 */

const fs = require('fs');
const path = require('path');
const PptxGenJS = require('pptxgenjs');
const parseArgs = require('./lib/parse_args');

async function main() {
  const opts = parseArgs(process.argv, { input: '', output: 'output.pptx', mode: 'editable' });

  if (!opts.input) {
    console.error('Usage: node gen_pptx.js --input slides.html --output deck.pptx [--mode editable|screenshots]');
    process.exit(1);
  }

  const inputPath = path.resolve(opts.input);
  if (!fs.existsSync(inputPath)) {
    console.error(`Error: Input file not found: ${inputPath}`);
    process.exit(1);
  }

  const pptx = new PptxGenJS();
  pptx.layout = 'LAYOUT_WIDE'; // 13.33 x 7.5 inches (16:9)

  if (opts.mode === 'screenshots') {
    await exportScreenshots(pptx, inputPath);
  } else {
    await exportEditable(pptx, inputPath);
  }

  const outputPath = path.resolve(opts.output);
  await pptx.writeFile({ fileName: outputPath });
  console.log(`PPTX saved to: ${outputPath}`);
}

async function exportEditable(pptx, inputPath) {
  let chromium;
  try {
    const { chromium: pw } = require('playwright');
    chromium = pw;
  } catch {
    // Fallback to regex parsing if Playwright is not installed
    const html = fs.readFileSync(inputPath, 'utf-8');
    const slideRegex = /<section[^>]*>([\s\S]*?)<\/section>/gi;
    const slides = [];
    let match;
    while ((match = slideRegex.exec(html)) !== null) slides.push(match[1]);
    if (slides.length === 0) {
      console.error('No <section> elements found. Install Playwright for DOM-based parsing: npm install playwright');
      process.exit(1);
    }
    exportEditableRegex(pptx, slides);
    return;
  }

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto(`file://${inputPath}`);

  const slideData = await page.evaluate(() => {
    const sections = document.querySelectorAll('section');
    return Array.from(sections).map(sec => {
      const bg = sec.style.background || sec.style.backgroundColor || '';
      const headings = Array.from(sec.querySelectorAll('h1,h2,h3,h4,h5,h6')).map(h => ({
        level: parseInt(h.tagName[1]),
        text: h.textContent.trim()
      }));
      const paragraphs = Array.from(sec.querySelectorAll('p')).map(p => ({
        text: p.textContent.trim()
      }));
      return { bg, headings, paragraphs };
    });
  });

  for (const slideInfo of slideData) {
    const slide = pptx.addSlide();
    if (slideInfo.bg) {
      const bgColor = slideInfo.bg.replace('#', '').replace(/^rgb\(/, '').replace(/\)$/, '');
      slide.background = { color: bgColor };
    }
    let y = 0.5;
    for (const h of slideInfo.headings) {
      if (!h.text) continue;
      const fontSize = Math.max(18, 44 - (h.level - 1) * 6);
      slide.addText(h.text, { x: 0.5, y, w: '90%', h: 1, fontSize, bold: h.level <= 2, color: '333333', fontFace: 'system-ui' });
      y += 0.8;
    }
    for (const p of slideInfo.paragraphs) {
      if (!p.text) continue;
      slide.addText(p.text, { x: 0.5, y, w: '90%', h: 0.6, fontSize: 18, color: '555555', fontFace: 'system-ui' });
      y += 0.5;
    }
  }

  await browser.close();
}

function exportEditableRegex(pptx, slides) {
  for (const slideHtml of slides) {
    const slide = pptx.addSlide();

    // Extract text content
    const textRegex = /<h[1-6][^>]*>([\s\S]*?)<\/h[1-6]>/gi;
    const bodyTextRegex = /<p[^>]*>([\s\S]*?)<\/p>/gi;
    const bgRegex = /background(?:-color)?:\s*([^;]+)/i;

    // Try to extract background
    const bgMatch = slideHtml.match(bgRegex);
    if (bgMatch) {
      const bgColor = bgMatch[1].trim();
      slide.background = { color: bgColor.replace('#', '') };
    }

    // Extract headings
    let y = 0.5;
    let hMatch;
    const textRegex2 = /<h(\d)[^>]*>([\s\S]*?)<\/h\1>/gi;
    while ((hMatch = textRegex2.exec(slideHtml)) !== null) {
      const level = parseInt(hMatch[1]);
      const text = hMatch[2].replace(/<[^>]*>/g, '').trim();
      if (!text) continue;

      const fontSize = Math.max(18, 44 - (level - 1) * 6);
      slide.addText(text, {
        x: 0.5, y, w: '90%', h: 1,
        fontSize, bold: level <= 2,
        color: '333333',
        fontFace: 'system-ui',
      });
      y += 0.8;
    }

    // Extract paragraphs
    const pRegex = /<p[^>]*>([\s\S]*?)<\/p>/gi;
    let pMatch;
    while ((pMatch = pRegex.exec(slideHtml)) !== null) {
      const text = pMatch[1].replace(/<[^>]*>/g, '').trim();
      if (!text) continue;

      slide.addText(text, {
        x: 0.5, y, w: '90%', h: 0.6,
        fontSize: 18, color: '555555',
        fontFace: 'system-ui',
      });
      y += 0.5;
    }
  }
}

async function exportScreenshots(pptx, inputPath) {
  // Check if playwright is available
  let chromium;
  try {
    const { chromium: pw } = require('playwright');
    chromium = pw;
  } catch {
    console.error('Screenshots mode requires Playwright. Install with: npm install playwright && npx playwright install chromium');
    process.exit(1);
  }

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto(`file://${inputPath}`);

  // Navigate through slides and screenshot each
  const sections = await page.$$eval('section', (els) => els.length);
  for (let i = 0; i < sections; i++) {
    await page.evaluate((idx) => {
      const secs = document.querySelectorAll('section');
      secs.forEach((s, j) => s.style.display = j === idx ? '' : 'none');
    }, i);

    await page.waitForTimeout(200);
    const screenshot = await page.screenshot({ type: 'png' });

    const slide = pptx.addSlide();
    slide.addImage({ data: `image/png;base64,${screenshot.toString('base64')}`, x: 0, y: 0, w: '100%', h: '100%' });
  }

  await browser.close();
}

main().catch(console.error);
