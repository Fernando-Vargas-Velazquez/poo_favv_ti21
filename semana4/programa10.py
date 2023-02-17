"""
    #Soluciones
    #Nombre: Fernando AVV
    #Fecha: 09/02/2023
    #Descripción: Funciones con def Parte 1
"""


def mayor(numero1, numero2): #define una función "mayor"
    result = None # se crea la variable result con un valor de None
    if numero1 > numero2: #Condición que dice si numero1 es mayor que numero2
        result = numero1 #Si se cumple la condición cambia el valor de result a numero1
    elif numero2 > numero1: #Condición que dice si numero2 es mayor a numero1
        result = numero2 #Si se cumple la condición cambia el valor de result por el numero2
    return result #Retorna result


print(mayor(2, 1))  #2
print(mayor(1, 2))  #2
print(mayor(2, 2))  #None
print(mayor(2, -1))  #2
print(mayor(-1, 2))  #2
print(mayor(-1, -1))  #None
print(mayor(-2, -1))  #-1
print(mayor(-1, -2))  #-1
