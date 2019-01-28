pedirNumero=True
while pedirNumero:
    try:
        numero=int(input("Introduzca un número"))
        if numero<20:
            print("El numero "+str(numero)+ " es menor de 20")
        elif numero>=20 and numero<=39:
            print("El numero "+str(numero)+ " es mayor o igual de 20 y menor de 40")
        elif numero>=40 and numero<=59:
            print("El numero "+str(numero)+ " es mayor o igual de 40 y menor de 60")
        elif numero>=60:
            print("El numero "+str(numero)+ " es mayor o igual de 60")
        pedirNumero=False
    except ValueError:
        print("El valor introducido fue incorrecto")
