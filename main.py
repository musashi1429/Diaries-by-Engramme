from souvenir import Souvenir
from class_emotion import Mot_cle
import os
from time import gmtime, strftime
import json
from engramme import Engramme
from io import StringIO
from json import dumps


souvenir = Souvenir()
while input("Ajout d'engramme ? Oui? ---> ")== "oui":
    os.system("clear")
    souvenir.set_souvenir(Mot_cle(input("Mot_cle-->  Mettre des mot cles coherent (personne,lieu,acte,emotion): --> "),input("Timellaps --> "),input("Synopsis---> ")))
    souvenir.set_engramme("info")
else:
    liste_retour = souvenir.get_rappel()

    print("au revoir")


liste_retour = souvenir.get_rappel()
engramme = souvenir.get_engramme()
for element in liste_retour:
    os.system("clear")
    print(element,engramme,strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
    fichier = open("save.json","a")
    fichier.write(json.dumps([element.mot_cle,element.date,element.info,engramme,strftime("%a, %d %b %Y %H:%M:%S", gmtime())]))
    fichier.close()
###
# save = Engramme()
# with open("save.json","r") as json_data:
#     print(type(json_data))
#     data_list = json.dumps(json_data)
# save_retour = save.put(data_list)
# print(save_retour)
