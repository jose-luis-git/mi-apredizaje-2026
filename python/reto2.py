import json

actividad = {
    "hobbies": "programar",
    "comida": "pollo"
}

with open("actividades.json", "w") as archivo_json:
    json.dump(actividad, archivo_json)

with open("actividades.json", "r") as archivo_json:
    datos = json.load(archivo_json)
    print(f"Hobbies: {datos["hobbies"]}")
    print(f"Comida: {datos["comida"]}")