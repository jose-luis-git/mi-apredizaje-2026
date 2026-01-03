#funciones como objetos

def saludar(nombre):
    print(f"Hola {nombre} como estas")

nombre = input("Digite su nombre: ")

saludo = saludar

saludo(nombre)