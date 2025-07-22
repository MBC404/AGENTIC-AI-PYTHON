import fitz  # PyMuPDF

doc = fitz.open(r"failpath")  

#read first 10 pages of pdf
for page_num in range(10):
    page = doc[page_num]
    text = page.get_text()
    print(f"\n--- Page {page_num + 1} ---\n")
    print(text)


doc.close()
