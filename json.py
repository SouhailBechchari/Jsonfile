import json


data = {
    "nom": "souhail",
    "age": 18,
    "ville": "marrakech"
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=2)

with open("data.json", "r") as json_file:
    imp_data = json.load(json_file)
    print("Contenu du fichier initial :")
    print(imp_data)


imp_data["langage"] = "Python"


with open("data.json", "w") as json_file:
    json.dump(imp_data, json_file, indent=2)

with open("data.json", "r") as json_file:
    new_data = json.load(json_file)
    print("\nContenu du fichier après modification :")
    print(new_data)