print('MULTIPLICACION DE DOS NUMEROS SIN EL OPERADOR *')
def multiplicacion(a,b):
    mult = 0
    for num in range(0, a, 1):
        mult = mult + b 
    print('El resultado de la multipliccion es :', mult)
    return 
a = int(input('ingrese un numero para multiplicacion :'))
b = int(input('ingrese otro numero para multiplicacion  :'))
multiplicacion(a,b)
