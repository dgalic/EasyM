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
TYPE_TEXT           = 'text'
TYPE_TABLE          = 'table'
TYPE_ATTRS          = 'attrs'

# exception classes
# interface functions
def encodeUTF8(elt):
    return elt.encode("utf-8")
# classes
# internal functions & classes

def Request(object):

    def __init__(self):
        """ Information d'initalisation ?
             - Problème comment limiter ne nombre de requete
        """
        self.request = None
        self.printer = False

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
            self.request = requests.get(url, timeout=TIME_REQUEST)
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

        if self.printer:
            printRequest()
        return True

    def printRequest(self):
        page = self.request
        history = "{"
        for a in page.history:
            history = history + " " + a + ","
        history = history + " }"

        ## Information on request
        info = u""" Url : %s\n Status : %s\n Redirection : %s\n Endoding : %s
                """ % (page.url, page.status_code, history, page.encoding)
        print encodeUTF8(info)

    def filtrerequest(self , response, selecteur):
        """ Ce charge de filtrer la requete et renvoie un dico
            avec les sélecteur voulue ou None.
            Peut-on savoir le format des selecteur ?
        """
        pass


if __name__ == '__main__':
    sys.exit(0)

