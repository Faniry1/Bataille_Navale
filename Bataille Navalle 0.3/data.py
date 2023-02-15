from tkinter import *
from random import *

# Nombre de Case
global Case
Case = 10 #int(input("Entier entre 2 et 10 ")) Nombre de côté

# Convertion du nombre de côté en pixel
global Side
Side = int(float(Case/2)*100)

# Taille d'un carré
global C
C = 50

# Compteur
global compteur
compteur = 0

# Les bateaux et leurs taille
global bate
bate = ["porte avion: 5","croiseur: 4",
          "contre tropilleur: 3","sous marin: 3",
          "tropilleur: 2"]

# MAP du Joueur et de l'ordinateur
global carte
carte = [["." for i in range(Case)] for j in range(Case)]
global carte2
carte2 = [["." for i in range(Case)]for i in range(Case)]

def carte0():
    global compteur
    compteur = 0
    for i in range(10):
        for j in range(10):
            carte[i][j] = '.'
            carte2[i][j] = '.'
carte0()
# Placement des bateau de l'ordinateur
def placemento(k):
    a = randint(0,1)
    if a == 0: # verticale
        x = randint(0,9-int(bate[compteur][-1:]))
        y = randint(0,9)
        if colision(x,y,carte2,int(bate[k][-1:]),"verticale") == False:
            for i in range(int(bate[k][-1:])):
                carte2[x+i][y] = "2"
        else:
            placemento(k)
    elif a == 1 : # verticale
        y = randint(0,9-int(bate[k][-1:]))
        x = randint(0,9)
        if colision(x,y,carte2,int(bate[k][-1:]),"horizontale") == False:
            for i in range(int(bate[k][-1:])):
                    carte2[x][y+i] = "2"
        else :
            placemento(k)

# Placement des bateauw
def placementBat(Action,i,j):
    carte[i][j] = Action

def tirSurOrdi(Action,i,j):
    carte2[i][j]=Action

def tirSurJoueur(Action,i,j):
    carte[i][j] = Action
    

# Sens par défauts
global sens
sens = "verticale"

# a est considérer comme le nombre de "1" dans la Map du Joueur soit le nombre de bateau
global a
def verifMapJoueur():
    a = 0
    for i in carte:
        if "1" in i:
            a += 1
    return a
a = verifMapJoueur()

# b est considérer comme le nombre de "2" dans la Map du Joueur soit le nombre de case de bateau           
global b
def verifMapOrdinateur():
    b = 0
    for i in carte2:
        if "2" in i:
            b += 1
    return b
b = verifMapOrdinateur()

def afficher(cart):
    for i in cart:
        print(i)


def colision(x,y,carte,taille, vers):
    a = False
    for i in range(taille):
        if vers == "verticale":
            if carte[x+i][y]!='.':
                a = True
        if vers == "horizontale":
            if carte[x][y+i]!='.':
                a = True  
    return a    
