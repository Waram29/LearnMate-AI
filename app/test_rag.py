import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import chromadb
from chromadb.utils import embedding_functions

from modules.prompt import get_prompt
from modules.llm import LocalLLM


CHROMA_DIR = "./vector_db"
COLLECTION_NAME = "learnmate_docs"

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path=CHROMA_DIR)

collection = client.get_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_function
)

# Question
question = "C'est quoi le Deep Learning ?"

results = collection.query(
    query_texts=[question],
    n_results=3
)

context = "\n".join(results["documents"][0])

# Mode pédagogique
mode = "Analogy"  # Choisissez parmi "Exam", "Beginner", "Detailed", "Step-by-Step", "Analogy"

prompt = get_prompt(mode, context, question)

# LLM local
llm = LocalLLM("models/mistral-7b-instruct-v0.2.Q4_K_M.gguf")

response = llm.generate(prompt)

print("\n===== QUESTION =====\n")
print(question)
print("\n===== RÉPONSE en mode : ", mode, "=====\n")
print(response)