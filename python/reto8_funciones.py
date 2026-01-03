def saludo(nombre):
    print(f"Hola {nombre} como estas")

def multiplicacion(a, b):
    return a * b

nombre = input("Digite su nombre: ")
saludo(nombre)

n1 = int(input("Digite un numero: "))
n2 = int(input("Digite otro numero: "))

resultado = multiplicacion(n1, n2)
print(f"Resultado de la multiplicacion: {resultado}")