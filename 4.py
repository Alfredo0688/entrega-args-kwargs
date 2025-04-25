#Calcular el promedio de una lista de números usando args y un operador ternario

lista_numeros = [10,20,30]


def calcularPromedio(longitud_lista, *lista):
    total_numeros = 0
    contador = 0
    for numero in lista:
        total_numeros += numero
        total_numeros / longitud_lista if longitud_lista == contador else None
        contador+= 1
    print(f"El promedio de los números es : {total_numeros/longitud_lista}")
calcularPromedio(len(lista_numeros),*lista_numeros )

