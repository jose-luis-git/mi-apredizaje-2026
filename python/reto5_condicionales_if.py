#condicionales if elif else

edad = int(input("Digite su edad: "))
nota = int(input("Digite su nota favorita: "))

if edad < 18 :
    print("Eres menor de edad")
    if nota < 50:
        print("Seguramente no te gusta estudiar")
    elif nota <= 90:
        print("Seguro te gusta estudiar")
    else:
        print("Seguro eres el mejor de tu clase")
else:
    print("Eres mayor de edad")
    if nota < 50:
        print("Seguramente no te gusta estudiar")
    elif nota <= 90:
        print("Seguro te gusta estudiar")
    else:
        print("Seguro eres el mejor de tu clase")
