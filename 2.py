#Buscar una palabra en una lista ingresada por teclado usando args y un operador
#ternario

lista = []

numero_elementos = int(input("Cuantos elementos tendrá su lista?: "))

for i in range(numero_elementos):
    elemento = input(f"Ingrese el {i + 1} elemento : ")
    lista.append(elemento)

#lista = ["Boca Juniors","Bayern Munich","Real Madrid"]

palabra_buscada = input("Que palabra de la lista le gustaría buscar?: ")

def buscarPalabra(palabra,*argumentos):
    for elemento in argumentos:
        
        print(elemento if elemento == palabra else None)
        
    #print(f"La palabra encontrada es: {palabra_encontrada}")


buscarPalabra(palabra_buscada, *lista) 

