def sauvegarde_basic(pseudos, fichier):
    f = open(fichier, 'w')  # w = write
    for pseudo in pseudos:
        f.write(pseudo)
        f.write('\n')
    f.close()


# On préfère utiliser la syntaxe suivante pour ouvrir des fichiers
# Ça permet d'éviter de devoir penser à fermer le fichier
def sauvegarde(pseudos, fichier):
    with open(fichier, 'w') as f:  # w = write
        for pseudo in pseudos:
            f.write(pseudo)
            f.write('\n')


def recuperer_sauvegarde(fichier):
    with open(fichier, 'r') as f:  # r = read
        pseudos = []
        for ligne in f:
            pseudo = ligne.strip('\n')  # Pour retirer le retour à la ligne
            pseudos.append(pseudo)
        return pseudos


def main():
    pseudos = ["aze89", "yoplait", "azareth"]
    # On enregistre les pseudos sur un fichier
    sauvegarde(pseudos, 'pseudos.txt')
    # On les récupère
    pseudos_bis = recuperer_sauvegarde('pseudos.txt')
    print(pseudos_bis)


if __name__ == "__main__":
    main()
