#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
"""
    Le module MConfig permet de gérer le fichier de configuration
    incluant les sélectuer css pour chaque site internet possédant
    les informations nécéssaire aux projet.
"""

# imports
from ConfigParser import ConfigParser
from mfiltre import Mfiltre as mfiltre
from mconstant import *

# constants
CONFIG_FILE     = 'mconfig.cfg'
URL_TITLE       = 'title'
URL_CONTENT     = 'content'
URL_CUT         = 'url_cut'
TITLE_SELECT    = 'title_select'
TITLE_FIELD     = 'title_field'
CONTENT_SELECT  = 'content_allselect'
CONTENT_FILTRE  = 'content_filtre'
ALLFIELD_NECESSITY = [
        URL_TITLE, URL_CONTENT, URL_CUT,
        TITLE_SELECT,TITLE_FIELD,
        CONTENT_SELECT, CONTENT_FILTRE]

class Mconfig(object):
    """
        La classe s'occupe d'un fichier CONFIG_FILE , se charge de le
        crée s'il n'existe pas, chaque section du fichier correspond à un site.
        Ce module effectue l'étape :
            - lire le fichier CONFIG_FILE avec module ConfigParser
            - traduire en un dictionnaire  clé section value :dico
                (clé : POSITION ;value: SELECTEUR)
            CONFIG_FILE -> DICO Sélecteur
        Si vide renvoie NONE
    """

    def __init__(self):
        """ On vérifie si le fichier CONFIG_FILE , on le crée sinon"""
        self.mconfig = ConfigParser()
        self.loadConfig()

    # Load file name CONFIG_FILE in yours mconfig
    def loadConfig(self):
        return self.mconfig.read(CONFIG_FILE)


    # Save your mconfig in file name CONFIG_FILE
    def saveConfig(self):
        try:
           f_mconfig = open(EASY_CONFIG, "wb")
           self.mconfig.write(f_mconfig)
           f.close(f_mconfig)
        except IOError:
            return False
        return True

    def isMfiltre(self, name, content):
        if name in self.mconfig.sections():
            print 'name is allready exist'
            return False

        # check if field as necessity to filtre as present
        field_view = []
        for elt in content.keys():
            if elt in ALLFIELD_NECESSITY:
                field_view.append(elt)

        lfv = len(field_view)
        laf = len(ALLFIELD_NECESSITY)
        if lfv != laf:
            print '%d /%d : all necessity fied not present' % (lfv, laf)
            return False

        # check list to CONTENT_SELECT have a good format 
        for elt in content[CONTENT_SELECT]:
            # elt is empty
            if not elt:
                print 'CONTENT_FIELD is empty'
                return False
            # check type
            typ = elt[0]
            if not typ in [TYPE_ATTRS, TYPE_TEXT, TYPE_TABLE]:
                print 'Type %s not exist' % (typ)
                return False

            # check length
            length = len(elt)
            field_test = []
            if length == 3:
                field = elt[2]
                if typ == TYPE_TABLE:
                    for k,v in field.items():
                        if not v in ALLFIELD_MINFO:
                            print 'Field %s not exist to MINFO' % (v)
                            return False
                else:
                    if not field in ALLFIELD_MINFO:
                        print  'field %s not exist to MINFO' % (field)
                        return False
            else:
                print 'Length to elt not equal 3'
                return False

        return True

    # add a new web site ; name = URL content=dico(option,field)
    def addSection(self, name, content):
        if self.testNewSection(name, content):
            pass
        else:
            pass

    def createFiltre(self, name):
        filtre = mfiltre(name)
        #Constant url
        url_title = self.mconfig.get(name, )
        #Constant title
        #Constant content
        pass

# if __name__ == '__main__':
