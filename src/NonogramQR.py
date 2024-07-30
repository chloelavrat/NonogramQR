from itertools import zip_longest
import pyqrcode
from reportlab.lib.pagesizes import A3
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def generate_qr_matrix(data):
    qr_code = pyqrcode.create(data)
    binary_matrix = qr_code.text(quiet_zone=0)
    binary_matrix = binary_matrix.replace('1', '*')
    binary_matrix = binary_matrix.replace('0', ' ')
    return binary_matrix[:-1]


def calculate_line_counts(matrix):
    """Calculate the counts of continuous characters in rows and columns.

    `matrix` is a multi-line string where each line represents a row."""
    rows = matrix.split('\n')
    columns = (''.join(chars) for chars in zip_longest(*rows, fillvalue=' '))

    def count_sequences(lines):
        return [[str(len(seq)) for seq in line.split()] for line in lines]

    return count_sequences(columns), count_sequences(rows)


def adjust_count_format(counts):
    """Adjust the number of elements for each count to match the longest sequences."""
    max_count_length = max(len(seq) for seq in counts)
    max_element_length = max(max(len(num) for num in seq) for seq in counts)

    formatted_counts = ([num.rjust(max_element_length)
                        for num in seq] for seq in counts)
    padding = ' ' * max_element_length
    return [[padding] * (max_count_length - len(seq)) + seq for seq in formatted_counts]


def export_counts_to_pdf(matrix, output_pdf):
    """Export the counts directly to a PDF file."""
    column_counts, row_counts = calculate_line_counts(matrix)
    column_counts = adjust_count_format(column_counts)
    row_counts = adjust_count_format(row_counts)
    row_counts = [';'.join(row) for row in row_counts]

    column_padding = ';' * len(row_counts[0].split(";"))
    column_counts = (';'.join(col) for col in zip(*column_counts))
    column_counts = [column_padding + col for col in column_counts]

    table_data = [col.split(';') for col in column_counts]
    table_data += [row.split(';') for row in row_counts]

    # Initialize PDF document
    pdf_document = SimpleDocTemplate(output_pdf, pagesize=A3)

    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        name='Title',
        fontSize=36,
        alignment=0,  # Center alignment
        spaceAfter=50,
    )
    subtitle_style = ParagraphStyle(
        name='Subtitle',
        fontSize=10,
        alignment=2,  # Right alignment
        spaceAfter=20
    )
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),  # Header background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),   # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),          # Center all text
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Data background
        ('GRID', (0, 0), (-1, -1), 1, colors.lightgrey),  # Grid lines
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),     # Header font
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),    # Data font
        ('BOTTOMPADDING', (0, 0), (-1, 0), 2),          # Header padding
    ])
    footer_style = ParagraphStyle(
        name='Footer',
        fontSize=10,
        alignment=1,  # Center alignment
        spaceBefore=20
    )

    # Create document elements
    title = Paragraph("NonogramQR", title_style)
    subtitle = Paragraph("Designed by Chloé Lavrat", subtitle_style)
    footer = Paragraph("www.chloelavrat.com", footer_style)
    table = Table(table_data)
    table.setStyle(table_style)

    # Build PDF with elements
    elements = [title, subtitle, table, footer]
    pdf_document.build(elements)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='Convert a string into a QR code and then into a nonogram PDF.',
        epilog="Have fun!"
    )
    parser.add_argument('message', nargs='*', default=["Love is love!"],
                        help='Message to encode')
    parser.add_argument('--output', default='NonogramQR.pdf',
                        help='Output PDF file name')
    args = parser.parse_args()

    input_string = args.message[0]

    if len(input_string) > 25:
        print("Error: String too long")
    else:
        qr_matrix = generate_qr_matrix(input_string)
        export_counts_to_pdf(qr_matrix, args.output)
