# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 18:53:33 2019

@author: xabif
"""

# -*- coding: utf-8 -*-
"""
Ce code a été réalisé par Xabi FAUT et Camille CHERBLANC, le 21 décembre.
Ce code permet de jouer à Space Invaders.
"""
#http://tkinter.fdex.eu/doc/event.html#nomtouchesevt    NOM DES TOUCHES

import Tkinter as tk
from random import randint
from tkMessageBox import askyesno, showinfo
import sys

LAlien=[[],[],[]]#plus propre
LARGEUR = 480
HAUTEUR = 320
starting = True

# position initiale des aliens
r=10
X = r
vitesse = 10

Linterdite = []
#état initial
isAlien = True
isRunning = False
ismissile = False
ismisalien = False

def space_invaders():
    # Alien catégorie 1
    def AlienCat1():
        global LAlien,r,X
        YY=r
        A1=can.create_rectangle(X,YY,X+20,YY+20,fill='pink')
        LAlien[0].append(A1)#ne réactualise pas les positions
        X+=60
    
    # Alien catégorie 2
    def AlienCat2():
        global Alien2,X,LAlien,r
        X-=60
        YY=r
        A2=can.create_rectangle(X,YY+40,X+20,YY+60,fill='violet') #récupérer les coordonnées pour les ajouter
        LAlien[1].append(A2)
        X+=60
    
    # Alien catégorie 3
    def AlienCat3():
        global AlienCat3,X,LAlien,r
        X-=60
        YY=r
        A3=can.create_rectangle(X,YY+80,X+20,YY+100,fill='brown')
        LAlien[2].append(A3)
        X+=60
    
    def DeplacementVaisseau(touche):
        global LARGEUR
        if touche =="Left" and can.coords(vaisseau)[0] >= 10:
            can.move(vaisseau,-10,0)
        if touche =="Right" and can.coords(vaisseau)[2] <= LARGEUR-10:
            can.move(vaisseau,10,0)
        
    
    def Clavier(event):
        global missile, ismissile, LARGEUR
        touche = event.keysym
        if touche == "space" and ismissile == False:
            xM = can.coords(vaisseau)[0]+10
            yM = can.coords(vaisseau)[1]-13
            print("missile created")
            ismissile = True
            missile = can.create_rectangle(xM-1,yM-8,xM+1,yM+12,outline ='black',fill ='blue')
            DeplacementMissile()
        DeplacementVaisseau(touche)
    
    def DeplacementMissile():
        global missile, ismissile, isAlien, isRunning
        if can.coords(missile)[1] <= 0 :
            print("missile deleted")
            can.delete(missile)
            missile = None
            ismissile = False
            return
        a = can.coords(missile)[0]
        b = can.coords(missile)[1]
        c = can.coords(missile)[2]
        d = can.coords(missile)[3]
        TM = can.find_overlapping(a,b,c,d)
        #TM = (id_du_missile) c'est un tupple
        if len(TM) > 1: #Si quelque chose rentre dans la zone
            print ('touché')
            for i in TM :
                if i in LAlien[2]:
                    varscore.set(varscore.get() + 10)
                    isAlien = False
                    for j in range(len(LAlien[2])):
                        if LAlien[2][j] == i :
                            Linterdite.append([2,j])
                    can.delete(i) 
              #      LAlien[2].remove(i)
                if i in LAlien[1]:
                    varscore.set(varscore.get() + 50)
                    isAlien = False
                    for j in range(len(LAlien[1])):
                        if LAlien[1][j] == i :
                            Linterdite.append([1,j])
                    can.delete(i)
              #      LAlien[1].remove(i)
                if i in LAlien[0]:
                    varscore.set(varscore.get() + 100)
                    isAlien = False
                    for j in range(len(LAlien[0])):
                        if LAlien[0][j] == i :
                            Linterdite.append([0,j])
                    can.delete(i) 
              #      LAlien[0].remove(i)
                if len (Linterdite) == 18 :
                    isRunning = False
                    boutonDebut.config(state="normal")
                    boutonStop.config(state="disabled")
                    showinfo('GAGNE','Vous avez gagné!!!')
                    rejouer()
                else :
                    can.delete(i)
            print("missile deleted")
            missile = None
            ismissile = False
            return
        can.move(missile,0,-10)    
        mf.after(25,DeplacementMissile)  
    
    def Random():
        global Linterdite, isRunning       
        rdm1 = randint(0, 2)
        rdm2 = randint(0, 5)#à adapter en fonction du nombre d'aliens
        print (Linterdite,(rdm1,rdm2))
        if [rdm1,rdm2] in Linterdite:
            [rdm1,rdm2] = Random()
        return (rdm1,rdm2)
    
    def misalien():
        global LAlien, ismisalien, misaliene
        if ismisalien == False:
            [rdm1,rdm2] = Random()
            xM = can.coords(LAlien[rdm1][rdm2])[0]+10
            yM = can.coords(LAlien[rdm1][rdm2])[1]+20
            ismisalien = True    
            misaliene = can.create_rectangle(xM-1,yM-10,xM+1,yM+10,outline ='black',fill ='red')
            DeplacementMisaliene()
        mf.after(1000,misalien)
    
    def DeplacementMisaliene():
        global HAUTEUR, vaisseau, ismisalien, misaliene, Bloc, isRunning
        if can.coords(misaliene)[1] >= HAUTEUR :
            can.delete(misaliene)
            misaliene = None
            ismisalien = False
            return
        a = can.coords(misaliene)[0]
        b = can.coords(misaliene)[1]
        c = can.coords(misaliene)[2]
        d = can.coords(misaliene)[3]
        TMa = can.find_overlapping(a,b,c,d)
        #TM = (id_du_misaliene) c'est un tupple
        if len(TMa) > 1: #Si quelque chose rentre dans la zone
            for i in TMa :
                if i == vaisseau :
                    varvie.set(varvie.get() - 1)
                    for j in range (1,len(TMa)): 
                        can.delete(TMa[j])
                    misaliene = None
                    ismisalien = False
                    if varvie.get() < 1:
                         isRunning = False
                         boutonDebut.config(state="normal")
                         boutonStop.config(state="disabled")
                         showinfo('GAME OVER','Vous avez perdu...')
                         rejouer()       
                    return
                if i in Bloc :
                    for j in TMa :
                        can.delete(j)
                    misaliene = None
                    ismisalien = False
                    return
        can.move(misaliene,0,+10)    
        if isRunning :    
            tps = Temps()
            mf.after(tps,DeplacementMisaliene)
    
    def Temps():
        global Linterdite
        return(190 - len(Linterdite) * 10)
    
    def BlocAbris():
        global Bloc
        #position initiale des blocs
        xB=50
        yB=215
        Bloc=[]
        L = 10
        i=0    
        #On veut 4 blocs abris
        while i < 4:
            limX=xB+60
            limY=yB+30
            departx=xB
            while yB<limY:
                while xB<limX:
                    #Ajoute à la liste des blocs de largeur L
                    Bloc.append(can.create_rectangle(xB,yB,xB+L,yB+L,outline ='gray',fill='green'))
                    #Il y aura un bloc L cases plus loin (ils seront donc collés)            
                    xB+=L
                xB=departx
                yB+=L
            i+=1
            xB+=100
            yB-=30
            
    def extremum():
        minus = sys.maxint
        maxus = -sys.maxint - 1
        maxusY = -sys.maxint - 1
        
        for aliens in LAlien:
            for alien in aliens:
                x, y, x2, y2 = can.coords(alien)
                if x2 > maxus:
                    maxus=x2
                if x < minus:
                    minus=x
                if y2 > maxusY:
                    maxusY=y2
        return minus,maxus,maxusY
    
    def DeplacementAlien(XXmin,XXmax,Y): 
        global isRunning, LARGEUR,vitesse, r
        # rebond à droite
        vitesseY = 0
        if XXmax > LARGEUR - 5 or XXmin < 0 + 5:
            vitesse = -vitesse
            vitesseY=10
        #Demande de rejouer quand l'alien est en bas
        if Y > 200 :
            """
            désactivé pour reste isRunning
            """
            isRunning = False
            boutonDebut.config(state="normal")
            boutonStop.config(state="disabled")
            showinfo('GAME OVER','Vous avez perdu...')
            rejouer()       
        #vérification de l'état initial
        #vitessex = vitesse
        return vitesse,vitesseY
            
    def DeplacementAliens():
        global LAlien
        [minus,maxus,maxusY]=extremum()
        vitessex,vitessey=DeplacementAlien(minus,maxus,maxusY)
        for ligne in LAlien:       
            for alien in ligne:
                can.move(alien, vitessex, vitessey)
        if isRunning:   
            mf.after(300,DeplacementAliens) 
            
    def rejouer():
        global Bloc,LAlien,LARGEUR,HAUTEUR,starting,r,X,vitesse,Linterdite,isAlien,isRunning,ismissile,ismisalien
        isRunning = False
        if askyesno('Rejouer ?','Voulez-vous rejouer?') :
            mf.destroy()
            LAlien=[[],[],[]]
            LARGEUR = 480
            HAUTEUR = 320
            starting = True
            r=10
            X = r
            vitesse = 10
            Linterdite = []
            #état initial
            isAlien = True
            isRunning = False
            ismissile = False
            ismisalien = False
            space_invaders()
        else :
            mf.destroy()
            
    def recommencer():
        global Bloc,LAlien,LARGEUR,HAUTEUR,starting,r,X,vitesse,Linterdite,isAlien,isRunning,ismissile,ismisalien
        isRunning = False
        boutonDebut.config(state="normal")
        boutonStop.config(state="disabled")
        if askyesno('Recommencer ?','Voulez-vous recommencer?') :
            mf.destroy()
            LAlien=[[],[],[]]
            LARGEUR = 480
            HAUTEUR = 320
            starting = True
            r=10
            X = r
            vitesse = 10
            Linterdite = []
            #état initial
            isAlien = True
            isRunning = False
            ismissile = False
            ismisalien = False
            space_invaders()
        else :
            mf.set('')
        
    def Commencer():
        global isRunning
        # vérification de l'état initial
        isRunning = True 
        boutonDebut.config(state="disabled")
        boutonStop.config(state="normal")
        boutonRejouer.config(state="normal")
        DeplacementAliens()
        misalien()
        if starting:
            can.grid(row = 1, column =3, rowspan = 5)
            can2.destroy()
    
    def Pause():
        global isRunning
        # vérification de l'état initial
        isRunning = False
        boutonDebut.config(state="normal")
        boutonStop.config(state="disabled")
    
    def Quit():
        global isRunning
        isRunning = False
        boutonDebut.config(state="normal")
        boutonStop.config(state="disabled")
        if askyesno('Quitter ?','Voulez-vous vraiment quitter ?') :
            mf.destroy()
        mf.set('')
    
    #Création de la fenetre
    mf = tk.Tk()
    mf.title('Space Invader')
    mf.geometry('700x350')
    
    varscore = tk.IntVar()
    varscore.set(0)
    
    varvie = tk.IntVar()
    varvie.set(3)
    
    #Création de widget Label, Button
    labelTextScore=tk.Label(mf, text='Score :')
    labelScore=tk.Label(mf, textvariable=varscore)
    labelTextVie=tk.Label(mf, text='Nombre de vies restantes :')
    labelVie=tk.Label(mf, textvariable=varvie)
    boutonDebut=tk.Button(mf, text="Commencer", command = Commencer)
    boutonStop =tk.Button(mf, text="Pause", command = Pause)
    boutonQuit=tk.Button(mf, text="Quitter", command = Quit)
    boutonRejouer=tk.Button(mf, text="Recommencer", command = recommencer)
    
    #Création d'un widget 'Canvas' contenant une image :
    can=tk.Canvas(mf, height=HAUTEUR,width=LARGEUR, bg='white')
    can2=tk.Canvas(mf,height=HAUTEUR,width=LARGEUR, bg='black')
    can2.grid(row = 1, column =3, rowspan = 5)
    can2.create_text(240,160,font=('Fixedsys',24),text="SPACE INVADERS by C & X",fill='blue')
    vaisseau = can.create_rectangle(15-10,280-10,15+10,280+10,outline ='blue',fill ='blue')
    
    BlocAbris()
    
    can.focus_set();
    
    #Il faut créer une fonction qui regroupe tous les evenements clavier car on ne peux avoir qu'un seul BIND
    can.bind('<Key>',Clavier)
    
    #Mise en page à l'aide de la méthode 'grid'
    labelScore.grid(row=1, column =2)
    labelTextScore.grid(row=1,column =1 )
    labelVie.grid(row=2, column =2)
    labelTextVie.grid(row=2,column =1 )
    boutonDebut.grid(row=3,column =1 )
    boutonStop.grid(row=4,column =1 )
    boutonRejouer.grid(row=5,column =1)
    boutonQuit.grid(row=6,column =1 )
    can.grid(row = 1, column=3, rowspan = 6)
    
    #Initialisation du bouton pause
    boutonStop.config(state="disabled")
    boutonRejouer.config(state="disabled")
    
    #Initialisation du fond d'écran
    #fond= tk.PhotoImage(file='fond.gif')
    #can.create_image(0,100,image=fond)
    
    #Test
    
    
    # On veut 6 ennemis par catégorie
    def creeralien() :
        i=0
        while i<6:
            AlienCat1()
            AlienCat2()
            AlienCat3()
            i+=1
    
    creeralien()
    mf.mainloop()

space_invaders()

