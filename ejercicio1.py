#Escribe una función recursiva llamada suma_lista que tome una lista de números como
#argumento y devuelva la suma de todos los elementos en la lista.?

def suma_lista(lista):
    return sum(lista)

lista = [1, 4, 3, 1, 5]
resultado = suma_lista(lista)
print("La suma de los numeros en la lista es:", resultado)