import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.pdf_loader import load_pdf
from modules.chunker import split_text
from modules.embeddings import EmbeddingModel
from modules.vector_store import VectorStore


# 1. Charger PDF
text = load_pdf("data/raw_pdfs/test.pdf")

# 2. Chunking
chunks = split_text(text)

print("Chunks :", len(chunks))

# 3. Embeddings
model = EmbeddingModel()

embeddings = model.encode(chunks)

print("Embeddings :", len(embeddings))

# 4. Stockage vectoriel
store = VectorStore()

store.add_embeddings(chunks, embeddings)
print("Vector store créé avec succès !")