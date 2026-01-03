import json

persona = {
    "nombre" : "jose",
    "edad": 17,
    "ciudad": "La Paz"
}

with open("persona.json", "w") as archivo_json:
    json.dump(persona, archivo_json, indent=4)

with open("persona.json", "r") as archivo_json:
    datos = json.load(archivo_json)
    print(f"Nombre: {datos["nombre"]}")
    print(f"Edad: {datos["edad"]}")
    print(f"Ciudad: {datos["ciudad"]}")