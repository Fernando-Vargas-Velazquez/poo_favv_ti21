"""
    #RETO 3
    #Nombre: Fernando AVV
    #Fecha: 05/02/2023
    #Descripción: Programa que dice cual el número mayor de dos números
"""
num1 = input("Ingresa el primer númer: ") #Pide la primera variable 
num2 = input("Ingresa el segundo número: ") #Pide la segunda variable

if int(num1) == int(num2): #Condición si num1 es igual a num2
    print("Los números ", num1, "y", num2, "SON IGUALES") #Salida de mensaje
elif int(num1) > int(num2): #Si no si num1 es mayor que num2
    print(num1," Es mayor que ",num2) #Salida de mensaje
elif int(num1) < int(num2): #Si no si num2 es mayor que num1
    print(num2, " Es mayor que ",num1)
