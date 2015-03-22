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
LOAD_LE                 =  [
        (0,SCND_NAME,None), (1,PARUTION,None) , (2,STATUS,None),
        (3,AUTHOR,None), (4,DRAWER,None), (5,FR_EDIT,None),
        (6,TEAM,None), (7,TAG,"(.*)\(") , (7,TYPE_M,"\((.*)\)"),
        (8,READ,None), (9,CLASSMENT,None), (11,NOTE,None)
                            ]
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
LOAD_JS                 =  [
        (0,AUTHOR,None), (1,SCND_NAME,None) , (2,PARUTION,None),
        (3,TYPE_M,None), (4,TEAM,None), (5,STATUS,None)
                            ]
CONTENT_LOAD_JS         = [
        [TYPE_TABLE , '#synopsis'           , LOAD_JS],
        [TYPE_TEXT  , '.table .row .cell'   , RESUME ]]

DICO_JS ={
        URL             : URL_JS,
        URL_TITLE       : URL_JS + '/mangas/',
        URL_CONTENT     : URL_JS + '/mangas/',
        URL_CUT         : '/mangas/',
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
        self.initFiltre()

    def initFiltre(self):
        filtres = self.Econf.websites()
        if filtres:
            for name in filtres:
                self.Efilt[name] = self.Econf.createFiltre(name)

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
        page = self.Ereq.getRequest(url)
        if not page:
            self.ErrReq.append((name,url,ERRCONTENT))
            return None

        mcontent = self.Efilt[name].mContent(page)
        if not mcontent:
            self.ErrFiltre.append((name,url,mid))

        return mcontent

    def __str__(self):
        print self.Mlib


def TcreateFileConfig():
    Econf = Mconfig()
    print Econf.addSection("Lecture en ligne", DICO_LE)
    print Econf.addSection("Japscan", DICO_JS)
    return Econf

def TloadTitreToContent():
    m = EasyM()
    a = m.Econf.websites()
    titles = m.titles(a[0])
    c = m.mcontent(a[0],titles[43]['id'])
    print m.Efilt[a[0]]
    return c

def TupdateAllTitle():
    m = EasyM()
    websites = m.Econf.websites()
    for site in websites:
        print site
        mtitre = []
        mtitre = m.titles(site)
        if mtitre:
            m.Elib.addMliste(mtitre, site)
    return m


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
