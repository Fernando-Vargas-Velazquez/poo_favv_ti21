"""
    #Soluciones
    #Nombre: Fernando AVV
    #Fecha: 06/02/2023
    #Descripción: Diferentes formas de hacer el mismo programa
"""

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

#Solución 1
if n1 > n2:
    print(n1)
if n2 > n1:
    print(n2)
if n1 == n2:
    print(None)

#Solución 2
    """
if n2 > n1:
    print(n2)
if n1 > n2:
    print(n1)
else:
    print(None)
    """
if n2 > n1:
    print(n2)
if n1 > n2:
    print(n1)
if n2 == n1:
    print(None)

    
#Solución 3
if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
else:
    print(None)
    
#Solución 4
if n1 == n2:
    print(None)
elif n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
    
#Solución 5
if n1 < n2:
    print(n2)
if n2 < n1:
    print(n1)
if n1 == n2:
    print(None)
    
#Solución 6
    """"
if n2 > n1:
    print(n2)
if n2 < n1:
    print(n1)
else:
    print(None)
    """
if n2 > n1:
    print(n2)
if n2 < n1:
    print(n1)
if n1 == n2:
    print(None)
#Solución 7
if (n2<n1>n2):
    print(n1)
elif (n1<n2>n1):
    print(n2)
else:
    print(None)
#Solución 8
if n1 <= n2:
    if n1 == n2:
        print(None)
    else:
        print(n2)
else:
    print(n1)
#Solución 9
if n1 >= n2:
    if n1 == n2:
        print(None)
    else:
        print(n1)
else:
    print(n2)
#Solución 10
if n1 == n2:
    print(None)
elif n1 > n2:
    print(n1)
else:
    print(n2)
#Solución 11
if n2 != n1:
    if n2 > n1:
        print(n2)
    elif n1 > n2:
        print(n1)
else:
    print(None)

#Solucion 12
if n2 != n1:
    if n1 < n2:
        print(n2)
    elif n2 < n1:
        print(n1)
else:
    print(None)
