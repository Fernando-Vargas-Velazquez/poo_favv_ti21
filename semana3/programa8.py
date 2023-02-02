"""
    #Programa 8
    #Nombre: Fernando AVV
    #Fecha: 1/02/2023
    #Descripción: Estructura de las condicionales if, elif y else
"""

"""
  op = 3
  if op == 2:
    print("Hola 2")
  elif op == 3:
    print("Hola 3")
  else:
    print("Hola?")
    
===============================================
  1.-Operadores Aritméticos
   + - / * // % **

   2.- Operadores de asignación
   =, +=, -=, /= , *=, //=, %=, **=

   3.- Operadores de comporación
   >, <, >=, !=, ==

   4.- Operadores lógicos
   and, or, not

   5.- Operadores de membrecia (membuship)
   in, not in
"""

num1 = int(input("Ingresa el primer número: ")) #ingresa el primer número
num2 = int(input("Ingrese el segundo número: ")) #ingresa el segundo número

if num1 < num2 : #Condiciona si num2 es mayor que num1 
    print(num2) #Imprime el num2
elif num2 < num1 : #Condiciona si num1 es mayor que num2
    print(num1) # imprime el num1
elif num1 == num2: #Condiciona si son iguales
    print(None) #imprime none
    
