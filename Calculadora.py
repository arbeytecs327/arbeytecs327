#from operator import truediv
#import os
#mport time
#num2 = 0

def MenuCal():
    print('CALCULADORA BASICA')
    print('Selecciona una opción:')
    print('[1] suma')
    print('[2] resta')
    print('[3] Multiplicacion')
    print('[4] Division')
    print('[0] SALIR')
    opcion = int(input('?__'))
    return opcion

def SolicitarDatos():
    num1 = int(input("ingrese el primer numero: "))
    num2 = int(input("ingrese el primer numero: "))
    return num1, num2

def operacion(operador, num1, num2):
    if(operador == 'suma'):
        resultado = num1 + num2
    elif(operador == 'resta'):
        resultado = num1 - num2
    elif(operador == 'multiplicacion'):
        resultado = num1 * num2
    elif(operador == 'division'):
        resultado = num1 / num2
    return resultado

while True:
    opcion = MenuCal()
    if(opcion == 1):
        num1, num2 = SolicitarDatos()
        print('el resultado de la suma es: ')
        print(operacion("suma", num1, num2))
    elif(opcion == 2):
        num1, num2 = SolicitarDatos()
        print('el resultado de la resta es: ')
        print(operacion("resta", num1, num2))
    elif(opcion == 3):
        num1, num2 = SolicitarDatos()
        print('el resultado de la multiplicacion es: ')
        print(operacion("multiplicacion", num1, num2))
    elif(opcion == 4):
        num1, num2 = SolicitarDatos()
        print('el resultado de la division es: ')
        print(operacion("division", num1, num2))
    elif(opcion == 0):
        break
    else:
        print('ingrese una opcion valida')
    print("\n")
print('salimos')
