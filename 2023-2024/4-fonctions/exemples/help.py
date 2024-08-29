# Fonctionnement de la documentation Python (docstring) et des tests automatiques (doctest)
def triple(n):
  """
  Fonction calculant le triple du nombre n (int ou float)
  ou la répétition trois fois de la chaîne n.
  >>> triple(3)
  9
  >>> triple(9.0)
  27.0
  >>> triple("ab")
  'ababab'
  """
  return n * 4

import doctest
doctest.testmod()
