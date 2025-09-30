---
title: "Test des tailles d'images"
author: "Marie"
date: \today
lang: fr
toc: true
toc-depth: 2
---

# Image taille par défaut

Sans réglage de taille :

![](img/briques.png)

---

# Image largeur en pourcentage

50% de la largeur du texte :

![](img/briques.png){ width=50% }

70% de la largeur du texte :

![](img/briques.png){ width=70% }

---

# Image largeur en centimètres

Largeur fixe à 8 cm :

![](img/briques.png){ width=8cm }

Largeur fixe à 12 cm :

![](img/briques.png){ width=12cm }

---

# Image hauteur fixée

Hauteur fixée à 4 cm (largeur adaptée automatiquement) :

![](img/briques.png){ height=4cm }

---

# Image largeur + hauteur (⚠️ peut déformer)

Largeur 6 cm et hauteur 3 cm :

![](img/briques.png){ width=6cm height=3cm }

---

# Figure avec légende et taille

![Schéma des briques de base](img/briques.png){#fig:briques width=60%}

Comme on le voit en Figure [@fig:briques], on peut ajuster la taille et garder une légende numérotée.
