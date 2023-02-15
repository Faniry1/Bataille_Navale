import tkinter as tk
from random import randrange
 
 
def move(event):
    x, y = event.x , event.y
    can.coords(img, x, y)

 
WIDTH, HEIGHT = 700, 600
 
fen = tk.Tk()
can = tk.Canvas(fen, width=WIDTH, height=HEIGHT)
can.pack(padx=100,pady=50)
 
#Importation de l'image et placement
img_import = tk.PhotoImage(file="titre.png")
img = can.create_image(200, 180, image=img_import)
 
#Bouton pour déplacer l'image
fen.bind("<B1-Motion>",move)


fen.mainloop()