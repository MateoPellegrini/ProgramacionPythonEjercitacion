print ("Ejercicio 1")
"""
Dada una lista de números list y un número n, determine en qué índice de la lista list se
encuentra el número n. En caso de no encontrarlo, el programa mostrará -1. 
"""
print ("a")
list =  [11 ,25 ,3 , -4 ,95]
def encontrar_indice(list, n):
    """
    Función que encuentra el índice de un número en una lista.
    :param lista: Lista de números
    :param n: Número a buscar
    :return: Índice del número en la lista o -1 si no se encuentra
    """
    if n in list:
        for i in range(len(list)): # Recorre la lista
            if list[i] == n:
                return print(i) # Devuelve el índice del número
    else:
        return print(-1) # Devuelve -1 si no se encuentra el número
    
encontrar_indice(list, 3) # 2
encontrar_indice(list, 100) # -1

print ("b")
"""
Dada una lista de números, calcule el mínimo y el máximo de la lista. Nota: es posible hacerlo
recorriendo una única vez la lista o recorriéndola dos veces. Piense las ventajas y desventajas de
ambos métodos
"""

print (" Las ventajas de recorrer la lista una sola vez son: " \
        "\n Mas efeciente." \
        "\n Las desventajas son: \n Mas complejo para escribir" \
        "\n Las ventajas de recorrer la lista dos veces son: " \
        "\n Simple de razonar ya que realiza una cosa por vez (primero el minimo y despues el mayor) " \
        "\n Las desventajas son: \n Menos eficiente")
def min_max(list):
    """
    Función que encuentra el mínimo y máximo de una lista.
    :param lista: Lista de números
    :return: Mínimo y máximo de la lista
    """
    min = list[0] 
    max = list[0]
    for i in range(len(list)):
        if list[i] < min: 
            min = list[i] 
        if list[i] > max: 
            max = list[i]
    return print(f"Minimo: {min}\nMaximo: {max}") 

    # Con MAX y MIN, se podria hacer en una sola linea:  print (min(list), max(list))

min_max(list) # -4 95

print ("c")
"""
Dada una lista de números, cree una nueva lista sumando 1 a cada elemento.
"""
def sumar_1(list):
    """
    Función que suma 1 a cada elemento de una lista.
    :param lista: Lista de números
    :return: Nueva lista con cada elemento incrementado en 1
    """
    nueva_lista = []
    for i in range(len(list)):
        nueva_lista.append(list[i] + 1) # Suma 1 a cada elemento y lo agrega a la nueva lista
    return print(nueva_lista)

print (" La lista original es: ", list)
sumar_1(list) # [12, 26, 4, -3, 96]

print ("d")
"""
Dada una lista palabras de cadenas de texto, devuelva una nueva lista formada sólo por las
cadenas de palabras que empiezan con "a".
"""
def filtrar_palabras(list):
    """
    Función que filtra palabras que empiezan con "a" de una lista.
    :param lista: Lista de cadenas de texto
    :return: Nueva lista con palabras que empiezan con "a"
    """
    nueva_lista = []
    for i in range(len(list)):
        if list[i].startswith("a"): # Verifica si la palabra empieza con "a"
            nueva_lista.append(list[i])

        """
        Alternativa se puede hace de una forma mas simple:
        if list[i][0] == "a":
            nueva_lista.append(list[i])
        """
    return print(nueva_lista)

filtrar_palabras(["arbol", "casa", "auto", "perro", "gato", "avion"]) # ['arbol', 'auto', 'avion']

print ("e")
"""
Dada una lista de números, calcule, por un lado, la suma de los elementos que se encuentran en
un índice par en la lista y, por otro lado, el producto de los elementos de posiciones con índice
impar.
"""
def suma_producto(list):
    """
    Función que calcula la suma de elementos en índices pares y el producto de elementos en índices impares.
    :param lista: Lista de números
    :return: Suma de elementos en índices pares y producto de elementos en índices impares
    """
    suma = 0
    producto = 1
    for i in range(len(list)):
        if i % 2 == 0:
            suma += list[i]
        else:
            producto *= list[i]
    return print(f"Suma de indices pares: {suma}\nProducto de indices impares: {producto}")

suma_producto([11, 25, 3, -4, 95]) # Suma de indices pares: 109 Producto de indices impares: -100

print ("f")
"""
Dada una lista cualquiera, cree una nueva lista con los mismos elementos pero en el orden inverso
"""
def invertir_lista(list):
    """
    Función que invierte una lista.
    :param lista: Lista de números
    :return: Nueva lista con los elementos en orden inverso
    """
    nueva_lista = list[::-1] # slicing inverso, start:stop:step -> inicio, fin, pasos, por defecto esta como 0:0:0 pero al poner 0:0:-1 recorre la lista hacia atras
    """
    Mas facil usar un for
    range(start, stop, step)
    start -> cantidad de elementos - 1
    stop -> -1
    step -> -1 
    for i in range(len(list)-1, -1, -1): # Recorre la lista al reves
    nueva_lista.append(list[i])
    """

    return print(nueva_lista)

invertir_lista(["arbol", "casa", "auto", "perro", "gato", "avion"]) # ['avion', 'gato', 'perro', 'auto', 'casa', 'arbol']