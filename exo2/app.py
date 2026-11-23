import json # Module json (Slide 34)

# Liste de dictionnaires "C" (Slide 32, Slide 33, Slide 60)
C = [
    {"nom": "compte1", "solde": 1000.0},
    {"nom": "compte2", "solde": 2500.0},
    {"nom": "compte3", "solde": 500.0},
    {"nom": "compte4", "solde": 3000.0}
]

def deposer(c: dict, somme: float) -> str: # Fonction avec typage et retour JSON (Slide 34, Slide 41, Slide 42, Slide 60)
    if somme > 0:
        c["solde"] += somme 
    return json.dumps({"compte": c["nom"], "solde": c["solde"]})

def retirer(c: dict, somme: float) -> str:
    if somme > 0 and c["solde"] >= somme: 
        c["solde"] -= somme
    return json.dumps({"compte": c["nom"], "solde": c["solde"]})

def afficher(c: list) -> str:
    total = 0.0
    for compte in c:
        total += compte["solde"]
    print(f"Solde total : {total}") 
    return json.dumps({"total": total})

def filtre1000(c: list) -> str:
    res = [compte for compte in c if compte["solde"] >= 1000] # Liste compréhension (Slide 40)
    return json.dumps(res)

def trier_decroissant(c: list) -> str:
    res = sorted(c, key=lambda compte: compte["solde"], reverse=True) # Fonction lambda (Slide 43)
    return json.dumps(res)

# Point d'entrée, Slide 55

if __name__ == "__main__": 
    print(deposer(C[0], 500.0))
    print(retirer(C[0], 200.0))
    print(afficher(C))
    print(filtre1000(C))
    print(trier_decroissant(C))