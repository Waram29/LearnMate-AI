from pypdf import PdfReader
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
pdf_path = os.path.join(BASE_DIR, "data", "raw_pdfs", "test.pdf")

def load_pdf(file_path):
    """
    Charge un fichier PDF et extrait tout le texte.
    """
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:  # éviter les pages vides
            text += page_text + "\n"

    return text


# # Test rapide (optionnel)
# if __name__ == "__main__":
#     content = load_pdf(pdf_path)
#     print(content[:5000])  # afficher un aperçu