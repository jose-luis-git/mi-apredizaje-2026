actividades = []

cantidad = int(input("Digite cuantas cosas agregara a la lista: "))

for i in range(cantidad):
    actividad = input("Digite su actividad o juego favorito: ")
    actividades.append(actividad)

for i in range(cantidad):
    print(actividades[i])