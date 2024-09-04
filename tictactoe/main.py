
#Fonction pour afficher les gris
def afficher_grille(gri):
    for ligne in gri:
        print(" | ".join(ligne))
        print('-' *9 )

def initialiser_grille():
    return [[" " for _ in range(3)] for _ in range(3)]


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


def verifier_victoire(grille,joueur):
    #Vérifier les lignes
    for ligne in grille:
        if all([case == joueur for case in ligne]):
            return True

    #Vérifier les colnnes
    for col in range(3):
        if all([grille[ligne][col] == joueur for ligne in range(3)]):
            return True

    #Vérifier les diagonales
    if all([grille[i][i] == joueur for i in range(3)]) or all([grille[i][2 - 1] == joueur for i in range(3)]):
        return True

    return False

def verifier_egalite(grille):
    return all([case !=  " "  for ligne in grille for case in ligne])

def boucle_principale_du_jeu():
    grille = initialiser_grille()
    joueur_actuel = "X"

    while True:
        afficher_grille(grille)
        jouer_tour(grille, joueur_actuel)
        if verifier_victoire(grille, joueur_actuel):
            afficher_grille(grille)
            print(f"Félicitations, Joueur {joueur_actuel } a gagné")
            break

        if verifier_egalite(grille):
            afficher_grille(grille)
            print("Match nul !")
            break
        #Alterner entre les joueurs
        joueur_actuel = "O" if joueur_actuel == "X" else "X"
boucle_principale_du_jeu()
    