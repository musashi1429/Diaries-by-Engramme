from time import strftime

class Emotion():
    def __init__(self,emotion,date,info):
        self.emotion = emotion
        self.date = date
        self.info = info

    def __str__(self):
         return "emotion:({}),date:({}),info({}) ".format(self.emotion,self.date,self.info)
