---
name: elimstat-price-brackets
description: Creates standardized price bracket documents for Elimstat products with proper brand styling, table formatting, and pricing display. Use when generating quotes, pricing sheets, or customer-facing pricing materials.
license: Complete terms in LICENSE.txt
---

# Elimstat Price Bracket Style Guide

## Description
This skill provides comprehensive guidelines and templates for creating standardized price bracket documents (PDF and PNG) for Elimstat products. Use this skill when creating pricing materials, quotes, proposals, or any customer-facing documents that display product pricing in a professional, branded format.

## When to Use This Skill
- Creating price sheets for quotes and proposals
- Generating customer-facing pricing documents
- Designing pricing tables for products
- Updating existing price bracket materials
- Ensuring brand consistency in pricing communications
- Creating both PDF and PNG versions of pricing materials
- Formatting multi-tier pricing (quantity breaks)

---

## Document Specifications

### Page Format
- **Size:** US Letter (8.5" × 11")
- **Orientation:** Portrait
- **Resolution (PNG):** 300 DPI
- **Margins:** 1 inch (72 points) on all sides
- **Background:** White (#FFFFFF)

### File Naming Convention
```
[Product_Name]_Price_Brackets.[pdf|png]
```
**Examples:**
- `ESD_Mat_Roll_Price_Brackets.pdf`
- `Wrist_Strap_Price_Brackets.png`

---

## Brand Colors

### Primary Colors
| Color Name | Hex Code | RGB | Usage |
|-----------|----------|-----|-------|
| **Primary Blue** | #184187 | 24, 65, 135 | Title text, borders, footer text |
| **Table Header Blue** | #0A308C | 10, 48, 140 | Table header background (Pantone 2748 UP) |
| **Light Blue** | #e6f5ff | 230, 245, 255 | Alternating table row backgrounds |
| **White** | #FFFFFF | 255, 255, 255 | Page background, table data rows |
| **Black** | #000000 | 0, 0, 0 | Table data text |

### CSS/Python Constants
```css
--primary-blue: #184187;
--table-header-blue: #0A308C;
--light-blue: #e6f5ff;
```

```python
PRIMARY_BLUE = colors.HexColor('#184187')
TABLE_HEADER_BLUE = colors.HexColor('#0A308C')
LIGHT_BLUE = colors.HexColor('#e6f5ff')
```

---

## Logo Specifications

### Logo Requirements
- **File:** `ElimstatBlueSimple.png`
- **Location:** Top center of document
- **Width:** 2.5 inches
- **Height:** 0.7 inches (maintains aspect ratio)
- **Space Below Logo:** 0.3 inches

### Logo Placement Diagram
```
┌─────────────────────────────┐
│  Top Margin: 1.0"           │
│         [LOGO]              │ ← 2.5" × 0.7"
│         0.3" space          │
└─────────────────────────────┘
```

---

## Typography System

### Document Title
- **Font:** Helvetica Bold
- **Size:** 24pt
- **Color:** Primary Blue (#184187)
- **Alignment:** Center
- **Space Below:** 0.4 inches
- **Format:** `[Product Name] Price Brackets`

### Table Typography

#### Header Row
- **Font:** Helvetica Bold
- **Size:** 14pt
- **Color:** White (#FFFFFF)
- **Background:** Table Header Blue (#0A308C)
- **Padding:** 16pt top and bottom
- **Alignment:** Center

#### Data Rows
- **Font (Column 1 - Sizes):** Helvetica Bold
- **Font (Columns 2+ - Prices):** Helvetica Regular
- **Size:** 12pt
- **Color:** Black (#000000)
- **Padding:** 12pt top and bottom
- **Alignment:** Center

### Footer Text
- **Font:** Helvetica Regular
- **Size:** 10pt
- **Color:** Primary Blue (#184187)
- **Alignment:** Center
- **Space Above:** 0.5 inches from table
- **Line Spacing:** Single line break between lines

---

## Table Specifications

### Table Structure
- **Total Width:** 6.5 inches (fits within margins)
- **Position:** Center-aligned on page

### Column Widths by Table Type

#### 2-Column Pricing
| Column | Width | Content |
|--------|-------|---------|
| Column 1 | 2.5" | Product sizes/dimensions |
| Column 2 | 4.0" | Single price tier |

#### 3-Column Pricing (Standard)
| Column | Width | Content |
|--------|-------|---------|
| Column 1 | 2.5" | Product sizes/dimensions |
| Column 2 | 2.0" | Lower quantity pricing |
| Column 3 | 2.0" | Higher quantity pricing |

#### 4-Column Pricing
| Column | Width | Content |
|--------|-------|---------|
| Column 1 | 2.5" | Product sizes/dimensions |
| Column 2 | 1.33" | Qty tier 1 |
| Column 3 | 1.33" | Qty tier 2 |
| Column 4 | 1.34" | Qty tier 3 |

### Table Styling

#### Borders
- **Grid Lines:** 1pt solid Primary Blue (#184187)
- **Header Bottom Border:** 2pt solid Primary Blue (#184187)

#### Row Backgrounds (Alternating Pattern)
```
Row 0 (Header):    Table Header Blue (#0A308C)
Row 1 (Data):      White (#FFFFFF)
Row 2 (Data):      Light Blue (#e6f5ff)
Row 3 (Data):      White (#FFFFFF)
Row 4 (Data):      Light Blue (#e6f5ff)
[Continue alternating...]
```

#### Cell Padding
- **Horizontal:** 8pt left and right
- **Vertical (Data):** 12pt top and bottom
- **Vertical (Header):** 16pt top and bottom

---

## Layout Structure

### Complete Layout Diagram
```
┌────────────────────────────────────┐
│  Top Margin: 1.0"                  │
│                                    │
│  [Elimstat Logo]                   │ ← 2.5" × 0.7"
│                                    │
│  Space: 0.3"                       │
│                                    │
│  [Document Title]                  │ ← 24pt Helvetica Bold
│                                    │
│  Space: 0.4"                       │
│                                    │
│  ┌──────────────────────────┐     │
│  │  Sizes  │  Qty 1-9  │ 10+ │     │ ← Header (#0A308C)
│  ├──────────────────────────┤     │
│  │  24" x 50' │ $443.78 │ $406 │     │ ← White row
│  ├──────────────────────────┤     │
│  │  30" x 50' │ $554.72 │ $508 │     │ ← Light blue row
│  └──────────────────────────┘     │
│                                    │
│  Space: 0.5"                       │
│                                    │
│  Phone | Fax | Email               │ ← 10pt Helvetica
│  Physical Address                  │
│                                    │
│  Bottom Margin: 1.0"               │
└────────────────────────────────────┘
```

---

## Contact Information Footer

### Standard Format

**Line 1:**
```
Phone: (937) 993-0300  |  Fax: (937) 324-8753  |  Email: sales@elimstat.com
```

**Line 2:**
```
888 Dayton Street Suite 105, Yellow Springs, Ohio 45387
```

### Footer Specifications
- **Separator:** Vertical pipe (|) with spaces: ` | `
- **Font:** Helvetica Regular
- **Size:** 10pt
- **Color:** Primary Blue (#184187)
- **Alignment:** Center
- **Spacing:** Single line break between Line 1 and Line 2
- **Position:** 0.5 inches below table

---

## Data Format Standards

### Size/Dimension Column Format
- **Format:** `[Width]" x [Length]'`
- **Examples:** 
  - `24" x 50'`
  - `36" x 40'`
- **Font Weight:** Bold
- **Notes:** Use straight quotation marks for inches ("), apostrophe for feet (')

### Quantity Headers Format
- **Format:** `Qty [range]`
- **Examples:** 
  - `Qty 1-9`
  - `Qty 10+`
  - `Qty 25-49`
  - `Qty 50+`
- **Font Weight:** Bold
- **Color:** White (on blue header background)

### Price Format
- **Format:** `$[amount] USD`
- **Examples:** 
  - `$443.78 USD`
  - `$1,234.56 USD`
  - `$99.99 USD`
- **Rules:**
  - Always 2 decimal places
  - Dollar sign ($) prefix
  - Always include "USD" suffix
  - Use comma separator for amounts ≥ $1,000
  - Font weight: Regular (not bold)

---

## Python Template Code

### ReportLab PDF Implementation
```python
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

# Brand colors
PRIMARY_BLUE = colors.HexColor('#184187')
LIGHT_BLUE = colors.HexColor('#e6f5ff')
TABLE_HEADER_BLUE = colors.HexColor('#0A308C')

def create_price_bracket_pdf(product_name, pricing_data, output_path):
    # Create document with 1" margins
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    elements = []
    
    # Logo (2.5" x 0.7")
    logo = Image(logo_path, width=2.5*inch, height=0.7*inch)
    elements.append(logo)
    elements.append(Spacer(1, 0.3*inch))
    
    # Title (24pt Helvetica Bold, Primary Blue)
    title_style = ParagraphStyle(
        'CustomTitle',
        fontSize=24,
        textColor=PRIMARY_BLUE,
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    title = Paragraph(f'{product_name} Price Brackets', title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.4*inch))
    
    # Table with brand styling
    num_cols = len(pricing_data[0])
    col_widths = [2.5*inch] + [2*inch] * (num_cols - 1)
    table = Table(pricing_data, colWidths=col_widths)
    
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 16),
        ('TOPPADDING', (0, 0), (-1, 0), 16),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, PRIMARY_BLUE),
        ('LINEBELOW', (0, 0), (-1, 0), 2, PRIMARY_BLUE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT_BLUE]),
    ]))
    
    elements.append(table)
    elements.append(Spacer(1, 0.5*inch))
    
    # Footer (10pt Helvetica, Primary Blue)
    footer_style = ParagraphStyle(
        'Footer',
        fontSize=10,
        textColor=PRIMARY_BLUE,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    footer_text = '''Phone: (937) 993-0300  |  Fax: (937) 324-8753  |  Email: sales@elimstat.com<br/>
    888 Dayton Street Suite 105, Yellow Springs, Ohio 45387'''
    footer = Paragraph(footer_text, footer_style)
    elements.append(footer)
    
    doc.build(elements)
    return output_path
```

### Matplotlib PNG Implementation
```python
import matplotlib.pyplot as plt
from PIL import Image as PILImage

def create_price_bracket_png(product_name, pricing_data, output_path):
    # Create figure (8.5" x 11" at 300 DPI)
    fig, ax = plt.subplots(figsize=(11, 8.5), dpi=300)
    ax.axis('off')
    
    # Logo placement
    logo = PILImage.open(logo_path)
    ax.imshow(logo, aspect='auto', extent=[0.15, 0.65, 0.85, 0.95])
    
    # Title (28pt, bold, Primary Blue)
    ax.text(0.5, 0.78, f'{product_name} Price Brackets', 
            ha='center', va='center', 
            fontsize=28, fontweight='bold',
            color='#184187')
    
    # Table
    table = ax.table(
        cellText=pricing_data, 
        cellLoc='center',
        bbox=[0.15, 0.25, 0.7, 0.45],
        colWidths=[0.3, 0.35, 0.35]
    )
    
    # Style header row
    for i in range(len(pricing_data[0])):
        cell = table[(0, i)]
        cell.set_facecolor('#0A308C')
        cell.set_text_props(weight='bold', color='white', fontsize=14)
    
    # Style data rows with alternating colors
    for i in range(1, len(pricing_data)):
        for j in range(len(pricing_data[0])):
            cell = table[(i, j)]
            cell.set_facecolor('#e6f5ff' if i % 2 == 0 else 'white')
            if j == 0:
                cell.set_text_props(weight='bold')
    
    # Footer
    ax.text(0.5, 0.12, 
            'Phone: (937) 993-0300  |  Fax: (937) 324-8753  |  Email: sales@elimstat.com', 
            ha='center', fontsize=10, color='#184187')
    ax.text(0.5, 0.08, 
            '888 Dayton Street Suite 105, Yellow Springs, Ohio 45387', 
            ha='center', fontsize=10, color='#184187')
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight', 
               facecolor='white', edgecolor='none')
    plt.close()
    
    return output_path
```

---

## Example Pricing Data Structures

### 2-Column Example (Single Price)
```python
pricing_data = [
    ['Sizes', 'Price (Each)'],
    ['24" x 50\'', '$443.78 USD'],
    ['30" x 50\'', '$554.72 USD'],
    ['36" x 50\'', '$665.66 USD']
]
```

### 3-Column Example (Quantity Break)
```python
pricing_data = [
    ['Sizes', 'Qty 1-9', 'Qty 10+'],
    ['24" x 50\'', '$443.78 USD', '$406.80 USD'],
    ['30" x 50\'', '$554.72 USD', '$508.49 USD'],
    ['36" x 50\'', '$665.66 USD', '$610.19 USD'],
    ['48" x 50\'', '$887.54 USD', '$813.57 USD']
]
```

### 4-Column Example (Multiple Quantity Breaks)
```python
pricing_data = [
    ['Sizes', 'Qty 1-9', 'Qty 10-24', 'Qty 25+'],
    ['24" x 50\'', '$443.78 USD', '$406.80 USD', '$389.50 USD'],
    ['30" x 50\'', '$554.72 USD', '$508.49 USD', '$487.00 USD'],
    ['36" x 50\'', '$665.66 USD', '$610.19 USD', '$584.50 USD']
]
```

---

## Quality Control Checklist

### Before Publishing Any Price Bracket Document
- ✓ Logo properly sized (2.5" × 0.7") and centered
- ✓ Title uses Helvetica Bold 24pt in Primary Blue (#184187)
- ✓ Title format: "[Product Name] Price Brackets"
- ✓ Table header uses Table Header Blue background (#0A308C)
- ✓ Table header text is white and bold (14pt)
- ✓ Alternating row colors applied (white and light blue #e6f5ff)
- ✓ Size column text is bold
- ✓ Price column text is regular weight
- ✓ All prices formatted with 2 decimal places and "USD"
- ✓ Thousands separator (comma) used correctly
- ✓ Table borders use Primary Blue (#184187)
- ✓ Contact information complete and accurate
- ✓ Footer text uses Primary Blue color
- ✓ Proper spacing maintained (0.3", 0.4", 0.5")
- ✓ PDF created at letter size (8.5" × 11")
- ✓ PNG created at 300 DPI
- ✓ Files named: [Product_Name]_Price_Brackets.[pdf|png]

---

## Python Requirements

### Required Libraries
```bash
pip install reportlab matplotlib pillow --break-system-packages
```

### Import Statements
```python
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
import matplotlib.pyplot as plt
from PIL import Image as PILImage
```

---

## Assets Required

### Logo File
- **File:** `ElimstatBlueSimple.png`
- **Typical Location:** `/mnt/skills/user/elimstat-brand-guidelines/`
- **Dimensions:** 2.5" × 0.7" when placed in document
- **Format:** PNG with transparency

---

## Usage Instructions for Claude

When this skill is active, Claude should:

1. **Generate properly formatted pricing data** following the 2, 3, or 4-column structures
2. **Apply exact brand colors** — use hex codes #184187, #0A308C, #e6f5ff
3. **Format prices consistently** — always 2 decimals, dollar sign, "USD" suffix, comma separators
4. **Use correct typography** — Helvetica Bold 24pt for titles, alternating bold/regular for table data
5. **Maintain proper spacing** — 0.3", 0.4", 0.5" spacing as specified
6. **Include complete footer** — phone, fax, email, and physical address
7. **Create both PDF and PNG** when requested
8. **Follow the quality checklist** before finalizing documents
9. **Use the Python template code** as a base for generating documents
10. **Reference the style guide specifications** for any customizations

### When Creating New Price Brackets
1. Confirm product name and pricing structure (2, 3, or 4 columns)
2. Verify all price data is formatted correctly
3. Use the provided Python template functions
4. Generate both PDF and PNG versions
5. Validate against the quality checklist
6. Use proper file naming convention

---

## Tips for Best Results

✅ **DO:**
- Use exact hex colors specified (#184187, #0A308C, #e6f5ff)
- Maintain consistent spacing (0.3", 0.4", 0.5")
- Keep logo at exactly 2.5" × 0.7"
- Use alternating row colors in all tables
- Include complete contact information in footer
- Format all prices with 2 decimal places and "USD"
- Export PNGs at 300 DPI for print quality
- Use straight quotation marks for dimensions

❌ **DON'T:**
- Stretch or distort the logo
- Use different shades of blue
- Change font sizes or weights
- Omit spacing specifications
- Skip the alternating row colors
- Format prices inconsistently
- Use wrong footer contact information
- Mix up column widths

---

## File Resources in This Package

- **SKILL.md** — This comprehensive guide
- **Elimstat_Price_Bracket_Style_Guide.pdf** — Complete 8-page visual reference
- **Elimstat_Price_Bracket_Style_Guide.md** — Markdown version of style guide
- **Elimstat_Price_Bracket_Quick_Reference.pdf** — One-page cheat sheet
- **elimstat_price_bracket_template.py** — Ready-to-use Python generator
- **ESD_Mat_Roll_Price_Brackets.pdf** — Example PDF output
- **ESD_Mat_Roll_Price_Brackets.png** — Example PNG output

---

**Version 1.0** | November 2025
© 2025 Elimstat.com — All Rights Reserved

