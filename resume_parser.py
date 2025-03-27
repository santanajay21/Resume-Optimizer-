from PyPDF2 import PdfReader 
from docx import Document 


"""file_path: path to the uploaded file that is temparaily stored in you server"""
"""file_extention: the extention pdf or docx determines which method is executed"""
def extract_text(file_path, file_extention):
    text = ""
    if file_extention == ".pdf":
        reader = PdfReader(file_path) # opens the pdf file 
        for page in reader.pages: # iterates through each page 
            text += page.extract_text() # extracts text from pdf and appends to text variable 
    elif file_extention == ".docx":
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text 

