#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

"""
    Le module s'occupe de sauvegarder les données collecter par Easym
    Et le gestion dans la LibrairieEasyM
"""

# imports
from mconstant import *

# constants
EASY_LIBRARY        = 'libEasyM.txt'


def formatName(name):
    """ formate le nom du manga à être un identifiant unique """
    name = unidecode(name).lower().replace(" ","")
    name = re.sub(r'[-+/\',.:?&#]'  , "", name)
    return name

class Mlib(object):

    def __init__(self):
        """ Information d'initalisation ?
            - charge la librairy ou la crée vide
        """
        self.initLib()

    def initLib(self):
        # test if file EASY_LIBRARY exits
        if not self.loadLib():
            open(EASY_LIBRARY, "w").close()

    def loadLib(self):
        try:
            f = open(EASY_LIBRARY, "r")
            sef.lib = eval(f.read())
            f.close()
        except IOError:
            self.lib = {}
            return False
        return True

    def saveLib(self):
        try:
           f = open(EASY_LIBRARY, "w")
           f.write(str(self.lib))
           f.close()
        except IOError:
            return False
        return True

    def addMliste(mliste, site):
        self.duplicate = []
        self.update = []
        for m in mliste:
            keyname = formatName(m[MNAME])
            if keyname in lib:
                if not site in lib[keyname]:
                    print keyname
                    lib[keyname][site] = m
                else:
                    # TODO dans le cas d'update les données
                    self.duplicate.append(m[MNAME])
                    continue
            else:
                print keyname
                lib[keyname][site] = m

    def __str__(self):
        nbM = len(self.lib)
        nbErr = len(self.errors)
        nbDup = len(self.errors)
        nbUpdate = len(self.errors)
        ## Information on Lib
        info = u"""
 Nombre de manga : %d
    Erreurs      : %d
    Duplication  : %d
    Update       : %d
 """ % (nbM, nbErr, nbDup, nbUpdate)
        return encodeUTF8(info)

