#decoradores

nombre = input("Digite su nombre: ")

def mostrar_nombre(func):
    def wrapper(nombre):
        print("Antes de la funcion")
        func(nombre)
        print("Despues de la funcion")
    return wrapper

@mostrar_nombre
def saludar(nombre):
    print(f"Hola {nombre} espero que estes bien")

saludar(nombre)