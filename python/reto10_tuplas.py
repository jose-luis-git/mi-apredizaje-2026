#tuplas no se pueden modificar

tupla = ()

numero1 = int(input("Digite un numero: "))
numero2 = int(input("Digite otro numero: "))

tupla = (numero1,) + (numero2,)

print(f"Tupla: {tupla}")