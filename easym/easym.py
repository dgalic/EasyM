#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

"""module docstring"""

# imports
from mrequest import Mrequest as mreqq
from mfiltre import Mfiltre as mfilt
from mlib import Mlib as mlib
from mconstant import *

# constants
URL_LE = 'http://www.lecture-en-ligne.com'
URL_JS = 'http://www.japscan.com'

# Field to constant infroamtion in web site

## LECTURE EN LIGNE
### constant
TITLE_PAGE_LE       = URL_LE
CONTENT_PAGE_LE     = URL_LE + '/manga/'
URL_CUT_LE          = CONTENT_PAGE_LE

### selecteur CSS
#### TITLE
SELECT_TITLE_LE         = 'optgroup option'
FIELD_TITLE_LE          = 'value'
#### CONTENT
SELECT_IMG_LE           = '.imagemanga'
SELECT_RESUME_LE        = '#resume p + p'
SELECT_TABLE_LE         = '.infos tbody tr td'
FILTRE_LE               = '#page'
LOAD_LE                 =  {
        0 : SCND_NAME, 1 : PARUTION , 2 : STATUS   ,
        3 : AUTHOR   , 4 : DRAWER   , 5 : FR_EDIT  ,
        6 : TEAM     , 7 : GENRE    , 8 : READ     ,
        9 : CLASSMENT, 11 : NOTE    }

CONTENT_LOAD_LE         = [
        [TYPE_TABLE, SELECT_TABLE_LE, LOAD_LE],
        [TYPE_ATTRS, SELECT_IMG_LE, "src", IMG_URL],
        [TYPE_TEXT, SELECT_RESUME_LE, RESUME]
        ]

## JAPSCAN
### constant
TITLE_PAGE_JS      = URL_JS + '/mangas/'
CONTENT_PAGE_JS    = URL_JS + '/mangas/'
URL_CUT_JS      = '/mangas'

### selecteur css
#### TITLE
SELECT_TITLE_JS         = '#liste_mangas .row .cell a[href^="/mangas/"]'
FIELD_TITLE_JS          = 'href'

### CONTENT PRIMARY PAGE
SELECT_RESUME_JS        = '#synopsis'
SELECT_TABLE_JS         = '.table .row .cell'
FILTRE_JS               = '.content'
LOAD_JS                 =  {
        0 : AUTHOR, 1 : SCND_NAME , 2 : PARUTION   ,
        3 : GENRE   , 4 : TEAM , 5 : STATUS  }
CONTENT_LOAD_JS         = [
        [TYPE_TABLE, SELECT_TABLE_JS, LOAD_JS],
        [TYPE_TEXT, SELECT_RESUME_JS, RESUME]
        ]

def FLE():
    mf = mfilt(URL_LE)
    mf.initTitle(SELECT_TITLE_LE, FIELD_TITLE_LE, URL_CUT_LE)
    mf.initContent(CONTENT_LOAD_LE, FILTRE_LE)
    mf.initUrl(TITLE_PAGE_LE, CONTENT_PAGE_LE)
    return mf

def FJS():
    mf = mfilt(URL_JS)
    mf.initTitle(SELECT_TITLE_JS, FIELD_TITLE_JS, URL_CUT_JS)
    mf.initContent(CONTENT_LOAD_JS, FILTRE_JS)
    mf.initUrl(TITLE_PAGE_JS, CONTENT_PAGE_JS)
    return mf

def test():
    j = FLE()
    l = FJS()
    tj = j.titles()
    tl = l.titles()
    print "taille : %d" % (len(tj))
    print "taille : %d" % (len(tl))
    print j
    print j.mcontent(tj[5]['id'])
    print l
    print l.mcontent(tl[5]['id'])

def loadfiltre(filtre):
    mtitles = filtre.titles()
    if not mtitles:
        print "Les titres non chargé"

    print "Nombre de Titre : %d" % (len(title))
    badformat = 0
    for i in title:
        if not(MNAME in i and  MID in i and MINFO in i):
            badformat+=1

    print "M mal formé : %d" %(badformat)
    return titres

def loadAllfiltre(filtres):
    FTitres = []

    for f in filtres:
        FTitres.append(loadfiltre(f))

    error = []
    maxOccurRequest = randint(10, 20)
    nbRequest = 0
    t = PAUSE_REQUEST_MIN
    idm = 0
    for m in titlesLE:
        info = testContentM_LE(m[MID])
        if not info:
            error.append(m[MNAME])
        else:
            print m[MNAME] + " : %d" %(idm)

        m[MINFO] = info

        if nbRequest >= maxOccurRequest:
            print "*** Sleep %d" % (t)
            sleep(t)
            nbRequest = 0
            maxOccurRequest = randint(10, 20)
            t = randint(PAUSE_REQUEST_MIN, PAUSE_REQUEST_MAX)
        else:
            nbRequest += 1
        idm+=1
    return (titlesLE, error)

def main():
    mreq = mreq()

    mfle =FLE()
    mfjs =FJS()

if __name__ == '__main__':
    main()

