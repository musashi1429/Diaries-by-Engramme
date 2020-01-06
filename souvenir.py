from class_emotion import Mot_cle
import json

class Souvenir():

    def __init__(self):
        self.souvenir = []
        self.engramme = []


    def set_souvenir(self,mot_cle):
        self.souvenir.append(mot_cle)

    def set_engramme(self,engramme):
        self.engramme.append(input("enregistrement-----> "))

    def get_rappel(self):
        return self.souvenir

    def get_engramme(self):
        return self.engramme
