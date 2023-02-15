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

def placer(i,j,carte, nombat):
    carte[i][j] = nombat

def colision(x,y,carte,taille,a):
    reponse = False
    for i in range(taille):
        if a == "verticale":
            if carte[x+i][y] != '.' :
                reponse = True
        if a=="horizontale":
            if carte[x][y+i] != '.' :
                reponse = True
    return reponse

def placementbatO(bateau,taille):
    a = randint(0,1)
    x,y = randint(0,9),randint(0,9)
    if a == 0:
        orient = "verticale"
        if x<10-taille and colision(x,y,carte2,taille,orient)==False:
            for i in range(taille):
                carte2[x+i][y] = bateau
        else:
            placementbatO(bateau,taille)
    if a ==1:
        orient = "horizontale"
        if y<10-taille and colision(x,y,carte2,taille,orient)==False:
            for i in range(taille):
                carte2[x][y+i] = bateau
        else:
            placementbatO(bateau,taille)
            
def placementTousBatO():
    for i in bate:
        placementbatO(i[:2],int(i[-1:]))
    
global sens
sens = "verticale"
def placementbatJ(x,y,bateau,taille):
    for i in range(taille):
        if sens == "verticale":
            carte1[x+i][y] = bateau
        else:
            carte1[x][y+i] = bateau

