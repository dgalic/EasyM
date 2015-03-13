"""
    Le module Mrequest s'occupe d'effectuer le requete http demander
    et de filtrer avec les selecteur fournie et de renvoyer le résultat
    pour chaque requête.
"""
# imports
import requests
from bs4 import BeautifulSoup

# constants
# exception classes
# interface functions
# classes
# internal functions & classes

def Request(object):

    def __init__(self):
        """ Information d'initalisation ?
             - Problème comment limiter ne nombre de requete
        """
        self.lastrequest = {}

    def loadrequest(self, url):
        """ Ce charge l'url et s'occupe :
                - regarder bonne reponse
                - redirection possible ?
                - encodage à verifié ? -> passer en utf-8
        """
        pass

    def filtrerequest(self , response, selecteur):
        """ Ce charge de filtrer la requete et renvoie un dico
            avec les sélecteur voulue ou None.
            Peut-on savoir le format des selecteur ?
        """
        pass


if __name__ == '__main__':
    sys.exit(0)

