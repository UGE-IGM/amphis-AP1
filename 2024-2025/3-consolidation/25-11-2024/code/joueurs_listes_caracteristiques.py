def afficher_etat_jeu(pseudos, couleurs, scores):
    for i in range(len(pseudos)):
        print(f"{pseudos[i]} a la couleur {couleurs[i]} et a {scores[i]} points.")


def main():
    pseudos = ["aze89", "yoplait", "azerath"]
    couleurs = ["red", "yellow", "green"]
    scores = [25, 20, 28]
    afficher_etat_jeu(pseudos, couleurs, scores)


if __name__ == "__main__":
    main()
