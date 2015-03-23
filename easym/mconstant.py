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
MALL = "EASYM"

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
PAUSE_REQUEST_MIN = 1
PAUSE_REQUEST_MAX = 4


def encodeUTF8(elt):
    return elt.encode("utf-8")

def getInfoM(name, mid ,minfo):
    info = u"""
 Titre : %s
 Identifiant : %s
 Status : %s
 Type : %s
 Titre secondaire : %s
 Auteur : %s
 Dessinateur : %s
 Editeur français : %s
 Parution : %s
 Team : %s
 Sens de lecture : %s
 Classement : %s
 Note : %s
 Tag : %s
 Resumé :
     %s
     """ % (name, mid, minfo[STATUS], minfo[TYPE_M], minfo[SCND_NAME],
            minfo[AUTHOR], minfo[DRAWER], minfo[FR_EDIT], minfo[PARUTION], minfo[TEAM],
            minfo[READ], minfo[CLASSMENT], minfo[NOTE] ,minfo[TAG], minfo[RESUME])
    return encodeUTF8(info)
