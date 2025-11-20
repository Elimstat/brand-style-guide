#!/usr/bin/env python3
"""
Elimstat Price Bracket Document Generator - Reusable Template
Version 1.0 | November 2025

This template follows the Elimstat Price Bracket Style Guide and can be used
to generate standardized pricing documents for any product.

Usage:
    python3 elimstat_price_bracket_template.py
    
Or import and use the functions:
    from elimstat_price_bracket_template import create_price_bracket_pdf, create_price_bracket_png
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
import matplotlib.pyplot as plt
from PIL import Image as PILImage
import os

# ============================================================================
# ELIMSTAT BRAND CONSTANTS
# ============================================================================

PRIMARY_BLUE = colors.HexColor('#184187')
LIGHT_BLUE = colors.HexColor('#e6f5ff')
TABLE_HEADER_BLUE = colors.HexColor('#0A308C')

LOGO_PATH = '/mnt/skills/user/elimstat-brand-guidelines/ElimstatBlueSimple.png'

CONTACT_INFO = {
    'phone': '(937) 993-0300',
    'fax': '(937) 324-8753',
    'email': 'sales@elimstat.com',
    'address': '888 Dayton Street Suite 105, Yellow Springs, Ohio 45387'
}

# ============================================================================
# PDF GENERATION FUNCTIONS
# ============================================================================

def create_price_bracket_pdf(product_name, pricing_data, output_path):
    """
    Create a standardized PDF price bracket document following Elimstat brand guidelines.
    
    Args:
        product_name (str): Name of the product (e.g., "ESD Mat Roll")
        pricing_data (list): Nested list of pricing data. First row should be headers.
                            Example: [
                                ['Sizes', 'Qty 1-9', 'Qty 10+'],
                                ['24" x 50\'', '$443.78 USD', '$406.80 USD'],
                                ...
                            ]
        output_path (str): Full path for the output PDF file
    
    Returns:
        str: Path to the created PDF file
    """
    
    # Create document with standard margins (1 inch on all sides)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    elements = []
    
    # ========================================================================
    # LOGO - 2.5" x 0.7" at top center
    # ========================================================================
    if os.path.exists(LOGO_PATH):
        logo = Image(LOGO_PATH, width=2.5*inch, height=0.7*inch)
        elements.append(logo)
        elements.append(Spacer(1, 0.3*inch))  # 0.3" space below logo
    
    # ========================================================================
    # TITLE - Helvetica Bold 24pt, Primary Blue, centered
    # ========================================================================
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
    elements.append(Spacer(1, 0.4*inch))  # 0.4" space below title
    
    # ========================================================================
    # TABLE - Calculate column widths based on number of columns
    # ========================================================================
    num_cols = len(pricing_data[0])
    
    # First column (sizes) is always 2.5", remaining columns share 4.0"
    if num_cols == 2:
        col_widths = [2.5*inch, 4.0*inch]
    elif num_cols == 3:
        col_widths = [2.5*inch, 2.0*inch, 2.0*inch]
    elif num_cols == 4:
        col_widths = [2.5*inch, 1.33*inch, 1.33*inch, 1.34*inch]
    else:
        # Default: first column 2.5", others split remaining 4.0"
        other_width = 4.0 / (num_cols - 1)
        col_widths = [2.5*inch] + [other_width*inch] * (num_cols - 1)
    
    table = Table(pricing_data, colWidths=col_widths)
    
    # ========================================================================
    # TABLE STYLING - Following Elimstat brand standards
    # ========================================================================
    table.setStyle(TableStyle([
        # Header row styling
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 16),
        ('TOPPADDING', (0, 0), (-1, 0), 16),
        
        # Data rows styling
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),  # Size column bold
        ('FONTNAME', (1, 1), (-1, -1), 'Helvetica'),      # Price columns regular
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 12),
        
        # Grid and borders
        ('GRID', (0, 0), (-1, -1), 1, PRIMARY_BLUE),
        ('LINEBELOW', (0, 0), (-1, 0), 2, PRIMARY_BLUE),
        
        # Alternating row colors (white and light blue)
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT_BLUE]),
    ]))
    
    elements.append(table)
    elements.append(Spacer(1, 0.5*inch))  # 0.5" space below table
    
    # ========================================================================
    # FOOTER - Contact information, Helvetica 10pt, Primary Blue, centered
    # ========================================================================
    footer_style = ParagraphStyle(
        'Footer',
        fontSize=10,
        textColor=PRIMARY_BLUE,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    footer_text = f'''Phone: {CONTACT_INFO['phone']}  |  Fax: {CONTACT_INFO['fax']}  |  Email: {CONTACT_INFO['email']}<br/>
    {CONTACT_INFO['address']}'''
    
    footer = Paragraph(footer_text, footer_style)
    elements.append(Spacer(1, 0.3*inch))
    elements.append(footer)
    
    # Build the PDF
    doc.build(elements)
    print(f"✓ PDF created: {output_path}")
    
    return output_path


# ============================================================================
# PNG GENERATION FUNCTIONS
# ============================================================================

def create_price_bracket_png(product_name, pricing_data, output_path):
    """
    Create a standardized PNG price bracket document following Elimstat brand guidelines.
    
    Args:
        product_name (str): Name of the product (e.g., "ESD Mat Roll")
        pricing_data (list): Nested list of pricing data. First row should be headers.
        output_path (str): Full path for the output PNG file
    
    Returns:
        str: Path to the created PNG file
    """
    
    # Create figure - 8.5x11 at 300 DPI
    fig, ax = plt.subplots(figsize=(11, 8.5), dpi=300)
    ax.axis('off')
    
    # ========================================================================
    # LOGO
    # ========================================================================
    if os.path.exists(LOGO_PATH):
        logo = PILImage.open(LOGO_PATH)
        ax.imshow(logo, aspect='auto', extent=[0.15, 0.65, 0.85, 0.95], zorder=10)
    
    # ========================================================================
    # TITLE
    # ========================================================================
    ax.text(0.5, 0.78, f'{product_name} Price Brackets', 
            ha='center', va='center', 
            fontsize=28, fontweight='bold',
            color='#184187')
    
    # ========================================================================
    # TABLE
    # ========================================================================
    num_cols = len(pricing_data[0])
    num_rows = len(pricing_data)
    
    # Calculate column widths
    if num_cols == 2:
        col_widths = [0.35, 0.65]
    elif num_cols == 3:
        col_widths = [0.3, 0.35, 0.35]
    elif num_cols == 4:
        col_widths = [0.3, 0.23, 0.23, 0.24]
    else:
        other_width = 0.7 / (num_cols - 1)
        col_widths = [0.3] + [other_width] * (num_cols - 1)
    
    # Create table
    table = ax.table(
        cellText=pricing_data, 
        cellLoc='center',
        bbox=[0.15, 0.25, 0.7, 0.45],
        colWidths=col_widths
    )
    
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    
    # ========================================================================
    # TABLE STYLING
    # ========================================================================
    
    # Header row
    for i in range(num_cols):
        cell = table[(0, i)]
        cell.set_facecolor('#0A308C')
        cell.set_text_props(weight='bold', color='white', fontsize=14)
        cell.set_height(0.08)
        cell.set_edgecolor('#184187')
        cell.set_linewidth(1)
    
    # Data rows
    for i in range(1, num_rows):
        for j in range(num_cols):
            cell = table[(i, j)]
            
            # Alternating row colors
            if i % 2 == 0:
                cell.set_facecolor('#e6f5ff')
            else:
                cell.set_facecolor('white')
            
            # First column (sizes) is bold
            if j == 0:
                cell.set_text_props(weight='bold')
            
            cell.set_edgecolor('#184187')
            cell.set_linewidth(1)
            cell.set_height(0.08)
    
    # ========================================================================
    # FOOTER
    # ========================================================================
    ax.text(0.5, 0.12, 
            f"Phone: {CONTACT_INFO['phone']}  |  Fax: {CONTACT_INFO['fax']}  |  Email: {CONTACT_INFO['email']}", 
            ha='center', va='center',
            fontsize=10, color='#184187')
    
    ax.text(0.5, 0.08, 
            CONTACT_INFO['address'], 
            ha='center', va='center',
            fontsize=10, color='#184187')
    
    # Save PNG at 300 DPI
    plt.savefig(output_path, dpi=300, bbox_inches='tight', 
               facecolor='white', edgecolor='none')
    plt.close()
    
    print(f"✓ PNG created: {output_path}")
    
    return output_path


# ============================================================================
# CONVENIENCE FUNCTION
# ============================================================================

def create_price_bracket_documents(product_name, pricing_data, output_dir='/mnt/user-data/outputs'):
    """
    Create both PDF and PNG versions of a price bracket document.
    
    Args:
        product_name (str): Name of the product (e.g., "ESD Mat Roll")
        pricing_data (list): Nested list of pricing data
        output_dir (str): Directory for output files (default: /mnt/user-data/outputs)
    
    Returns:
        tuple: (pdf_path, png_path)
    """
    
    # Create safe filename
    safe_name = product_name.replace(' ', '_').replace('/', '_')
    
    pdf_path = os.path.join(output_dir, f'{safe_name}_Price_Brackets.pdf')
    png_path = os.path.join(output_dir, f'{safe_name}_Price_Brackets.png')
    
    # Create both documents
    create_price_bracket_pdf(product_name, pricing_data, pdf_path)
    create_price_bracket_png(product_name, pricing_data, png_path)
    
    print(f"\n✓ Documents created successfully!")
    print(f"  PDF: {pdf_path}")
    print(f"  PNG: {png_path}")
    
    return pdf_path, png_path


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == '__main__':
    # Example: ESD Mat Roll pricing
    pricing_data = [
        ['Sizes', 'Qty 1-9', 'Qty 10+'],
        ['24" x 50\'', '$443.78 USD', '$406.80 USD'],
        ['30" x 50\'', '$554.72 USD', '$508.49 USD'],
        ['36" x 50\'', '$665.66 USD', '$610.19 USD'],
        ['48" x 50\'', '$887.54 USD', '$813.57 USD']
    ]
    
    create_price_bracket_documents('ESD Mat Roll', pricing_data)
    
    print("\n" + "="*60)
    print("To create documents for a different product:")
    print("="*60)
    print("""
    from elimstat_price_bracket_template import create_price_bracket_documents
    
    # Your pricing data
    data = [
        ['Size', 'Price'],
        ['Small', '$99.99 USD'],
        ['Large', '$149.99 USD']
    ]
    
    # Generate documents
    create_price_bracket_documents('Your Product Name', data)
    """)
