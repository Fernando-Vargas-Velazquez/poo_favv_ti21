"""
    #Soluciones
    #Nombre: Fernando AVV
    #Fecha: 09/02/2023
    #Descripción: Funciones con def Parte 2
"""


def mayor(numero1: int, numero2: int) -> int: #define la función "mayor"
    result = None #Crea la variable result y define como None
    if numero1 > numero2: #Condición que dice que si numero 1 es mayor que numero2 
        result = numero1 #Va a definicr el valor de relut como numero1
    elif numero2 > numero1: #Condición que dice que si numero2 es mayor que numero1 
        result = numero2 #va a definir result como numero2
    return result  #Va a retornar el valor de result


print(mayor(2, 1))  #2
print(mayor(1, 2))  #2
print(mayor(2, 2))  #None
print(mayor(2, -1))  #2
print(mayor(-1, 2))  #2
print(mayor(-1, -1))  #None
print(mayor(-2, -1))  #-1
print(mayor(-1, -2))  #-1
