"""
1. Dada una contrase˜na verificar que su longitud es superior a 8 caracteres.
"""
print("Ejercicio 1")

def verificar_contrasena(contrasena):
    """
    Verifica si la longitud de la contrase˜na es superior a 8 caracteres.
    :param contrasena: La contrase˜na a verificar.
    :return: True si la longitud es superior a 8, False en caso contrario.
    """
    return print (len(contrasena) > 8)

verificar_contrasena("12345678") # False, tiene 8 caracteres
verificar_contrasena("123456789") # True, tiene 9 caracteres

"""
2. Escribir un programa que verifique si un n´umero es divisible por 4
"""

print("Ejercicio 2")

def es_divisible_por_4(numero):
    """
    Verifica si un n´umero es divisible por 4.
    :param numero: El n´umero a verificar.
    :return: True si es divisible por 4, False en caso contrario.
    """
    return print (numero % 4 == 0)

es_divisible_por_4(8) # True
es_divisible_por_4(9) # False

"""
3.  Determinar e informar el mayor valor de 3 numeros enteros. ¿Que cambiarias en el algoritmo si se
trataran de 3 numeros reales o de 3 caracteres o de 3 palabras?. ¿Y si se buscara el menor valor?
"""

print("Ejercicio 3")
def mayor_de_tres(a, b, c):
    """
    Determina el mayor de tres numeros enteros.
    :param a: Primer numero.
    :param b: Segundo numero.
    :param c: Tercer numero.
    :return: El mayor de los tres numeros.
    """
    return print (max(a, b, c)) # max() devuelve el mayor de los tres numeros

# Si se tratara de 3 numeros reales, el algoritmo seguiria siendo el mismo, ya que max() funciona con numeros reales.
# Si se tratara de 3 caracteres, el algoritmo seguiria siendo el mismo, ya que max() funciona con caracteres.
# Si se tratara de 3 palabras, el algoritmo seguiria siendo el mismo, ya que max() funciona con palabras.
# Si se buscara el menor valor, se podria usar min() en lugar de max().
mayor_de_tres(1, 2, 3) # 3

"""
4.  Dados 3 lados de un tri´angulo, informar si el mismo es equil´atero, is´osceles o escaleno
"""
print("Ejercicio 4")
def tipo_triangulo(lado1, lado2, lado3):
    """
    Determina el tipo de tri´angulo dado sus lados.
    :param lado1: Primer lado.
    :param lado2: Segundo lado.
    :param lado3: Tercer lado.
    :return: Tipo de tri´angulo (equilatero, isosceles o escaleno).
    """
    if lado1 == lado2 == lado3:
        return print ("Equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return print ("Isosceles")
    else:
        return print ("Escaleno")
    
# Ejemplo de uso
tipo_triangulo(3, 3, 3) # Equilatero
tipo_triangulo(3, 3, 2) # Isosceles
tipo_triangulo(3, 2, 1) # Escaleno

"""
5.  Convertir las calificaciones alfabeticas ‘I’, ‘A’, ‘B’, ‘M’, ‘D’ y ‘E’ en calificaciones numericas 5, 6, 7, 8, 9 y
10 respectivamente. Ingresar una calificacion alfabetica e informar por pantalla la calificacion numerica
correspondiente, en caso de ingresar cualquier otra letra mostrar ((error calificacion inexistente)).
"""
print("Ejercicio 5")

def calificacion_numerica(calificacion):
    """
    Convierte una calificacion alfabetica en calificacion numerica.
    :param calificacion: Calificacion alfabetica.
    :return: Calificacion numerica o mensaje de error.
    """
    if calificacion == 'I':
        return print (5)
    elif calificacion == 'A':
        return print (6)
    elif calificacion == 'B':
        return print (7)
    elif calificacion == 'M':
        return print (8)
    elif calificacion == 'D':
        return print (9)
    elif calificacion == 'E':
        return print (10)
    else:
        return print ("Error, calificacion inexistente")
    
calificacion_numerica("I") # 5 

"""
6.  Escribir un programa que le pregunte a las personas su fecha de cumpleanos y en base a eso imprimir
su signo zodiaco. Recomendacion, pedirle a la persona ingresar la fecha con cierto formato, por ejemplo
DD/MM y si la persona no lo respeta, imprimir un mensaje de error.
"""
print ("Ejercicio 6")

def signo_zodiaco():
    """
    Pregunta la fecha de cumpleanos y determina el signo zodiacal.
    :return: Signo zodiacal o mensaje de error.
    """
    fecha = input("Ingrese su fecha de cumpleanos (DD/MM): ")

    partes = fecha.split("/")
    if len(partes) != 2 or not partes[0].isdigit() or not partes[1].isdigit():
        print("Error: Formato inválido. Use DD/MM.")
        return
    
    dia, mes = map(int, partes)
    
    if mes == 1 and dia >= 20 or mes == 2 and dia <= 18:
        return print ("Acuario")
    elif mes == 2 and dia >= 19 or mes == 3 and dia <= 20:
        return print ("Piscis")
    elif mes == 3 and dia >= 21 or mes == 4 and dia <= 19:
        return print ("Aries")
    elif mes == 4 and dia >= 20 or mes == 5 and dia <= 20:
        return print ("Tauro")
    elif mes == 5 and dia >= 21 or mes == 6 and dia <= 20:
        return print ("Geminis")
    elif mes == 6 and dia >= 21 or mes == 7 and dia <= 22:
        return print ("Cancer")
    elif mes == 7 and dia >= 23 or mes == 8 and dia <= 22:
        return print ("Leo")
    elif mes == 8 and dia >= 23 or mes == 9 and dia <= 22:
        return print ("Virgo")
    elif mes == 9 and dia >= 23 or mes == 10 and dia <= 22:
        return print ("Libra")
    elif mes == 10 and dia >= 23 or mes == 11 and dia <= 21:
        return print ("Escorpio")
    elif mes == 11 and dia >= 22 or mes == 12 and dia <= 21:
        return print ("Sagitario")
    elif mes == 12 and dia >= 22 or mes == 1 and dia <=19:
        return print ("Capricornio")
    else:
        return print ("Error, fecha invalida")
    
#signo_zodiaco() # Ejemplo de uso, ingresar una fecha valida como 15/03 para Piscis o 25/12 para Capricornio


"""
7.  En el centro de la ciudad de Rosario el estacionamiento en via se encuentra tarifado y esta dividido
en tres zonas con tarifas diferenciadas. El vehiculo puede estacionarse como maximo por 3 horas en
el mismo sitio, luego de este tiempo, para renovar el servicio, hay que mover el vehiculo. La siguinte
tabla muestra los costos por hora en cada una de las zonas:
Zona Primer hora Segunda hora Tercer Hora
A $57,00 $71,20 $85,50
B $47,00 $58,70 $70,50
C $37,00 $46,20 $55,50
Escribir un programa que dada la zona, A, B o C, y la cantidad de horas que el vehiculo estara
estacionado, devuelva el costo a pagar. En caso de que el tiempo de estacionamiento supere las 3 horas,
imprimir un mensaje de error acorde.
"""
print("Ejercicio 7")

def costo_estacionamiento(zona, horas):
    """
    Calcula el costo del estacionamiento en base a la zona y horas.
    :param zona: Zona de estacionamiento (A, B o C).
    :param horas: Cantidad de horas estacionado.
    :return: Costo total o mensaje de error.
    """
    if horas > 3:
        return print ("Error: El tiempo de estacionamiento no puede superar las 3 horas.")
    
    if zona == 'A':
        tarifas = [57.00, 71.20, 85.50]
    elif zona == 'B':
        tarifas = [47.00, 58.70, 70.50]
    elif zona == 'C':
        tarifas = [37.00, 46.20, 55.50]
    else:
        return print ("Error: Zona inválida.")
    
    costo_total = tarifas[horas-1] # Se resta 1 porque las listas son 0-indexadas
    return print (f"Costo total: ${costo_total}")

# Ejemplo de uso
costo_estacionamiento('A', 2) # Costo total: $71.20

"""
8. Una marca de ropa tienen descuentos diferentes dependiendo de la sede del local:
Item Rosario Funes Rold´an
Zapatillas 30 % 40 % 25 %
Remeras 20 % 30 % 15 %
Pantalones 10 % 5 % 20 %
Dado un item y la sede del local, devolver el descuento que se recibir´a
"""
print("Ejercicio 8")

def descuento_ropa(item, sede):
    """
    Devuelve el descuento de ropa en base al item y la sede.
    :param item: Item de ropa (Zapatillas, Remeras o Pantalones).
    :param sede: Sede del local (Rosario, Funes o Roldan).
    :return: Descuento correspondiente o mensaje de error.
    """

    # Definimos los descuentos en un diccionario
    # donde la clave es el item y el valor es otro diccionario con las sedes y sus respectivos descuentos
    descuentos = {
        'Zapatillas': {'Rosario': 30, 'Funes': 40, 'Roldan': 25},
        'Remeras': {'Rosario': 20, 'Funes': 30, 'Roldan': 15},
        'Pantalones': {'Rosario': 10, 'Funes': 5, 'Roldan': 20}
    }
    
    if item not in descuentos or sede not in descuentos[item]:  # Verificamos si el item y la sede son válidos, "in" se refiera a si el item o sede se encuentra en el diccionario
        return print ("Error: Item o sede inválida.")
    
    descuento = descuentos[item][sede]

    return descuento

print (f"Descuento: {descuento_ropa('Zapatillas', 'Funes')}%") # Descuento: 40%
print (f"Descuento: {descuento_ropa('Remeras', 'Rosario')}%") # Descuento: 20%


"""
9. Ahora, supongamos que ademas dependiendo del dia de la semana se puede recibir un descuento
adicional acumulable. Es decir, si se recibio un descuento del 10 % segun el item y la sede y la compra
se realiza un lunes, el descuento total sera un 20 % . Escribir un programa en el que la persona pueda
ingresar el dia de la semana, el item a comprar y la sede del local. Luego, informar el descuento total
a recibir. Utilizar la siguiente tabla de descuentos
Lunes Miercoles Jueves
Descuento 10 % 8 % 5 %
"""

def descuento_adicional(dia, item, sede):
    """
    Devuelve el descuento total en base al dia, item y sede.
    :param dia: Dia de la semana (Lunes, Martes, Miercoles, Jueves, Viernes, Sabado o Domingo).
    :param item: Item de ropa (Zapatillas, Remeras o Pantalones).
    :param sede: Sede del local (Rosario, Funes o Roldan).
    :return: Descuento total correspondiente o mensaje de error.
    """
    
    # Descuentos adicionales en un diccionario
    descuentos_adicionales = {
        'Lunes': 10,
        'Miercoles': 8,
        'Jueves': 5
    }
    
    # Obtener el descuento del item y la sede
    descuento_item = descuento_ropa(item, sede)
        
    if dia not in descuentos_adicionales:  # Verificamos si el dia es válido
        extra = 0
    else:
        extra = descuentos_adicionales[dia]
    

    descuento_total = descuento_item + extra  # Sumar el descuento del item y el descuento adicional
    
    return print (f"Descuento total: {descuento_total}%")


descuento_adicional('Lunes', 'Zapatillas', 'Funes') # Descuento total: 50%
descuento_adicional('Martes', 'Zapatillas', 'Funes') # Descuento total: 40% - No hay descuento adicional
descuento_adicional('Miercoles', 'Remeras', 'Rosario') # Descuento total: 28%