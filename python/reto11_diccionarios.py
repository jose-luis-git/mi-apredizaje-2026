diccionario = {}

nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))
ciudad = input("Digite su ciudad: ")

diccionario["nombre"] = nombre
diccionario["edad"] = edad
diccionario["ciudad"] = ciudad

print(f"Nombre: {diccionario["nombre"]}")
print(f"Edad: {diccionario["edad"]}")
print(f"Ciudad: {diccionario["ciudad"]}")