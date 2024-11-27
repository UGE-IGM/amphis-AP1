def afficher_etat_jeu(joueurs):
    for joueur in joueurs:
        # On utilise une f-string pour plus de lisibilité
        print(f"{joueur['pseudo']} a la couleur {joueur['couleur']} et a {joueur['score']} points.")

    
def change_score(joueur, score):
    joueur["score"] = score


def main():
    joueur1 = {'pseudo': 'qsdf89',
               'couleur': 'red',
               'score': 25}
    joueur2 = {'pseudo': 'yoplait',
               'couleur': 'yellow',
               'score': 20}
    joueur3 = {'pseudo': 'azerath',
               'couleur': 'green',
               'score': 28}
    joueurs = [joueur1, joueur2, joueur3]
    change_score(joueur3, 35)
    afficher_etat_jeu(joueurs)


if __name__ == "__main__":
    main()
