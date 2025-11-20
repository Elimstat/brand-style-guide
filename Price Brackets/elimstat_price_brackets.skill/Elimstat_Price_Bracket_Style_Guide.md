# Elimstat Price Bracket Style Guide

## Version 1.0 | November 2025

---

## Overview

This style guide defines the standardized format for creating price bracket documents (PDF and PNG) for Elimstat.com products. These documents are used for quotes, proposals, and customer-facing pricing communications.

---

## Document Specifications

### Page Format
- **Size:** US Letter (8.5" x 11")
- **Orientation:** Portrait
- **Resolution (PNG):** 300 DPI
- **Margins:** 1 inch (72 points) on all sides
- **Background:** White (#FFFFFF)

### File Naming Convention
```
[Product_Name]_Price_Brackets.[pdf|png]
Example: ESD_Mat_Roll_Price_Brackets.pdf
```

---

## Brand Colors

### Primary Colors
| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| **Primary Blue** | #184187 | 24, 65, 135 | Title text, borders, footer text |
| **Table Header Blue** | #0A308C | 10, 48, 140 | Table header background (Pantone 2748 UP) |
| **Light Blue** | #e6f5ff | 230, 245, 255 | Alternating table row backgrounds |
| **White** | #FFFFFF | 255, 255, 255 | Page background, table data rows |
| **Black** | #000000 | 0, 0, 0 | Table data text |

---

## Logo Specifications

### Logo File
- **File:** `ElimstatBlueSimple.png`
- **Location:** Top center of document
- **Width:** 2.5 inches
- **Height:** 0.7 inches (maintains aspect ratio)
- **Space Below Logo:** 0.3 inches

### Logo Placement
```
┌─────────────────────────────┐
│         [LOGO]              │ ← Top Margin: 1"
│                             │
│         0.3" space          │
└─────────────────────────────┘
```

---

## Typography

### Document Title
- **Font:** Helvetica Bold
- **Size:** 24pt
- **Color:** Primary Blue (#184187)
- **Alignment:** Center
- **Space Below:** 0.4 inches
- **Format:** `[Product Name] Price Brackets`

### Table Text

#### Header Row
- **Font:** Helvetica Bold
- **Size:** 14pt
- **Color:** White (#FFFFFF)
- **Background:** Table Header Blue (#0A308C)
- **Padding:** 16pt top and bottom
- **Alignment:** Center

#### Data Rows
- **Font (Column 1 - Sizes):** Helvetica Bold
- **Font (Columns 2-3 - Prices):** Helvetica Regular
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
- **Line Spacing:** 0.04 inches between lines

---

## Table Specifications

### Table Structure
- **Total Width:** 6.5 inches (fits within margins)
- **Position:** Center-aligned on page

### Column Widths
| Column | Width | Content |
|--------|-------|---------|
| Column 1 | 2.5" | Product sizes/dimensions |
| Column 2 | 2.0" | Lower quantity pricing |
| Column 3 | 2.0" | Higher quantity pricing |

### Table Styling

#### Borders
- **Grid Lines:** 1pt solid Primary Blue (#184187)
- **Header Bottom Border:** 2pt solid Primary Blue (#184187)

#### Row Backgrounds
```
Row 0 (Header):    Table Header Blue (#0A308C)
Row 1 (Data):      White (#FFFFFF)
Row 2 (Data):      Light Blue (#e6f5ff)
Row 3 (Data):      White (#FFFFFF)
Row 4 (Data):      Light Blue (#e6f5ff)
[Continue alternating pattern]
```

#### Cell Padding
- **Horizontal:** 8pt left and right
- **Vertical:** 12pt top and bottom (data rows)
- **Vertical:** 16pt top and bottom (header row)

---

## Layout Structure

### Vertical Spacing
```
┌────────────────────────────────────┐
│  Top Margin: 1.0"                  │
│                                    │
│  [Elimstat Logo]                   │ ← 2.5" x 0.7"
│                                    │
│  Space: 0.3"                       │
│                                    │
│  [Document Title]                  │ ← 24pt Helvetica Bold
│                                    │
│  Space: 0.4"                       │
│                                    │
│  ┌──────────────────────────┐     │
│  │      Price Table          │     │
│  │                           │     │
│  │                           │     │
│  └──────────────────────────┘     │
│                                    │
│  Space: 0.5"                       │
│                                    │
│  [Contact Information]             │ ← 10pt Helvetica
│  Line 1: Phone | Fax | Email       │
│  Line 2: Physical Address          │
│                                    │
│  Bottom Margin: 1.0"               │
└────────────────────────────────────┘
```

---

## Contact Information Footer

### Format
**Line 1:**
```
Phone: (937) 993-0300  |  Fax: (937) 324-8753  |  Email: sales@elimstat.com
```

**Line 2:**
```
888 Dayton Street Suite 105, Yellow Springs, Ohio 45387
```

### Specifications
- **Separator:** Vertical pipe (|) with spaces: ` | `
- **Font:** Helvetica Regular
- **Size:** 10pt
- **Color:** Primary Blue (#184187)
- **Alignment:** Center
- **Line Spacing:** Single line break between Line 1 and Line 2

---

## Table Data Format Standards

### Size/Dimension Column
- **Format:** `[Width]" x [Length]'`
- **Example:** `24" x 50'`
- **Font Weight:** Bold
- **Notes:** Use straight quotation marks for inches ("), apostrophe for feet (')

### Quantity Headers
- **Format:** `Qty [range]`
- **Examples:** 
  - `Qty 1-9`
  - `Qty 10+`
  - `Qty 25-49`
  - `Qty 50+`
- **Font Weight:** Bold
- **Color:** White (on blue background)

### Price Format
- **Format:** `$[amount] USD`
- **Examples:** 
  - `$443.78 USD`
  - `$1,234.56 USD`
- **Decimal Places:** Always 2 decimal places
- **Currency Symbol:** Dollar sign ($)
- **Currency Code:** Always include "USD"
- **Thousands Separator:** Comma for amounts ≥ $1,000
- **Font Weight:** Regular (not bold)

---

## PDF-Specific Requirements

### ReportLab Implementation
```python
# PDF page size
pagesize=letter  # 8.5" x 11"

# Margins
rightMargin=72   # 1 inch
leftMargin=72    # 1 inch
topMargin=72     # 1 inch
bottomMargin=72  # 1 inch

# Logo
logo = Image(logo_path, width=2.5*inch, height=0.7*inch)

# Title style
title_style = ParagraphStyle(
    'CustomTitle',
    fontSize=24,
    textColor=colors.HexColor('#184187'),
    spaceAfter=30,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

# Table dimensions
table = Table(data, colWidths=[2.5*inch, 2*inch, 2*inch])
```

---

## PNG-Specific Requirements

### Matplotlib Implementation
```python
# Figure size and resolution
fig, ax = plt.subplots(figsize=(11, 8.5), dpi=300)

# Logo placement
extent=[0.15, 0.65, 0.85, 0.95]  # [left, right, bottom, top]

# Title placement
ax.text(0.5, 0.78, title_text, 
        ha='center', va='center', 
        fontsize=28, fontweight='bold',
        color='#184187')

# Table bounding box
bbox=[0.15, 0.25, 0.7, 0.45]  # [left, bottom, width, height]

# Export settings
plt.savefig(png_path, dpi=300, bbox_inches='tight', 
           facecolor='white', edgecolor='none')
```

---

## Quality Control Checklist

### Before Publishing
- [ ] Logo is properly sized and positioned
- [ ] Title uses correct font (Helvetica Bold 24pt) and color
- [ ] Table header uses Table Header Blue background (#0A308C)
- [ ] Table header text is white and bold
- [ ] Alternating row colors applied correctly
- [ ] Size column text is bold
- [ ] Price column text is regular weight
- [ ] All prices formatted with 2 decimal places and "USD"
- [ ] Table borders use Primary Blue (#184187)
- [ ] Contact information is complete and accurate
- [ ] Footer uses Primary Blue color
- [ ] Proper spacing maintained throughout
- [ ] PDF is created at letter size
- [ ] PNG is created at 300 DPI
- [ ] Files named according to convention

---

## Example Table Templates

### 2-Column Pricing (Single Quantity Break)
```
| Sizes          | Price (Each)  |
|----------------|---------------|
| 24" x 50'      | $443.78 USD   |
| 30" x 50'      | $554.72 USD   |
```

### 3-Column Pricing (Two Quantity Breaks)
```
| Sizes          | Qty 1-9       | Qty 10+       |
|----------------|---------------|---------------|
| 24" x 50'      | $443.78 USD   | $406.80 USD   |
| 30" x 50'      | $554.72 USD   | $508.49 USD   |
```

### 4-Column Pricing (Three Quantity Breaks)
```
| Sizes          | Qty 1-9       | Qty 10-24     | Qty 25+       |
|----------------|---------------|---------------|---------------|
| 24" x 50'      | $443.78 USD   | $406.80 USD   | $389.50 USD   |
```

**Note:** Adjust column widths proportionally to maintain 6.5" total table width.

---

## Python Template Script

```python
#!/usr/bin/env python3
"""
Elimstat Price Bracket Generator
Standard template for creating branded pricing documents
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

# Elimstat Brand Colors
PRIMARY_BLUE = colors.HexColor('#184187')
LIGHT_BLUE = colors.HexColor('#e6f5ff')
TABLE_HEADER_BLUE = colors.HexColor('#0A308C')

def create_price_bracket_document(product_name, pricing_data, output_path):
    """
    Create a standardized price bracket document
    
    Args:
        product_name: Name of product (e.g., "ESD Mat Roll")
        pricing_data: List of lists [[header_row], [data_row_1], ...]
        output_path: File path for output PDF
    """
    
    # Create document
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    elements = []
    
    # Logo
    logo_path = '/path/to/ElimstatBlueSimple.png'
    logo = Image(logo_path, width=2.5*inch, height=0.7*inch)
    elements.append(logo)
    elements.append(Spacer(1, 0.3*inch))
    
    # Title
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
    
    # Table
    num_cols = len(pricing_data[0])
    col_widths = [2.5*inch] + [2*inch] * (num_cols - 1)
    table = Table(pricing_data, colWidths=col_widths)
    
    # Apply standard styling
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 16),
        ('TOPPADDING', (0, 0), (-1, 0), 16),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
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
    
    # Footer
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
    
    # Build PDF
    doc.build(elements)
    
    return output_path
```

---

## Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | November 2025 | Initial style guide creation | Elimstat |

---

## Contact & Support

For questions about this style guide or assistance with price bracket documents:

**Email:** sales@elimstat.com  
**Phone:** (937) 993-0300

---

**© 2025 Elimstat.com - All Rights Reserved**
