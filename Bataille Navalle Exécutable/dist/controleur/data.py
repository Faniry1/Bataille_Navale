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

# Réinitialise la carte du joueur et de l'ordinateur 
def carte0():
    global compteur
    compteur = 0
    for i in range(10):
        for j in range(10):
            carte[i][j] = '.'
            carte2[i][j] = '.'
carte0()

# Placement des bateau de l'ordinateur
global Coop2
Coop2 = [[None,None,""],[None,None,""],[None,None,""],[None,None,""],[None,None,""]]
def placemento(k):
    a = randint(0,1)
    if a == 0: # verticale
        Coop2[k][2] = "verticale"
        x = randint(0,9-int(bate[compteur][-1:]))
        y = randint(0,9)
        Coop2[k][0],Coop2[k][1] = y*C+25,x*C+C*int(bate[k][-1:])//2
        if colision(x,y,carte2,int(bate[k][-1:]),"verticale") == False:
            for i in range(int(bate[k][-1:])):
                carte2[x+i][y] = str(k+1)
        else:
            placemento(k)
    elif a == 1 : # horizontale
        Coop2[k][2] = "horizontale"
        y = randint(0,9-int(bate[k][-1:]))
        x = randint(0,9)
        Coop2[k][0],Coop2[k][1] = y*C+C*int(bate[k][-1:])//2,x*C+25
        if colision(x,y,carte2,int(bate[k][-1:]),"horizontale") == False:
            for i in range(int(bate[k][-1:])):
                    carte2[x][y+i] = str(k+1)
        else :
            placemento(k)

# Placement des bateauw
def placementBat(Action,i,j):
    carte[i][j] = Action

# Réinitialise une case
def enleverBat(nom):
    for i in range(10):
        for j in range(10):
            if carte[i][j] == nom:
                carte[i][j] = '.'

# Place l'Action dans la carte du joueur
def tirSurOrdi(Action,i,j):
    carte2[i][j]=Action

# Place l'Action dans la carte du joueur
def tirSurJoueur(Action,i,j):
    carte[i][j] = Action
    

# Sens par défauts
global sens
sens = "verticale"

global a
# Vérifie le nobre de case bateau restant chez le joueur
def verifMapJoueur():
    a = 17
    for i in range(10):
        for j in range(10):
            if carte[i][j] == 'T' :
                a = a-1
    return a
a = verifMapJoueur()
        
global b
# Vérifie le nobre de case bateau restant chez l'ordinateur
def verifMapOrdinateur():
    b = 17
    for i in range(10):
        for j in range(10):
            if carte2[i][j] == 'T' :
                b = b-1
    return b
b = verifMapOrdinateur()

# Permet d'afficher la carte dans la console
def afficher(cart):
    for i in cart:
        print(i)

# Vérification de la colision entre les bateaux de l'ordinateur
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

# Vérification de la colision entre bateau du Joueur
def colision2(x,y,taille,v):
    a = False
    for i in range(((-taille)+1)//2,taille-taille//2):
        if v == "verticale":
            if carte[x+i][y] != '.':
                a = True
        if v == "horizontale":
            if carte[x][y+i] != '.':
                a = True
    return a

# Fonction qui vérifir si b est dans la carte du Joueur
def estdans(b):
    a = False
    for i in range(10):
        for j in range(10):
            if carte[i][j]==b:
                a = True
    return a
def estdans2(b):
    a = False
    for i in range(10):
        for j in range(10):
            if carte2[i][j]==b:
                a = True
    return a