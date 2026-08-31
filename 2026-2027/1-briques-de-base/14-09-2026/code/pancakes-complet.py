# Programme 'pancakes'
# date : 06/09/2022
# auteurs : équipe AP1

nom_recette = 'des pancakes'
nb_personnes_ref = 2

q_farine = 125
u_farine = 'g'

q_sucre = 15
u_sucre = 'g'

q_levure = 0.5
u_levure = 'sachet'

q_beurre = 32.5
u_beurre = 'g'

q_sel = 1/2
u_sel = 'pincée(s)'

q_lait = 15
u_lait = 'cl'

q_oeuf = 1
u_oeuf = 'unité(s)'

texte_recette = '''
Étape 1 (beurre) :
Faire fondre le beurre, dans une casserole à feu doux ou dans un bol au
micro-ondes.

Étape 2 (farine, levure, sucre) :
Mettre la farine, la levure et le sucre dans un saladier. Mélanger et
creuser un puits.

Étape 3 (oeuf) :
Ajouter ensuite les oeufs entiers et fouetter l'ensemble.

Étape 4 (beurre, lait) :
Incorporer le beurre fondu, fouetter puis délayer progressivement le
mélange avec le lait afin d'éviter les grumeaux.

Étape 5 :
Laisser reposer la pâte au minimum 1 heure au réfrigérateur.

Étape 6 :
Dans une poêle chaude et légèrement huilée, faire cuire comme des crêpes,
mais en les faisant plus petites. Réserver au chaud et déguster.
'''


if __name__ == '__main__':
    nb_convives = int(input('Combien de personnes ? '))
    print('Pour faire', nom_recette, 
          'pour', nb_convives, 'il vous faudra :')
    rapport = nb_convives / nb_personnes_ref
    print(q_farine * rapport, u_farine, 'de farine')
    print(q_sucre * rapport, u_sucre, 'de sucre')
    print(q_levure * rapport, u_levure, 'de levure')
    print(q_beurre * rapport, u_beurre, 'de beurre')
    print(q_sel * rapport, u_sel, 'de sel')
    print(q_lait * rapport, u_lait, 'de lait')
    print(q_oeuf * rapport, u_oeuf, 'de oeuf')
    
    print(texte_recette)
