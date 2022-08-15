print('NUMERO MAYOR')
lista=[]
n = int(input('ingrese la cantidad de numeros a evaluar :'))

for num in range(n):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)
mayor = max(lista)
print(lista)
print('El numero mayor es: ',mayor)