"""
    #Programa 3
    #Nombre: Fernando AVV
    #Fecha: 24/01/2023
    #Descripción: Format y operaciones aridméticas
"""
numero1 = 10 #Se crea la variable numero1
numero2 = 5 #Se crea la variable numero2

print(numero1 + numero2)#Este print imprimira el número 15

print("{}+{}". format(numero1, numero2))#Este print imprimira 10+5

print("{}+{}=". format(numero1, numero2) , (numero1+numero2))#Este print imprimira 10+5=15

print((numero1*numero2),"=", "{}*{}". format(numero2, numero1) )#Este print imprimira 50 = 2*10

print("El resultado de dividir:","{}/{}". format(numero1, numero2) ,"es", (numero1/numero2))#Este print imprimira "El resultado de dividir: 10/5 es 2"
