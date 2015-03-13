#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
"""
    Le module Mrequest s'occupe d'effectuer le requete http demander
    et de filtrer avec les selecteur fournie et de renvoyer le résultat
    pour chaque requête.
"""
# imports
import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from unidecode import unidecode

# constants
# exception classes
# interface functions
# classes
# internal functions & classes
def encodeUTF8(elt):
    return elt.encode("utf-8")

class MRequest(object):

    def __init__(self, trequest = 0.5):
        """ Information d'initalisation ?
             - Problème comment limiter ne nombre de requete
        """
        self.request = None
        self.time_request = trequest

    def getRequest(self, url):
        """
            Charge les donnée a l'adresse url.
            Gére les erreurs:
                - TimeOut
                - ConnexionError
            Renvoie les données reencodé en utf-8
        """
        # TODO : voir a amélioré la gestion des erreurs
        try :
            self.request = requests.get(url, timeout=self.time_request)
        except requests.exceptions.Timeout:
            print "Erreur : Timeout request"
            return False
        except requests.exceptions.ConnectionError:
            print "Erreur : ConnexionError request"
            return False

        if not self.request.status_code == requests.codes.ok:
            return False

        if not self.request.encoding == 'utf-8':
            self.request.encoding = 'utf-8'

        return True

    def __str__(self):
        if  not self.request:
            return "Not request are ask"
        page = self.request
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
        return encodeUTF8(info)

#if __name__ == '__main__':
