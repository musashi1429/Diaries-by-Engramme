from time import strftime

class Mot_cle():
    def __init__(self,mot_cle,date,info):
        self.mot_cle = mot_cle
        self.date = date
        self.info = info

    def __str__(self):
         return "Hashtag:({}),date:({}),info({}) ".format(self.mot_cle,self.date,self.info)
