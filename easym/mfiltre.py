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

#constant
ERR_TITLE       = 'tilte'
ERR_CONTENT     = 'content'
ERR_POS_FILTRE  = 'filtre'
ERR_POS_TEXT    = 'text'
ERR_POS_ATTRS   = 'attrs'
ERR_POS_TABLE   = 'table'

class Mfiltre(object):

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.errors = []

    def initUrl(self, url_title, url_content):
        self.base_url_title = url_title
        self.base_url_content = url_content

    def initTitle(self, selecteur, field, url_prefix=""):
        self.selecteur = selecteur
        self.field = field
        self.url_prefix = url_prefix

    def initContent(self, fieldload, filtre="*"):
        self.fieldload = eval(fieldload)
        self.filtre = filtre

    def getUrlTitle(self):
        return self.base_url_title

    def getUrlContent(self):
        return self.base_url_content

    def mTitleContent(self, mpage):
        ## catch name and identifier
        name = mpage.text
        url = mpage.attrs[self.field]
        result = re.match(self.url_prefix + "(.*)/", url)
        mid = result.group(1)
        return (name, mid)

    def mTitle(self, content):
        """ retourne une liste d'element (titre, web site id, info -> none) """
        soup = BeautifulSoup(content.text)
        ## keep only inforamtion necessary information with selecteur
        pageFiltre = soup.select(self.selecteur)
        if not pageFiltre:
            self.errors.apprend((ERR_TITLE, ERR_POS_FILTRE))
            return None
        titles = pageFiltre

        lmanga = []
        ## catch Titles information in website
        for m in titles:
            (name, mid) = self.mTitleContent(m)
            lmanga.append({MNAME: name , MID : mid , MINFO : None})

        return lmanga

    def selectElt(self, page, filtre):
        try:
            ret = page.select(filtre)[0]
        except IndexError: # erreurs aucun élement selectionné
            return None
        return ret

    def mTableContent(self, page, select, fields):
        EltFiltre = page.select(select)
        if not EltFiltre:
            self.errors.apprend((ERR_CONTENT, ERR_POS_TABLE))
            return None

        ligne = [i.text for i in EltFiltre]
        length = len(ligne)
        dico = {}
        for field in fields:
            (position, field_librairy, pattern) = field
            value = None
            if position < length:
                if pattern:
                    result = re.search(pattern, ligne[position])
                    value = result.group(1)
                else:
                    value = ligne[position]
                dico[field_librairy] = value

        return dico

    def mEltAttrs(self, page, select, field):
        EltFiltre = self.selectElt(page, select)
        if not EltFiltre:
            self.errors.apprend((ERR_CONTENT, ERR_POS_ATTRS))
            return None
        return EltFiltre.attrs[field]

    def mText(self, page, select):
        pageFiltre = self.selectElt(page, select)
        if not pageFiltre:
            self.errors.apprend((ERR_CONTENT, ERR_POS_TEXT))
            return None
        return pageFiltre.text

    def mContent(self, content):
        """
        Pour le contenu d'un page principale d'un manga
        Le remplie dans un dictionnaire qui correspont
        au champ MINFO de la librairy
        """
        soup = BeautifulSoup(content.text)

        # Filtre possible pour travailler sur un ensemble plus petit
        pageFiltre = self.selectElt(soup,self.filtre)
        if not pageFiltre:
            self.errors.apprend((ERR_CONTENT, ERR_POS_FILTRE))
            return None
        page = pageFiltre

        dico = {}
        for elt in self.fieldload:
            if elt[0] == TYPE_TEXT:
                text = self.mText(page, elt[1])
                dico[elt[2]] = text

            if elt[0] == TYPE_ATTRS:
                (s,f) = elt[1]
                attr = self.mEltAttrs(page, s, f)
                dico[elt[2]] = attr

            if elt[0] == TYPE_TABLE:
                table = self.mTableContent(page, elt[1], elt[2])
                dico.update(table)

        return dico

    def __str__(self):
        fieldload = ""
        for elt in self.fieldload:
            fieldload += "%s\n       " % (elt)

        ## Information on filtre web site
        info = u"""
 Nom : %s
 Url : %s
 Title : %s
    Selecteur : %s
    Field     : %s
 Content : %s
    Filtre    : %s
    Field Load:
        %s
 Error : %d

 """ % (self.name, self.url, self.base_url_title, self.selecteur, self.field,
        self.base_url_content, self.filtre, fieldload, len(self.errors))
        return encodeUTF8(info)

