from data import *
from tkinter import *

# Creation de la fenêtre
global root
root = Tk()
root.title("World Of Warship")

# Creation du terrain du Joueur et de l'ordinateur
terrain1 = Canvas(root, width=pixel,height=pixel, background="ivory")
terrain2 = Canvas(root, width=pixel,height=pixel, background="ivory")
# terrain1.pack(side = "left",padx=30,pady=30)

def cadrillage1():
    Lettre = ["A","B","C","D","E","F","G","H","I","J"]
    for i in range(case):
        terrain1.create_window(C//2+i*C,pixel+10,window=Label(text=str(i+1),bg="lightsteelblue2"))
        terrain1.create_window(pixel+7,C//2+i*C, window=Label(text=Lettre[i],bg="lightsteelblue2"))
        for j in range(case):
            x1=j*C
            x2=j*C+C
            y1=i*C
            y2=C+i*C
            if carte1[i][j]==".":
                terrain1.create_rectangle(x1,y1,x2,y2,fill="lightsteelblue2",outline="black",activeoutline="white",activewidth=3)
            elif carte1[i][j]=="X":
                terrain1.create_rectangle(x1,y1,x2,y2,fill="blue2",outline="black",activeoutline="white",activewidth=3)
            elif len(carte1[i][j])==3:
                terrain1.create_rectangle(x1,y1,x2,y2,fill="red",outline="black",activeoutline="white",activewidth=3)
            else:
                terrain1.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="white",outline="black")
    terrain1.create_window(pixel//2,-10, window=Label(text="Joueur",bg="lightsteelblue2"))

def cadrillage2():
    Lettre = ["A","B","C","D","E","F","G","H","I","J"]
    for i in range(case):
        terrain2.create_window(C//2+i*C,pixel+10,window=Label(text=str(i+1),bg="lightsteelblue2"))
        terrain2.create_window(pixel+7,C//2+i*C, window=Label(text=Lettre[i],bg="lightsteelblue2"))
        for j in range(case):
            if carte2[i][j]=='.':
                terrain2.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="lightsteelblue2",outline="black",activeoutline="white",activewidth=3)
            elif carte2[i][j]=="X":
                terrain2.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="blue2",outline="black",activeoutline="white",activewidth=3)
            elif len(carte2[i][j])==2:
                terrain2.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="lightsteelblue2",outline="black",activeoutline="white",activewidth=3)
            elif len(carte2[i][j])>=2:
                terrain2.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="red",outline="black",activeoutline="white")
    terrain2.create_window(pixel//2,-10, window=Label(text="Ordinateur",bg="lightsteelblue2"))

def orientation(event):
    global sens
    if sens == "verticale":
        sens = "horizontale"
    else:
        sens = "verticale"
    regle["text"] = "Placer votre "+ bate[compteur][:-3]+" de taille "+ bate[compteur][-1:]+" en "+sens

global compteur
compteur = 0
def placement(event):
    global compteur
    global sens
    x,y = event.x,event.y
    if compteur >= 5:
        terrain1.unbind("<Button-1>")
        terrain2.pack(side = "left",padx=30,pady=30)
    else:
        if compteur == 4:
            regle.destroy()
            cadrillage2()
            terrain2.pack(side="left")
        for i in range(pixel//C):
            for j in range(pixel//C):
                if sens == "verticale":
                    if j*C<x<C+j*C and i*C<y<C+i*C and i<=case-int(bate[compteur][-1:]) and colision(i,j,carte1,int(bate[compteur][-1:]),"verticale")==False:
                        for p in range(int(bate[compteur][-1:])):
                            placer(i+p,j,carte1,bate[compteur][:2])
                        compteur +=1
                if sens == "horizontale" :
                    if j*C<x<C+j*C and i*C<y<C+i*C and j<=case-int(bate[compteur][-1:]) and colision(i,j,carte1,int(bate[compteur][-1:]),"horizontale")==False:
                        for p in range(int(bate[compteur][-1:])):
                            placer(i,j+p,carte1,bate[compteur][:2])
                        compteur +=1
        if compteur<=4:
            regle["text"] = "Placer votre "+ bate[compteur][:-3]+" de taille "+ bate[compteur][-1:]+" en "+sens
    cadrillage1()
        
regle = Label(height=1, font="Arial 20 bold",text="Placer votre "+ bate[compteur][:-3]+" de taille "+ bate[compteur][-1:] + " en "+ sens,bg="lightsteelblue1")   
def jeu():
    regle.pack(pady = 40)
    cadrillage1()
    terrain1.pack(side="left",pady=30,padx = 30)
    ia.destroy()
    ligne.destroy()

def quitter():
    root.destroy()


ia = Button(root,font ="Times 20 italic",text="Jouer contre Ordinateur",command=jeu,height=3,width=30,bg="grey")
ligne = Button(root,font ="Times 20 italic",text="Jouer en ligne",height=3,width=30,bg="grey")
ia.pack(fill=X, pady=10)
ligne.pack(fill=X,pady=10)
sortie = Button(root,font ="Arial 15 bold",text="Quit",command=quitter,height=1,bg="grey")
sortie.pack(side="bottom")
