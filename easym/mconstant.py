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
STATUS      = 'status'  # ENCOURS , TERMINER, ONESHOT, PAUSE, ABANDONNE
AUTHOR      = 'author'  ## FORMAT
DRAWER      = 'drawer'  ## FORMAT
GENRE       = 'genre'   ## TAG | Shōjo Shōnen Josei Seinen
IMG_URL     = 'img'     ## pour l'affichage
RESUME      = 'resume'  ## TEXT

## Un plus
SCND_NAME   = 'alternatif_name'
PARUTION    = 'parution'
FR_EDIT     = 'editor_fr'
TEAM        = 'team'
READ        = 'read'
CLASSMENT   = 'classment'
NOTE        = 'note'
