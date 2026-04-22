def split_text(text, chunk_size=500, overlap=100):
    """
    Découpe un texte en petits morceaux (chunks)
    pour le traitement RAG.
    """

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap  # overlap pour garder le contexte

    return chunks


# # Test rapide
# if __name__ == "__main__":
#     sample_text = "Ceci est un exemple de texte " * 100
#     chunks = split_text(sample_text)

#     print("Nombre de chunks :", len(chunks))
#     print(chunks[0])
#     for i, chunk in enumerate(chunks):
#         print(f"Chunk {i+1} : {chunk[:1000]}...")  # afficher les 100 premiers caractères de chaque chunk