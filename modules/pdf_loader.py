from pypdf import PdfReader
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
pdf_path = os.path.join(BASE_DIR, "data", "raw_pdfs", "test.pdf")

def clean_text(text):
    # 1. Supprimer les espaces blancs excessifs et les sauts de ligne
    text = re.sub(r'\s+', ' ', text)
    
    # 2. Supprimer les caractères spéciaux invisibles (ASCII non imprimables)
    text = re.sub(r'[^\x00-\x7f]', r'', text) 
    
    # 3. Supprimer les mentions "Page X" ou "Page X/Y" (insensible à la casse)
    # Le pattern cherche "Page" suivi d'un espace et de chiffres
    text = re.sub(r'(?i)page\s?\d+(\s?/\s?\d+)?', '', text)
    return text.strip() 

def load_pdf(file_path):
    reader = PdfReader(file_path)
    full_text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            full_text += content + "\n"
    # On applique le nettoyage ici
    cleaned_content = clean_text(full_text)
    return cleaned_content


# # Test rapide 
# if __name__ == "__main__":
#     content = load_pdf(pdf_path)
#     print(content[:10000])  # Affiche les 10 000 premiers caractères du PDF nettoyé