def sauvegarde_fichier(fichier_de_sauvegarde, scores):
    f = open('save/' + fichier_de_sauvegarde, 'w')
    for joueur in scores:
        f.write(joueur)
        f.write('\n')
        f.write(str(scores[joueur]))
        f.write('\n')
    f.close()


def recupere_sauvegarde(fichier_de_sauvegarde):
    f = open('save/' + fichier_de_sauvegarde, 'r')
    mode_pseudo = True
    scores = {}
    dernier_pseudo = ""
    for ligne in f:
        if mode_pseudo:
            dernier_pseudo = ligne
        else:
            score = int(ligne)
            scores[dernier_pseudo] = score
        mode_pseudo = not mode_pseudo
    return scores


def main():
    scores = {'qsdf89': 25, 'yoplait': 28, 'azerath': 35}
    fichier_de_sauvegarde = input('Où voulez-vous sauvegarder vos scores ?')
    sauvegarde_fichier(fichier_de_sauvegarde, scores)
    save = recupere_sauvegarde(fichier_de_sauvegarde)
    print(save)


if __name__ == "__main__":
    main()
