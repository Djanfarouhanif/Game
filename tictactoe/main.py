
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

#Postion de jouer 
def demander_position_joueur(joueur):
    while True:
        try:
            position = int(input(f"Joueur {joueur}, entrez un numéro de case (1-9):")) -1
            if position < 0 or position > 8:
                raise ValueError
            return divmod(position, 3)

        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro de case entre 1 et 9")
#Fonction pour jouer la partie
def jouer_tour(grille, joueur):
    position = demander_position_joueur(joueur)
    if grille[position[0]][position[1]] == " ":
        grille[position[0]][position[1]] = joueur
    else:
        print("Case déja occupé. Choisisszer une autre case.")
        jouer_tour(grille, joueur)

#Exécution du tour de jeu pour un joueur
joueur_actuel = "X"
jouer_tour(grille, joueur_actuel)
afficher_grille(grille)