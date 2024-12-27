
# [['Alice', 2], ['Bob', 3], ['Charlie', 1]]
def decide_vainqueur(resultat_votes):
    vote_maximum = 0
    candidat_gagnant = ''
    for resultat in resultat_votes:
        if resultat[1] > vote_maximum:
            vote_maximum = resultat[1]
            candidat_gagnant = resultat[0]
    return (candidat_gagnant, vote_maximum)

print(decide_vainqueur([['Alice', 2], ['Bob', 3], ['Charlie', 1]]))

# Une autre solution un peu plus compliquée,
# qui repose sur la même idée mais commence par aplatir la liste de listes
# [['Alice', 2], ['Bob', 3], ['Charlie', 1]]
# Votes aplatis : ['Alice', 2, 'Bob', 3, 'Charlie', 1]
def decide_vainqueur_2(resultat_votes):
    votes_aplatis = []
    for vote in resultat_votes:
        for element in vote:
            votes_aplatis.append(element)
    # votes_aplatis = les résultats aplatis
    i = 1
    maximum = 0
    while i < len(votes_aplatis):
        if votes_aplatis[i] > maximum:
            maximum = votes_aplatis[i]
        i += 2
    i = 0
    while i < len(votes_aplatis):
        if votes_aplatis[i] == maximum:
            return (votes_aplatis[i-1], votes_aplatis[i])
        i += 1

print(decide_vainqueur([['Alice', 2], ['Bob', 3], ['Charlie', 1]]))
