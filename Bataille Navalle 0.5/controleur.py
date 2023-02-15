from view import *

# Appelle de la fonction accueil pour mettre le menu d'accueil
acceuil()
# Clique droite appuyer changer d'orientation
cnv1.bind("<Button-3>",orientation)
# Clique gauche appuyer enregistrement des coordonées du clic
cnv1.bind("<Button-1>",clic)
# Clique gauche maintenu deplacement du bateau
cnv1.bind("<B1-Motion>",moved)
# Clique gauche relachée, poser dans le cadrillage, si possible
cnv1.bind("<B1-ButtonRelease>",poser)
# Clique sur le terrain adversaire, permet de tirer
cnv2.bind("<Button-1>",tir_joueur)


root.mainloop()