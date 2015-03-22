#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

"""module docstring"""

# imports
from mrequest import Mrequest
from mfiltre import Mfiltre
from mlib import Mlib
from mconfig import *
from mconstant import *

# constants
ERRTITLE    = 'title'
ERRCONTENT  = 'content'

# Field to constant information in web site
## LECTURE EN LIGNE
URL_LE = 'http://www.lecture-en-ligne.com'
#### CONTENT
LOAD_LE                 =  {
        0 : SCND_NAME, 1 : PARUTION , 2 : STATUS   ,
        3 : AUTHOR   , 4 : DRAWER   , 5 : FR_EDIT  ,
        6 : TEAM     , 7 : GENRE    , 8 : READ     ,
        9 : CLASSMENT, 11 : NOTE    }

CONTENT_LOAD_LE         = [
        [TYPE_TABLE , '.infos tbody tr td'  , LOAD_LE],
        [TYPE_ATTRS , ('.imagemanga','src') , IMG_URL],
        [TYPE_TEXT  , '#resume p + p'       , RESUME]
        ]

DICO_LE ={
        URL             : URL_LE,
        URL_TITLE       : URL_LE,
        URL_CONTENT     : URL_LE + '/manga/',
        URL_CUT         : URL_LE + '/manga/',
        TITLE_SELECT    : 'optgroup option',
        TITLE_FIELD     : 'value',
        CONTENT_SELECT  : CONTENT_LOAD_LE,
        CONTENT_FILTRE  : '#page',
        }

## JAPSCAN
URL_JS = 'http://www.japscan.com'
#### CONTENT
LOAD_JS                 =  {
        0 : AUTHOR, 1 : SCND_NAME , 2 : PARUTION   ,
        3 : GENRE   , 4 : TEAM , 5 : STATUS  }
CONTENT_LOAD_JS         = [
        [TYPE_TABLE , '#synopsis'           , LOAD_JS],
        [TYPE_TEXT  , '.table .row .cell'   , RESUME ]]

DICO_JS ={
        URL             : URL_JS,
        URL_TITLE       : URL_JS + '/mangas/',
        URL_CONTENT     : URL_JS + '/mangas/',
        URL_CUT         : '/manga/',
        TITLE_SELECT    : '#liste_mangas .row .cell a[href^="/mangas/"]',
        TITLE_FIELD     : 'href',
        CONTENT_SELECT  : CONTENT_LOAD_JS,
        CONTENT_FILTRE  : '.content',
        }

class EasyM(object):

    def __init__(self):
        self.Ereq = Mrequest()
        self.Econf = Mconfig()
        self.Efilt = {}
        self.Elib = Mlib()
        self.ErrReq = []
        self.ErrFiltre = []
        pass

    def initFiltre(self):
        filtre = self.Econf.websites()
        if filtre:
            for elt in filtres:
                self.Efilt[name] = self.Econf.createFiltre(elt)

    def titles(self, name):
        url = self.Efilt[name].getUrlTitle()
        page = self.Ereq.getRequest(url)
        if not page:
            self.ErrReq.append((name,url,ERRTITLE))
            return None

        mtitles = self.Efilt[name].mTitle(page)
        if not mtitles:
            self.ErrFiltre.append((name,url,ERRTITLE))

        return mtitles

    def mcontent(self, name, mid):
        url = self.Efilt[name].getUrlContent() + mid + '/'
        page = self.mreq.getRequest(url)
        if not page:
            self.ErrReq.append((name,url,ERRCONTENT))
            return None

        mcontent = self.Efilt[name].mContent(page)
        if not mcontent:
            self.ErrFiltre.append((name,url,mid))

        return mcontent

    def __str__(self):
        print self.elibrairy


def createFileConfig():
    Econf = Mconfig()
    print Econf.addSection("Lecture en ligne", DICO_LE)
    print Econf.addSection("Japscan", DICO_JS)

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


#if __name__ == '__main__':
