"""
1. Imprimir los primeros 20 números naturales
"""
print ("Ejercicio 1")

def imprimir_naturales_20():
    """
    Imprime los primeros 20 números naturales.
    """
    for i in range(20):
        print(i)

imprimir_naturales_20() # 0 a 19

"""
2. Imprimir la tabla de multiplicar del número 5
"""
print ("Ejercicio 2")

def tabla_multiplicar_5():
    """
    Imprime la tabla de multiplicar del número 5.
    """
    for i in range(1, 11): # del 1 al 10
        print(f"5 x {i} = {5 * i}")

tabla_multiplicar_5()

"""
3.  Imprima los números de -10 a -1.
"""
print ("Ejercicio 3")

def imprimir_negativos():
    """
    Imprime los números de -10 a -1.
    """
    for i in range(-10, 0):
        print(i)

imprimir_negativos()

"""
4.  Dada la siguiente secuencia de números:
numeros = [12 , 75 , 150 , 180 , 145 , 525 , 50]

imprimir los números divisibles por 5 menores a 150.
"""

print ("Ejercicio 4")
def imprimir_divisibles_por_5_menores_a_150():
    """
    Imprime los números divisibles por 5 menores a 150 de la lista numeros.
    """
    numeros = [12, 75, 150, 180, 145, 525, 50]
    for numero in numeros:
        if numero < 150 and numero % 5 == 0:
            print(numero)

imprimir_divisibles_por_5_menores_a_150()

"""
5. Imprimir los primeros 10 valores de la secuencia de Fibonacci. La secuencia de Fibonacci es una serie
de números en la cual los dos primeros números son 0 y 1, y el siguiente número se corresponde a la
suma de los dos números anteriores. Resultado esperado:
0 1 1 2 3 5 8 13 21 34
"""
print ("Ejercicio 5")

def imprimir_fibonacci_10():
    """
    Imprime los primeros 10 números de la secuencia de Fibonacci.
    """
    a, b = 0, 1
    for _ in range(10):
        print(a, end=" ")
        a, b = b, a + b

imprimir_fibonacci_10()

"""
6. Imprimir el valor factorial del número 5 usando un bucle. El valor factorial (símbolo: !) se obtiene de
multiplicar todos los números enteros desde el número elegido hasta 1. Resultado esperado: 120
"""
print ("Ejercicio 6")
def factorial_5():
    """
    Imprime el valor factorial del número 5.
    """
    numero = 5
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}")

factorial_5()

"""
7. Explique el resultado de los siguientes programas
a. 
lista = []
for j in lista :
    print ( j )
b. 
i = 1
for i in [1 , 2 , 3]:
    print ( i )
print ( i )
"""

# Efercicio 7

def a():
    lista = []
    for j in lista :
        print ( j )

a() # No imprime nada ya que lista esta vacia

def b():
    i = 1
    for i in [1 , 2 , 3]:
        print ( i )
    print ( i )

b() # Imprimira 1 2 3 3, ya que el primer i se remplaza por 1, 2, 3, y luego se muestra i que el valor actual es 3
