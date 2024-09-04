
#Fonction pour afficher les gris
def afficher_grille(gri):
    for ligne in gri:
        print(" | ".join(ligne))
        print('-' *9 )

def initialiser_grille():
    return [[" " for _ in range(3)] for _ in range(3)]

# Initializer la grille
grille = initialiser_grille()

afficher_grille(grille)