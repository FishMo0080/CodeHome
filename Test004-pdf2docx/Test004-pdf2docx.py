from pdf2docx import parse
pdf_file = 'input/Pycharm使用快捷键.pdf'
docx_file = 'output/Pycharm使用快捷键.xlsx'
# convert pdf to docx
parse(pdf_file, docx_file)