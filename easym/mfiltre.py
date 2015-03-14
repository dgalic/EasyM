#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
"""
    Le module correspond à un filtre pour chaque site web
    - Pour chercher les Titres
        des mangas et leurs lien vers les informations les concernant
    - Pour chercher leurs Contenus
        des mangas selon une structure précise
"""
# imports
from bs4 import BeautifulSoup
from mconstant import *

class Mfiltre(object):

    def __init__(self, url, url_title, url_content):
        """ Information d'initalisation ?
        """
        self.url = url
        self.base_url_title = url_title
        self.base_url_content = url_content

    def initTitle(self, selecteur, field, url_prefix=""):
        self.selecteur = selecteur
        self.field = field
        self.url_prefix = url_prefix

    def initContent(self, fieldload, filtre="*"):
        self.fieldload = fieldload
        self.filtre = filtre

    def getTitleContent(mpage):
            ## catch name and identifier
            name = mpage.text
            url = mpage.attrs[self.field]
            result = re.match(self.url_prefix + "(.*)/", url)
            mid = result.group(1)
            return (name, mid)

    def getMTitle(self, content):
        """ retourne une liste d'element (titre, web site id, info -> vide) """
        soup = BeautifulSoup(content.text)

        ## keep only inforamtion necessary information with selecteur
        titles = soup.select(self.selecteur)

        lmanga = []
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

    def getMContent(content):
        """
        Pour le contenu d'un page principale d'un manga
        Le remplie dans un dictionnaire qui correspont
        au champ INFO de la librairy
        """
        soup = BeautifulSoup(content.text)

        # Filtre possible pour travailler sur un ensemble plus petit
        page = soup.select(self.filtre)[0]

        dico = {}
        for elt in self.fieldload:
            if elt[0] == TYPE_TEXT:
                text = self.getText(page, elt[1])
                dico[elt[2]] = text

            if elt[0] == TYPE_ATTRS:
                attr = self.getEltAttrs(page, elt[1], elt[2])
                dico[elt[3]] = attr

            if elt[0] == TYPE_TABLE:
                table = self.getTableContent(page, elt[1], elt[2])
                dico.update(table)

        return dico
