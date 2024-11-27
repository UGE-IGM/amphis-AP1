def afficher_etat_jeu(joueurs):
    for joueur in joueurs:
        print(f"{joueur[0]} a la couleur {joueur[1]} et a {joueur[2]} points.")


def main():
    joueur1 = ["qsdf89", "red", 25]
    joueur2 = ["yoplait", "yellow", 20]
    joueur3 = ["azerath", "green", 28]
    joueurs = [joueur1, joueur2, joueur3]
    afficher_etat_jeu(joueurs)


if __name__ == "__main__":
    main()
