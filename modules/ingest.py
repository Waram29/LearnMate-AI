import re
from pathlib import Path

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from chromadb.utils import embedding_functions


DATA_DIR = Path("data/raw_pdfs")
CHROMA_DIR = Path("./vector_db")

COLLECTION_NAME = "learnmate_docs"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

def clean_text(text):
    # 1. Supprimer les espaces blancs excessifs et les sauts de ligne
    text = re.sub(r'\s+', ' ', text)
    
    # 2. Supprimer les caractères spéciaux invisibles (ASCII non imprimables)
    text = re.sub(r'[^\x00-\x7f]', r'', text) 
    
    # 3. Supprimer les mentions "Page X" ou "Page X/Y" (insensible à la casse)
    # Le pattern cherche "Page" suivi d'un espace et de chiffres
    text = re.sub(r'(?i)page\s?\d+(\s?/\s?\d+)?', '', text)
    return text.strip() 

def extract_pages(pdf_path):
    reader = PdfReader(str(pdf_path))
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        text = clean_text(text)

        if text:
            pages.append({
                "text": text,
                "page": i + 1,
                "filename": pdf_path.name,
            })

    return pages


def ingest_documents():

    pdf_files = list(DATA_DIR.glob("*.pdf"))
    print("PDF trouvés :", pdf_files)

    if not pdf_files:
        print("Aucun PDF trouvé.")
        return

    all_pages = []

    for pdf in pdf_files:
        all_pages.extend(extract_pages(pdf))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = []

    for page in all_pages:
        splits = splitter.split_text(page["text"])

        for i, chunk in enumerate(splits):
            chunks.append({
                "id": f"{page['filename']}_{page['page']}_{i}",
                "text": chunk,
                "metadata": {
                    "filename": page["filename"],
                    "page": page["page"]
                }
            })

    # Embedding intégré dans Chroma
    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function
    )

    collection.add(
        ids=[c["id"] for c in chunks],
        documents=[c["text"] for c in chunks],
        metadatas=[c["metadata"] for c in chunks]
    )

    print(f"{len(chunks)} chunks ajoutés avec succès.")


if __name__ == "__main__":
    ingest_documents()