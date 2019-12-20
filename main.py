from souvenir import Souvenir
from class_emotion import Mot_cle
import os
from time import gmtime, strftime
import json


souvenir = Souvenir()
while input("Ajout d'engramme ? Oui? ---> ")== "oui":
    os.system("clear")
    souvenir.set_souvenir(Mot_cle(input("Mot_cle-->  Mettre des mot cles coherent (personne,lieu,acte,emotion): --> "),input("Timellaps --> "),input("souvenir---> ")))
else:
    liste_retour = souvenir.get_rappel()

    print("au revoir")


liste_retour = souvenir.get_rappel()
for element in liste_retour:
    os.system("clear")
    print(element,strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
    fichier = open("save.json","a")
    fichier.write(json.dumps([element.mot_cle,element.date,element.info,strftime("%a, %d %b %Y %H:%M:%S", gmtime())]))
    fichier.close()
