from tkinter import *
from random import *
import pygame

# Nombre de Case
Case = 10 #int(input("Entier entre 2 et 10 ")) Nombre de côté

# Convertion du nombre de côté en pixel
Side = int(float(Case/2)*100)
C = 50

# Création de la fenêtre
root = Tk()
root.title("Bataille Navale")
root.attributes('-fullscreen', True)

# Les bateaux et leurs taille
bate = ["porte avion: 5","croiseur: 4",
          "contre tropilleur: 3","sous marin: 3",
          "tropilleur: 2","Rien: 0"]

# Tour du bateau
compteur = 0

# Sens par défauts
sens = "verticale"

# Image des bateaux
vert=[PhotoImage(file = "porteavionv.png"),PhotoImage(file = "croiseurv.png"),PhotoImage(file = "contretorpilleurv.png"),
      PhotoImage(file = "sousmarinv.png"),PhotoImage(file = "torpilleurv.png"),PhotoImage(file = "r.png")]
hori=[PhotoImage(file = "porteavionh.png"),PhotoImage(file = "croiseurh.png"),PhotoImage(file = "contretorpilleurh.png"),
      PhotoImage(file = "sousmarinh.png"),PhotoImage(file = "torpilleurh.png"),PhotoImage(file = "r.png")]

# Image de fond
fond = PhotoImage(file = "bg.png")
label1 = Label( root, image = fond)
label1.place(x = 0,y = 75)

# Initiation au son
pygame.mixer.init()
musique =  pygame.mixer.Sound("sondefond.mp3")
explosion = pygame.mixer.Sound("explosion.mp3")
gameover = pygame.mixer.Sound("gameover.wav")
eau = pygame.mixer.Sound("eau.mp3")
musique.play(-1)

# Création du terrain du Joueur
cnv1=Canvas(root, width=Side,height=Side, background="ivory")
cool = Label(height=5,width=C,text="Placez votre "+bate[compteur]+" en " +sens,image='',bg='white')
def plateau():
    global bouton
    cnv1.pack(side=LEFT,padx=C*3,pady=C)
    # Cadrillage des deux terrains
    for i in range(Side//C):
        for j in range(Side//C):
            cnv1.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="white")
    #Nomation du cadrillage Joueur
    joueur = Label(height=1,width=10,text="Joueur",bg="blue")
    cnv1.create_window(Side//2,-10,window=joueur)
    Liste = ["A","B","C","D","E","F","G","H","I","J"]
    for k in range(Case):
        cnv1.create_window(C//2+k*C,Side+10,window=Label(height=1,width=1,text=str(k+1),bg="ivory"))
        cnv1.create_window(-5,C//2+k*C,window=Label(height=1,width=1,text=Liste[k],bg="ivory"))   
    bouton.destroy()
    bouton2.destroy()
    cool.pack(side="left",padx=C)

# Nom du jeu
titre= Label(height=1, font="Arial 30 bold",text="Bataille Navale",bg="green")
titre.pack(side="top",fill=X,pady=10)

# Commencement du jeu
bouton = Button(root, text="Jouer contre Ordinateur",command=plateau,width=40,bg="cyan")
bouton.pack(padx=100, pady=20)

bouton2 = Button(root, text="Jouer en ligne",width=40,bg="cyan")
bouton2.pack(padx=100, pady=30)

# Création du terrain Ordinateur
cnv2=Canvas(root, width=Side,height=Side, background="ivory")

# Changement d'Orientation du bateau
def orientation(event):
    global sens
    if sens=="horizontale":
        sens = "verticale"
    else:
        sens = "horizontale"
    cool["text"]="Placez votre "+bate[compteur]+" en " +sens
#Changement d'orientation au clic droit
cnv1.bind("<Button-3>",orientation)

# Fixer la taille de la fenêtre
root.resizable(False, False)

# Placement du bateau du joueur
carte = [["." for i in range(Case)] for j in range(Case)]
def placement(event):
    global sens
    global bate
    global compteur
    global carte
    x,y = event.x,event.y
    if compteur<len(bate)-1:
        for i in range(Side//C):
            for j in range(Side//C):
                if sens == "verticale":
                    if j*C<x<C+j*C and i*C<y<C+i*C:
                        cnv1.create_rectangle(j*C,i*C,C+j*C,i*C+(C*int(bate[compteur][-1:])),fill="grey")
                        center= (j*C+C/2+1,i*C+(C*int(bate[compteur][-1:]))/2)
                        cnv1.create_image(center, image=vert[compteur])
                        for p in range(int(bate[compteur][-1:])):
                            carte[i+p][j] = "1"
                        compteur +=1
                if sens == "horizontale":
                    if j*C<x<C+j*C and i*C<y<C+i*C:
                        cnv1.create_rectangle(j*C,i*C,(j*C)+(C*int(bate[compteur][-1:])),i*C+C,fill="grey")
                        center= (j*C+(C*int(bate[compteur][-1:]))/2,i*C+C/2+1)
                        cnv1.create_image(center, image=hori[compteur])
                        for p in range(int(bate[compteur][-1:])):
                            carte[i][j+p] = "1"
                        compteur +=1
    if compteur==5:
        cool.destroy()
        cnv2.pack(side=RIGHT,padx=C*3,pady=Side//10)
        Liste = ["A","B","C","D","E","F","G","H","I","J"]
        for k in range(Case):
            cnv2.create_window(C//2+k*C,Side+10,window=Label(height=1,width=1,text=str(k+1),bg="ivory"))
            cnv2.create_window(-5,C//2+k*C,window=Label(height=1,width=1,text=Liste[k],bg="ivory")) 
        #Nomation du cdrillage Ordinateur
        Ordinateur = Label(height=1,width=10,text="Ordinateur",bg="red")
        cnv2.create_window(Side//2,-10,window=Ordinateur)
        for i in range(Side//C):
            for j in range(Side//C):
                cnv2.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="white")
    cool["text"]="Placez votre "+bate[compteur]+" en " +sens
cnv1.bind("<Button-1>",placement)

# Carte de l'orinateur
carte2 = [["." for i in range(Case)]for i in range(Case)]
# Placement des bateau de l'ordinateur
def placemento():
    for k in range(len(bate)):
        x = randint(0,Case-int(bate[k][-1:]))
        y = randint(0,Case-int(bate[k][-1:]))
        a = randint(1,2)
        for l in range(int(bate[k][-1:])):
            if a==1:
                carte2[x][y+l] =  "2"
            if a==2:
                carte2[x+l][y] =  "2"
placemento()
            
# Vérification  du gagneur
def verif1(cart):
    global C
    global fermer
    a = 0
    for i in cart:
        if "2" in i:
            a += 1
    if a==0:
        sans = Label(height=10, width=C,text = "Joueur, Vous avez gagné",bg="green")
        sans.pack(padx =Side//2,pady=Side//2)
        cnv1.destroy()
        cnv2.destroy()

# Tir du joueur
def tir_joueur(event):
    global carte2
    global carte
    x,y = event.x,event.y
    for i in range(Side//C):
        for j in range(Side//C):
            if j*C<x<C+j*C and i*C<y<C+i*C:
                if carte2[i][j] =='.':
                    cnv2.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="blue")
                    carte2[i][j] ='X'
                    eau.play()
                if carte2[i][j] =='2':
                    cnv2.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="red")
                    carte2[i][j] ='T'
                    explosion.play()
    verif1(carte2)
    tir_ordi()
    verif2(carte)
cnv2.bind("<Button-1>",tir_joueur)

def verif2(cart):
    global fermer
    a = 0
    for i in cart:
        if "1" in i:
            a += 1
    if a==0:
        sans = Label(height=10, width=C,text = "Joueur, Vous avez perdu",bg="red")
        sans.pack(padx =Side//2,pady=Side//2)
        cnv1.destroy()
        cnv2.destroy()
        gameover.play()

# Tir de l'ordinateur après le tir du joueur
def tir_ordi():
    global carte
    x,y = randint(0,Side-1),randint(0,Side-1)
    for i in range(Side//C):
        for j in range(Side//C):
            if j*C<x<C+j*C and i*C<y<C+i*C:
                if carte[i][j] == 'X' or carte[i][j] == 'T':
                    tir_ordi()
                elif carte[i][j] =='.':
                    cnv1.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="blue")
                    carte[i][j] ='X'
                elif carte[i][j] =='1':
                    cnv1.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="red")
                    carte[i][j] ='T'

# Quitter la fenêtre
def quitter():
    pygame.quit()
    root.destroy()
# Bouton pour fermer
fermer = Button(root, text="Fermer",command=quitter,width=15,bg="red")
fermer.pack(side="bottom",pady=10)

root.mainloop()