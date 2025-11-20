---
name: elimstat-brand-guidelines
description: Applies Elimstat.com's official brand colors and typography to any sort of artifact that may benefit from having Elimstat.com's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.
license: Complete terms in LICENSE.txt
---

# Elimstat Brand Style Guide

## Description
This skill provides comprehensive brand guidelines for Elimstat, covering logo usage, color systems, typography, and design standards for both print and web materials. Use this skill when creating any branded content, marketing materials, product documentation, or design assets for Elimstat.

## When to Use This Skill
- Creating or reviewing specification sheets and product documentation
- Designing web pages or updating the Elimstat website
- Writing marketing copy or email communications
- Designing branded apparel or promotional materials
- Ensuring brand consistency across any customer-facing materials
- Selecting colors, fonts, or logos for any Elimstat project

---

## Logo Usage Guidelines

### Available Logo Variations

#### 1. Ion Only
**File:** `ElimstatIon.jpg`
**Use for:**
- Print spec sheets (small spaces)
- Favicon and app icons
- Social media profile images
- Compact layouts where full logo won't fit

#### 2. Full Logo (Blue)
**File:** `ElimstatBlueSimple.png` or `Elimstat@0.5x.jpg`
**Use for:**
- General print materials
- Product labels
- Business cards and letterhead
- Documents and presentations (light backgrounds)

#### 3. White Logo (Reverse)
**File:** `ElimstatWhite.png`
**Use for:**
- Website header (dark backgrounds)
- Branded clothing and apparel
- Dark packaging
- Presentations with dark themes

#### 4. Lightning Bolt Version
**File:** `ElimstatBolts-BnB.webp`
**Use for:**
- Email signatures
- Quotes and proposals
- Digital communications
- Bennett & Bennett co-branding

### Logo Usage Rules
- **Clear space:** Minimum 20px around logo on all sides
- **Never** stretch, skew, or distort logo proportions
- **Minimum size:** 80px width (digital) or 0.75" (print)
- Use white logo on dark backgrounds
- Use blue logo on light backgrounds

---

## Color System

### Print Colors (Pantone System)

#### Primary Brand Color: Pantone 2748 UP
- **RGB:** 10, 48, 140
- **Hex:** #0A308C
- **CMYK:** 100, 83, 0, 32
- **Use:** All print materials, spec sheets, product documentation

#### Print Applications
| Application | Color Specification | Notes |
|------------|-------------------|-------|
| Spec Sheet Headers | Pantone 2748 UP | Headers, graphic lines, section dividers |
| Body Text | Black (100K) | All body copy, descriptions, specifications |
| Table Headers | Pantone 2748 UP | White text on blue background |
| Backgrounds | 10% tint of Pantone 2748 UP | Highlight boxes, alternating table rows |

**Important:** For critical color matching in print, always use Pantone spot color. CMYK values are approximations for 4-color process printing.

### Web Colors (RGB/Hex System)

#### Primary Palette
| Color Name | Hex | RGB | Use |
|-----------|-----|-----|-----|
| **Primary Blue** | #184187 | 24, 65, 135 | Navigation, headers, titles |
| **Light Blue** | #e6f5ff | 230, 245, 255 | Backgrounds, widgets, menus |
| **Medium Blue** | #4da6ff | 77, 166, 255 | Hover states, current items |
| **Bright Blue** | #0170bc | 1, 112, 188 | Accent elements |
| **Google Blue** | #4285f4 | 66, 133, 244 | Links, borders, accents |

#### Accent Colors
| Color Name | Hex | RGB | Use |
|-----------|-----|-----|-----|
| **Coral** | #f4a792 | 244, 167, 146 | Navigation hover |
| **Orange** | #bc4d00 | 188, 77, 0 | General hover states |
| **Category Blue** | #1e73be | 30, 115, 190 | Category headings |
| **Button Blue** | #3899ff | 56, 153, 255 | Call-to-action buttons |
| **Hover Blue** | #3a7bce | 58, 123, 206 | Button hover states |

#### CSS Variables
```css
--primary-blue: #184187;
--light-blue: #e6f5ff;
--medium-blue: #4da6ff;
--bright-blue: #0170bc;
--google-blue: #4285f4;
--coral: #f4a792;
--orange: #bc4d00;
--category-blue: #1e73be;
--button-blue: #3899ff;
--hover-blue: #3a7bce;
```

---

## Typography System

### Print Typography

| Element | Font | Size | Leading | Tracking | Use |
|---------|------|------|---------|----------|-----|
| **Document Title** | Helvetica Bold | 18pt | Auto | Default | Main header |
| **Series Title** | Museo Sans / Proxima Nova | 14pt | Auto | Default | Product series |
| **Section Headers** | Museo Sans 700 | 13.2pt | 15.84pt | Default | Major sections |
| **Product IDs** | Museo Sans 900 | 12pt | 18pt | 10pt | Model numbers |
| **Body Text** | Museo Sans 100 | 12pt | 18pt | 10pt | Primary text |
| **Emphasis** | Museo Sans 900 | 12pt | 18pt | 10pt | Bold/important text |
| **Footnotes** | Museo Sans | 10pt | 12pt | Default | Tolerances, notes |

#### InDesign Keyboard Shortcuts
- `Option + Command + 1` — Hair space (fine-tuning)
- `Option + Command + 6` — En space (tables and aligned text)
- `~` — Sixth space (bullet point spacing)

### Web Typography

| Element | Font Family | Size | Weight | Use |
|---------|------------|------|--------|-----|
| **Page Titles (H1)** | Source Sans Pro | 150% / 1.5em | Bold (700) | Main page headings |
| **Category Titles (H2)** | Source Sans Pro | 170% / 1.7em | Bold (700) | Product categories |
| **Navigation Menu** | System Default | 1.3em | Normal (400) | Main navigation |
| **Body Text** | System Default | 1em (16px base) | Normal (400) | General content |
| **Product Descriptions** | System Default | 1.2em | Normal (400) | Product details |
| **Footer** | System Default | 1.3em | Normal (400) | Footer content |

#### Web Font Stack
```css
font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
```

---

## Compliance Standards

### Required Compliance Statement
**Standard text for all spec sheets:**
> "This product meets the ANSI/ESD S20.20 STM S4.1 Standard using FTMS 101C Method 4046. Material is Lead-Free. RoHS Compliant."

### Industry Standards to Reference
- **ANSI/ESD S20.20** — Electrostatic Discharge Control Program Standard
- **STM S4.1** — Worksurfaces Resistance Measurements
- **FTMS 101C Method 4046** — Federal Test Method Standard
- **RoHS Compliance** — Restriction of Hazardous Substances Directive
- **Lead-Free Certification** — Federal compliance for lead content

---

## Standard Document Structure

### Spec Sheet Section Order
1. **Document Title** — Product name and series identifier (Helvetica Bold 18pt)
2. **Product Description** — Overview paragraph with key features
3. **Physical Properties** — Material, dimensions, weight, color options
4. **Electrical Properties** — Resistance specifications, static decay rates
5. **Specifications Table** — Detailed technical data using Bennett Table Style
6. **Standards & Compliance** — ANSI/ESD references, RoHS, Lead-Free certification
7. **Testing Procedures** — General test procedures (when applicable)
8. **Material Handling** — Application instructions (when applicable)

---

## Required Graphic Elements

### Print Materials
- **Blue Graphic Line 2** — Header decoration (.ai vector format) in Pantone 2748 UP
- **Blue Line Footer** — Footer graphic element (.ai vector format) in Pantone 2748 UP
- **Elimstat Logo** — Appropriate version (0.25x or 0.5x for spec sheets)
- **Bennett Table Style** — Standardized table formatting

### Web Materials
- **Logo Hover Effect** — White outer glow on hover (CSS filter property)
- **Responsive Design** — 768px mobile/desktop breakpoint
- **Color Consistency** — Use CSS variables for all brand colors

---

## Brand Consistency Checklist

### Print Materials
- ✓ Helvetica Bold 18pt for document title
- ✓ Pantone 2748 UP blue applied correctly
- ✓ Museo Sans used for body text
- ✓ Blue Graphic Line 2 in header
- ✓ Blue Line Footer at bottom
- ✓ Appropriate logo version (0.25x or 0.5x)
- ✓ Bennett Table Style applied
- ✓ Compliance statements included
- ✓ ANSI/ESD standards referenced
- ✓ RoHS compliance noted

### Web Materials
- ✓ White logo on dark header background
- ✓ Primary blue (#184187) for navigation
- ✓ Source Sans Pro for headings
- ✓ Google blue (#4285f4) for links
- ✓ Coral hover effects on navigation
- ✓ Light blue backgrounds for widgets
- ✓ Logo hover effect enabled
- ✓ Responsive design implemented
- ✓ Accessibility standards met (WCAG AA)
- ✓ Consistent spacing and alignment

---

## Technical Specifications

### Print Specifications
- **Recommended Printer:** HP Color LaserJet CP1215 or equivalent
- **Color Management:** Enabled, match to Pantone
- **Color Mode:** CMYK for print
- **Spot Color:** Pantone 2748 UP (when available)
- **Paper:** Uncoated white stock for Pantone accuracy

### Web Specifications
- **Color Space:** RGB (sRGB IEC61966-2.1)
- **Logo Format:** WebP for general use, PNG for header
- **Responsive Breakpoints:** 768px (mobile/desktop)
- **Browser Support:** Modern browsers with graceful degradation
- **Accessibility:** WCAG AA compliant color contrast
- **Website CSS:** ELIMSTAT0718.CSS (WordPress)

---

## File Locations & Resources

- **Master Template:** Google Drive / BNB Content / QC Data
- **Backup Location:** Dropbox / Elimstat Data / Product Specifications
- **Graphic Assets:** Style Guide folder / Creative Cloud
- **Website CSS:** ELIMSTAT0718.CSS (WordPress)
- **Logo Files:** Available in multiple formats across brand folders

---

## Usage Instructions for Claude

When this skill is active, Claude should:

1. **Reference specific guidelines** when asked about colors, fonts, or logos
2. **Validate designs** against the checklist items
3. **Suggest corrections** when materials don't match brand standards
4. **Quote exact specifications** (hex codes, font sizes, etc.) rather than approximating
5. **Recommend appropriate logo versions** based on the use case
6. **Include compliance statements** when creating technical documentation
7. **Use the standard document structure** for spec sheets
8. **Apply web color variables** for digital content
9. **Maintain brand voice** — professional, technical, precise

---

**Version 2.0** | November 11, 2025
© 2025 Elimstat.com — All Rights Reserved

