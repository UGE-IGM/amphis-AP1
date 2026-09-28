Quelques idées en vrac ( à ordonner après ) :

Boucles while :
 - Vocabulaire condition d'arrêt/ de continuation
- Risque de boucle infini
- Comment débugguer une boucle while ? (si elle ne termine pas, c'est que la condition d'arrêt n'est jamais vérifiée, où sont les lignes qui modifient les variables dans la condition/quand sont-elles exécutées ?)
- Montrer un exemple de saisie contrôlée
- (en bonus si on a le temps : montrer un exemple type do while où on a envie de faire une première itération)
- Parcours d'itérables (list/str) avec boucles while, peut faire la transition avec boucles for
- Préciser assez tôt la différence indice/élément, parce qu'ils font souvent la confusion, voire en tirer une règle d'or.

Listes :
- J'aimerais bien introduire la notion de listes par un exemple du type : j'ai mon programme qui gère un étudiant, comment l'adapter pour qu'il en gère 2 ? et 5 ? (je rajoute des variables etud\_2, etud\_3, etud\_4, etud\_5). C'est un peu laborieux... et si je veux en rajouter une quantité non bornée ?
- Rappeler clairement/plusieurs fois l'indexation à partir de 0
- Parler des index négatifs
- Ne pas trop insister/ne même pas présenter les opérations de suppressions dans les listes, à part pop()... ou en tout cas bien mentionner qu'on en a rarement besoin pour l'instant
- Montrer un exemple d'out of range et la syntaxe de l'erreur associée

Fonctions :
- Quelle image choisit-on pour l'introduire ? Pour les fonctions en maths j'aime bien l'image du distributeur automatique (je rentre un code, j'obtiens un snack en sortie, et on peut filer avec l'entrée supplémentaire de l'argent, le domaine de définition, l'image,etc) mais je ne sais pas si ça s'adapte ici
- Fait-on le parallèle avec les fonctions mathématiques, puis en appuyant les différences (effets de bords, valeur de retour absente ou multiple ? )
- Type des arguments, type de retour
- Print et return : différence entre fonction et affichage.

Pour les fonctions, on peut reprendre (au moins en partie) tes slides de l'année dernière. J'aimerais bien toucher un mot une première fois sur espace de noms/variables locales, au moins sur un dessin, mais sans leur prendre la tête tout de suite avec des questions type "si j'ai un x à l'extérieur et que j'incrémente x qui est aussi l'argument de ma fonction qu'est-ce que ça fait ? "


- Bref retour sur les booléens
- Notes de cours
- Annonce TP noté 1
- Modèle de mémoire (cf la section associée des briques de base)
- Retour des exercices pendant un CM ?
- Chaînes de caractères ?

# TODOs

- slide 4 ("Sur un exemple") : ajouter un commentaire pour dire qu'à la fin de la boucle, `i > 15` (condition d'arrêt)
- présenter `for` avant `range` ? (en mode "on va essayer de comprendre la formule magique")
