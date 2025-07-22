import fitz  
import tiktoken

def extract_pdf_text(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def chunk_text(text, max_tokens=300):
    enc = tiktoken.get_encoding("cl100k_base")
    words = text.split(". ")
    chunks, current = [], ""

    for sentence in words:
        if len(enc.encode(current + sentence)) < max_tokens:
            current += sentence + ". "
        else:
            chunks.append(current.strip())
            current = sentence + ". "
    
    if current:
        chunks.append(current.strip())
    return chunks

pdf_path = r"C:\Users\chait\Downloads\sr550_maintenance_manual.pdf"
pdf_text = extract_pdf_text(pdf_path)
chunks = chunk_text(pdf_text)
print(f"Created {len(chunks)} text chunks.")
