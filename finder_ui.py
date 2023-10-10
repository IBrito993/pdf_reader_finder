import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to read PDF and find the phrase
def process_pdf():
    file_path = file_entry.get()
    search_phrase = phrase_entry.get()

    try:
        pdf_reader = PyPDF2.PdfReader(open(file_path, 'rb'))
        found = False
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_content = page.extract_text()
            if search_phrase in page_content:
                found = True
                result_label.config(text=f'Phrase found on page {page_num + 1}')
                break
        if not found:
            result_label.config(text='Phrase not found in the PDF')
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')

# Create the main window
root = tk.Tk()
root.title('PDF Phrase Search')

# File selection
file_label = tk.Label(root, text='Select PDF File:')
file_label.pack()
file_entry = tk.Entry(root, width=50)
file_entry.pack()
file_button = tk.Button(root, text='Browse', command=lambda: file_entry.insert(0, filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])))
file_button.pack()

# Phrase input
phrase_label = tk.Label(root, text='Enter Search Phrase:')
phrase_label.pack()
phrase_entry = tk.Entry(root, width=50)
phrase_entry.pack()

# Search button
search_button = tk.Button(root, text='Search', command=process_pdf)
search_button.pack()

# Result display
result_label = tk.Label(root, text='')
result_label.pack()

# Run the application
root.mainloop()
