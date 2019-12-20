from time import strftime

class Mot_cle():
    def __init__(self,mot_cle,date,info):
        self.mot_cle = mot_cle
        self.date = date
        self.info = info

<<<<<<< HEAD
    def __repr__(self):
         return "emotion:({}),date:({}),info({}) ".format(self.emotion,self.date,self.info)
=======
    def __str__(self):
         return "Hashtag:({}),date:({}),info({}) ".format(self.mot_cle,self.date,self.info)
>>>>>>> 4ad55cd424d347a1670eccb8b44d59baf0bd9d92
