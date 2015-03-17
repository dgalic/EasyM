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
import re
from bs4 import BeautifulSoup
from mconstant import *
from mrequest import Mrequest as mreq

def encodeUTF8(elt):
    return elt.encode("utf-8")

class Mfiltre(object):

    def __init__(self, url):
        """ Information d'initalisation ?
        """
        self.url = url
        self.mreq = mreq()

    def initUrl(self, url_title, url_content):
        self.base_url_title = url_title
        self.base_url_content = url_content

    def initTitle(self, selecteur, field, url_prefix=""):
        self.selecteur = selecteur
        self.field = field
        self.url_prefix = url_prefix

    def initContent(self, fieldload, filtre="*"):
        self.fieldload = fieldload
        self.filtre = filtre

    def getTitleContent(self, mpage):
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
            lmanga.append({MNAME: name , MID : mid , MINFO : None})

        return lmanga

    def getTableContent(self, page, select, field):
        info = page.select(select)

        ligne = [i.text for i in info]
        dico = { v:ligne[k] for k,v in field.items()}
        return dico

    def selectElt(self, filtre):
        try:
            ret = page.select(filtre)[0]
        except IndexError: # erreurs aucun élement selectionné
            return None
        return ret


    def getEltAttrs(self, page, select, field):
        EltFiltre = self.select(select)
        if not pageFiltre:
            return None
        return EltFiltre.attrs[field]


    def getText(self, page, select):
        pageFiltre = self.select(select)
        if not pageFiltre:
            return None
        return pageFiltre.text

    def getMContent(self, content):
        """
        Pour le contenu d'un page principale d'un manga
        Le remplie dans un dictionnaire qui correspont
        au champ MINFO de la librairy
        """
        soup = BeautifulSoup(content.text)

        # Filtre possible pour travailler sur un ensemble plus petit
        pageFiltre = self.select(select)
        if not pageFiltre:
            return None
        page = pageFiltre

        dico = {}
        for elt in self.fieldload:
            if elt[0] == TYPE_TEXT:
                text = self.getText(page, elt[1])
                dico[elt[2]] = text

            if elt[0] == TYPE_ATTRS:
                (s,f) = elt[1]
                attr = self.getEltAttrs(page, s, f)
                dico[elt[2]] = attr

            if elt[0] == TYPE_TABLE:
                table = self.getTableContent(page, elt[1], elt[2])
                dico.update(table)

        return dico

    def titles(self):
        page = self.mreq.getRequest(self.base_url_title)
        if not page:
            return None

        return self.getMTitle(page)

    def mcontent(self, mid):
        url = self.base_url_content + mid +'/'
        page = self.mreq.getRequest(url)
        if not page:
            return None

        return self.getMContent(page)

    def __str__(self):
        ## Information on filtre web site
        info = u"""
 Url : %s
 Title : %s
    selecteur : %s
    field     : %s
 Content      : %s
    filtre    : %s
    Field Load:
       %s
 """ % (self.url, self.base_url_title, self.selecteur, self.field,
         self.base_url_content, self.filtre, self.fieldload )
        return encodeUTF8(info)

