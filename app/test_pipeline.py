import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.pdf_loader import load_pdf
from modules.chunker import split_text
from modules.embeddings import EmbeddingModel


# 1. Charger PDF
text = load_pdf("data/raw_pdfs/test.pdf")

# 2. Chunking
chunks = split_text(text)

print("Nombre de chunks :", len(chunks))

# 3. Embeddings
model = EmbeddingModel()

embeddings = model.encode(chunks)

print("Nombre d'embeddings :", len(embeddings))
print("Dimension d'un embedding :", len(embeddings[0]))
