"""
    #RETO 4
    #Nombre: Fernando AVV
    #Fecha: 08/02/2023
    #Descripción: Programa que imprime los números pares en un rago dado por el usuario
"""
n1 = int(input("Ingrese el primer número: ")) #Pide la primera variable
n2 = int(input("Ingrese el segundo número: ")) #Pide la segunda variable
""" Estas dos variables van a hacer un rango de número """
for i in range(n1, n2): #Realiza un ciclo 
    """la variable n1 dice el inicio del ciclo y n2 el fin del ciclo """
    if (i % 2 == 0): #Condiciona que el modulo de un número dividido por dos sea 0
        """Esa quiere decir que el valor es un número par"""
        print(i) #Imprime el valor de i 
        """i guarda los número por los que pasa el ciclo"""
