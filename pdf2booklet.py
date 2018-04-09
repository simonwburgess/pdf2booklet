import argparse
import pdf2bookletutils

from PyPDF2 import PdfFileReader, PdfFileWriter


parser = argparse.ArgumentParser()
parser.add_argument("source", help="Name of the source PDF file")
parser.add_argument("-d", "--destination", help="Name of the destination PDF file.  Defaults to <source>.booklet.pdf")
args = parser.parse_args()

source_filename = args.source

if args.destination is None:
    destination_filename = source_filename + ".booklet.pdf"
else:
    destination_filename = args.destination

source_pdf = PdfFileReader(source_filename)
destination_pdf = PdfFileWriter()

pages = pdf2bookletutils.get_page_order(source_pdf)
for page in pages:
    pdf2bookletutils.copy_page(page, source_pdf, destination_pdf)

with open(destination_filename, 'wb') as out:
    destination_pdf.write(out)

print("\nDone")
