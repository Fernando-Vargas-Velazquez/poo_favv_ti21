"""
    #RETO 2
    #Nombre: Fernando AVV
    #Fecha: 04/02/2023
    #Descripción: Programa que calcula tu edad
"""
print("Programa que calcula tu edad") #Imprime texto
a_N = int(input("Ingresa el año en el que naciste: ")) #Pide la variable a_N que es el año de nacimiento
a_A = int(input("Ingresa el año actual: ")) #Pide la variable a_A que es el año actual

edad = a_A - a_N #Calcula la edad

print("Tu edad es: ",edad,"Años") #Imprime la edad que tienes

if int(edad) >=18: #Condición si edas es mayoy o igual a 18
    print("Eres mayor de edad") #Imprime mensaje si es mayor de edad
else: #SiNo es mayor
    print("Eres menor de edad") #Si no es mayor imprime el mansaje 
