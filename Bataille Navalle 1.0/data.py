from random import *

# taille d'une Case
global case
case = 10

# Coté d'un carré
global C
C =50

# Taille d'une case en pixel
global pixel
pixel = case * C

# Carte du Joueur et Ordinateur
global carte1
carte1 = [[ '.' for i in range(case)] for j in range(case)]
global carte2
carte2 = [[ '.' for i in range(case)] for j in range(case)]

# Les bateaux et leurs taille
global bate
bate = ["porte avion: 5","croiseur: 4",
          "contre tropilleur: 3","sous marin: 3",
          "tropilleur: 2"]


