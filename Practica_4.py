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


# Ejercicio 8
"""
8. Resuelva los siguientes ejercicios
a. Calcular el cuadrado de los primeros 10 números enteros.
b. Calcular la suma de los números enteros entre 0 y 100 inclusive.
c. Calcular la suma de los números pares menores a 100. ¿Cuántos números pares hay menores a
100?
d. Calcular la suma de los números impares menores a 100. ¿Cuántos números impares hay menores
a 100?
"""

print ("Ejercicio 8")
print ("a")
def cuadrado_primeros_10():
    """
    Calcula el cuadrado de los primero 10 numero enteros
    """
    for i in range (10):
        print (f"El cuadrado de {i} es {i**2}")
    
cuadrado_primeros_10()

print ("b")
def suma_entre_0_y_100():
    """
    Calcula la suma de los numeros entre 0 y 100
    """
    suma = 0
    for i in range (101):
        suma += i
    print (f"La suma de los numeros entre 0 y 100 es {suma}")

suma_entre_0_y_100()

print ("c")
def suma_pares_menores_a_100():
    """
    Calcula la suma de los numeros pares menores a 100 y la cantidad de numeros pares menores a 100
    """
    suma = 0
    contador = 0
    for i in range (0, 100, 2): # de 0 a 100 de 2 en 2
        suma += i
        contador += 1
    print (f"La suma de los numeros pares menores a 100 es {suma} y la cantidad de numeros pares es {contador}")

suma_pares_menores_a_100()

print ("d")
def suma_impares_menores_a_100():
    """
    Calcula la suma de los numeros impares menores a 100 y la cantidad de numeros impares menores a 100
    """
    suma = 0
    contador = 0
    for i in range (1, 100, 2): # de 1 a 100 de 2 en 2
        suma += i
        contador += 1
    print (f"La suma de los numeros impares menores a 100 es {suma} y la cantidad de numeros impares es {contador}")

suma_impares_menores_a_100()

print ("Ejercicio 9")
"""
¿Cuál es el problema asociado al siguiente programa? No hace falta ejecutarlo para responder esta
pregunta.
x = 0
while x < 5:
print ( x )
"""
# El problema es que la variable X nunca se incrementa, por lo que el bucle se ejecutara infinitamente, ya que X siempre sera menor a 5
print ("El problema es que la variable X nunca se incrementa, por lo que el bucle se ejecutara infinitamente, ya que X siempre sera menor a 5")

print ("Ejercicio 10")
"""
Escriba un programa que dada una secuencia de números y un valor de umbral vaya sumando los
números de la secuencia hasta que la suma alcance el umbral. Utilice break para terminar la ejecución
del bucle cuando la suma alcance el umbral.
"""

def sumas_hasta_humbral():
    """
    Suma los numeros de una lista hasta que la suma alcance el umbral
    """
    numeros =  [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]
    umbral = 21
    suma = 0
    for numero in numeros:
        suma += numero
        if suma >= umbral:
            break
    print (f"La suma de los numeros es {suma} y el umbral es {umbral}")

sumas_hasta_humbral()

print ("Ejercicio 11")
"""
Escriba un programa que dada una secuencia numérica compute la suma de los números pares. Utilice
un bucle while y la sentencia continue para saltear los casos donde el número no sea par.
"""

def suma_pares_con_continue():
    """
    Suma los numeros pares de una lista usando continue
    """
    numeros = [1 , 2 , 3 , 4 , 5 , 6 , 7, 8 , 9 , 10]
    suma = 0
    i = 0
    while i < len(numeros):
        if numeros[i] % 2 != 0: # Si el numero no es par
            i += 1 # Incrementa el contador 
            continue # Salta a la siguiente iteracion
        suma += numeros[i]
        i += 1
    print (f"La suma de los numeros pares es {suma}")
    
suma_pares_con_continue()

print ("Ejercicio 12")
"""
Escriba un programa que solicite un numero entero al usuario y compute la suma de todos los numeros
naturales menores a él. Este programa debe ser interactivo. Es decir, el programa solicita un numero al
usuario, devuelve la suma, y solicita un nuevo número. Esto continúa así hasta que el usuario ingresa
"salir", determinando que el programa debe terminar. Utilice un bucle while para resolver este
problema. Tenga en cuenta la sentencia break para determinar la interrupción del bucle
"""

def suma_hasta_salir():
    """
    Suma los numeros naturales menores a un numero ingresado por el usuario
    """
    while True:
        numero = input("Ingrese un numero entero o 'salir' para terminar: ")
        if numero.lower() == "salir":
            break
        try:
            numero = int(numero)
            suma = sum(range(numero)) # Suma de los numeros naturales menores a numero
            print (f"La suma de los numeros naturales menores a {numero} es {suma}")
        except ValueError:
            print ("Ingrese un numero entero valido")

        """
        if numero.lower() == "salir":
            break
        else:
            numero = int(numero)
            suma = sum(range(numero)) # Suma de los numeros naturales menores a numero
            print (f"La suma de los numeros naturales menores a {numero} es {suma}")
        """

suma_hasta_salir()

print ("Ejercicio 13")
"""
Una mañana ponés un billete en la vereda al lado del Monumento a la Bandera. A partir de ahí, cada
día vas y duplicás la cantidad de billetes, apilándolos prolijamente. ¿Cuánto tiempo pasa antes de que
la pila de billetes sea más alta que la del Monumento? Considere los siguientes valores para comenzar
a resolver el problema:
"""

def calcular_dias_para_superar_monumento():
    """
    Calcula los dias que tarda en superar el monumento
    """
    altura_monumento = 70 # metros
    billete_grosor = 0.11 * 0.001 # metros
    billetes_n = 1 # cantidad de billetes
    dias = 1 # contador de dias

    while billetes_n * billete_grosor < altura_monumento:
        billetes_n *= 2 # Duplica la cantidad de billetes
        dias += 1 # Incrementa el contador de dias

    print (f"Se necesitan {dias} dias para que la pila de billetes supere el monumento")

calcular_dias_para_superar_monumento()

print ("Ejercicio 14")
"""
Escriba un programa reciba dos números como parámetros, y compute cuántos múltiplos del primero
hay, que sean menores que el segundo.
a. Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
b. Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor
que el segundo.
c. Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?
"""

def contar_multiplos_con_for(primer_numero, segundo_numero):
    """
    Cuenta los multiplos de primer_numero menores que segundo_numero usando for
    """
    contador = 0
    for i in range(primer_numero, segundo_numero, primer_numero):
        contador += 1
    return print (f"La cantidad de multiplos de {primer_numero} menores que {segundo_numero} son: {contador}")

contar_multiplos_con_for(3, 20)

def contar_multiplos_con_while(primer_numero, segundo_numero):
    """
    Cuenta los multiplos de primer_numero menores que segundo_numero usando while
    """
    contador = 0
    i = primer_numero
    while i < segundo_numero:
        contador += 1
        i += primer_numero
    return print (f"La cantidad de multiplos de {primer_numero} menores que {segundo_numero} son: {contador}")

contar_multiplos_con_while(3, 20)

print ("c: Mas clara es WHILE, ya que es mas explicita, y menos operaciones hace el FOR ya que no tiene que contar los pasos")
print ("PD: Si dominas el FOR con RANGE, es mas claro y menos operaciones hace el FOR")