from llama_cpp import Llama


class LocalLLM:
    def __init__(self, model_path):
        print("Chargement du modèle LLM...")
        self.llm = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=4, # Utilise 4 cœurs du processeur, adapté au CPU,
            verbose=False
        )
        # print("Modèle LLM prêt.")

    def generate(self, prompt):
        response = self.llm(
            prompt,
            max_tokens=350, 
            temperature=0.1,  # Très faible pour éviter les hallucinations
            stop=["</s>"] # Arrête la génération à la fin de la réponse
        )

        return response["choices"][0]["text"]