menu = """
Bienvenido al conversor de monedas 👌

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuantos pesos colombianos tienes?: ")
    esos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $"+dolares+ " dólares")
elif opcion == 2:
    pesos = input("Ingrese su cantidad de dinero en pesos argentinos: ")
    pesos = float(pesos)
    dolares = pesos/65
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("La cantidad es: " + dolares + " dólares")
elif opcion == 3:
    pesos = input("Ingrese su cantidad de dinero en pesos mexicanos: ")
    pesos = float(pesos)
    dolares = pesos/20
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("La cantidad es: " + dolares + " dólares")
else:
    print("Elige una opción correcta por favor")


