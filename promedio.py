from turtle import end_fill


print('PROMEDIO DE NOTAS DE ESTUDIANTES')
parcial = float(input('ingrese su primer nota: '))
und = 1
n = 1
nota = 0
while(und == 1):
    n = n+1
    nota = float(input('ingrese la siguiente nota: '))
    salir = int(input('''¿desea ingresar mas notas? : '''
                   ''' ingrese 1 para si, '''
                   ''' ingrese 2 para no: '''))
    parcial = parcial + nota
    if (salir == 2):
        und = 2
promedio = parcial/n
print('El promedio de las', n , 'notas es: ', promedio)
