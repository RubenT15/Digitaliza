def printOptions():
    print("1.Suma"
          " 2.Resta"
          " 3.Multiplicacion"
          " 4.Division"
          " 5.Exponencial")
def calc(option,num1,num2):
    return {
         1: num1+num2,
         2: num1-num2,
         3: num1*num2,
         4: num1/num2,
         5: num1**num2,
    }.get(option, 0)
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
while opcion<1 or opcion>5:
    printOptions()
    try:
        opcion=int(input("¿Que tipo de operacion deseas realizar? "))
    except ValueError:
        opcion=0
try:        
    resultado=calc(opcion,num1,num2)
    print("El resultado es "+str(resultado))
except ZeroDivisionError:
    print("No puedes dividir entre 0!")
except:
    print("Algo fue mal")

