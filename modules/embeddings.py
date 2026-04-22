from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """
        Initialise le modèle d'embedding.
        """
        print("Chargement du modèle embeddings...")
        self.model = SentenceTransformer(model_name)
        print("Modèle prêt.")

    def encode(self, chunks):
        """
        Convertit les chunks en embeddings.
        """
        embeddings = self.model.encode(chunks)
        return embeddings


# # Test rapide
# if __name__ == "__main__":
#     model = EmbeddingModel()

#     test_chunks = [
#         "L'intelligence artificielle est un domaine fascinant.",
#         "Les réseaux neuronaux sont utilisés en machine learning."
#     ]

#     vectors = model.encode(test_chunks)

#     print("Nombre de vecteurs :", len(vectors))
#     print("Dimension d'un vecteur :", len(vectors[0]))
#     print("Premier vecteur :", vectors[0][:20], "...")  # afficher les 5 premiers éléments du premier vecteur