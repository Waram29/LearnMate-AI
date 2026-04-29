from llama_cpp import Llama
import os

class LLMManager:
    def __init__(self, model_path="models/Llama-3.2-1B-Instruct-Q4_K_M.gguf"):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Modèle introuvable : {model_path}")
            
        self.llm = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=4,
            verbose=False
        )

    def generate_response(self, question, context, level="débutant"):
        instructions = {
            "débutant": "Explique simplement. Reste strictement fidèle au contexte. N'invente rien.",
            "intermédiaire": "Explique avec clarté en utilisant les termes techniques du contexte.",
            "avancé": "Analyse technique précise basée uniquement sur les données fournies."
        }
        
        prompt_instruction = instructions.get(level.lower(), instructions["débutant"])

        # On renforce la consigne de fidélité dans le System Prompt
        full_prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
Tu es une IA pédagogique rigoureuse. 
CONSIGNE CRITIQUE : Réponds en utilisant UNIQUEMENT les informations du contexte fourni. 
Si une information n'est pas dans le contexte, dis que tu ne sais pas. 
Ne fais pas d'analogies inutiles.
Niveau de réponse : {level}
Instruction : {prompt_instruction}<|eot_id|>
<|start_header_id|>user<|end_header_id|>
CONTEXTE :
{context}

QUESTION :
{question}<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>"""

        output = self.llm(
            full_prompt,
            max_tokens=256,  # Limite la longueur de la réponse pour éviter les digressions
            temperature=0.1,  # RÉGLAGE CLÉ : Presque aucune créativité pour éviter les hallucinations
            top_p=0.9,
            repeat_penalty=1.2,
            stop=["<|eot_id|>"],
            echo=False
        )
        
        return output["choices"][0]["text"].strip()

# from llama_cpp import Llama
# import os

# class LLMManager:
#     def __init__(self, model_path="models/Llama-3.2-1B-Instruct-Q4_K_M.gguf"):
#         if not os.path.exists(model_path):
#             raise FileNotFoundError(f"⚠️ Modèle introuvable ! Place le fichier GGUF dans : {model_path}")
            
#         print("Chargement du modèle...")
#         # Configuration optimisée pour i5-8265U
#         self.llm = Llama(
#             model_path=model_path,
#             n_ctx=2048,      # Mémoire de travail (tokens)
#             n_threads=4,     # Utilise 4 cœurs de ton processeur
#             n_batch=512,     # Vitesse de traitement par lot
#             verbose=False    # Cache les logs techniques pour une console propre
#         )

#     def generate_response(self, question, context, level="débutant"):
#         # Les instructions selon le niveau demandé par ton prof
#         instructions = {
#             "débutant": "Explique de manière très simple, avec des analogies, sans jargon technique.",
#             "intermédiaire": "Donne une explication équilibrée avec des exemples concrets du cours.",
#             "avancé": "Fournis une analyse technique approfondie, utilise le jargon expert et sois précis."
#         }
        
#         prompt_instruction = instructions.get(level.lower(), instructions["débutant"])

#         # Format de prompt spécifique à Llama 3.2
#         full_prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
# Tu es LearnMate AI. Ta mission est d'aider l'étudiant à comprendre son cours.
# Instruction : {prompt_instruction}
# Utilise UNIQUEMENT le contexte suivant pour répondre.<|eot_id|>
# <|start_header_id|>user<|end_header_id|>
# CONTEXTE :
# {context}

# QUESTION :
# {question}<|eot_id|>
# <|start_header_id|>assistant<|end_header_id|>"""

#         output = self.llm(
#             full_prompt,
#             max_tokens=1024,
#             temperature=0.7, # Un peu de créativité pour l'explication
#             stop=["<|eot_id|>"],
#             echo=False
#         )
        
#         return output["choices"][0]["text"].strip()
