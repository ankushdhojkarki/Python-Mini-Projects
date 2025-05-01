from pypdf import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("How many PDFs would you like to merge?\n"))

for i in range(0, n):
    name = input(f"Enter the name of the PDF {i+1}: \n")
    pdfs.append(name)
for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
