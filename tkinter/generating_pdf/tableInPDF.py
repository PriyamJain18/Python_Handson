from fpdf import FPDF
import csv

with open("countries.txt", encoding="utf-8") as csv_file:
    data = list(csv.reader(csv_file, delimiter=","))


pdf = FPDF()
pdf.set_title("Countries of the World")
pdf.set_author("Priyam")
pdf.set_font("helvetica", size=12)

pdf.add_page()
with pdf.table(
    borders_layout= "NO_HORIZONTAL_LINES",
    cell_fill_color=(200, 220, 255),
    col_widths=(40, 35, 40, 45),
    line_height=6,
    text_align=("LEFT", "C", "R", "L"),
    width=160
) as table:
    for data_row in data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.output("table.pdf")