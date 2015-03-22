#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkMessageBox import *

def alert():
    showinfo("alerte", "Bravo!")

class EasyMGUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
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
        Canvas(FrameVote, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, pady=5)

        # Boutons pour les avis sur les mangas
        boui = Button(FrameVote, text = 'Oui',bg='green',activebackground='lawn green')
        boui.pack(side=LEFT, padx=5,pady=5)
        bnon = Button(FrameVote, text = 'Non', bg='red',activebackground='orange red')
        bnon.pack(side=RIGHT, padx=5, pady=5)
        Button(FrameVote, text = '>>> Suivant >>>').pack(side=BOTTOM, padx=5, pady=5)
        FrameVote.pack()
        return FrameVote

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

