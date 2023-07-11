from fpdf import FPDF
import glob
from pathlib import Path

#create a list of filepaths
filepaths = glob.glob("Text_Files/*.txt")

# create one pdf file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# go through each text file
for filepath in filepaths:
    #add a page to the PDF doc for each text file
    pdf.add_page()

    # Get the filename without the extension
    # and cover it to title case (e.g. Cat)
    filename = Path(filepath).stem
    name = filename.title()

    #add the name to the PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=name, ln=1)

#produce the PDF
pdf.output("output.pdf")
