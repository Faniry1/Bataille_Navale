#Nom Prenom
#!/usr/bin/env python
# coding: utf-8


from copy import*
from fractions import*
from random import*

#.............................................................................
#E: M liste de listes (sans contrainte de type ni de taille)
#   M peut contenir: entier, float, string, Fraction
#affichage en colonnes de largeur constante = longueur maximale + 3
#S: --
def affiche_str (M):
    maxi=0
    for L in M:
        for val in L:
            if len(str(val))>maxi:
                maxi=len(str(val))
                
    chaine_format="% "+ str(maxi+3) +"s"    
    for L in M:
        for val in L:
            print(chaine_format  %(val), end="")
        print("") 

#E: x de type fraction
#simplification en fraction irréductible
#S la fraction simplifiée: --
def formate_fraction(x):
    if x.numerator%x.denominator==0:
        return x.numerator//x.denominator
    else:
        return Fraction(x.numerator , x.denominator)            
############################################




# placer ici vos fonctions auxiliaires




############################################
#E: m  matrice carrée rationnelle
#   détermine si m est echelonnée en lignes
#S: renvoie un booléen
def bien_echelonnee(m):
    pass
    
    
    
#E: m  matrice carrée rationnelle
#   modifie m pour l'echelonner en lignes
#S: renvoie :  la matrice échelonnée, la liste des indices des colonnes des pivots, le nombre de permutations de lignes
def echelon_det_gauss(m):
    pass



#E: m  matrice carrée rationnelle
#   calcule le déterminant de m par échelonnement
#S: renvoie  det(m) 
def det_gauss(m):
    pass



#E: m  matrice carrée rationnelle
#   calcule le déterminant de m par développement selon ... à compléter
#S: renvoie  det(m) 
def det_rec(m):
    pass



#E: m  matrice carrée rationnelle inversible
#   calcule l'inverse de  m: transposee de la comatrice
#S: renvoie la matrice m^{-1} 
def inverse_cofacteurs(m):
    pass



#E: m  matrice carrée rationnelle
#   calcule le déterminant de m par échelonnement
#S: renvoie  det(m) 
def det_gauss_optimise(m):
    pass


#############################################

if __name__=='__main__':
   
   #placer ici les tests de toutes vos fonctions auxiliaires
   