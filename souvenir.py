from class_emotion import Mot_cle
import json

class Souvenir():

    def __init__(self):
        self.souvenir = []


    def set_souvenir(self,mot_cle):
        self.souvenir.append(mot_cle)

    def get_rappel(self):
        return self.souvenir
