# -*- coding: UTF-8 -*-
""" Test EasyM """

# imports
import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from unidecode import unidecode

import sys
import re

# constants
TIME_REQUEST        = 0.5
PAUSE_REQUEST_MIN   = 1
PAUSE_REQUEST_MAX   = 3
EASY_LIBRARY        = 'libEasyM.txt'
TYPE_TEXT           = 'text'
TYPE_TABLE          = 'table'
TYPE_ATTRS          = 'attrs'

# Description to library manga
## KEY   Name prepare at manga
## VALUE Dictionary information at this manga 

### Dictianary for MANGA
## KEY url site
URL_LE = 'http://www.lecture-en-ligne.com'
URL_JS = 'http://www.japscan.com'
URL_JP = 'http://www.japan-shin.com'

## VALUE Information in this site
MNAME = 'name'
MID = 'id'

INFO = 'information'
#### Dictionnary VALUE : INFO
### FIED to INFO
SCND_NAME   = 'alternatif_name'
PARUTION    = 'parution'
STATUS      = 'status'
AUTHOR      = 'author'
DRAWER      = 'drawer'
FR_EDIT     = 'editor_fr'
TEAM        = 'team'
GENRE       = 'genre'
READ        = 'read'
CLASSMENT   = 'classment'
NOTE        = 'note'
IMG_URL     = 'img'
RESUME      = 'resume'


# Field to constant infroamtion in web site

## LECTURE EN LIGNE
### constant
TITLE_LINK_LE           = ''
CONTENT_LINK_LE         = '/manga/'
LINK_TITLE_PAGE_LE      = URL_LE + TITLE_LINK_LE
LINK_CONTENT_PAGE_LE    = URL_LE + CONTENT_LINK_LE
PATTERN_URL_CUT_LE      = LINK_CONTENT_PAGE_LE

### selecteur CSS
#### TITLE
SELECT_TITLE_LE         = 'optgroup option'
FIELD_TITLE_LE          = 'value'

#### CONTENT PRIMARY PAGE
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
TITLE_LINK_JS           = '/mangas/'
CONTENT_LINK_JS         = '/mangas/'
LINK_TITLE_PAGE_JS      = URL_JS + TITLE_LINK_JS
LINK_CONTENT_PAGE_JS    = URL_JS + CONTENT_LINK_JS
PATTERN_URL_CUT_JS      = TITLE_LINK_JS

### selecteur css
#### TITLE
SELECT_TITLE_JS         = '#liste_mangas .row .cell a[href^="/mangas/"]'
FIELD_TITLE_JS          = 'href'

### CONTENT PRIMARY PAGE
SELECT_RESUME_LE        = '#synopsis'




def getInfoR(page):
    history = "{"
    for a in page.history:
        history = history + " " + a + ","
    history = history + " }"

    ## Information on request
    info = u"""
  Url : %s
  Status : %s
  Redirection : %s
  Endoding : %s
            """ % (page.url, page.status_code, history, page.encoding)

    print encodeUTF8(info)

def getInfoM(manga):
    minfo = manga[INFO]
    info = """
 Titre : %s
 Identifiant : %s
 Status : %s
 Titre secondaire : %s
 Auteur : %s
 Dessinateur : %s
 Editeur français : %s
 Parution : %s
 Team : %s
 Genre : %s
 Sens de lecture : %s
 Classement : %s
 Note : %s
 Resumé :
     %s
     """ % (manga[MNAME], manga[MID],
            minfo[STATUS], minfo[SCND_NAME ],
            minfo[AUTHOR], minfo[DRAWER], minfo[FR_EDIT],
            minfo[PARUTION], minfo[TEAM],
            minfo[GENRE], minfo[READ],
            minfo[CLASSMENT], minfo[NOTE],
            minfo[RESUME])
    print info

def encodeUTF8(elt):
    return elt.encode("utf-8")

def getRequest(url, aff=False):
    try :
        page = requests.get(url, timeout=TIME_REQUEST)
    except requests.exceptions.Timeout:
       print "Erreur : Timeout request"
       return None
    except requests.exceptions.ConnectionError:
       print "Erreur : ConnexionError request"
       return None

    if not page.status_code == requests.codes.ok:
        return None

    if not page.encoding == 'utf-8':
        page.encoding = 'utf-8'

    if aff:
        getInfoR(page)
    return page

def getTitle(content, selecteur, field, url_cut, aff=False):
    soup = BeautifulSoup(content.text)

    ## keep only inforamtion necessary information with selecteur
    titles = soup.select(selecteur)

    lmanga = []
    ## catch name and identifier to manga in web site
    for m in titles:
        ## catch name and identifier
        name = m.text

        url = m.attrs[field]
        result = re.match(url_cut + "(.*)/", url)
        id_manga = result.group(1)

        lmanga.append({MNAME: name , MID : id_manga , INFO : None})

    if aff:
        print "Title length : %d" % (len(lmanga))

    return lmanga

def title_LE():
    page = getRequest(LINK_TITLE_PAGE_LE)
    if not page:
        return None

    select = SELECT_TITLE_LE
    field  = FIELD_TITLE_LE
    url_cut = PATTERN_URL_CUT_LE

    titles = getTitle(page, select, field, url_cut)
    return titles

def title_JS():
    page = getRequest(LINK_TITLE_PAGE_JS)
    if not page:
        return None

    select = SELECT_TITLE_JS
    field  = FIELD_TITLE_JS
    url_cut = PATTERN_URL_CUT_JS

    titles = getTitle(page, select, field, url_cut)
    return titles

def formatName(name):
    """ formate le nom du manga à être un identifiant unique """
    name = unidecode(name).lower().replace(" ","")
    name = re.sub(r'[-+/\',.:?&#]'  , "", name)
    return name


def addMLib(lib, mliste, site):
    errors = []
    for m in mliste:
        keyname = formatName(m[MNAME])
        if keyname in lib:
            sites_manga = lib[keyname]
            if not site in sites_manga:
                print keyname
                sites_manga[site] = m
            else:
                # TODO dans le cas d'update les données
                errors.append(m[MNAME])
                continue
        else:
            print keyname
            lib[keyname] = {site : m}

    return (lib,errors)

def openLib():
    try:
        f = open(EASY_LIBRARY, "r")
        lib = eval(f.read())
        f.close()
    except IOError:
        lib = {}
    return lib

def saveLib(library):
    try:
        f = open(EASY_LIBRARY, "w")
        f.write(str(library))
        f.close()
    except IOError:
        return False
    return True

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

############################################ Not test
def testContentM_LE(id_manga):
    url = LINK_CONTENT_PAGE_LE + id_manga +'/'
    page = getRequest(url)

    if not page:
       print "Error: page Empty"
       return page

    field_load = CONTENT_LOAD_LE
    filtre = FILTRE_LE

    return getContentM(page, field_load, filtre)

def testload_info():
    titlesLE = title_LE()

    if not titlesLE:
        print "titles is empty"
        sys.exit(None)

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

        m[INFO] = info

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
