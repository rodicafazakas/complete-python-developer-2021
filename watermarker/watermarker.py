import PyPDF2
import sys

# 1. Merge various pdf files in a folder
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(PyPDF2.PdfFileReader(open(pdf, 'rb')))
    merger.write('merged.pdf')


pdf_combiner(inputs)


# 2. Watermark the merged file

# open and read files
input_file = open("merged.pdf", 'rb')
input_pdf = PyPDF2.PdfFileReader(input_file)

watermark_file = open("watermark.pdf", 'rb')
watermark_pdf = PyPDF2.PdfFileReader(watermark_file)

output = PyPDF2.PdfFileWriter()

# Accessing the pages of the pdf file and the watermark file to be merged,
# Index 0 is used to access the first page
for i in range(input_pdf.getNumPages()):
    pdf_page = input_pdf.getPage(i)
    pdf_page.mergePage(watermark_pdf.getPage(0))
    output.addPage(pdf_page)


merged_file = open('merged_watermarked.pdf', 'wb')
output.write(merged_file)
