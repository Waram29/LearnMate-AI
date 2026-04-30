import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.llm_manager import LLMManager

def test():
    # Simulation d'un petit contexte de cours
    contexte_test = """
    Le protocole 'LearnMate-Sync' est utilisé exclusivement à l'Université de Fès. 
    Il fonctionne sur le port 9999 et utilise un algorithme de compression nommé 'Z-Fassi'. 
    Contrairement au TCP, il ne vérifie pas l'ordre des paquets mais leur empreinte thermique.
    """
    question_test = "Comment le protocole LearnMate-Sync vérifie-t-il les paquets ?"
    
    llm = LLMManager()
    
    print("\n--- TEST EN COURS (Niveau débutant) ---")
    reponse = llm.generate_response(question_test, contexte_test, level="débutant")
    print(f"RÉPONSE : {reponse}")

if __name__ == "__main__":
    test()