import json

class Engramme():
    def __init__(self):
        self.save = []

    def import_save(self):

        with open("save.json","r") as json_data:
            print(type(json_data))
            data_list = json.dumps(json_data)
            print(data_dict)
        data_str = json.dumps(data_list)
        return data_dict

    def put(self,data_dict):
        with open("save.json","r") as json_data:
            print(type(json_data))
            data_list = json.dumps(json_data)
        self.save.append(json.dumps(data_list))
        return self.save
