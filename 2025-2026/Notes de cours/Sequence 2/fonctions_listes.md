### Fonctions sur les listes

On peut définir des fonctions qui prennent en paramètre des variables représentant des listes. On pourrait par exemple mettre dans une fonction le code qu'on a déjà vu :
```python
def affiche(liste):
"""
Affiche les éléments de la liste, un par ligne.
"""
    for elem in liste:
        print(elem)
```
Un autre exemple :
```python
def somme(liste):
    """
Calcule la somme des éléments de la liste,
si liste contient exclusivement des entiers ou des flottants.
Sinon, la fonction soulève une erreur.
"""
    somme = 0
    for elem in liste:
        somme += elem
    return somme
```

#### En place, hors place

On pourrait aussi définir une fonction qui calcule une liste à partir d'une liste donnée en paramètre :
``` python
def garde_les_positifs(liste):
    """
Renvoie une liste contenant seulement les entiers positifs présents de liste.
>>> garde_les_positifs([5, 1, 3, 8])
[5, 1, 3, 8]
>>> garde_les_positifs([5, -1, -3, 8])
[5, 8]
>>> garde_les_positifs([-5, -1, -3, -8])
[]
"""
    nouvelle_liste = []
    for elem in liste:
        if elem > 0:
            nouvelle_liste.append(elem)
    return nouvelle_liste
```

**Remarque :** Cette fonction *ne modifie pas* son paramètre `liste`.

Une **différence très importante** par rapport à ce qu'on a vu jusqu'à présent est que lorsqu'un de ses paramètres est une liste, une fonction *peut la modifier*. Par exemple :
``` python
def echange_indices(liste, i, j):
    """
Échange les éléments d'indice i et j de la liste.
"""
    tmp = liste[i]
    liste[i] = liste[j]
    liste[j] = tmp
```
On parle de modification *en place*. Lorsqu'une fonction crée une nouvelle liste plutôt que de modifier son paramètre, en parle de fonction *hors place*. En version hors-place, la fonction ci-dessus s'écrirait :
``` python
def echange_indices_hors_place(liste, i, j):
    """
Renvoie une copie de liste où les éléments d'indice i et j ont été échangés
"""
    nouvelle_liste = liste.copy() # Crée une copie de la liste
    tmp = liste[i]
    nouvelle_liste[i] = liste[j]
    nouvelle_liste[j] = tmp
```
*Remarque :* ici, il n'y a en réalité pas besoin de la variable `tmp` !

Le fait que les fonctions puissent modifier les listes qu'elles prennent en paramètre peut se révéler très pratique. C'est aussi parfois une importante source de bugs !


#### Exemple : un jeu de morpion

Voir le fichier `morpion_complet.py`.

