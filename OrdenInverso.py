print('INVERTIR EL ORDEN DE LOS NUMEROS')

def invertir_numero(n):
    numero = 0
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10
    return numero
numero = int(input('ingrese un numero entero de 3 cifras :'))
numero_invertido = invertir_numero(numero)
print('El número ingresado ', numero, 'al invertir el orden es :', numero_invertido)