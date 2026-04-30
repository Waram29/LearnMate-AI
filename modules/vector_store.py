import chromadb
import os

class VectorStore:

    def __init__(self):
        # Définition du chemin absolu pour la persistance
        self.db_path = os.path.abspath("./vector_db")

        # Vérifier si le répertoire existe, sinon, le créer
        if not os.path.exists(self.db_path):
            os.makedirs(self.db_path)
            print(f"Le répertoire {self.db_path} a été créé.")
            
        self.client = chromadb.PersistentClient(path=self.db_path)

        # Création ou récupération de la collection
        self.collection = self.client.get_or_create_collection(
            name="embeddings_collection"
        )

    def add_embeddings(self, chunks, embeddings):
        # Génération des IDs uniques
        ids = [str(i) for i in range(len(chunks))]
        
        # Préparation des métadonnées (dictionnaire pour chaque chunk)
        metadatas = [{"text": text} for text in chunks]

        # Ajout des données dans la collection
        self.collection.add(
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        
    def get_collection_count(self):
        """Utile pour vérifier que les données sont bien présentes."""
        return self.collection.count()
    

# import chromadb
# from chromadb.config import Settings

# class VectorStore:

#     def __init__(self):
#         self.client = chromadb.Client(
#             Settings(
#                 persist_directory="vector_db",
#                 anonymized_telemetry=False
#             )
#         )

#         self.collection = self.client.get_or_create_collection(
#             name="learnmate_collection"
#         )

#     def add_embeddings(self, chunks, embeddings):

#         ids = [str(i) for i in range(len(chunks))]

#         self.collection.add(
#             documents=chunks,
#             embeddings=embeddings,
#             ids=ids
#         )

#     def persist(self):
#         self.client.persist()