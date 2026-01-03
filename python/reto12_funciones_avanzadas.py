#funciones mas avanzadas

def saludar(nombre="conocido"):
    print(f"Hola {nombre} espero que estes bien")

saludar()

nombre = input("Cual es tu nombre para que te salude: ")
saludar(nombre)