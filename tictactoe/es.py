def affichier_grille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" *  9)

def initialiser_grille():
    return [[ " " for _ in range(3)] for _ in range(3)]


grille = initialiser_grille()
print(grille)

affichier_grille(grille)