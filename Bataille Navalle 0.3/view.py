from data import *
import pygame

# Création de la fenêtre
global root
root = Tk()
root.title("Bataille Navale")
root.geometry("1200x900")
root.resizable(False, False)

# Création du terrain Ordinateur
cnv2=Canvas(root, width=Side,height=Side, background="ivory")

# Image des bateaux
global vert
global hori
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
musique.set_volume(0.1)

# Création du terrain du Joueur
cnv1=Canvas(root, width=Side,height=Side, background="ivory")

# Création du terrain Ordinateur
cnv2=Canvas(root, width=Side,height=Side, background="ivory")

# Nom du jeu
titre= Label(height=1, font="Arial 40 bold",text="WORLD OF WORLDSHIPS",bg="DodgerBlue3")
titre.pack(side="top",fill=X,pady=10)

# Toucher le Bouton pour activer plateau()
def plateau():
    global compteur
    compteur = 0
    carte0()
    for z in range(len(bate)):
        placemento(z)
    continuer.pack_forget()
    menu.pack(side="top",pady=10)
    restart.pack(side="bottom",pady=10)
    cnv1.pack(side=LEFT,padx=20,pady=20)
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
    bouton.pack_forget()
    bouton2.pack_forget()
    bouton3.pack_forget()
    # Instruction en Label
    global cool
    cool = Label(height=5,width=C,text="Placez votre "+bate[compteur]+" en " +sens,image='',bg='white')
    cool.pack(side="left",padx=C)

# Changement d'Orientation du bateau
def orientation(event):
    global sens
    global compteur
    if sens=="horizontale":
        sens = "verticale"
    else:
        sens = "horizontale"
    if compteur<len(bate):
        cool["text"]="Placez votre "+bate[compteur]+" en " +sens
       
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
        cool.pack_forget()
        cnv2.pack(side=RIGHT,padx=20,pady=20)
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

# Le gagnant
global sans
sans=Label()
# Vérifie et renvoi le gagnant
def verif(a,b):
    global sans
    if a==0:
        sans = Label(height=5, width=30,font ="times 30 italic",text = "Joueur, Vous avez perdu",bg="red3")
        sans.pack(padx =50,pady=50)
        cnv1.pack_forget()
        cnv2.pack_forget()
        gameover.play()
    elif b==0:
        sans = Label(height=5, width=30,font ="times 30 italic",text = "Joueur, Vous avez gagné",bg="green3")
        sans.pack(padx =50,pady=50)
        cnv1.pack_forget()
        cnv2.pack_forget()

# Son active ou désactive
global voice
voice = "Mute"
def parametre():
    bouton.pack_forget()
    bouton2.pack_forget()
    bouton3.pack_forget()
    retour.pack(side = "left",padx=50, pady=30)
    global mute, lang
    # Bouton pour le Son
    mute = Button(root,font="times 20 italic", text=voice,command = couper , width=40,bg="cyan")
    mute.pack(padx=100, pady=30)
    # Bouton pour la résolution
    global res
    reso = ["1200x900","1500x990","1900x1080","-fullscreen"]
    res = Spinbox(root,values=reso ,width=40,bg="cyan",
                  justify=CENTER,wrap=True,font="times 20 italic",
                  command=resolution)
    res.pack(padx=100, pady=30)
    # Bouton pour la Langue
    lang = Button(root,font="times 20 italic", text="Langue" ,width=40,bg="cyan")
    lang.pack(padx=100, pady=30)

# Réglage de la résolution
def resolution():
    if res.get() == "-fullscreen":
        root.attributes('-fullscreen', True)
    else:
        root.attributes('-fullscreen', False)
        root.geometry(res.get())


# Ce que fait le bouton retour
def ret():
    acceuil()
    mute.pack_forget()
    retour.pack_forget()
    lang.pack_forget()
    res.pack_forget()
global retour
retour = Button(root,font="Arial 20 bold", text="<Retour ",command =ret, width=10,bg="cyan")

def couper():
    global voice
    if voice=="Mute":
        pygame.quit()
        voice = "Son"
        mute["text"] = "Son"
    else:
        voice = "Mute"
        mute["text"] = "Mute"
        pygame.mixer.init()
        musique.play(-1)

global bouton, bouton2, bouton3
# Bouton pour Jouer contre Ordinateur
bouton = Button(root, font="Times 20 italic", text="Jouer contre Ordinateur",command=plateau,width=40,bg="cyan")
# Bouton pour Jouer en ligne
bouton2 = Button(root,font="times 20 italic", text="Jouer en ligne",width=40,bg="cyan")
# Bouton pour Paramètre
bouton3 = Button(root,font="times 20 italic", text="Paramètre",command=parametre,width=40,bg="cyan")

# Menu acceuil
def acceuil():
    bouton.pack(padx=100, pady=20)
    bouton2.pack(padx=100, pady=30)
    bouton3.pack(padx=100, pady=30)

# Quiter la fenêtre et pygame
def quitter():
    pygame.quit()
    root.destroy()
    
# Bouton pour fermer
fermer = Button(root, font="Arial 15 bold",text="Fermer",command=quitter,width=10,bg="red")
fermer.pack(side=BOTTOM,pady=10)

def restart():
    global compteur
    cnv2.pack_forget()
    compteur = 0
    cool.pack_forget()
    sans.pack_forget()
    carte0()
    plateau()
    sans.pack_forget()
    
# Bouton pour fermer
restart = Button(root, font="Arial 15 bold",text="Restart",command=restart,width=10,bg="yellow")

def cont():
    menu.pack(side=TOP)
    restart.pack(side=BOTTOM)
    continuer.pack_forget()
    bouton.pack_forget()
    bouton2.pack_forget()
    bouton3.pack_forget()
    global compteur
    cnv1.pack(side=LEFT,padx=20,pady=20)
    if compteur>len(bate)-1:
        cnv2.pack(side=RIGHT,padx=20,pady=20)
    else:
        cool.pack(side=RIGHT,padx=20,pady=20)
        
# Bouton continuer
continuer = Button(root,font ="Times 20 italic", text="Continuer",command = cont, width=40,bg="cyan")
# Menu avec continuer
def men():
    menu.pack_forget()
    cnv1.pack_forget()
    cnv2.pack_forget()
    cool.pack_forget()
    restart.pack_forget()
    continuer.pack(padx=100,pady=30)
    acceuil()
# Bouton menu
menu = Button(root, font="Arial 15 bold",text="Menu",command=men,width=10,bg="grey")