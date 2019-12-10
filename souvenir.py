from class_emotion import Emotion
import json

class Souvenir():

    def __init__(self):
        self.souvenir = []


    def set_souvenir(self,emotion):
        self.souvenir.append(emotion)

    def get_rappel(self):
        return self.souvenir
