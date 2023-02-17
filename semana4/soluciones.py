"""
    #Soluciones
    #Nombre: Fernando AVV
    #Fecha: 06/02/2023
    #Descripción: Diferentes formas de hacer el mismo programa
"""

n1 = int(input("Número 1: ")) #Pide el valor de n1
n2 = int(input("Número 2: ")) #Pide el valor de n2

#Solución 1
if n1 > n2: #Condición n1 es mayor que n2
    print(n1) #Imprime n1
if n2 > n1: #Condición n2 es mayor que n1
    print(n2) #Imprime n2
if n1 == n2: #Condición n1 es igual que n2
    print(None) #Imprime None

#Solución 2
if n2 > n1: #Condición n2 es mayor que n1
    print(n2) #Imprime n2
if n1 > n2: #Condición n1 es mayor que n2
    print(n1) #Imprime n1
if n2 == n1: #Condición n2 es igual que n1
    print(None) #Imprime None

    
#Solución 3
if n1 > n2: #Condición n1 es mayor que n2
    print(n1) #Imprime n1
elif n2 > n1: #Condición n2 es mayor que n1
    print(n2) #Imprime n2
else:  #Sino hace lo siguiente
    print(None) #Imprime None
    
#Solución 4
if n1 == n2: #Condición n1 esigual que n2
    print(None) #Imprime None
elif n1 > n2:  #Condición n1 es mayor que n2
    print(n1) #Imprime n1
elif n2 > n1:  #Condición n2 es mayor que n1
    print(n2) #Imprime n2
    
#Solución 5
if n1 < n2: #Condición n1 es menor que n2
    print(n2) #Imprime n2
if n2 < n1: #Condición n2 es menor que n1
    print(n1) #Imprime n1
if n1 == n2: #Condición n1 es igual que n2
    print(None) #Imprime None
    
#Solución 6
if n2 > n1: #Condición n2 es mayor que n1
    print(n2) #Imprime n2
if n2 < n1:  #Condición n2 es menor que n1
    print(n1) #Imprime n1
if n1 == n2: #Condición n1 es igual que n2
    print(None) #Imprime None
#Solución 7
if (n2<n1>n2): #Condición n2 es mayor que n1 y n1 es menor que n2
    print(n1) #Imprime n1
elif (n1<n2>n1): #Condición n1 es mayor que n2 y n2 es menor que n1
    print(n2) #Imprime n2
else: #Si no se cumple has lo siguiente
    print(None) #Imprime None
#Solución 8
if n1 <= n2: #Condición si n1 es menor/igual que n2
    if n1 == n2: #Condición si n1 y n2 son iguales
        print(None) #Imprime None
    else: #Si no se cumple has lo siguiente
        print(n2) #Imprime n2
else: #Si no se cumple has lo siguiente
    print(n1) #Imprime n1
#Solución 9
if n1 >= n2: #Condición si n1 es mayor/igual que n2
    if n1 == n2: #Condición si n1 es igual que n2 
        print(None) #Imprime None
    else: #Si no se cumple has lo siguiente
        print(n1) #Imprime n1
else: #Si no se cumple has lo siguiente
    print(n2) #Imprime n2
#Solución 10
if n1 == n2: #Condición n1 es igual que n2
    print(None) #Imprime None
elif n1 > n2: #Condición si n1 es mayor que n2
    print(n1) #Imprime n1
else: #Si no se cumple has lo siguiente
    print(n2) #Imprime n2
#Solución 11
if n2 != n1: #Condición si n2 es diferente a n1
    if n2 > n1: #Condición si n2 es mayor que n1 
        print(n2) #Imprime n2
    elif n1 > n2: #Condición si n1 es mayor que n2
        print(n1) #Imprime n1
else: #Si no se cumple has lo siguiente
    print(None) #Imprime None

#Solucion 12
if n2 != n1: #Condición si n2 es diferente a n1
    if n1 < n2:  #Condición si n1 es menor que n2
        print(n2) #Imprime n2
    elif n2 < n1: #Condición si n2 es menor que n1
        print(n1) #Imprime n1
else: #Si no se cumple has lo siguiente
    print(None) #Imprime None
