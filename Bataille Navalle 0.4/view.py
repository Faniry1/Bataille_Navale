from data import *
import pygame

# Création de la fenêtre
global root
root = Tk()
root.title("Bataille Navale")
root.geometry("1200x900")
root.resizable(False, False)

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
explosion.set_volume(0)
gameover.set_volume(0)
eau.set_volume(0)

# Création du terrain du Joueur
global xcnv1
xcnv1 = Side+C*2
cnv1=Canvas(root, width= xcnv1,height=Side, background="ivory")

# Création du terrain Ordinateur
cnv2=Canvas(root, width=Side,height=Side, background="ivory")

# Nom du jeu
titre= Label(height=1, font="Arial 40 bold",text="WORLD OF WORLDSHIPS",bg="DodgerBlue3")
titre.pack(side="top",fill=X,pady=10)

# Toucher le Bouton pour activer plateau()
global etat
etat = 0
def plateau():
    global compteur , etat
    compteur = 0
    etat = 1
    carte0()
    for z in range(len(bate)):
        placemento(z)
    continuer.pack_forget()
    menu.pack(side="top",pady=10)
    restart.pack(side="bottom",pady=10)
    cnv1["width"]=600
    cnv1.pack(side=LEFT,padx=20,pady=20)
    # Cadrillage du cadriage du Joueur
    for i in range(Side//C):
        for j in range(Side//C):
            cnv1.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="lightsteelblue1")
    # Mettre le bateau
    createboat() 
    #Nomation du cadrillage Joueur
    joueur = Label(height=1,width=10,text=str(name),bg="lightsteelblue1")
    cnv1.create_window(Side//2,-10,window=joueur)
    Liste = ["A","B","C","D","E","F","G","H","I","J"]
    for k in range(Case):
        cnv1.create_window(C//2+k*C,Side+10,window=Label(height=1,width=1,text=str(k+1),bg="lightsteelblue1"))
        cnv1.create_window(-5,C//2+k*C,window=Label(height=1,width=1,text=Liste[k],bg="lightsteelblue1"))   
    bouton.pack_forget()
    bouton2.pack_forget()
    bouton3.pack_forget()
    boutbat.pack(side="right",padx=20)

# Changement d'Orientation du bateau
def orientation(event):
    global sens
    global compteur
    if sens=="horizontale":
        sens = "verticale"
    else:
        sens = "horizontale"
       
def createboat():
    global compteur
    global boat
    global boat1,boat2,boat3,boat4,boat5   
    global xboat, yboat
    xboat=540
    yboat=250
    global sens
    sens = "verticale"
    if compteur == 0:
        boat1 = cnv1.create_image(xboat,yboat,image=vert[0])
        boat = boat1
    elif compteur == 1:
        boat2 = cnv1.create_image(xboat,yboat,image=vert[1])
        boat = boat2
    elif compteur == 2:
        boat3 = cnv1.create_image(xboat,250,image=vert[2])
        boat = boat3
    elif compteur == 3:
        boat4 = cnv1.create_image(xboat,yboat,image=vert[3])
        boat = boat4
    elif compteur == 4:
        boat5 = cnv1.create_image(xboat,yboat,image=vert[4])
        boat = boat5

def terrainOrdi():
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
                if carte2[i][j] =='X' or carte2[i][j] =='T' :
                    tirvalide = False
                elif carte2[i][j] =='.':
                    cnv2.create_rectangle(j*C,i*C,C+j*C,i*C+C,fill="blue")
                    tirSurOrdi('X',i,j)
                    eau.play()
                    tirvalide = True
                elif carte2[i][j] !='X' and carte2[i][j] !='.':
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
    x,y = randint(0,9),randint(0,9)
    if carte[x][y] == 'X' or carte[x][y] == 'T':
        tir_ordi()
    elif carte[x][y] =='.':
        cnv1.create_rectangle(y*C,x*C,C+y*C,x*C+C,fill="blue")
        tirSurJoueur('X',x,y)
    elif carte[x][y] != ".":
        cnv1.create_rectangle(y*C,x*C,C+y*C,x*C+C,fill="firebrick1")
        tirSurJoueur('T',x,y)

# Le gagnant
global sans
sans=Label()
# Vérifie et renvoi le gagnant
def verif(a,b):
    global sans,etat
    if a==0:
        etat = 0
        sans = Label(height=5, width=30,font ="times 30 italic",text = "Joueur, Vous avez perdu",bg="red3")
        sans.pack(padx =50,pady=50)
        cnv1.pack_forget()
        cnv2.pack_forget()
        gameover.play()
    elif b==0:
        etat = 0
        sans = Label(height=5, width=30,font ="times 30 italic",text = "Joueur, Vous avez gagné",bg="green3")
        sans.pack(padx =50,pady=50)
        cnv1.pack_forget()
        cnv2.pack_forget()


# Modifier ton nom
name = StringVar()
nomdujoueur=Label(root,text="Paramètre", bg = "gray",font="Arial 30 bold",
                  width = 700)
# Permet d'augmenter ou de diminuer le volume
def volume(r):
    r= float(r)
    pygame.quit()
    pygame.mixer.init()
    musique.play(-1)
    musique.set_volume(r/2/100)
    explosion.set_volume(r/100)
    gameover.set_volume(r/100)
    eau.set_volume(r/100)
volum = Scale(root,orient="horizontal", activebackground="black",
              bg="cyan", label = "Volume", length = 700,
              command =volume,from_=0,to=100,width=10,
              font = "Times 20 italic",variable=10)

# Son active ou désactive
# global voice
# voice = "Son"
def parametre():
    bouton.pack_forget()
    bouton2.pack_forget()
    bouton3.pack_forget()
    continuer.pack_forget()
    nomdujoueur.pack(padx=100,pady=30)
    retour.pack(side = "left",padx=50, pady=30)
    volum.pack(padx=100,pady=30)
    global mute, lang
    # Bouton pour le Son
#     mute = Button(root,font="times 20 italic", text=voice,command = couper , width=40,bg="cyan")
#     mute.pack(padx=100, pady=30)
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
    global etat
    if etat == 1:
        continuer.pack(pady=30)
    acceuil()
#     mute.pack_forget()
    retour.pack_forget()
    lang.pack_forget()
    res.pack_forget()
    volum.pack_forget()
    nomdujoueur.pack_forget()
global retour
retour = Button(root,font="Arial 20 bold", text="<Retour ",command =ret, width=10,bg="cyan")

# Permet de couper ou de remettre le son
# def couper():
#     global voice
#     if voice=="Mute":
#         pygame.quit()
#         voice = "Son"
#         mute["text"] = "Son"
#     else:
#         voice = "Mute"
#         mute["text"] = "Mute"
#         pygame.mixer.init()
#         musique.play(-1)

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

# Quitter la fenêtre et pygame
def quitter():
    pygame.quit()
    root.destroy()
    
# Bouton pour fermer
fermer = Button(root, font="Arial 15 bold",text="Fermer",command=quitter,width=10,bg="red")
fermer.pack(side=BOTTOM,pady=10)
# Fonction qui permet de recommencer le jeu
def restart():
    global compteur
    cnv2.pack_forget()
    compteur = 0
    boutbat["text"] = "Bateau suivant"
    sans.pack_forget()
    carte0()
    cnv1.delete(boat1)
    plateau()
    sans.pack_forget()
    
# Bouton pour fermer
restart = Button(root, font="Arial 15 bold",text="Restart",command=restart,width=10,bg="yellow")
# Fonction continuer, permet de reprendre la partie en cours
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
        boutbat.pack(side = "right",padx=30)
        
# Bouton continuer
continuer = Button(root,font ="Times 20 italic", text="Continuer",command = cont, width=40,bg="cyan")
# Menu avec continuer
def men():
    global etat
    sans.pack_forget()
    boutbat.pack_forget()
    menu.pack_forget()
    cnv1.pack_forget()
    cnv2.pack_forget()
    restart.pack_forget()
    if etat ==1:
        continuer.pack(padx=100,pady=30)
    acceuil()
    
# Bouton menu
menu = Button(root, font="Arial 15 bold",text="Menu",command=men,width=10,bg="grey")

old=[None,None]
def clic(event):
    # Enregistre les coordonées du clic
    old[0]= event.x
    old[1]= event.y

# Maintenance du clic gauche, permet de deplacer le bateau
def moved(event):
    global boat, compteur # Le bateau utilisé et le compteur
    global xboat,yboat # Les coordonnées du bateau selictionner
    global long # la longeur du bateau selectionner
    # Selection de la longueur du bateau en fonction du compteur
    if compteur == 0:
        long = 5
    elif compteur == 1:
        long = 4
    elif compteur == 2 or compteur == 3:
        long = 3
    elif compteur == 4:
        long = 2
    # Definission de la zone de deplacement d'un bateau quand elle est en verticale
    if xboat-25<event.x<xboat+25 and yboat-25*long<event.y<yboat+25*long and sens=="verticale" and 25*long<event.y<500-25*long and 25<event.x<700-25:
        # Appelle la fonction dand data.py qui permet de réinitialiser à 0 l'ancienne position du bateau
        enleverBat(str(compteur+1))
        # Deplacement du bateau en question
        cnv1.move(boat,event.x-old[0],event.y-old[1])
        # Initialisation des coodonnées du bateau pour le déplacer
        xboat,old[0]=event.x,event.x
        yboat,old[1]=event.y,event.y
        # Remplace l'image horizontale en verticale
        if sens=="verticale":
            # Permet de supprimer l'image du bateau
            cnv1.delete(boat)
            # Remplace l'image supprimer par une autre image 
            boat = cnv1.create_image(xboat,yboat,image=vert[compteur])
        # Remplace l'image verticale en horizontale
        elif sens=="horizontale":
            # Permet de supprimer l'image du bateau
            cnv1.delete(boat)
            # Remplace l'image supprimer par une autre image
            boat = cnv1.create_image(xboat,yboat,image=hori[compteur])
    
    # Idem qu'en haut mais quand elle est en horizontale
    elif xboat-25*long<event.x<xboat+25*long and yboat-25<event.y<yboat+25 and sens=="horizontale" and 25*long<event.x<525-25*long and 25<event.y<500-25:
        enleverBat(str(compteur+1))
        cnv1.move(boat,event.x-old[0],event.y-old[1])
        xboat,old[0]=event.x,event.x
        yboat,old[1]=event.y,event.y
        if sens=="verticale":
            cnv.delete(boat)
            boat = cnv1.create_image(xboat,yboat,image=vert[compteur])
        elif sens=="horizontale":
            cnv1.delete(boat)
            boat = cnv1.create_image(xboat,yboat,image=hori[compteur])

# Relachement du clique gauche, permet de poser les bateau dans les cases
def poser(event):
    global boat , compteur , long
    # Recherche les coordonnées de la souris en carreau
    for i in range(10):
        for j in range(10):
            if j*C<xboat<j*C+C and i*C<yboat<i*C+C and sens=="verticale" and colision2(i,j,long,"verticale")==False:
                # Supprime le bateau pour pouvoir bien le placer après
                cnv1.delete(boat)
                # Replacement du bateau en fonction de sa taille
                if long%2 != 0:
                    boat = cnv1.create_image(j*C+25,i*C+25,image=vert[compteur])
                else:
                    boat = cnv1.create_image(j*C+25,i*C,image=vert[compteur])
                # Placement des bateaus dans la carte(une liste de liste)
                for k in range(((-long)+1)//2,long-long//2):
                    placementBat(str(compteur+1),k+i,j)
            # Pareil qu'en haut       
            elif j*C<xboat<j*C+C and i*C<yboat<i*C+C and sens=="horizontale" and colision2(i,j,long,"horizontale")==False:
                cnv1.delete(boat)
                if long%2 != 0:
                    boat = cnv1.create_image(j*C+25,i*C+25,image=hori[compteur])
                else:
                    boat = cnv1.create_image(j*C,i*C+25,image=hori[compteur])
                for k in range(((-long)+1)//2 ,long-long//2):
                    placementBat(str(compteur+1),i,k+j)
    
# Creation de la fonction pour le compteur et le bateau suivant
def bateauSuivant():
    global compteur
    global xcnv1
    #Augmenter le compteur d'un quand on appui sur ce bouton
    if estdans(str(compteur+1)):
        compteur = compteur +1
        # Création du bateau suivant
        createboat()
    # Quand on place le dernier bateau changer le text du bouton
    if compteur == 4:
        boutbat["text"]= "Commencer la partie"
    # Quand tous les bateaux sont placer 
    elif compteur == 5:
        # faire apparaître le terrain de l'ordinateur
        cnv1["width"]=Side
        terrainOrdi()
        # oublier le bouton commencer
        boutbat.pack_forget()
# Le bouton pour passer au bateau suiveant
boutbat = Button(root,font="Arial 15 bold", text="Bateau suivant", command=bateauSuivant)