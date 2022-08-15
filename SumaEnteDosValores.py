print('SUMA DE VALORES ENTRE DOS NUMEROS')
numero1 = int(input('ingrese un numero entero: '))
numero2 = int(input('ingrese otro numero entero: '))
suma = 0
for num in range(numero1, numero2 + 1 , 1):
    suma = suma + num
print('la suma de los numeros ingresados es: ', suma)
