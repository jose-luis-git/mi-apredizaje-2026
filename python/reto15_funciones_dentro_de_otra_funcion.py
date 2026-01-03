def envoltura(nombre):
    def contenido():
        print(f"Este es un saludo para {nombre} desde contenido")
    contenido()

nombre = input("Digite su nombre: ")

envoltura(nombre)