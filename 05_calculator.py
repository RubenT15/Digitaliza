opcion=0
numCorrecto=True
num1=0
num2=0
resultado=0
while numCorrecto:
    try:
        num1=int(input("Introduzca un numero"))
        num2=int(input("Introduzca otro numero"))
        numCorrecto=False
    except ValueError:
        print("Introduzca unicamente numeros")
while opcion<1 or opcion>4:
    print("1.Suma"
          " 2.Multiplicacion"
          " 3.Division"
          " 4.Exponencial")
    try:
        opcion=int(input("¿Que tipo de operacion deseas realizar? "))
    except ValueError:
        opcion=0
if opcion==1:
    resultado=num1+num2
elif opcion==2:
    resultado=num1*num2
elif opcion==3:
    resultado=num1/num2
elif opcion==4:
    resultado=num1**num2
    
print("El resultado es "+str(resultado))
