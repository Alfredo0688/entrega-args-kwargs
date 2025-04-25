###Calcular el mayor de dos números ingresados por teclado usando un operador ternario

valor1 = input("Ingrese un número: ")
valor2 = input("Ingrese otro número: ")

valor_mayor = valor1 if valor1 > valor2 else valor2 if valor2 > valor1 else "Los valores son iguales"

print(F"El número mayor es : {valor_mayor}")




