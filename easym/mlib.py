#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

"""
    Le module s'occupe de sauvegarder les données collecter par EasyM
    Et la gestion de ces données LibrairieEasyM
"""

# imports
from mconstant import *
from os import path

# constants
EASY_LIBRARY        = 'libEasyM.txt'


def formatName(name):
    """ formate le nom du manga à être un identifiant unique """
    name = unidecode(name).lower().replace(" ","")
    name = re.sub(r'[-+/\',.:?&#]'  , "", name)
    return name

class Mlib(object):

    def __init__(self):
        self.Mlib = {}
        self.initLib()

    def initLib(self):
        # test if file EASY_LIBRARY exits
        if path.exists(EASY_LIBRARY):
            self.loadLib()
        else:
            print "file not exist"
            open(EASY_LIBRARY, "w").close()
            self.saveLib()

    def loadLib(self):
        try:
            f = open(EASY_LIBRARY, "r")
            self.Mlib = eval(f.read())
            f.close()
        except IOError:
            return False
        return True

    def saveLib(self):
        try:
           f = open(EASY_LIBRARY, "w")
           f.write(str(self.Mlib))
           f.close()
        except IOError:
            return False
        return True

    def getIdMangas(self):
        return self.lib.keys()

    def getIdMToUpdate(self):
        """ we look for all manga id if we miss:
            - information in value MINFO
            - field in MINFO : to return change code in website
        """
        update = []
        for mid, info in self.Mlib():
            for website in info.keys():
                if not info[website][INFO]:
                    update.append((mid,website))
                else:
                    for field in info[website][INFO].keys():
                        if not info[website][INFO][field]:
                            update.append((mid,website,field))

        return update

    def addMliste(mliste, site):
        self.duplicate = []
        self.update = []
        for m in mliste:
            keyname = formatName(m[MNAME])
            if keyname in self.Mlib:
                if not site in self.Mlib[keyname]:
                    print keyname
                    self.Mlib[keyname][site] = m
                else:
                    # TODO dans le cas d'update les données
                    self.duplicate.append(m[MNAME])
                    continue
            else:
                print keyname
                lib[keyname][site] = m

    def __str__(self):
        nbM = len(self.lib)
        ## Information on Lib
        info = u"""
 Nombre de manga : %d
    Erreurs      : %d
    Duplication  : %d
    Update       : %d
 """ % (nbM, nbErr, nbDup, nbUpdate)
        return encodeUTF8(info)

