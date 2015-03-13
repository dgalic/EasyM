
#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
"""
    Le module MFiltre s'occupe de filtrée les données pour 2 cas dans EasyM
    - Pour chercher les Titre
        des mangas et leurs lien vers les informations concernant
    - Pour chercher le Contenu
        des mangas selon une structure précise
"""
# imports
import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from unidecode import unidecode

# constants
MNAME   = 'name'
MID     = 'id'
INFO    = 'information'

TYPE_TEXT           = 'text'
TYPE_TABLE          = 'table'
TYPE_ATTRS          = 'attrs'
# exception classes
# interface functions
# classes
# internal functions & classes
def encodeUTF8(elt):
    return elt.encode("utf-8")

class MFiltre(object):

    def __init__(self):
        """ Information d'initalisation ?
        """
        pass

    def getTitleContent(mpage):
            ## catch name and identifier
            name = m.text
            url = m.attrs[self.field]
            result = re.match(url_cut + "(.*)/", url)
            mid = result.group(1)
            return (name, mid)

    def getTitle(self, content, selecteur, field, url_cut):
        soup = BeautifulSoup(content.text)

        ## keep only inforamtion necessary information with selecteur
        titles = soup.select(selecteur)

        lmanga = []
        self.field = field
        ## catch Titles information in website
        for m in titles:
            (name, mid) = self.getTitleContent(m)
            lmanga.append({MNAME: name , MID : id_manga , INFO : None})

        return lmanga

    def getTableContent(page, select, field):
        info = page.select(select)

        ligne = [i.text for i in info]
        dico = { v:ligne[k] for k,v in field.items()}
        return dico

    def getEltAttrs(page, select, field):
        return page.select(select)[0].attrs[field]

    def getText(page, select):
        return page.select(select)[0].text

    def getContentM(content, field_load, filtre="*"):
        soup = BeautifulSoup(content.text)

        # Filtre possible pour travailler sur un ensemble plus petit
        page = soup.select(filtre)[0]

        dico = {}
        for elt in field_load:
            if elt[0] == TYPE_TEXT:
                text = getText(page, elt[1])
                dico[elt[2]] = text

            if elt[0] == TYPE_ATTRS:
                attr = getEltAttrs(page, elt[1], elt[2])
                dico[elt[3]] = attr

            if elt[0] == TYPE_TABLE:
                table = getTableContent(page, elt[1], elt[2])
                dico.update(table)

        return dico
