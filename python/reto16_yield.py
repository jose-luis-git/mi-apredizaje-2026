#yield 

numeros = []

while(True):
    try:
        cantidad = int(input("Digite la cantidad de elementos que registrara: "))
        if cantidad < 0:
            raise ValueError("Numero negativo invalido")
        break
    except ValueError as e:
        print(f"Error: {e}")

for i in range(cantidad):
    while(True):
        try:
            numero = int(input("Digite un numero: "))
            numeros.append(numero)
            break
        except ValueError as e:
            print(f"Error: {e}")
    
def contador_positivo(*numeros):
    for n in numeros:
        if n > 0:
            yield n
        else:
            break
        

for x in contador_positivo(*numeros):
    print(x)