from funtions import *

numeros = []
nro=int(input("Números: "))

while nro!=0:
    numeros.append(nro)
    nro=int(input("Números: "))
    
eliminar=int(input("Número a eliminar: "))
if eliminar in numeros:
    numeros.remove(eliminar)
else:
    print("Ese número no está entre los ingresados.")
    
print("Sumatoria de los números:", sumatoria(numeros))

limite=int(input("Filtrar números menores a: "))
for n in numerosMenores(numeros, limite):
    print(n)
    
print("Frecuencias: ")
for tupla in frecuencias(numeros):
    print(tupla[0], "aparece", tupla[1], "veces")


