from view import *

#placement des bateaux au hasard dans la MapOrdinateur
for k in range(len(bate)):
    placemento(k)
cnv1.bind("<Button-3>",orientation)
cnv2.bind("<Button-1>",tir_joueur)
cnv1.bind("<Button-1>",placement)
# cnv1.bind("<B1-Motion>",move)

root.mainloop()