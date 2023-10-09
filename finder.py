import PyPDF2
import openai


class PDFReader:
    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path
        self.pdf_reader = PyPDF2.PdfReader(open(pdf_file_path, 'rb'))

    def read_pdf_line_by_line(self):
        content = []
        for page_num in range(len(self.pdf_reader.pages)):
            page = self.pdf_reader.pages[page_num]
            content.extend(page.extract_text().splitlines())
        return content

    def find_phrase_and_page(self, phrase):
        for page_num in range(len(self.pdf_reader.pages)):
            page =  self.pdf_reader.pages[page_num]
            page_content = page.extract_text()
            if phrase in page_content:
                print(f'Phrase "{phrase}" found on page {page_num + 1}')

    def extract_content_from_page_to_page(self, start_page, end_page):
        content = []
        for page_num in range(start_page - 1, end_page):
            page = self.pdf_reader.pages[page_num]
            content.append(page.extract_text())
        return '\n'.join(content)

# Set your OpenAI API key here
openai.organization = "org-X9Hw9MAngHB0YWLljgwwEd5M"
openai.api_key = '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'

def generate_summary_from_text(text):
    prompt = f"Can you write a comprehensive summary in french of the most important events of the following text, every event on a individual numerated paragraph with a maximum of 7 paragraphs:{text}"
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=2500
    )
    summary = response.choices[0].text.strip()
    return summary

# Example usage
if __name__ == "__main__":
    pdf_path = r'C:\Users\IvanB\Documents\1984.pdf'  # Provide the path to your PDF file
    pdf_reader = PDFReader(pdf_path)

    # # Read PDF line by line
    # lines = pdf_reader.read_pdf_line_by_line()
    # print("PDF Content Line by Line:")
    # for line in lines:
    #    print(line)

    # # Find a phrase and indicate the page
    # search_phrase = 'TRES IMPRESIONES ORIGINALES'
    # pdf_reader.find_phrase_and_page(search_phrase)


    # Extract content from page 3 to page 5
    start_page = 31
    end_page = 32
    extracted_content = pdf_reader.extract_content_from_page_to_page(start_page, end_page)
    # print(f"\nExtracted Content from page {start_page} to page {end_page}:\n{extracted_content}")

    summary = generate_summary_from_text(extracted_content)
    print("\nGenerated Summary:")
    print(summary)

