#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
#from tkMessageBox import *
from easym import EasyM
from mconstant import *
from random import randint

def alert():
    showinfo("alerte", "Bravo!")

class EasyMGUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.easym = EasyM()
        self.initGUI()

    def initGUI(self):
        self.initMenuBar()
        self.frame = self.initFrameVote()

    def initMenuBar(self):
        self.menubar = Menu(self)

        menu1 = Menu(self.menubar, tearoff=0)
        menu1.add_command(label="Voter", command=self.eventVoter)
        menu1.add_command(label="Recommendation", command=alert)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self.parent.quit)
        self.menubar.add_cascade(label="EasyM", menu=menu1)

        menu2 = Menu(self.menubar, tearoff=0)
        menu2.add_command(label="Liste manga", command=self.eventListeManga)
        menu2.add_command(label="Ajouter un site", command=alert)
        self.menubar.add_cascade(label="Manga", menu=menu2)

        menu3 = Menu(self.menubar, tearoff=0)
        menu3.add_command(label="A propos", command=alert)
        self.menubar.add_cascade(label="Aide", menu=menu3)

        self.parent.config(menu=self.menubar)

    def eventListeManga(self):
        self.frame.destroy()
        self.frame = self.initFrameAddListM()

    def eventVoter(self):
        self.frame.destroy()
        self.frame = self.initFrameVote()

    def initFrameVote(self):
        FrameVote = Frame(self.parent, borderwidth=2)

        # Affichage d'un manga
        self.initFrameInfo(FrameVote)

        Framebutton = Frame(FrameVote, borderwidth=2)
        # Boutons pour les avis sur les mangas
        boui = Button(Framebutton, text = 'Oui',bg='green',
                activebackground='lawn green',command=self.eventVoter)
        boui.pack(side=LEFT, padx=5,pady=5)
        bnon = Button(Framebutton, text = 'Non', bg='red',
                activebackground='orange red',command=self.eventVoter)
        bnon.pack(side=RIGHT, padx=5, pady=5)
        suivant = Button(Framebutton, text = '>>> Suivant >>>',
                command=self.eventVoter)
        suivant.pack(side=BOTTOM, padx=5, pady=5)
        Framebutton.pack()
        FrameVote.pack()
        return FrameVote

    def addLabel(self, parent, minfo, field):
        if field in minfo and minfo[field] != None:
            Ltext = u"%s %s" %(TITRE_FIELD[field],minfo[field])
            w = Label(parent, text=Ltext,justify=LEFT)
            w.pack()

    def initFrameInfo(self,parent):
        # Affichage d'un manga
        self.FrameInfo = Frame(parent, relief=RAISED,width=300,borderwidth=2)

        liste = Listbox(self.FrameInfo)
        randvalue = randint(0, len(self.easym.othervoter))
        idm = self.easym.othervoter[randvalue]
        manga = self.easym.Elib.Mlib[idm]
        for site in manga:
            minfo = manga[site][MINFO]
            liste.insert(1, "Website :"+site)
            liste.insert(2,self.addLabel(parent, minfo, STATUS))
            liste.insert(3,self.addLabel(parent, minfo, TYPE_M))
            liste.insert(4,self.addLabel(parent, minfo, SCND_NAME))
            liste.insert(5,self.addLabel(parent, minfo, AUTHOR))
            liste.insert(6,self.addLabel(parent, minfo, DRAWER))
            liste.insert(7,self.addLabel(parent, minfo, FR_EDIT))
            liste.insert(8,self.addLabel(parent, minfo, PARUTION))
            liste.insert(9,self.addLabel(parent, minfo, TEAM))
            liste.insert(10,self.addLabel(parent, minfo, READ))
            liste.insert(11,self.addLabel(parent, minfo, NOTE))
            liste.insert(12,self.addLabel(parent, minfo, TAG))
            #liste.insert(13,self.addLabel(parent, minfo, RESUME))
        self.FrameInfo.pack(fill=BOTH,side=TOP )

    def initFrameAddListM(self):
        FrameListeM = Frame(self.parent, borderwidth=2)

        liste = Listbox(FrameListeM)
        liste.insert(1, "Python")
        liste.insert(2, "PHP")
        liste.insert(3, "jQuery")
        liste.insert(4, "CSS")
        liste.insert(5, "Javascript")

        liste.pack()
        FrameListeM.pack()
        return FrameListeM

def main():
    root = Tk()
    root['bg']='white'
    app = EasyMGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()

