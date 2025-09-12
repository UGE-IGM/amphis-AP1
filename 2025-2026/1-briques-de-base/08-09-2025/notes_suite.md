
## Modèle de mémoire de Python 

*Modèle de mémoire : une image simplifiée de la manière dont fonctionne la mémoire de l'interpréteur Python*

Deux zones principales :
- la zone des données (le « tas », en anglais *heap*)
- la zone des espaces de noms (la « pile », en anglais *stack*)

Dans Python Tutor : pile à gauche, tas à droite

#### Le tas

Le tas est comme un *très* gros cahier dans lequel sont décrits les objets manipulés par un programme
- Chaque objet décrit dans le cahier commence à un certain numéro de page, qu'on appelle son *adresse*
- Certaines pages sont blanches, d'autres sont remplies

#### La pile

La pile est comme l'index du cahier

- À chaque variable est associé le numéro de page d'un objet
- Un groupe de variables et les numéros de page correspondants est appelé **espace de noms**
- La pile contient l'espace de noms **global**, contenant les noms définis par nos programmes  
  *(en réalité la pile contient aussi d'autres espaces de noms, on en reparlera)*


```python
%%nbtutor -r -f
x = 3
y ='UGE'
z = x + 2
```

#### La notion d'état

L'**état** de l'interpréteur pendant l'exécution c'est

- le numéro de la ligne suivante à exécuter dans le programme
- le contenu de diverses variables internes de l'interpréteur
- le contenu de la pile (donc tous les espaces de noms)
- le contenu du tas (donc toutes les données du programme)

à un moment donné. Les **instructions** modifient généralement l'état.

#### Étapes d'une affectation 

##### Affectation simple


```python
x = 40 + 2
```

1.  Évaluation de l'expression à droite du `=` (ici `42`)

    ![affectation1.png](img/affectation1.png)

    La valeur `42` de type `int` est stockée dans le tas *(écrite sur une page du cahier)*

2. Création du nom `x` dans l'espace de noms (sauf s'il existe déjà)
   ![affectation2.png](img/affectation2.png)
   On ajoute `x` à la pile *(on ajoute une ligne pour `x` à l'index du cahier)*

3. Création du lien entre *variable* et *valeur*
   ![affectation3.png](img/affectation3.png)
   L'adresse de l'objet `42` est associée à la variable `x` *(on écrit dans l'index le numéro de la page contenant l'objet `42` à `x`)*

##### Deuxième exemple


```python
y = x
```

<img src='img/warning.png' width=50px style='display:inline'> Dans cet exemple le `x` en partie droite de l'affectation désigne la **valeur** actuellement associée à la variable `x` !

1. Calcul du *membre droit* après remplacement de chaque variable par la valeur associée (ici `x` remplacé par `42`)
    ![affectation4.png](img/affectation4.png)

2. Création du nom `y` (sauf si déjà créé) 
    ![affectation5bis.png](img/affectation5_bis.png)

3. Création du lien entre `y` et `42`
    ![affectation5.png](img/affectation5.png)

#### Troisième exemple


```python
x = x + 1
```

<img src='img/warning.png' width=50px style='display:inline'> Dans cet exemple, le `x` de gauche désigne le nom `x` lui-même, mais celui de droite désigne la **valeur** actuellement associée à `x`

1. Calcul du *membre droit* après remplacement de chaque variable par la valeur associée (ici `x` remplacé par `42`, résultat : `43`)
    ![affectation6.png](img/affectation6.png)

2. Nom `x` déjà existant, création du lien entre `x` et 43
    ![affectation7.png](img/affectation7.png)

#### <img src='img/warning.png' width=50px style='display:inline'> Piège !

Que vaut maintenant `y` ?


```python
y

```

Même si `x` et `y` désignaient avant le même objet (la même adresse, le même *numéro de page*), changer la page que désigne `x` n'a aucun effet sur `y` ! On n'a pas *modifié* l'objet 42, qui est toujours là !


```python
%%nbtutor -r -f
x = 40 + 2
y = x
x = x + 1
```

**Remarque :** L'instruction `x = x + 1` peut aussi s'écrire `x += 1`. On appelle cela une **incrémentation** de `x`.


```python
x += 1
```

De même, `x *= 2` est une version plus concise de `x = x * 2`.

##### Dernier exemple


```python
x = -6.5
```

![affectation8.png](img/affectation8.png)

##### <img src='img/warning.png' width=50px style='display:inline'> Quelques points de détail

- On peut réaffecter une valeur de type différent à une variable (comme dans le dernier exemple)
- En cas de réaffectation, le lien précédent est oublié
- Quand aucun lien n'existe vers un objet, il est "détruit" par le ramasse-miettes ou *garbage collector* (la page est effacée !)

##### Exercice : état de la mémoire après une suite d'affectations

Dessiner l'état de la mémoire à l'issue des instructions suivantes :


```python
x = 2
y = 3
x += y
y *= 2
```

#### Nommage des variables

Règles de nommage des variables :

- Commencent par une *lettre*, suivie de *lettres et de chiffres*
- Le caractère *underscore* `'_'` est considéré comme une lettre
- Éviter les caractères spéciaux (accents, cédille, etc.)
- Les *mots réservés* (ou mots-clés) de Python sont interdits
- Il y a aussi des **conventions** (*vues plus tard*)

*Exemples :*  `_ex2   Ex2mpl1`

*Contre-exemple :*  `2024eiffel`

##### Mots-clés et autres mots réservés

Les mots suivants sont **réservés** pour le langage :

```python
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

https://docs.python.org/fr/3/reference/lexical_analysis.html#keywords

##### Exercice : nommage de variables

Indiquer parmi les mots suivants ceux qui ne sont pas des noms valides pour une variable :
  
```
    bonjour                Hi!                  au revoir              oui
    Ciao                   NON                  byeBye7                6hello6
    abc                    def                  6hello6                _upem_
    good_morning           __repr__             good-afternoon         f()
```



## Saisie et affichage 

Fonction de saisie : `x = input("Veuillez rentrer ...")`
  
- L'utilisateur tape une ligne au clavier
- La ligne est stockée sous forme de chaîne de caractères (`str`)
- Cette valeur peut ensuite être affectée à une variable (ici `x`)
- Le message d'invite pour l'utilisateur est facultatif

https://docs.python.org/fr/3/library/functions.html#input


```python
nb_personnes_ref = 2
nb_convives = input("Combien de personnes ? ")
rapport = nb_convives / nb_personnes_ref
```


```python
nb_personnes_ref = 2
# on convertit immédiatement le texte saisi en int :
nb_convives = int(input("Combien de personnes ? "))
rapport = nb_convives / nb_personnes_ref
```

Fonction d'affichage : `print(x)`
  
- Affiche dans le terminal la chaîne de caractères associée à `x`
- On peut afficher plusieurs valeurs à la suite : `print(x, y, z, ...)`
- Appelle automatiquement la fonction `str` sur chacun de ses arguments
- S'il y a plusieurs arguments, insère automatiquement des espaces
- Passe automatiquement à la ligne

https://docs.python.org/fr/3/library/functions.html#print


```python
nb_personnes_ref = 2
# on convertit immédiatement le texte saisi en int :
nb_convives = int(input("Combien de personnes ? "))
rapport = nb_convives / nb_personnes_ref
print("Je multiplie toutes les quantités par", rapport)
```

**Remarque :** *Il existe de nombreuses possibilités pour l'affichage de texte, consulter la [documentation officielle](https://docs.python.org/fr/3/tutorial/inputoutput.html) pour plus de détails.*



# Structures de contrôle 

Les programmes et algorithmes les plus simples consistent à exécuter des instructions les unes après les autres, en **séquence**. C'est néanmoins très vite limité : il arrive fréquemment qu'on ait envie d'agir d'une certaine façon dans un cas et d'une autre dans un autre. Typiquement, on voudrait pouvoir continuer le programme de manière adaptée à une entrée de l'utilisateur. 

On va donc s'intéresser aux structures dites *conditionnelles*. Ces structures permettent de *"brancher"* dans le code en fonction de l'évaluation d'une condition, que l'on exprime sous forme d'**expression booléenne**.

Faisons donc d'abord un point sur ce type très important d'expressions :

## Expressions booléennes 

Les instructions conditionnelles sont écrites à l'aide d'**expressions booléennes**, c'est à dire d'expressions qui s'évaluent en un valeur de type `bool` (`True` ou `False`).

Elles peuvent contenir des opérateurs de comparaison, des opérateurs logiques, etc.

## Opérateurs de comparaison

```python
a < b   # a strictement inférieur b
a <= b  # a inférieur ou égal à b
a >= b  # a supérieur ou égal à b
a > b   # a strictement supérieur à b
```

- `a` et `b` sont des **expressions**
- elles doivent s'évaluer en des valeurs **de même type** (sauf exceptions)


Les opérateurs de comparaison fonctionnent sur de nombreux types de valeurs
- Sur les `int` et `float` : ordre habituel sur les nombres
- Sur les `str` : ordre *lexicographique* (dictionnaire)
- Sur d'autres types qu'on verra plus tard

![](img/warning.png){ width=50px } **Rappel :** on ne peut pas ordonner des valeurs de types différents (sauf des nombres) ! 

## Égalité ou inégalité 

```python
a == b  # a égal à b
a != b  # a différent de b
```

- `a` et `b` sont des **expressions**
- elles peuvent être de types différents


Les opérateurs `==` et `!=` acceptent des opérandes de types différents
- renvoie généralement `False` si les opérandes sont de types différents
- sauf parfois entre nombres

![](img/warning.png){ width=50px } **Attention !** Ne pas confondre l'opérateur d'égalité (`==`) avec la syntaxe de l'affectation (`=`) !


```python
17 % 2 == 1
```


```python
a = -5
a != abs(a)
```


```python
1.0 == 3 - 2  # l'égalité fonctionne aussi avec les float...
```


```python
0.3 == 3 * 0.1  # mais réserve parfois des surprises
```

Les opérateurs `==` et `!=` acceptent des opérandes de types différents
- renvoie généralement `False` si les opérandes sont de types différents
- sauf parfois entre nombres


```python
2 == '2'
```


```python
'bonjour' != None
```


```python
2 == 2.0  # Cas particulier : vrai car float(2) == 2.0
```

![](img/warning.png){ width=50px } **Attention !** Ne pas confondre l'opérateur d'égalité (`==`) avec la syntaxe de l'affectation (`=`) !



## Opérateurs logiques 

On peut combiner plusieurs expressions booléennes `a` et `b` à l'aide d'opérateurs logiques, inspirés de la logique mathématique.

On peut résumer le comportement de ces opérateurs à l'aide de tableaux, appelés **tables de vérité**.

### Négation

L'expression `not a` vaut `True` si `a` s'évalue en `False`, et `False` sinon (correspond à $\lnot a$).

`a`     | `not a` 
--------|---------
`True`  | `False`
`False` | `True`   

### Conjonction

L'expression `a and b` vaut `True` si `a` et `b` s'évaluent toutes les deux en `True`, et `False` sinon (correspond à $a \land b$).

`a`| `b` | `a and  b`
---|---|---
`True` | `True` | `True` 
`True` | `False` | `False` 
`False` | `True` | `False` 
`False` | `False` | `False`

### Disjonction

L'expression `a or b` vaut `True` si `a` s'évalue en `True` ou `b` s'évalue en `True`, et  `False` sinon (correspond à $a \lor b$).

`a` | `b` | `a or  b`
---|---|---
`True` | `True` | `True` 
`True` | `False` | `True` 
`False` | `True` | `True` 
`False` | `False` | `False`


```python
not (3 + 4 != 7)
```


```python
4 < 1 or 'Bonjour' >= 'Au revoir'
```

![](img/non-exigible.png){ width=50px } En réalité les opérateurs `and` et `or` ont un comportement un peu spécial appelé **évaluation séquentielle** : on n'évalue le deuxième opérande que si c'est nécessaire pour déterminer le résultat.

- `a and b` est à peu près équivalent à `b if a else a`
- `a or b` est à peu près équivalent à `a if a else b`

Cela signifie qu'on n'évalue pas toujours `b` dans `a and b` et dans `a or b`. Par exemple :


```python
1/0  # erreur : division par 0
```


```python
True or 1/0 == 1    # ne provoque pas d'erreur !
```


```python
False and 1/0 == 1  # ne provoque pas d'erreur !
```

![](img/non-exigible.png){ width=50px } En Python, presque tout objet possède une valeur de vérité et peut s'utiliser comme un booléen... mais les règles sont un peu complexes.

Par exemple :

- les nombres égaux à 0 sont interprétés comme "faux"
- la chaîne vide est interprétée comme "faux"
- la valeur `None` est interprétée comme "faux", etc.

Tout le reste est interprété comme "vrai"

Si on combine ces deux aspects du langage, ça peut donner des choses assez surprenantes...


```python
'patate' and 'courgette'
```




    'courgette'




```python
'patate' or 'courgette'
```




    'patate'



Ce comportement est largement **hors programme** et non exigible !



### Quelques règles utiles

#### Lois de De Morgan

- dire "non (a ou b)" revient à dire "(non a) et (non b)"
- dire "non (a et b)" revient à dire "(non a) ou (non b)"

En Python :

```python
not (a and b) == (not a) or (not b)  # vrai pour tous a et b
not (a or b) == (not a) and (not b)  # vrai pour tous a et b
```

#### Distributivité

- la conjonction est distributive sur la disjonction
- la disjonction est distributive sur la conjonction

En Python :

```python
a and (b or c) == (a and b) or (a and c)  # vrai pour tous a, b et c
a or (b and c) == (a or b) and (a or c)   # vrai pour tous a, b et c
```

#### Commutativité

- `a and b` est (presque) équivalente à `b and a` (mais elle change l'ordre d'évaluation)
- `a or b` est (presque) équivalente à `b or a` (idem)

#### Absorption

- `a or True` est (presque) équivalente à `True`
- `True or a` est équivalente à `True`

- `a and False` est (presque) équivalente à `False`
- `False and a` est équivalente à `False`

#### Invariance

- `a and True` est (presque) équivalente à `a`
- `True and a` est équivalente à `a`

- `a or False` est (presque) équivalente à `a`
- `False or a` est équivalente à `a`

#### Égalité et négation

- `not a == b` est équivalent à `a != b`
- `not a != b` est équivalent à `a == b`

#### Comparaisons et opérateurs logiques

- `a < b` est équivalent à `a <= b and a != b`
- `a <= b` est équivalent à `a < b or a == b`
- `a > b` est équivalent à `a >= b and a != b`
- `a >= b` est équivalent à `a > b or a == b`

#### Comparaisons et négation

- `not a < b` est équivalent à `a >= b` ou encore `b <= a`
- `not a <= b` est équivalent à `a > b` ou encore `b < a`
- `not a > b` est équivalent à `a <= b` ou encore `b >= a`
- `not a >= b` est équivalent à `a < b` ou encore `b > a`


```python
x = -1
inf, sup = 0, 10
x >= inf and x <= sup
```


```python
x = -1
inf, sup = 0, 10
x < inf or x > sup
```


```python
x = 1
inf, sup = 0, 10
not (x < inf or x > sup)
```


```python
x = 12
inf, sup = 0, 10
not (x >= inf and x <= sup)
```

Si `£` et `¥` représentent des opérateurs de comparaison, 
```python
exp1 £ exp2 ¥ exp3
```
est une abréviation de 
```python
exp1 £ exp2 and exp2 ¥ exp3
```



### Enchaînement de comparaisons

![](img/non-exigible.png){ width=50px } En Python on peut rassembler plusieurs comparaisons successives en une seule expression (c'est impossible dans de nombreux autres langages).


```python
x, inf, sup = 1, 0, 10
inf <= x <= sup
```


```python
a, b, c = 1, 1, 2
a == b == c
```

**Attention**, cela mène parfois à des écritures un peu bizarres...


```python
x, inf, sup = 1, 4, 10
inf < sup > x  # ???
```


```python
a = 1
b = 2
c = 1
a != b != c
```

### Exercice : multiple de 3 ou 5

Étant donnée une variable `x` désignant un nombre,
1. écrire deux expressions booléennes différentes qui valent `True` si `x` est un multiple de 3 et de 5 et `False` sinon, 
2. écrire deux expressions booléennes différentes qui valent `True` si `x` n'est un multiple ni de 3 ni de 5 et `False` sinon.


```python
x = 10
x % 3 == 0 and x % 5 == 0
```


```python
x = 7
not(x % 3 == 0) and not(x % 5 == 0)
```

### Exercice

Donner le résultat des expressions logiques suivantes pour les valeurs indiquées de `a`, `b` et `c`


```python
a, b, c = 10, 2, 6
a < b or a > c
```


```python
a, b, c = 10, 2, 6
a + b < 2 * c
```


```python
a, b, c = 10, 2, 6
a - b == b + c
```


```python
a, b, c = 10, 2, 6
(a > b and a > c) or (b > a and b > c)
```


```python
a, b, c = 10, 2, 6
a < b < c
```


```python
a, b, c = 10, 2, 6
a == b == c
```


```python
a, b, c = 10, 2, 6
(a <= b and a <= c) or not (b < a)
```


```python
a, b, c = 10, 2, 6
not (a > b and a > c) or (b > a and b > c)
```



# Instructions conditionnelles 

## Cas simple : Conditionnelle `Si` 
On peut maintenant modifier le flot d'instructions selon la valeur d'expressions booléennes, ou conditions :

- **Si** une certaine condition est vraie, exécuter un certain groupe (ou bloc) d'instructions
- **Sinon**, passer directement à la suite du programme
![](img/conditionnelle1.png){ width=300px }

La syntaxe d'une instruction conditionnelle est :

```python
# début
if condition:
    # bloc 
    # d'instructions
    # indenté
# suite (*)
```

- Ici `condition` est une expression booléenne
- Les instructions du bloc **v** sont exécutées uniquement si `condition` est évaluée à `True`
- Dans tous les cas, l'exécution reprend à l'instruction suivant le bloc indenté (ligne `suite (*)`)

### Exemple : pile ou face ?
Un programme qui :
1. tire un nombre au hasard entre `0` et `1`
2. affiche `pile` s'il a tiré `1`, `face` s'il a tiré `0`


```python
from random import randint # randint permet de tirer un nombre aléatoire

tirage = randint(0,1)
print(tirage)
if tirage == 1:
    print("pile")
    
if tirage == 0:
    print("face")
```

### Exemple : mettre deux chaînes dans l'ordre

Supposons qu'il existe deux variables `a` et `b` désignant des `str`. 

Écrire un bout de programme qui modifie ces variables pour que `a` désigne la plus petite chaîne et `b` la plus grande (dans l'ordre lexicographique)


```python
a = input()
b = input()
if a > b:
    # on intervertit les valeurs
    temp = a  # variable temporaire
    a = b
    b = temp
print(a, b)
```


```python
a = input()
b = input()
if a > b:
    # variante
    a, b = b, a
print(a, b)
```

## La notion de bloc

Sur cet exemple, on a vu un groupe de lignes commençant par des espaces, appelé **bloc**. Un bloc est utilisé pour regrouper plusieurs instructions dépendant de la même condition.

- Un tel groupe d'instructions est appelé un **bloc**
- Le décalage du début de ligne est appelé **indentation**
- Un bloc se termine quand une ligne **moins indentée** apparaît (sur l'exemple : `print(a, b)`)

- Pour indenter la ligne courante : touche "tabulation" (⇥) 
- Pour désindenter une ligne : "Shift + tabulation" (⇧ + ⇥)
- Changer l'indentation change le sens du programme (essayez !)


```python
from random import randint # randint permet de tirer un nombre aléatoire

tirage = randint(0,1)
print(tirage)
if tirage == 1:
    print("Le résultat est :")
    print("pile")
    
if tirage == 0:
    print("Le résultat est :")
    print("face")
```

### Erreurs fréquentes liées à l'indentation :


```python
if a > b  # oubli des deux points (:)
    temp = a
    a = b
    b = temp
```


```python
if a > b:
    temp = a
    a = b
   b = temp  # ligne pas assez indentée 
```


```python
if a > b:
    temp = a
    a = b
     b = temp  # ligne trop indentée 
```


```python
if a > b:
a, b = b, a  # oubli d'indentation
```

## Conditionnelles `Si ... Sinon ...`



On peut ajouter un second bloc d'instructions
- **Si** une certaine condition est vraie, exécuter le premier bloc
- **Sinon**, exécuter le second
- Enfin, continuer l'exécution normale du programme

Syntaxe :

```python
# début
if condition:
    # bloc v
else:
    # bloc f
# suite
```

Ici `condition` est une expression booléenne

Seul *l'un des deux* blocs d'instructions, **v** *ou bien* **f**, est exécuté
- Le bloc **v** uniquement si `condition` est évaluée à `True`
- Le bloc **f** uniquement si `condition` est évaluée à `False`
- Dans tous les cas, reprise à l'instruction suivant le bloc **f**

<img src='img/conditionnelle2.png' width='30%'>

### Exemple : division euclidienne


```python
dividende = int(input("Donnez moi un dividende : "))
diviseur = int(input("Donnez moi un diviseur : "))
if diviseur != 0:
    quotient = dividende // diviseur
    reste = dividende % diviseur
    print(dividende, '=', quotient, '*', diviseur, '+', reste)
else:
    print('Erreur : division par zéro')
```

## Exemple : pile ou face ?


```python
from random import randint # randint permet de tirer un nombre aléatoire

tirage = randint(0,1)
print(tirage)
if tirage == 1:
    print("pile")
    
if tirage == 0:
    print("face")
```


```python
from random import randint # randint permet de tirer un nombre aléatoire

tirage = randint(0,1)
print(tirage)
if tirage == 1:
    print("pile")
else: # Dans ce cas, tirage vaut nécessairement 0
    print("face")
```

## Exercice

Écrire un programme qui permet de jouer à pile ou face :
1. Demander à l'utilisateur de saisir `1` pour `pile` et `0` pour face
2. Tirer un nombre au hasard, l'afficher et afficher `Gagné !` ou `Perdu !` en fonction du résultat

On pourra améliorer le programme pour permettre de saisir directement `pile` ou `face` plutôt que `1` ou `0`.


```python
from random import randint
nombre_choisi = int(input("Pile (1) ou face (0) ? "))
tirage = randint(0,1)
if tirage == nombre_choisi:
    print("Gagné !")
else:
    print("Perdu !")
```


```python
from random import randint
choix = input("pile ou face ? ")
if choix == "pile":
    nombre_choisi = 1
else:
    nombre_choisi = 0
tirage = randint(0,1)
if tirage == 1:
    print("Le résultat est pile.")
else:
    print("Le résultat est face.")
if tirage == nombre_choisi:
    print("Gagné !")
else:
    print("Perdu !")
```

#### Exercices

1. Écrire un programme qui saisit un nombre entier et affiche `positif` si l'entier est positif ou nul et `negatif` sinon.
2. Écrire un programme qui saisit deux nombres entiers et affiche le plus grand des deux.


```python
entier = int(input("Donnez moi un entier : "))
if entier >= 0:
    print("positif")
else:
    print("negatif")
```


```python
entier1 = int(input("Donnez moi un premier entier : "))
entier2 = int(input("Donnez moi un deuxième entier : "))
print("L'entier le plus grand est", end = " ")
if entier1 > entier2:
    print(entier1)
else:
    print(entier2)    
```

## Conditionnelles composées

Cette construction peut être imbriquée :

```python
# début
if <condition 1>:
    if <condition 2>:
        # bloc v1v2
    else:
        # bloc v1f2
    # suite 2
else:
    # bloc f1
# suite 1
```

Toutes les variantes sont possibles — si chaque `else` correspond à un `if` de même indentation !

<img src='img/conditionnelle3.png' width='60%' style='display:inline'>

### Exemple : pile ou face, deux fois
Écrire un programme qui tire deux fois à pile ou face et affiche `Gagné` si les deux tirages sont `pile`, `Perdu` sinon.


```python
from random import randint
tirage1 = randint(0,1)
print("Premier tirage :", tirage1)
if tirage1 == 1:
    tirage2 = randint(0,1)
    print("Second tirage :", tirage2)
    if tirage2 == 1:
        print("Gagné")
    else:
        print("Perdu")
else:
    print("Perdu")
```

### Exemple : discriminant

On suppose qu'il existe trois variables `a`, `b` et `c` désignant des nombres. On veut déterminer le nombre de solutions réelles de l'équation `a`$x^2$ + `b`$x$ + `c` = 0. Les cas suivants sont à considérer :

-   si `a` = `b` = `c` = 0, il y a une infinité de solutions
-   si `a` = `b` = 0 et `c` $\neq$ 0, il n'y a pas de solution
-   si `a` = 0 et `b` $\neq$ 0, il y a exactement une solution
-   sinon, on calcule le discriminant
    $\Delta$ = `b`$^2$ - 4`ac` et,
    -   si $\Delta < 0$, il n'y a pas de solution ;
    -   si $\Delta = 0$, il y a exactement une solution ;
    -   sinon $\Delta > 0$ et il y a exactement deux solutions.

Écrire un programme qui demande à l'utilisateur de saisir au clavier
les trois valeurs `a`, `b` et `c` et qui calcule et affiche le
nombre de solutions **réelles** de l'équation du second degré associée.


```python
a, b, c = ...

# Calcul et affichage du nombre de solutions
if a == 0:
    if b == 0:
        if c == 0:
            print("Une infinité de solutions")
        else:
            print("Pas de solution")
    else :
        print("Une solution")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Pas de solution")
    else:
        if delta == 0:
            print("Une solution")
        else:
            print("Deux solutions")
```

## Conditionnelles enchaînées 
  
Cas particulier où le bloc `else` contient seulement un autre `if` : le mot-clé `elif`

Le code...
```python
# début
if <condition 1>:
    # bloc **v1**
else:
    if <condition 2>:
        # bloc **f1v2**
    else:
        # bloc **f1f2**
# suite
```

... s'écrit aussi :
```python
# début
if <condition 1>:
    # bloc **v1**
elif <condition 2>:
    # bloc **f1v2**
else:
    # bloc **f1f2**
# suite
```

On peut ainsi enchaîner autant de conditions qu'on le souhaite, lorsque les cas ne se recouvrent pas :

```python
# début
if <condition 1>:
    # bloc **v1**
elif <condition 2>:
    # bloc **f1v2**
elif <condition 3>:
    # bloc **f1f2v3**
else:
    # bloc **f1f2f3**
# suite
```

#### Exemple : pile ou face, deux fois (variante)
Écrire un programme qui tire deux fois à pile ou face et affiche `Gagné` si les deux tirages sont différents (`pile` puis `face` ou bien `face` puis `pile`) et affiche `Perdu` sinon.


```python
from random import randint
tirage1 = randint(0,1)
print("Premier tirage :", tirage1)
tirage2 = randint(0,1)
print("Second tirage :", tirage2)
if tirage1 == 1 and tirage2 == 1:
    print("Gagné")
elif tirage1 == 0 and tirage2 == 0:
    print("Gagné")
else:
    print("Perdu")
```


```python
# Une variante
from random import randint
tirage1 = randint(0,1)
print("Premier tirage :", tirage1)
tirage2 = randint(0,1)
print("Second tirage :", tirage2)
if tirage1 == 1 and tirage2 == 1 or tirage1 == 0 and tirage2 == 0:
    print("Gagné")
else:
    print("Perdu")
```


```python
# Une autre variante
from random import randint
tirage1 = randint(0,1)
print("Premier tirage :", tirage1)
tirage2 = randint(0,1)
print("Second tirage :", tirage2)
if tirage1 == tirage2:
    print("Gagné")
else:
    print("Perdu")
```



# Boucles 
Comment faire si l'on veut répéter une instruction ?

### Exemple : pile ou face, rejouer tant qu'on perd
Écrire un programme qui nous fait rejouer à pile ou face tant qu'on perd.


```python
# Un premier essai
from random import randint
tirage = randint(0,1)
nombre_choisi = int(input("Pile (1) ou face (0) ? "))
if tirage == nombre_choisi:
    print("Gagné")
else:
    print("Perdu. Essaye encore.")
    tirage = randint(0,1)
    nombre_choisi = int(input("Pile (1) ou face (0) ? "))
    if tirage == nombre_choisi:
        print("Gagné")
    # ...
    # Ça peut durer longtemps !
```


```python
# Un deuxième essai
from random import randint
gagne = False
while not(gagne):
    tirage = randint(0,1)
    nombre_choisi = int(input("Pile (1) ou face (0) ? "))
    if tirage == nombre_choisi:
        print("Gagné")
        gagne = True
    else:
        print("Perdu. Essaye encore.")
```


```python
# Une variante
from random import randint
tirage = 0
nombre_choisi = 1
while tirage != nombre_choisi:
    tirage = randint(0,1)
    nombre_choisi = int(input("Pile (1) ou face (0) ? "))
    if tirage != nombre_choisi:
        print("Perdu. Essaye encore.")
print("Gagné !")
```

### Exemple : pile ou face, rejouer
Écrire un programme qui nous fait rejouer à pile ou face tant qu'on perd et qu'on veut rejouer.


```python
from random import randint
rejouer = True
perdu = True
while rejouer and perdu:
    tirage = randint(0,1)
    nombre_choisi = int(input("Pile (1) ou face (0) ? "))
    if tirage == nombre_choisi:
        perdu = False
    else:
        print("Perdu.")
        reponse = input("Voulez-vous rejouer ? [o/n]")
        if reponse == "n":
            rejouer = False
if not perdu:
    print("Gagné")
```

### Exemple : Compter de 1 à 100


```python
# à corriger !
i = 0
while i < 100:
    print(i+1, end=" ")
    i = i + 1  # ou bien : i += 1
```

#### Exercice

1. Compter de 1 à 100 par pas de 2, de 3...
1. Compter 100 à 1 par pas de -1, de -2...
1. Compter de `a` à `b` par pas de `c` pour `a`, `b` et `c` trois entiers quelconques. Dans quels cas a-t-on des problèmes ?


```python
i = 1
pas = 4
while i <= 100:
    print(i, end=" ")
    i = i + pas  # ou bien : i += 1
```


```python
i = 100
pas = -4
while i > 0:
    print(i, end=" ")
    i = i + pas  # ou bien : i += 1
```


```python
a, b, c = 27, 42, 2
i = a
pas = c
while i <= b:
    print(i, end=" ")
    i = i + pas  # ou bien : i += 1
```

#### Exercice

1. Simuler le lancer de 10 000 pièces et calculer la proportion de "pile" obtenue
1. Simuler le lancer d'une pièce jusqu'à la première "face" obtenue, et afficher le nombre de lancers effectués


```python
nb_lancers = 1e6

i = 1
pile = 0
while i <= nb_lancers :
    lancer = randint(0, 1)
    if lancer == 0:
        pile += 1
    i += 1
print(pile/nb_lancers)
```

### Exemple : Jouer à pierre-feuille-ciseau


```python
from random import randint

coup_humain = int(input("Pierre (1), feuille (2) ou ciseaux (3) ? "))

coup_ordi = randint(1, 3)
if coup_ordi == 1:
    print("L'ordinateur a joué pierre.")
elif coup_ordi == 2:
    print("L'ordinateur a joué feuille.")
else:
    print("L'ordinateur a joué ciseaux.")

if coup_ordi == coup_humain:
    print("Égalité.")
elif coup_humain == (coup_ordi + 1) % 3:
    print("Vous avez gagné.")
else:
    print("Vous avez perdu.")
```

#### Exercice

1. Expliquer la ligne 15
1. Expliquer ce qu'il se passe si l'humain entre 4.
1. Proposer de rejouer une partie
1. Afficher le nombre de parties jouées et le score final

### Répétition simple

On peut répéter un bloc d'instructions grâce à une boucle « tant que » ou boucle `while`.

- **Si** une certaine condition est vraie,
  on va exécuter un certain bloc d'instructions ;
- **Sinon**, on va passer directement à la suite du programme ;
- Après chaque exécution du bloc, on réévalue la condition.

**Vocabulaire :**

- L'expression booléenne `condition` est appelée **condition de continuation**.
- Sa négation (`not condition`) est appelée **condition d'arrêt**.
- Le bloc d'instructions est appelé **corps de la boucle**.
- Chaque exécution du corps de la boucle est appelée **itération**.

<img src='img/while1.png' width='30%'>

**Syntaxe :**

```python
# début
while condition:
    # bloc d'instructions
    # (corps de la boucle)
# suite
```

- `condition` est une **expression booléenne**
- corps exécuté uniquement si `condition` s'évalue à `True`
- après chaque exécution du corps, on réévalue `condition`
    - si `condition` s'évalue à `False`, sortie de la boucle
    - sinon, nouvelle **itération**

Il peut n'y avoir aucune itération, ou un nombre infini !



## Outil d'analyse : tableau de valeurs

Utile pour exécuter manuellement une boucle

- Une colonne pour indiquer le numéro de la dernière ligne du programme exécutée
- Une colonne pour indiquer le nombre d'itérations exécutées
- Une colonne par variable "intéressante"
- Une colonne pour la condition de continuation
- Éventuellement des colonnes explicatives supplémentaires

On remplit le tableau au moins pour **la ligne précédant la boucle** et pour **la dernière ligne du corps**

### Exemple : Calculer $a^p$

On veut calculer $2^n$ (sans utiliser `**`).

Algorithme naïf : on remarque que $2^n = 2^{n-1} \times 2 = 1 \times 2 \times 2 \times \cdots \times 2$

1. on commence par fixer le résultat à 1
2. on multiplie le résultat par 2 `n` fois


```python
a = 2
p = 4
res = 1  # pourquoi ?
i = 0
while i < p:
    res = res * a
    i = i + 1
print(a, "puissance", p, "égale", res)
```

    2 puissance 4 égale 16


ligne  | itération | `a` | `p` | `res` |  `i` | `i < p` | commentaire
-------|-----------|-----|-----|-------|------|---------|-----------------------------
1      |           | 2   |     |       |      |         |
2      |           | -   | 4   |       |      |         |
3      |           | -   | -   | 1     |      |         |
4      |           | -   | -   | -     | 0    | `True`  | 
5      |           | -   | -   | -     | -    | `True`  | condition vraie, on entre
6      | 1         | -   | -   | 2     | -    | `True`  | 
7      | 1         | -   | -   | -     | 1    | `True`  | fin de la 1e itération
5      |           | -   | -   | -     | -    | `True`  | condition vraie, on continue
6      | 2         | -   | -   | 4     | -    | `True`  | 
7      | 2         | -   | -   | -     | 2    | `True`  | fin de la 2e itération
5      |           | -   | -   | -     | -    | `True`  | condition vraie, on continue
6      | 3         | -   | -   | 8     | -    | `True`  | 
7      | 3         | -   | -   | -     | 3    | `True`  | fin de la 3e itération
5      |           | -   | -   | -     | -    | `True`  | condition vraie, on continue
6      | 4         | -   | -   | 16    | -    | `True`  | 
7      | 4         | -   | -   | -     | 4    | `False` | fin de la 4e itération
5      |           | -   | -   | -     | -    | `False` | condition fausse, on arrête
8      |           | -   | -   | -     | -    | `False` | suite du programme

**Remarques :**
- après la ligne 4 et chaque exécution de la ligne 7 on a `res == a**i`
- `i` se rapproche de `p` à chaque tour sans le dépasser

Version "compacte" sans regarder toutes les lignes ni les variables qui ne changent pas :

ligne  | itération | `res` |  `i` | `i < p` | commentaire
-------|-----------|-------|------|---------|-----------------------------
4      |           | 1     | 0    | `True`  | juste avant la première itération
7      | 1         | 2     | 1    | `True`  | à la fin de la 1e itération
7      | 2         | 4     | 2    | `True`  | à la fin de la 2e itération
7      | 3         | 8     | 3    | `True`  | à la fin de la 3e itération
7      | 4         | 16    | 4    | `False` | à la fin de la 4e itération (sortie)

**Remarques :**
- pendant tout le programme `a` vaut `2` et `p` vaut `4`
- après la ligne 4 et chaque exécution de la ligne 7 on a `res == a**i`
- `i` se rapproche de `p` à chaque tour sans le dépasser
- à la fin de la dernière itération `i == p` et donc `res == a**p`

#### Variante


```python
a = 2
p = 4
res = 1
i = p  # changement !
while i > 0:  # changement !
    res *= a
    i -= 1  # changement !
print(a, "puissance", p, "égale", res)
```

Tableau de valeurs compact :

ligne  | itération | res  |  i   | i > 0   | commentaire
-------|-----------|------|------|---------|-----------------------------
4      |           | 1    | 4    | `True`  | avant la première itération
7      | 1         | 2    | 3    | `True`  |
7      | 2         | 4    | 2    | `True`  |
7      | 3         | 8    | 1    | `True`  |
7      | 4         | 16   | 0    | `False` | sortie de la boucle

**Remarques :**
- pendant tout le programme `a` vaut `2` et `p` vaut `4`
- après la ligne 4 et chaque exécution de la ligne 7 on a `res == a**(p-i)`
- la valeur de `i` est positive au début et décroît strictement
- à la fin de la dernière itération `i == 0` et donc `res == a**(p-0) == a**p`



## Terminaison et correction d'une boucle

En général rien ne garantit :

- qu'une boucle `while` va se terminer un jour

    ```python
    while(True):
        print("spam")
    ```
    
- ni qu'elle produit le bon effet

Pour cela il faut en général faire des **preuves**

Les deux sections suivantes présentent des méthodes classiques pour présenter ces preuves : elles ne sont pas exigibles au contrôle. Néanmoins intéressantes et importantes, elles seront d'ailleurs détaillées dans le cours *Algorithmique et structures de données* en L2.

#### ![](img/non-exigible.png){ width=50px } Preuve de terminaison : variant

Méthode possible pour montrer qu'une boucle termine

- montrer qu'une certaine quantité décroît strictement à chaque tour de boucle
- montrer qu'elle ne peut pas décroître indéfiniment

On appelle une telle quantité **variant de boucle**, son existence garantit la terminaison

#### Exemple : algorithme d'Euclide

Algorithme de l'antiquité permettant de déterminer le PGCD de deux nombres entiers


```python
a0, b0 = 129, 36  # entiers positifs quelconques

a, b = a0, b0
while b > 0:
    r = a % b
    a = b
    b = r

print("le pgcd de", a0, "et", b0, "est", a)
```

Pourquoi l'algorithme termine-t-il ?

- on peut choisir comme variant la **valeur de `b`**
- initialement, `b > 0`
- la boucle ne s'exécute pas si `b <= 0`
- la valeur de `b` décroît strictement

Comme il ne peut exister de suite infinie strictement décroissante d'entiers positifs, la boucle termine

On peut repérer le variant dans le **tableau de valeurs**

ligne  | itération | `a` | `b` | `a % b` | commentaire
-------|-----------|-----|-----|---------|------------------------
3      |           | 129 | 36  | 21      | avant la boucle
7      | 1         | 36  | 21  | 15      | fin de 1e itération
7      | 2         | 21  | 15  | 6       | ...
7      | 3         | 16  | 6   | 3       |
7      | 4         | 6   | 3   | 0       | 
7      | 5         | 3   | 0   | -       | on va sortir de la boucle

**Variant :** la valeur de `b` est positive au début et décroît strictement

#### ![](img/non-exigible.png){ width=50px } Preuve de correction : invariant

Méthode possible pour montrer qu'une boucle produit le bon effet :

- montrer qu'une certaine propriété $I$ est vraie avant l'entrée dans la boucle
- montrer que **si** $I$ est vraie au début du corps **alors** elle est encore vraie à la fin
- en déduire que $I$ est vraie à la sortie de la boucle

On appelle une telle propriété **invariant**, son existence peut permettre de garantir la correction

#### Exemple : retour sur le calcul de puissance




```python
a = 2
p = 4
res = 1
i = 0
while i < p:
    res *= a
    i += 1
print(a, "puissance", p, "égale", res)
```

ligne  | itération | `res` |  `i` | `i < p` | commentaire
-------|-----------|-------|------|---------|-----------------------------
4      |           | 1     | 0    | `True`  | juste avant la première itération
7      | 1         | 2     | 1    | `True`  | à la fin de la 1e itération
7      | 2         | 4     | 2    | `True`  | à la fin de la 2e itération
7      | 3         | 8     | 3    | `True`  | à la fin de la 3e itération
7      | 4         | 16    | 4    | `False` | à la fin de la 4e itération (sortie)

**Remarques :**
- **Variant :** `p - i` décroît de 1 à chaque tour et la boucle s'arrête quand il atteint `0`
- **Invariant :** après la ligne 4 et chaque exécution de la ligne 7 on a `res == a**i`
- **En sortie de boucle :** `i == p` et donc `res == a**p`

#### Variante


```python
a = 2
p = 4
res = 1
i = p
while i > 0:
    res *= a
    i -= 1
print(a, "puissance", p, "égale", res)
```

ligne  | itération | `res` | `i`  | `i > 0` | commentaire
-------|-----------|-------|------|---------|-----------------------------
4      |           | 1     | 4    | `True`  | avant la première itération
7      | 1         | 2     | 3    | `True`  |
7      | 2         | 4     | 2    | `True`  |
7      | 3         | 8     | 1    | `True`  |
7      | 4         | 16    | 0    | `False` | sortie de la boucle

**Remarques :**
- **Variant :** `i` décroît de 1 à chaque tour et la boucle s'arrête quand il atteint 0
- **Invariant :** après la ligne 4 et chaque exécution de la ligne 7 on a `res == a**(p-i)`
- **En sortie de boucle :** `i == 0` et donc `res == a**(p-0) == a**p`

#### Exemple : encadrer un nombre

On veut encadrer un nombre positif $n$ entre deux puissances successives d'un nombre $b$. On cherche l'unique entier $k$ tel que :

$$
b^k \leq n < b^{k+1}
$$

On appelle parfois $k$ le *logarithme entier* de $n$ en base $b$, parce que

$$
k \leq \log_b n < k+1
$$

Par exemple :

- pour $b = 10$ on a $10^3 \leq 1024 < 10^4$, donc $k = 3$.
- pour $b = 2$ on a $2^{10} \leq 1024 < 2^{11}$, donc $k = 10$.


```python
n = 1000  # le nombre à encadrer
b = 10    # base de la puissance
exp = 0   # exposant courant
temp = 1  # valeurs successives de b**exp
while temp <= n:
    temp *= b
    exp += 1
print("le plus petit k tel que", b, "à la puissance k " 
      "est inférieur ou égal à", n, "est", exp-1)  # compléter
```

ligne  | temp  | exp  | temp < n | commentaire
-------|-------|------|----------|-----------------------------
4      | 1     | 0    | `True`   | avant la première itération
7      | 10    | 1    | `True`   |
7      | 100   | 2    | `True`   |
7      | 1000  | 3    | `True`   |
7      | 10000 | 4    | `False`  | on sort de la boucle

- **Variant :** `n - temp` initialement $\geq 0$, diminue à chaque tour
- **Invariant** (simplifié) lignes 4 et 7 : `temp == 10**exp` et `10**(exp-1) <= n`
- **À la fin:** `10**(exp-1) <= n` et `10**exp > n`, autrement dit `10**(exp-1) <= n < 10**exp`

#### Exemple : convertir un nombre en binaire

Le nombre 42 s'écrit `101010` en binaire parce que

\begin{align*}
42 & = 0 + 2 \times 21\\
   & = 0 + 2 \times (1 + 2 \times 10))\\
   & = \ldots\\
   & = 0 + 2 \times (1 + 2 \times (0 + 2 \times (1 + 2 \times (0 + 2 \times (1 + 2 \times 0)))))\\
   & = 0 \times 2^0 + 1 \times 2^1 + 0 \times 2^2 + 1 \times 2^3 + 0 \times 2^4 + 1 \times 2^5
\end{align*}



```python
bin(42)
```

Algorithme de conversion de $n>0$ en binaire :

1. Calculer le quotient $q$ et le reste $r$ de $n$ par 2
2. Ajouter $r$ comme nouveau chiffre à **gauche** du résultat
3. Poser $n = q$ et recommencer en 1 si $n > 0$

Suite de l'exemple :

\begin{align*}
& 42 & & = 2 * 21 & & + 0 & & \rightarrow \text{chiffre } 0\\
& 21 & & = 2 * 10 & & + 1 & & \rightarrow \text{chiffre } 1\\
& 10 & & = 2 * 5 & & + 0 & & \rightarrow \text{chiffre } 0\\
& 5 & & = 2 * 2 & & + 1 & & \rightarrow \text{chiffre } 1\\
& 2 & & = 2 * 1 & & + 0 & & \rightarrow \text{chiffre } 0\\
& 1 & & = 2 * 0 & & + 1 & & \rightarrow \text{chiffre } 1\\
\end{align*}


```python
n = 42
k = n
res = ""  # on utilise une chaîne
while k > 0:
    q = k // 2
    r = k % 2
    res = str(r) + res
    k = q
print(res)
```

ligne  | itér  | `k`   | `r` | `res`      | $\texttt{k}\times2^{\text{itér}}$ | val. `res` | `k > 0`  | commentaire
-------|-------|-------|-----|------------|----------------------------|------------|----------|-----------------------------
3      | 0     | 42    |     | `''`       | $42\times2^0=42$ | 0          | `True`   | avant la première itération
8      | 1     | 21    | 0   | `'0'`      | $21\times2^1=42$        | 0          | `True`   | fin de la 1e itération
8      | 2     | 10    | 1   | `'10'`     | $10\times2^2=40$        | 2          | `True`   |
8      | 3     | 5     | 0   | `'010'`    | $5\times2^3=40$         | 2          | `True`   |
8      | 4     | 2     | 1   | `'1010'`   | $2\times2^4=32$         | 10         | `True`   |
8      | 5     | 1     | 0   | `'01010'`  | $1\times2^5=32$         | 10         | `True`   |
8      | 6     | 0     | 1   | `'101010'` | $0\times2^6=32$         | 42         | `False`  | sortie de la boucle

- **Invariant** : `res` contient les (nombre d'itérations) derniers chiffres de la conversion de `n` en binaire  
  <div style='color:gray'>$k \times\, 2^\text{(itér)} +$ (valeur de res) $= n$</div>
- **Variant :** `n - temp` initialement $\geq 0$, diminue à chaque tour

**Exercice :**
- dresser le tableau de valeurs pour $n = 25$
- adapter l'algorithme pour convertir $n$ en base 4, puis en base $b < 10$

  ref : [Compter comme les Shadoks](https://www.youtube.com/watch?v=lP9PaDs2xgQ)

**Exercice :** quel est l'invariant de boucle pour l'algorithme d'Euclide ?



## Boucles imbriquées 

On peut écrire une boucle à l'intérieur d'une autre boucle

<img src='img/while2.png' width='40%'>

La syntaxe d'une double boucle `while` :
```python
# début
while condition1:
    # début corps 1
    while condition2:
        # corps 2
    # fin corps 1
# suite
```

#### Exemple : table d'addition

But : afficher toutes les additions de nombres inférieurs à `n`


```python
m = 3
n = 11

a = 0  # hors de la boucle externe !
while a < m:
    b = 0  # dans la boucle externe !
    while b < n:
        print(a, '+', b, '=', a+b)
        b += 1  # dans la boucle interne !
    a += 1  # dans la boucle externe !
```

**Exercices :** 
1. afficher toutes les additions `a + b = c` pour `a` entre 0 et `n` et `b` entre 0 et `m`
2. essayer d'écrire le programme en utilisant une seule boucle (*non recommandé en temps normal !*)

#### Exemple : compter jusqu'à 59, dix nombres par ligne 


```python
# paramètres
limite = 60
nb_colonnes = 7

courant = 0
while courant < limite:
    colonne = 0
    while colonne < nb_colonnes and courant < limite:
        print(courant, end = '\t')
        colonne += 1
        courant += 1
    print()  # affiche un retour à la ligne
```

**Exercice :** (pas si évident) faire en sorte que les nombres successifs apparaissent sur une même colonne


```python
# paramètres
limite = 37
nb_colonnes = 10

nb_lignes = limite // nb_colonnes + 1
ligne = 0
while ligne < nb_lignes:
    colonne = 0
    courant = ligne
    while courant < limite and colonne < nb_colonnes:
        print(courant, end = '\t')
        courant += nb_lignes
        colonne += 1
    ligne += 1
    print()  # affiche un retour à la ligne
```



### ![](img/non-exigible.png){ width=50px } Contrôle de boucle 

Tout ce qui suit est *non exigible en contrôle*.

#### Instruction `break`

On peut sortir prématurément d’une boucle `while`
- Instruction `break` dans le corps (en général dans une conditionnelle)
- Force une sortie de boucle et passe directement à la suite du programme
- On ne réévalue pas la condition du `while`
  

<img src='img/while3.png' width='30%'>

**Exemple :** saisie contrôlée sans duplication de l'instruction `input` :


```python
while True:
    note_cc1 = float(input('Note du premier contrôle : '))
    if 0 <= note_cc1 <= 20:
        # saisie correcte, on termine la boucle
        break
    # saisie incorrecte, on recommence
    print('Erreur de saisie.')
```

#### Instruction `continue`

On peut passer prématurément à l’itération suivante
- Instruction `continue` dans le corps de la boucle
- On retourne directement à la condition, et on la réévalue


```python
while True:
    saisie = input("Dis-moi quelque chose : ")
    if saisie == "":
        print("Tu n'as rien dit !")
        continue
    if saisie == "je réfléchis":  # elif inutile ici !
        print("OK, j'attends...")
        continue
    if saisie == "stop":  # elif inutile ici !
        print("D'accord...")
        break
    if saisie == "arrête":  # elif inutile ici !
        print("C'est bon, j'ai compris !")
        break
    # else inutile ici !
    print("Ta phrase fait", len(saisie), "caractères.")
```

#### Remarques sur `break` et `continue`

- Ces deux instructions ne sont à utiliser que par des programmeurs confirmés
- Elles compliquent en général la compréhension et l'analyse du code
- On peut toujours s'en sortir sans (en utilisant des `if`), même si ça peut rendre le code moins "élégant"


```python
saisie = ""
while saisie != "stop" and saisie != "arrête":
    saisie = input("Dis-moi quelque chose : ")
    if saisie == "":
        print("Tu n'as rien dit !")
    elif saisie == "je réfléchis":
        print("OK, j'attends...")
    else:
        print("Ta phrase fait", len(saisie), "caractères.")
if saisie == "stop":
    print("D'accord...")
elif saisie == "arrête":
    print("C'est bon, j'ai compris !")
```


```python
a, b, c = ...

# Calcul et affichage du nombre de solutions
if a == b == c == 0:
    print("Une infinité de solutions réelles (et complexes)")
elif a == b == 0:  # A ce stade, si a = b = 0, c est différent de 0 !!!
    print("Aucune solution")
elif a == 0 :      # A ce stade, si a = 0, b est différent de 0 !!!
    print("Une solution réelle")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Pas de solution réelle")
    elif delta == 0:
        print("Une solution réelle")
    else:
        print("Deux solutions réelles")
```



# Introduction aux listes 

Il arrive souvent que l'on veuille faire référence à plusieurs données en même temps (parce qu'ils sont de même type, ou parce qu'elles se rapportent au même objet, par exemple). Par ailleurs, on ne sait pas toujours quelle quantité de données on va devoir retenir pour le bon déroulé de notre programme ou algorithme. 
Difficile dans ces cas de savoir le nombre exact de variables à déclarer et initialiser !
On a donc envie de pouvoir regrouper des données en les organisant en *collections ordonnées*, ayant en plus un caractère *dynamique* et *mutable* : on peut ajouter des éléments à notre collection à notre guise, en supprimer, en modifier...

En algorithmique, on parle souvent de *tableaux*, en Python, le type correspondant est **list**, et on parlera sans arrêt de *listes*.

Nous approfondirons tout cela dans la séquence de cours suivante (on verra en particulier en détail les notions de *mutabilité*, d'*itérabilité*, de boucle * for*), mais voici déjà quelques bases pour manipuler ces objets un peu spéciaux mais très utiles !
 
Pour résumer :

**Objectif :** désigner avec une seule variable une collection de valeurs

**Liste :** suite **indexée** (numérotée) d'objets quelconques (type `list` en python)

-   Élements "rangés" dans des "cases" numérotées de 0 à $n-1$

-   En mémoire : tableau à $n$ cases, chacune contenant une référence
    (*"flèche"*) vers un objet

-   Peut contenir des objets de plusieurs types différents

-   **Mutable** : peut être modifiée, agrandie, raccourcie...

<div style='float:left; margin-right:40pt; width:10cm'><img src='img/commode_liste.png'> *Une métaphore* </div>

<div style='float:left; margin-right:40pt; width:10cm'><img src='img/schema_list_py.png'> *Un peu plus proche de la réalité* </div>

## Création et affichage

**Création :** suite entre `[` et `]` d'expressions séparées par `,`


```python
lst = [3, 'toto', 4.5, False, None]
print(lst)
```

Liste vide `[]` : liste ne contenant aucun objet


```python
lst = []
print(lst)
```

Une liste peut contenir d'autres listes !


```python
lst = ['test', [1, [2], 3]]
print(lst)
```

[Exemple (Python tutor)](http://pythontutor.com/visualize.html#code=%23Cr%C3%A9ation%20et%20affichage%0A%0Alst_ex1%20%3D%20%5B1,%204.5,%20'toto',%20False%5D%0A%0Alst_vide%20%3D%20%5B%5D%0A%0Alst_ex2%20%3D%20%5B1,%202,%20%5B3,'haha'%5D,%20'hoho'%5D%0A%0Aprint%28%22Le%20premier%20exemple%20%3A%20%22,lst_ex1%29%0Aprint%28%22La%20liste%20vide%20%3A%20%22,%20lst_vide%29%0Aprint%28%22Le%20deuxi%C3%A8me%20exemple%20%3A%20%22,%20lst_ex2%29%0A%0A%23Acc%C3%A8s%20%C3%A0%20un%20%C3%A9l%C3%A9ment%0Ai%20%3D%202%0Aval_ex1%20%3D%20lst_ex1%5Bi%5D%0Aval_ex2%20%3D%20lst_ex2%5Bi%5D%0Aprint%28%22Les%20%C3%A9l%C3%A9ments%20d'indice%22,%20i,%20%22sont%22,%20val_ex1,%20%22et%22,%20val_ex2%29%0A%0A%23Longueur%0Ataille_ex1%20%3D%20len%28lst_ex1%29%0Ataille_vide%20%3D%20len%28lst_vide%29%0A%0Aprint%28%22La%20longueur%20de%20lst_ex2%20est%22,%20len%28lst_ex2%29%29%0A%0A%23Modification%20d'un%20%C3%A9l%C3%A9ment%0Alst_ex1%5B0%5D%20%3D%20%22allo%3F%3F%22%0Aval_ex2%5B1%5D%20%3D%20%22blop%22%0A%0Aprint%28%22Est-ce%20que%20lst_ex2%20est%20modifi%C3%A9e%3F%5Cn%22,%20lst_ex2%29%0A%0Alst_ex2%5B2%5D%20%3D%2042%0A%0Aprint%28%22Est-ce%20que%20val_ex2%20est%20modifi%C3%A9e%3F%5Cn%22,%20val_ex2%29%0A%0A%23ajout%20d'un%20%C3%A9l%C3%A9ment%0Alst_ex1.append%28%22et%20hop%22%29%0A%23retirer%20un%20%C3%A9l%C3%A9ment%20%28case%20d'indice%202%29%0Alst_ex1.pop%282%29%0A%23%20retirer%20le%20dernier%20%C3%A9l%C3%A9ment%0Alst_ex1.pop%28%29%0A%23%20encore%20une%20fois%20sans%20perdre%20la%20valeur%20en%20route%0Ares%20%3D%20lst_ex1.pop%28%29&cumulative=false&heapPrimitives=false&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)  
(exemple filé à exploiter tout au long du cours)

## Opérations et fonctions de base

### Longueur d'une liste

La longueur d'une liste (le nombre d'éléments qu'elle contient) s'obtient par la fonction `len`.


```python
lst = [3, 'toto', 4.5, False, None]
print(len(lst))
```


```python
print(len([]))
```

### Accès aux éléments

Les éléments d'une liste à $n$ éléments sont numérotés de 0 à $n-1$.  
Le numéro d'un élément est appelé son *indice*.  
L'accès à un élément donné s'appelle l'**indexation**.


```python
lst = [3, 'toto', 4.5]
print(lst[1])
```

![](img/warning.png){ width=50px } **Attention !** 

- Le premier élément d'une liste est l'élément d'indice `0` !
- Si la liste a `n` éléments, il n'existe pas d'élément d'indice `n` !
- L'accès à un indice supérieur ou égal à la taille de la liste provoque une erreur !


```python
lst = [3, 'toto', 4.5]
print(lst[3])
```

**Exercice :** Écrire une fonction qui affiche tous les éléments d'une liste (un par ligne)


```python
def affiche_elements(lst):
    ...

lst = [3, 'toto', 4.5]
affiche_elements(lst)
```


```python
def affiche_elements(lst):
    i = 0
    while i < len(lst):
        print(lst[i])
        i = i + 1


lst = [3, 'toto', 4.5]
affiche_elements(lst)
```

### Modification d'un élément

On peut modifier le $i$-ème élément de `lst` à l'aide d'une affectation :


```python
lst = [3, 'toto', 4.5, False, None]
print(lst[2])
lst[2] = 'titi'
print(lst)
```

**Attention**, ceci ne crée pas une nouvelle liste mais modifie la
liste sur place !


```python
lst = [3, 'toto', 4.5, False, None]
lst_bis = lst
lst[2] = 'titi'
lst_bis
```

### Concaténation et répétition

Comme pour les chaînes de caractères (`str`) on peut utiliser les opérateurs `+` pour fabriquer la concaténation de deux listes et `*` pour répéter une liste.


```python
[3, 'toto', 4.5] + [False, None]
```


```python
[] + [3, 'toto', 4.5] + []
```


```python
3 * ['a', 'b']
```


```python
[0] * 13
```

On peut utiliser ces opérateurs pour recopier une liste. Comparer :


```python
lst = [3, 'toto', 4.5]
lst2 = lst
lst3 = lst + []
lst4 = lst * 1
```

### Test d'appartenance

**Exercice :** Écrire une fonction recevant une liste et une valeur, et
renvoyant `True` si la valeur apparaît dans la liste (`False` sinon)


```python
def appartient(lst, val):
    ...
```


```python
def appartient(lst, val):
    i = 0
    while i < len(lst):
        if lst[i] == val:
            return True
        i += 1
    return False

lst = ['Hildegarde', 'Cunégonde', 'Médor']

print(appartient(lst, 'Cunégonde'))

if appartient(lst, 'Médor'):
    print('Bon chien !')
```











**Remarque :** Cette fonctionnalité existe déjà en Python :

-   `val in lst` vaut `True` si `val` apparaît dans `lst`, `False` sinon
-   Réciproquement, on peut écrire `val not in lst`


```python
lst = ['Hildegarde', 'Cunégonde', 'Médor']
'Cunégonde' in lst
```


```python
lst = ['Hildegarde', 'Cunégonde', 'Médor']
'Rex' not in lst
```


```python
lst = ['Hildegarde', 'Cunégonde', 'Médor']
if 'Médor' in lst:
    print('Bon chien !')
```

## Manipulations par méthodes

On va maintenant énumérer un certain nombre de méthodes prédéfinies sur les listes, permettant des modifications plus complexes. Pour plus de détails, on pourra consulter la [documentation en ligne](https://docs.python.org/3/).

### Agrandir ou rétrécir une liste

Plusieurs instructions ont un effet sur la taille de la liste :

-   L'instruction `lst.append(elem)` ajoute l'élément `elem` à la fin de
    la liste `lst`

-   L'instruction `lst.pop()` supprime le dernier élément de `lst` et
    renvoie sa valeur

-   L'instruction `lst.pop(i)` supprime l'élément d'indice `i` de `lst` et
    renvoie sa valeur

*Les fonctions `append` et `pop` sont appelées **méthodes**, ou fonctions
s'appliquant à un objet (nous en verrons d'autres dans les cours
suivants)*

**Attention**, ces instructions ne créent pas une nouvelle liste mais
modifient la liste sur place !

**Attention**, ne pas confondre `x = lst[2]` et `x = lst.pop(2)` !


```python
lst = [3, 'toto', 4.5, False, None]
lst_bis = lst

lst.append(1)
print(lst_bis)

elem = lst_bis.pop(2)
print(elem)

print(lst)
```



# Introduction aux fonctions 



En programmation, une fonction est :
- un morceau de programme
- portant en général un **nom**
- acceptant zéro, un ou plusieurs **paramètres**
- produisant le plus souvent un **résultat**. 

Des exceptions existent, mais la forme la plus courante d'une fonction est donc proche de celle d'une fonction mathématique.

L'utilisation de fonctions améliore les aspects suivants du code :

-  **Lisibilité :** 
    - isoler une partie du programme (par exemple un gros calcul compliqué)
    - éviter une trop grande imbrication des `if`, des `while`
-  **Modularité et robustesse:** 
    - réutiliser le même code plusieurs fois (évite de recopier le code)
    - faciliter la correction des bugs, l'évolution et la maintenance
-  **Généricité :**
    - changer la valeur des paramètres (même calcul mais avec différentes valeurs de départ)

## Fonctions prédéfinies et bibliothèque standard

En Python, il existe un grand nombre de fonctions prédéfinies, que nous avons déjà utilisées, par exemple :

* `int(obj)` : 1 paramètre, 1 résultat. Reçoit en paramètre un objet (par exemple `str` ou `float`), essaie de le transformer en entier et renvoie l'entier obtenu.


```python
int("34")
```

* `len(obj)` : 1 paramètre, 1 résultat. Reçoit un objet (par exemple `str`) et renvoie sa longueur.


```python
len("bonjour")
```

* `randint(mini, maxi)` : 2 paramètres, 1 résultat. Reçoit deux nombres, et renvoie un entier aléatoire compris entre ces deux nombres (inclus).


```python
from random import randint
randint(1, 34)
```

Il y en a beaucoup d'autres, comme `print, input, float, str...`.

Ces fonctions sont appelées _prédéfinies_ (ou _built-in_)
- il est inutile de les connaître toutes par cœur
- liste des fonctions prédéfinies sur [cette page](https://docs.python.org/3/library/functions.html)

Il existe également de nombreux _modules_ officiels (par exemple le module `random`)
- bibliothèques de fonctions, de types et d'objets
- liste des modules prédéfinis documentée [ici](https://docs.python.org/3/library).

## Définition de fonction

Pour définir une nouvelle fonction on utilise la syntaxe suivante :

```python
# ligne suivante : en-tête de fonction
def nom_fonction(param_1, ..., param_n):  
    # corps de la fonction
    # utilisant param_1 à param_n
    ...
    # peut renvoyer un résultat :
    return resultat
```

Une fonction peut :

* prendre un certain nombre de paramètres (ici, $n$, qui s'appellent `param_1` à `param_n`)
* renvoyer une valeur (via l’instruction `return`)

## Appel de fonction

Une fois définie, `nom_fonction` peut être utilisée dans le code (on parle d'un **appel**) en indiquant entre parenthèses ses paramètres séparés par des virgules :

```python
# définition de fonction
def nom_fonction(param_1, ..., param_n): 
    ...

# reste du programme 
...
# appel de la fonction :
une_var = nom_fonction(expr_1, ..., expr_n)
```

### Exemples

#### Fonction à paramètres et résultat


```python
# fonction à deux paramètres produisant un résultat
def maximum(a, b):
    if a >= b:
        return a
    else:
        return b
```


```python
nb1 = 14
nb2 = 31

maximum(nb1, nb2)  # ne sert à rien !!

# On appelle la fonction et on garde le résultat dans c :
c = maximum(nb1, nb2)
print("le max de", nb1, "et", nb2, "est", c)

# On peut aussi utiliser directement le résultat :
print("le max de", nb1, "et", nb2, "est", maximum(nb1, nb2))
```

**Entraînement :** 

- Décrire l'exécution pas à pas du programme (avec état de la mémoire). On peut aussi essayer avec [Python Tutor](http://www.pythontutor.com/visualize.html#code=%23%20fonction%20%C3%A0%20deux%20param%C3%A8tres,%20sans%20effet%20de%20bord%0Adef%20maximum%28a,%20b%29%3A%0A%20%20%20%20if%20a%20%3E%20b%3A%0A%20%20%20%20%20%20%20%20return%20a%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20b%0A%20%20%20%20%0Anb1%20%3D%20int%28input%28%29%29%0Anb2%20%3D%20int%28input%28%29%29%0A%0A%23%20On%20appelle%20la%20fonction%20et%20on%20garde%20le%20r%C3%A9sultat%20dans%20c%20%3A%0Ac%20%3D%20maximum%28nb1,%20nb2%29%0Aprint%28%22le%20max%20de%22,%20nb1,%20%22et%22,%20nb2,%20%22est%22,%20c%29%0A%0A%23%20On%20peut%20aussi%20utiliser%20directement%20le%20r%C3%A9sultat%20%3A%0Aprint%28%22le%20max%20de%22,%20nb1,%20%22et%22,%20nb2,%20%22est%22,%20maximum%28nb1,%20nb2%29%29&cumulative=false&curInstr=0&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).
- Dresser un tableau de valeurs de l'exécution du programme

### Fonction sans paramètre

- En principe, une fonction sans paramètre devrait avoir toujours le même comportement
- Dans l'exemple suivant, on utilise un générateur pseudo-aléatoire, ce qui explique que la fonction ne renvoie pas toujours le même résultat
- Une fonction pourrait aussi recevoir des données depuis l'extérieur (utilisateur, requête réseau...).

Dans ces cas, on parle de **causes secondaires**


```python
from random import randint

def lance_de() :
    return randint(1,6)

compteur = 1
while lance_de() != 6: 
    compteur = compteur + 1
print('Obtenu un 6 en', compteur, 'jets de dé.')
```

### Fonction sans valeur de retour

- Si l'exécution arrive à la dernière instruction du corps de la fonction sans rencontrer d'instruction `return expr`, alors la valeur de retour par défaut est `None` (même comportement si `return` seul)
- En général une telle fonction a quand même un effet sur l'environnement (affichages, dessin, écriture dans un fichier, envoi d'informations sur le réseau...)

Pour tous les effets autres que le renvoi d'un résultat, on parle d'**effets secondaires**


```python
from turtle import *

def trace_polygone(nb_cotes, taille_cote):
    down()
    i = 0
    while i < nb_cotes:
        forward(taille_cote)
        left(360 / nb_cotes)
        i = i + 1

# faire une affectation ici ne servirait à rien (essayer !)
trace_polygone(5, 100)
exitonclick()
```

### Erreur fréquente : confusion (paramètre / saisie) et (retour / affichage)

Les programmeurs débutants confondent très souvent la notion de paramètre et celle de saisie (au clavier par exemple) et la notion de valeur de retour avec celle de valeur affichée. 


```python
# ATTENTION CECI EST INCORRECT, A NE PAS REPRODUIRE !!!
def pgcd(a, b):
    a = int(input())  # NON !
    b = int(input())  # NON !
    while a % b != 0:
        r = a % b
        a = b
        b = r
    print("le pgcd est", b)  # NON !
```

<div style='color:red'>NE SURTOUT PAS PROGRAMMER COMME ÇA !</div>

- Comment écrire un programme vérifiant si trois entiers sont
  premiers entre eux à l'aide de cette fonction ?
- Combien ce programme ferait-il de saisies ?
- Qu'afficherait ce programme ?



