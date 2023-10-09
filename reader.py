import PyPDF2

def read_pdf_content(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        content = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            content += page.extract_text()
        return content


pdf_path = r'C:\Users\IvanB\Documents\documento-cita-70910.pdf'
extracted_content = read_pdf_content(pdf_path)
print("Extracted PDF Content:")
print(extracted_content)