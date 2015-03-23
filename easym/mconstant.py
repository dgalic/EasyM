#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

# constants
TIME_REQUEST        = 1
PAUSE_REQUEST_MIN   = 1
PAUSE_REQUEST_MAX   = 3
TYPE_TEXT           = 'text'
TYPE_TABLE          = 'table'
TYPE_ATTRS          = 'attrs'

# Description to library manga
## KEY   Name prepare at manga
## VALUE Dictionary information at this manga 

### Dictianary for MANGA
## KEY url site
MALL = "EASYM"  # all information formaté
MVOTER = "VOTER" # 3 liste

## VALUE Information in this site
MNAME = 'name'
MID = 'id'

MINFO = 'information'
#### Dictionnary VALUE : MINFO
### FIED to MINFO
STATUS      = 'status'  ## ENCOURS , TERMINER, ONESHOT, PAUSE, ABANDONNE
AUTHOR      = 'author'  ## FORMAT
DRAWER      = 'drawer'  ## FORMAT
TYPE_M      = 'type'    ## Shōjo Shōnen Josei Seinen ect
TAG         = 'tag'     ## TAG mots clée du manga
RESUME      = 'resume'  ## TEXT

## Un plus
IMG_URL     = 'img'     ## pour l'affichage
SCND_NAME   = 'alternatif_name'
PARUTION    = 'parution'
FR_EDIT     = 'editor_fr'
TEAM        = 'team'
READ        = 'read'
CLASSMENT   = 'classment'
NOTE        = 'note'

ALLFIELD_MINFO = [  STATUS, AUTHOR, DRAWER, TYPE_M, TAG,
                    RESUME, IMG_URL, SCND_NAME,
                    PARUTION, FR_EDIT, TEAM,
                    READ, CLASSMENT, NOTE]

TITRE_FIELD = { STATUS      : u'Status :',
                AUTHOR      : u'Auteur :',
                DRAWER      : u'Desinateur :',
                TYPE_M      : u'Type :',
                TAG         : u'Tag :',
                RESUME      : u'Resumé :\n',
                SCND_NAME   : u'Titre secondaire :',
                PARUTION    : u'Année de parution :',
                FR_EDIT     : u'Editeur français :',
                TEAM        : u'Team :',
                READ        : u'Sens de lecture:',
                CLASSMENT   : u'Classement :',
                NOTE        : u'Note :'
            }
PAUSE_REQUEST_MIN = 1
PAUSE_REQUEST_MAX = 4


def encodeUTF8(elt):
    return elt.encode("utf-8")

def addText(minfo, field):
    if field in minfo and minfo[field] != None:
        return u"%s %s\n" %(TITRE_FIELD[field],minfo[field])
    return u""

def getInfoM(name, mid ,minfo):
    text = u""
    text = text + addText(minfo, STATUS)
    text = text + addText(minfo, TYPE_M)
    text = text + addText(minfo, SCND_NAME)
    text = text + addText(minfo, AUTHOR)
    text = text + addText(minfo, DRAWER)
    text = text + addText(minfo, FR_EDIT)
    text = text + addText(minfo, PARUTION)
    text = text + addText(minfo, TEAM)
    text = text + addText(minfo, READ)
    text = text + addText(minfo, NOTE)
    text = text + addText(minfo, TAG)
    text = text + addText(minfo, RESUME)
    info = u"""
 Titre : %s
 Identifiant : %s
%s""" % (name, mid, text)
    return encodeUTF8(info)
