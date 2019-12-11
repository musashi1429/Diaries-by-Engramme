from souvenir import Souvenir
from class_emotion import Emotion
import os
from time import gmtime, strftime
import json
from engramme import Engramme
from io import StringIO
from json import dumps


souvenir = Souvenir()
while input("Ajout d'engramme ? Oui? ---> ")== "oui":
    os.system("clear")
    print(strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
    souvenir.set_souvenir(Emotion(input("emotion -->  choississez une emotion : Joie.Tristesse.Peur.Colère.Dégoût.Surprise. --> "),input("Date --> "),input("souvenir---> ")))
else:
    liste_retour = souvenir.get_rappel()

    print("au revoir")


liste_retour = souvenir.get_rappel()
for element in liste_retour:
    os.system("clear")
    print(element)
    fichier = open("save.json","a")
    fichier.write(json.dumps([element.emotion,element.date,element.info]))
    fichier.close()
###
save = Engramme()
with open("save.json","r") as json_data:
    print(type(json_data))
    data_list = json.dumps(json_data)
save_retour = save.put(data_list)
print(save_retour)
