#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

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
STATUS      = 'status' ## ENCOURS , TERMINER, ONESHOT, PAUSE, ABANDONNE
AUTHOR      = 'author' ## FORMAT
DRAWER      = 'drawer' ## FORMAT
FR_EDIT     = 'editor_fr'
TEAM        = 'team'
GENRE       = 'genre' ## TAG | Shōjo Shōnen Josei Seinen
READ        = 'read'
CLASSMENT   = 'classment' ##
NOTE        = 'note' ##
IMG_URL     = 'img'
RESUME      = 'resume' ##


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
