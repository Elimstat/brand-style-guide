# Elimstat Price Bracket Documentation Package

## Overview
This package contains comprehensive documentation and tools for creating standardized price bracket documents for Elimstat products. All documents follow Elimstat's brand guidelines and can be used to create consistent, professional pricing materials.

---

## Files Included

### 📘 Style Guide Documents

#### 1. `Elimstat_Price_Bracket_Style_Guide.pdf`
**Complete Visual Style Guide (8 pages)**
- Comprehensive documentation with visual examples
- Detailed specifications for all design elements
- Color swatches and typography samples
- Full example tables and layouts
- Quality control checklist
- **Use this for:** Complete reference when creating or reviewing price bracket documents

#### 2. `Elimstat_Price_Bracket_Style_Guide.md`
**Markdown Text Version**
- Same content as PDF in markdown format
- Easy to read in text editors or GitHub
- Includes Python code templates
- Searchable and easy to copy/paste from
- **Use this for:** Quick reference, searching specific specs, or integrating into development workflows

#### 3. `Elimstat_Price_Bracket_Quick_Reference.pdf`
**One-Page Cheat Sheet**
- All essential specifications on a single page
- Perfect for printing and keeping at your desk
- Quick lookup for colors, fonts, spacing
- Example table included
- **Use this for:** Quick daily reference while working

---

### 🛠️ Production Tools

#### 4. `elimstat_price_bracket_template.py`
**Reusable Python Template**

A complete, ready-to-use Python script that generates both PDF and PNG price bracket documents following all brand standards.

**Features:**
- Generates both PDF and PNG in one command
- Automatically applies all brand styling
- Handles 2, 3, or 4 column pricing tables
- Includes Elimstat logo and contact information
- Easy to customize for different products

**Quick Start:**
```python
from elimstat_price_bracket_template import create_price_bracket_documents

# Your pricing data
pricing_data = [
    ['Sizes', 'Qty 1-9', 'Qty 10+'],
    ['24" x 50\'', '$443.78 USD', '$406.80 USD'],
    ['30" x 50\'', '$554.72 USD', '$508.49 USD'],
]

# Generate documents
create_price_bracket_documents('Your Product Name', pricing_data)
```

**Run directly:**
```bash
python3 elimstat_price_bracket_template.py
```

---

### 📄 Example Documents

#### 5. `ESD_Mat_Roll_Price_Brackets.pdf`
**Example PDF Output**
- Real example of a completed price bracket document
- Shows proper logo placement, table styling, and footer
- Use as a visual reference for what the final output should look like

#### 6. `ESD_Mat_Roll_Price_Brackets.png`
**Example PNG Output**
- High-resolution (300 DPI) PNG version
- Perfect for web use, email, or presentations
- Shows how PNG output differs from PDF

---

## Quick Reference

### Brand Colors
| Color | Hex | Usage |
|-------|-----|-------|
| Primary Blue | #184187 | Titles, borders, footer |
| Table Header Blue | #0A308C | Table header background |
| Light Blue | #e6f5ff | Alternating table rows |

### Key Specifications
- **Page Size:** US Letter (8.5" × 11")
- **Margins:** 1 inch on all sides
- **Logo Size:** 2.5" × 0.7"
- **Title Font:** Helvetica Bold 24pt
- **PNG Resolution:** 300 DPI

### File Naming Convention
```
[Product_Name]_Price_Brackets.[pdf|png]
```
Examples:
- `ESD_Mat_Roll_Price_Brackets.pdf`
- `Wrist_Strap_Price_Brackets.png`

---

## How to Use This Package

### For Creating New Price Brackets:

1. **Review the style guide** (PDF or Quick Reference)
2. **Prepare your pricing data** in a nested list format
3. **Use the Python template** to generate documents:
   ```python
   from elimstat_price_bracket_template import create_price_bracket_documents
   
   my_pricing = [
       ['Sizes', 'Qty 1-9', 'Qty 10+'],
       ['Small', '$99.99 USD', '$89.99 USD'],
       ['Large', '$199.99 USD', '$179.99 USD'],
   ]
   
   create_price_bracket_documents('My Product', my_pricing)
   ```
4. **Review output** against the quality checklist

### For Quality Control:

1. **Open the Quick Reference** (print it out for easy access)
2. **Compare your document** against the example outputs
3. **Use the checklist** in the full style guide (page 8)
4. **Verify all specifications** match the standards

### For Development/Integration:

1. **Reference the markdown guide** for detailed specifications
2. **Use the Python template** as a starting point
3. **Import functions** from the template into your own scripts
4. **Follow the documented standards** for colors, fonts, and layout

---

## Requirements

### Python Libraries (for template):
```bash
pip install reportlab matplotlib pillow --break-system-packages
```

### Assets Required:
- `ElimstatBlueSimple.png` (logo file)
- Located at: `/mnt/skills/user/elimstat-brand-guidelines/`

---

## Contact Information

**For questions about price bracket documents:**
- Email: sales@elimstat.com
- Phone: (937) 993-0300
- Fax: (937) 324-8753

**Company Address:**
888 Dayton Street Suite 105
Yellow Springs, Ohio 45387

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | November 2025 | Initial release of standardized format |

---

## Tips for Best Results

✅ **DO:**
- Use the exact hex colors specified
- Maintain consistent spacing (0.3", 0.4", 0.5")
- Keep logo at 2.5" × 0.7"
- Use alternating row colors in tables
- Include complete contact information in footer
- Format prices with 2 decimal places and "USD"
- Use 300 DPI for all PNG exports

❌ **DON'T:**
- Stretch or distort the logo
- Use different blue shades
- Change font sizes or weights
- Omit spacing specifications
- Skip the alternating row colors
- Format prices inconsistently

---

## File Structure Summary

```
📦 Elimstat Price Bracket Package
├── 📘 Documentation
│   ├── Elimstat_Price_Bracket_Style_Guide.pdf (Complete guide)
│   ├── Elimstat_Price_Bracket_Style_Guide.md (Text version)
│   └── Elimstat_Price_Bracket_Quick_Reference.pdf (Cheat sheet)
├── 🛠️ Tools
│   └── elimstat_price_bracket_template.py (Generator script)
├── 📄 Examples
│   ├── ESD_Mat_Roll_Price_Brackets.pdf (Example PDF)
│   └── ESD_Mat_Roll_Price_Brackets.png (Example PNG)
└── 📖 README.md (This file)
```

---

**© 2025 Elimstat.com - All Rights Reserved**
