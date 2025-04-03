#Ejercicio 1
"""
print ( saludo + " " + destino + puntuacion )
saludo = " Hola "
destino = " Mundo "
puntuacion = "!"
"""
# A la hora de ejecutar el print, se produce un error porque las variables no han sido definidas antes de ser utilizadas. (Primero se definen y luego se utilizan)
"""
cateto1 = 3
cateto2 = 4
hipotenusa = (( cateto1 ** 2) + ( cateto2 ** 2)) ** 0.5
del cateto1
del cateto2
print ( hipotenusa )
"""
# En este caso no se produce error porque las variables cateto1 y cateto2 han sido definidas antes de ser utilizadas.
"""
del tengo_hambre
tengo_hambre = False
del tengo_hambre
tengo_hambre = True
"""
# En este caso, al inicio se quiere borrar una variable que no ha sido definida, por lo que se produce un error.

# Ejercicio 2
"""
En Python podemos usar el operador == para preguntarnos si dos cosas son iguales o no. Si a == b
nos devuelve True, entonces a y b se consideran iguales. En otro caso nos devolverá False. Verificar
qué pares de las siguientes expresiones son iguales:

a. 3
b. 3.0
c. (0.1 + 0.2) * 10
d. 22 / 7
e. 22 // 7 #Redondea hacia abajo
"""
a = 3
b = 3.0 # 3.0 o 3
c = (0.1 + 0.2) * 10 # 3.0000000000000004
d = 22 / 7 # 3.142857142857143
e = 22 // 7 # 3


# Ejercicio 3
"""
¿Cuáles son las diferencias y similitudes entre las siguientes expresiones?
a. 1) 10 + 5
2) 10 + 5.0
3) 10 + 5.
b. 1) 11 / 2
2) 11 // 2
3) 11.0 // 2

print (10 + 5) # 15 Entero
print (10 + 5.0) # 15.0 Decimal
print (10 + 5.) # 15.0 Decimal

print (11 / 2) # 5.5 Decimal
print (11 // 2) # 5 Entero
print (11.0 // 2) # 5.0 Decimal | Redondea hacia abajo
"""

# Ejercicio 4
"""
En Python los operadores de suma y de resta, + y -, pueden ser utilizados con un único argumento (u
operando). Ejecutar cada una de las siguientes expresiones e interpretar los resultados.
a. +1
b. -1
c. +-1
d. –1
print (+1) # 1
print (-1) # -1
print (+-1) # -1
print (-1) # -1
"""

# Ejercicio 5
print ("Ejercicio 5")
"""
Modelar los siguientes problemas, nombrando los datos relevantes y el resultado, junto con la forma
que tendrán sus representaciones internas en Python. Luego programar la solución
"""

"""
a. Se tienen DOS HABITACIONES dentro de un hogar, CADA una con una TEMPERATURA AMBIENTE. Se quiere
saber a qué temperatura estarán las habitaciones, dado suficiente tiempo para que se transmita
el calor de una a la otra. Se conoce que en este caso es válido promediar temperaturas.
"""

print ("a")
def temperatura_equilibrio(temperatura1, temperatura2):
    """
    Esta función calcula la temperatura de equilibrio entre dos habitaciones.
    :param temperatura1: Temperatura de la primera habitación.
    :param temperatura2: Temperatura de la segunda habitación.
    :return: Temperatura de equilibrio.
    """
    promedio = (temperatura1 + temperatura2) / 2
    return print (f" La temperatura promedio de las habitaciones sera de: {promedio}")

# Ejemplo de uso
temp1 = 22.5
temp2 = 25.0
temperatura_equilibrio(temp1, temp2)
"""
b. Se tiene una MULTITUD afuera, CADA PERSONA le dirá su nombre a cada otra persona en la multitud. Se quiere saber CUANTO TIEMPO llevará hacer esto, dado que decir una vez tu nombre lleva
aproximádamente 4 segundos y medio.
"""
print ("b")

def tiempo_multitud(multitud):
    """
    Esta función calcula el tiempo total que llevará a todas las personas en la multitud decir su nombre.
    :param multitud: Número de personas en la multitud.
    :return: Tiempo total en segundos.
    """
    tiempo_por_persona = 4.5  # segundos
    tiempo_total = (multitud * (multitud - 1)) * tiempo_por_persona / 2
    # Se itera sobre cada persona y se multiplica por el tiempo que tarda en decir su nombre
    # Combinaciones de 2 personas
    # Se divide por 2 porque cada combinación se cuenta dos veces (A dice el nombre de B y B dice el nombre de A)
    return print (f" El tiempo total para que todas las personas digan su nombre sera de: {tiempo_total} segundos")

# Ejemplo de uso
tiempo_multitud(10)  # Ejemplo con 10 personas
"""
c. Hay DOS PERSONAS con nombres muy largos, pero similares. Se quiere conocer, por un lado, si tienen
el MISMO TAMAÑO, y por otro lado si son IGUALES. Ayuda para el programa: buscar la función len
"""
print ("c")
def comparar_nombres(nombre1, nombre2):
    """
    Esta función compara dos nombres y determina si tienen el mismo tamaño y si son iguales.
    :param nombre1: Primer nombre.
    :param nombre2: Segundo nombre.
    :return: Tupla con resultados de comparación.
    """
    mismo_tamano = len(nombre1) == len(nombre2)
    son_iguales = nombre1 == nombre2
    return print (f" Los nombres son iguales: {son_iguales} \n Tienen el mismo tamaño: {mismo_tamano}")

# Ejemplo de uso
nombre1 = "Juan Carlos"
nombre2 = "Juan Carlos"
comparar_nombres(nombre1, nombre2)  # Ejemplo con nombres iguales

# Ejercicio 6
"""
Traducir las siguientes expresiones del lenguaje natural a expresiónes booleanas en equivalentes en
Python. Determinar su veracidad o falsedad corriendo la expresión en el intérprete.
a. La longitud de la cadena "Hola, mundo" es 14.
b. El área de un cuadrado de lado 5 es igual a la raíz cudrada de 625.
c. El diametro de un circulo de radio 3,25 es menor que 7 y mayor a 6.
d. La apromixación de Pi = 22 / 7 es un número mayor que 3, y 2 + 2 es igual a 5.
e. El numero 10 es mayor a 5 o 0 dividido 0 es igual 0.
f. La cadena "Python" tiene longitud 5 y 1+"1" es igual a 2.
"""

print ("Ejercicio 6")
print ("a")
print (len("Hola, mundo") == 14) # False, es 11 ya que se cuentan los espacios y la coma
print ("b")
print (5 ** 2 == 625 ** 0.5) # True, 25 == 25, se puede usar la funcion pow(5,2) o 5**2 o para la raiz math.sqrt() o 625**(1/2)
print ("c")
print (3.25 * 2 < 7 and 3.25 * 2 > 6) # True, el diametro es 6.5
print ("d")
print (22 / 7 > 3 and 2 + 2 == 5) # False, ya que 2 + 2 es igual a 4
print ("e")
print (10 > 5 or 0 / 0 == 0) # True, ya que 10 es mayor a 5
print ("f")
print (len("Python") == 5 and 1 + int("1") == 2) # False, ya que la longitud de Python es 6 y 1 + 1 es igual a 2
                                                 # (1 + "1")  Esto produce un error ya que no se puede sumar un entero y una cadena de texto

# Ejercicio 7
"""
Poner paréntesis en las siguientes expresiones de acuerdo a las reglas de precedencia y asociatividad
de los operadores. Si no conoce la precedencia de algún operador, se aconseja probarla primero en
el intérprete. Una vez hecho esto, determinar el tipo de cada subexpresión entre paréntesis hasta
determinal el tipo de la expresión completa.
a. 3 * 5 - 7 * 4 / 14 + 3 / 1
b. 2 ** 1 + 3 / 5 // 4
c. 8 / 4 / 2 ** 2 ** 2
"""
print ("Ejercicio 7")
print ("a")
print ("(3∗5)−((7∗4)/14)+(3/1)")
print (3 * 5 - (7 * 4) / 14 + (3 / 1)) # 15 - 2 + 3 = 16.0
print ("b")
print ("(2∗∗1)+((3/5)//4)")
print (2 ** 1 + (3 / 5) // 4) # 2 + 0.0 = 2.0
print ("c")
print ("8/4/(2∗∗(2∗∗2))")
print (8 / 4 / (2 ** (2 ** 2))) # 8 / 4 / 16 = 0.125