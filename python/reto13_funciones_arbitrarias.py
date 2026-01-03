#funcinoes con *args y **kwargs

#*args 

cantidad = int(input("Digite la cantidad de numeros que ingresara: "))

numeros = []

for i in range(cantidad):
    numero = int(input("Digite un numero: "))
    numeros.append(numero)

def sumar_numeros(*numeros):
    return sum(numeros)

suma = sumar_numeros(*numeros)

print(f"La suma de todos los numeros es: {suma}")

#**kwargs

nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))
ciudad = input("Digite su ciudad: ")

def mostrar_persona(**informacion):
    for clave, valor in informacion.items():
        print(clave, ": ", valor)

mostrar_persona(nombre=nombre,edad=edad,ciudad=ciudad)
