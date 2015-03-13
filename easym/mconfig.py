"""
    Le module MConfig perrmet de gérer le fichier de configuration
    incluant les sélectuer css pour chaque site internet possédant
    les informations nécéssaire aux projet.
"""

# imports
from ConfigParser import Configparser

# constants
CONFIG_FILE='configm.cfg'
# exception classes
# classes

class Config(object):
    """
        La classe s'occupe d'un fichier CONFIG_FILE , se charge de le
        crée s'il n'existe pas, chaque section du fichier correspond à un site.
        Ce module effectue l'étape :
            - lire le fichier CONFIG_FILE avec module ConfigParser
            - traduire en un dictionnaire  clé section value :dico
                (clé : POSITION ;value: SELECTEUR)
            CONFIG_FILE -> DICO Sélecteur
        Si vide renvoie NONE
    """

    def __init__(self):
        """ On vérifie si le fichier CONFIG_FILE , on le crée sinon"""
        self.mconfig = ConfigParser.ConfigParser()
        self.load_source()

    # Va charger le fichierr CONFIG_FILE dans mconfig
    def loadConfig(self):
        pass

    # ajoute ajoute la nouvelle insatnce new file aux fichier de config
    def addSource(self, new_file):
        pass

    # Sauvegarde le fichier de configuration crourant
    def saveConfig(self):
        pass

    # Sort les information d'un section de notre configuration dans un dico
    def readSection(self, section):
        pass

# internal functions & classes

def check_config_file():
    return False

# if __name__ == '__main__':
