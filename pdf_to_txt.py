import PyPDF2

# input
read_pdf = PyPDF2.PdfFileReader(open('input.pdf', 'rb'))

# extract text from pdf
text = ''
for i in range(read_pdf.numPages):
    pdf_get_page = read_pdf.getPage(i)
    text += pdf_get_page.extractText()

# output
text_file = open("output.txt", "w", encoding="utf-8")
text_file.write(text)
text_file.close()
