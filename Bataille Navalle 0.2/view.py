from data import *
import pygame

# Création de la fenêtre
global root
root = Tk()
root.title("Bataille Navale")
# root.attributes('-fullscreen', True)
# root.resizable(False, False)

# Image des bateaux
global vert
global hori
vert=[PhotoImage(file = "porteavionv.png"),PhotoImage(file = "croiseurv.png"),PhotoImage(file = "contretorpilleurv.png"),
      PhotoImage(file = "sousmarinv.png"),PhotoImage(file = "torpilleurv.png"),PhotoImage(file = "r.png")]
hori=[PhotoImage(file = "porteavionh.png"),PhotoImage(file = "croiseurh.png"),PhotoImage(file = "contretorpilleurh.png"),
      PhotoImage(file = "sousmarinh.png"),PhotoImage(file = "torpilleurh.png"),PhotoImage(file = "r.png")]

# # Image de fond
# fond = PhotoImage(file = "bg.png")
# label1 = Label( root, image = fond)
# label1.place(x = 0,y = 75)

# Initiation au son
pygame.mixer.init()
musique =  pygame.mixer.Sound("sondefond.mp3")
explosion = pygame.mixer.Sound("explosion.mp3")
gameover = pygame.mixer.Sound("gameover.wav")
eau = pygame.mixer.Sound("eau.mp3")
# musique.play(-1)

cnv = Canvas(root, width=3000,height=1500, background="white")

# Création du terrain du Joueur
cnv1=Canvas(cnv, width=Side,height=Side, background="ivory")

# Création du terrain Ordinateur
cnv2=Canvas(cnv, width=Side,height=Side, background="ivory")

# Instruction en Label
cool = Label(height=5,width=C,text="Placez votre "+bate[compteur]+" en " +sens,image='',bg='white')

# Nom du jeu
titre= Label(height=1, font="Arial 40 bold",text="WORLD OF WORLDSHIPS",bg="DodgerBlue3")
titre.pack(side="top",fill=X,pady=10)

# Toucher le Bouton pour activer plateau()
def plateau():
    cnv.pack()
    cnv1.pack(side=LEFT,padx=C*3,pady=C)
    packbateau()
    # Cadrillage du cadriage du Joueur
    for i in range(Side//C):
        for j in range(Side//C):
            cnv1.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="lightsteelblue1")
    #Nomation du cadrillage Joueur
    joueur = Label(height=1,width=10,text="Joueur",bg="lightsteelblue1")
    cnv1.create_window(Side//2,-10,window=joueur)
    Liste = ["A","B","C","D","E","F","G","H","I","J"]
    for k in range(Case):
        cnv1.create_window(C//2+k*C,Side+10,window=Label(height=1,width=1,text=str(k+1),bg="lightsteelblue1"))
        cnv1.create_window(-5,C//2+k*C,window=Label(height=1,width=1,text=Liste[k],bg="lightsteelblue1"))   
    bouton.destroy()
    bouton2.destroy()
    cool.pack(side="left",padx=C)
#     global img
#     a = vert[compteur]
#     img =cnv1.create_image(Side//2,Side//2,image = a)

# Changement d'Orientation du bateau
def orientation(event):
    global sens
    if sens=="horizontale":
        sens = "verticale"
    else:
        sens = "horizontale"
    cool["text"]="Placez votre "+bate[compteur]+" en " +sens

def packbateau():
    global bt1,bt2,bt3,bt4,bt5
    bt1 = cnv.create_image((1000-200,Side//2),image=vert[0])
    bt2 = cnv.create_image((1060-200,Side//2),image=vert[1])
    bt3 = cnv.create_image((1120-200,Side//2),image=vert[2])
    bt4 = cnv.create_image((1180-200,Side//2),image=vert[3])
    bt5 = cnv.create_image((1240-200,Side//2),image=vert[4])
        
def placement(event):
    global compteur
    x,y = event.x,event.y
    if compteur < len(bate):
        for i in range(Side//C):
            for j in range(Side//C):
                if sens == "verticale":
                    if j*C<x<C+j*C and i*C<y<C+i*C:
                        if i<11-int(bate[compteur][-1:]) and colision(i,j,carte,int(bate[compteur][-1:]),"verticale") == False:
                            cnv1.create_rectangle(j*C,i*C,C+j*C,i*C+(C*int(bate[compteur][-1:])),fill="grey")
                            center= (j*C+C/2+1,i*C+(C*int(bate[compteur][-1:]))/2)
                            cnv1.create_image(center, image=vert[compteur])
                            for p in range(int(bate[compteur][-1:])):
                                placementBat("1",i+p,j)
                            compteur +=1
                if sens == "horizontale":
                    if j*C<x<C+j*C and i*C<y<C+i*C:
                        if j<11-int(bate[compteur][-1:]) and colision(i,j,carte,int(bate[compteur][-1:]),"horizontale") == False:
                            cnv1.create_rectangle(j*C,i*C,(j*C)+(C*int(bate[compteur][-1:])),i*C+C,fill="grey")
                            center= (j*C+(C*int(bate[compteur][-1:]))/2,i*C+C/2+1)
                            cnv1.create_image(center, image=hori[compteur])
                            for p in range(int(bate[compteur][-1:])):
                                placementBat("1",i,j+p)
                            compteur +=1
        if compteur <len(bate)-1:
            cool["text"]="Placez votre "+bate[compteur]+" en " + sens
    if compteur==5:
        terrainOrdi()
        compteur+=1

def terrainOrdi():
        cool.destroy()
        cnv2.pack(side=RIGHT,padx=C*3,pady=Side//10)
        Liste = ["A","B","C","D","E","F","G","H","I","J"]
        for k in range(Case):
            cnv2.create_window(C//2+k*C,Side+10,window=Label(height=1,width=1,text=str(k+1),bg="ivory"))
            cnv2.create_window(-5,C//2+k*C,window=Label(height=1,width=1,text=Liste[k],bg="ivory")) 
        #Nomation du cdrillage Ordinateur
        Ordinateur = Label(height=1,width=10,text="Ordinateur",bg="plum1")
        cnv2.create_window(Side//2,-10,window=Ordinateur)
        # Creation du terrain de l'ordinateur
        for i in range(Side//C):
            for j in range(Side//C):
                cnv2.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="plum1")

# Tir du joueur
def tir_joueur(event):
    global a
    global b
    x,y = event.x,event.y
    tirvalide = False
    for i in range(Side//C):
        for j in range(Side//C):
            if j*C<x<C+j*C and i*C<y<C+i*C:
                if carte2[i][j] =='.':
                    cnv2.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="blue")
                    tirSurOrdi("X",i,j)
                    eau.play()
                    tirvalide = True
                elif carte2[i][j] =='2':
                    cnv2.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="firebrick1")
                    tirSurOrdi("T",i,j)
                    explosion.play()
                    tirvalide = True
    a = verifMapJoueur()
    if tirvalide == True:
        tir_ordi()
    b = verifMapOrdinateur()
    verif(a,b)


# Tir au hasard de l'ordinateur
def tir_ordi():
    x,y = randint(0,Side-1),randint(0,Side-1)
    for i in range(Side//C):
        for j in range(Side//C):
            if j*C<=x<=C+j*C and i*C<y<C+i*C:
                if carte[i][j] == 'X' or carte[i][j] == 'T':
                    tir_ordi()
                elif carte[i][j] =='.':
                    cnv1.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="blue")
                    tirSurJoueur('X',i,j)
                elif carte[i][j] =='1':
                    cnv1.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="firebrick1")
                    tirSurJoueur('T',i,j)
# Vérifie et renvoi le gagnant
def verif(a,b):
    if a==0:
        sans = Label(height=10, width=C,font ="times 30 italic",text = "Joueur, Vous avez perdu",bg="red3")
        sans.pack(padx =30,pady=20)
        cnv1.destroy()
        cnv2.destroy()
        gameover.play()
    elif b==0:
        sans = Label(height=10, width=C,font ="times 30 italic",text = "Joueur, Vous avez gagné",bg="green3")
        sans.pack(padx =30,pady=20)
        cnv1.destroy()
        cnv2.destroy()

# Bouton pour Jouer contre Ordinateur
bouton = Button(root, font="Times 20 italic", text="Jouer contre Ordinateur",command=plateau,width=40,bg="cyan")
bouton.pack(padx=100, pady=20)

# Bouton pour Jouer en ligne
bouton2 = Button(root,font="times 20 italic", text="Jouer en ligne",width=40,bg="cyan")
bouton2.pack(padx=100, pady=30)

# Quiter la fenêtre et pygame
def quitter():
    pygame.quit()
    root.destroy()
    
# Bouton pour fermer
fermer = Button(root, font="Arial 15 bold",text="Fermer",command=quitter,width=15,bg="red")
fermer.pack(side="bottom",pady=10)

def move(event):
    x, y = event.x , event.y
    cnv1.coords(img, x, y)


