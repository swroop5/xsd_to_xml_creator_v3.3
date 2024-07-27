import PyPDF2

def pdf_to_text(pdf_path, text_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        with open(text_path, 'w', encoding='utf-8') as text_file:
            num_pages = len(pdf_reader.pages)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                text_file.write(text)

pdf_path = 'Spezifikation_XJustiz_3_3_1.pdf'
text_path = 'xjustiz_3_3_1.txt'

pdf_to_text(pdf_path, text_path)