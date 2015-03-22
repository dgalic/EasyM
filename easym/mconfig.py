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
URL             = 'url'
URL_TITLE       = 'title'
URL_CONTENT     = 'content'
URL_CUT         = 'url_cut'
TITLE_SELECT    = 'title_select'
TITLE_FIELD     = 'title_field'
CONTENT_SELECT  = 'content_allselect'
CONTENT_FILTRE  = 'content_filtre'
ALLFIELD_NECESSITY = [
        URL, URL_TITLE, URL_CONTENT,
        TITLE_SELECT,TITLE_FIELD,
        CONTENT_SELECT]

class Mconfig(object):
    """
        La classe s'occupe d'un fichier CONFIG_FILE , se charge de le
        crée s'il n'existe pas, chaque section du fichier correspond à un site.
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
           f_mconfig = open(CONFIG_FILE, "wb")
           self.mconfig.write(f_mconfig)
           f_mconfig.close()
        except IOError:
            return False
        return True

    def websites(self):
        return self.mconfig.sections()

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
        if self.isMfiltre(name, content):
            self.mconfig.add_section(name)
            for option,value in content.items():
                self.mconfig.set(name, option, value)
            return self.saveConfig()
        return False

    def createFiltre(self, name):
        url  = self.mconfig.get(name, URL)
        filtre = mfiltre(name, URL)
        #Constant url
        url_title = self.mconfig.get(name, URL_TITLE)
        url_content = self.mconfig.get(name, URL_CONTENT)
        filtre.initUrl(url_title, url_content)
        #Constant title
        title_select = self.mconfig.get(name, TITLE_SELECT)
        title_field = self.mconfig.get(name, TITLE_FIELD)
        if self.mconfig.has_option(URL_CUT):
            url_cut = self.mconfig.get(name, URL_CUT)
            filtre.initTitle(title_select, title_field, url_cut)
        else:
            filtre.initTitle(title_select, title_field)
        #Constant content
        content_select = self.mconfig.get(name, CONTENT_SELECT)
        if self.mconfig.has_option(CONTENT_FILTRE):
            content_filtre = self.mconfig.get(name, CONTENT_FILTRE)
            filtre.initContent(content_select, content_filtre)
        else:
            filtre.initContent(content_select)

    def __str__(self):
        website = self.mconfig.sections()
        web_site_str = ""
        for elt in self.website:
            web_site_str += "%s\n       " % (elt)
        ## Information on filtre web site
        info = u"""
 Nombre de site web : %d
 Site web :
        %s
 """ % (len(website), web_site_str)
        return encodeUTF8(info)

