"""
    #Programa 1 (El reto)
    #Nombre: Fernando AVV
    #Fecha: 03/02/2023
    #Descripción: Calculadora con diferentes operadores
"""

print("Calculadora con diferentes operadores") #Imprime texto
print("-------------------------------------") #Imprime texto
print("Ingresa 1 si quieres sumar") #Imprime texto
print("Ingresa 2 si quieres restar") #Imprime texto
print("Ingresa 3 si quieres multiplicar") #Imprime texto
print("Ingresa 4 si quieres dividir") #Imprime texto
print("-------------------------------------") #Imprime texto

operador = input("¿Qué operación quieres hacer?: ") #Es la acción que quiere realizar
if operador == "": #Condición si el operador esta vacío
    print("No valido") #Imprime un mensaje de alerta
else: #SiNo se cimple la condición va a realizar otra cosa
    if int(operador) <= 0 or int(operador) >= 5: #Condición si el operador es diferente a los pedidos
        print("No valido") #Imprime un mensaje de alerta
    else:  #SiNo se cimple la condición va a realizar otra cosa
        num1 = int(input("Ingresa el primer número: ")) #Pide la variable num1
        num2 = int(input("Ingresa el segundo número: ")) #Pide la variable num2
        if int(operador) == 1: #Condición si el operador es igual a 1
            print("Realiza Suma de:",num1, "+",num2) #Mensaje de lo que se va ahacer
            sum = num1 + num2 #Realiza la operación
            print("El resultado de la suma es: ",sum) #Imprime el resultado de la operación
        elif int(operador) == 2: #Condición si el operador es igual a 2
            print("Realiza Resta de:",num1, "-",num2) #Mensaje de lo que se va ahacer
            res = num1 - num2 #Realiza la operación
            print("El resultado de la resta es: ",res) #Imprime el resultado de la operación
        elif int(operador) == 3:
            print("Realiza Multiplicación de:",num1, "*",num2) #Mensaje de lo que se va ahacer
            mul = num1 * num2 #Realiza la operación
            print("El resultado de la multiplicación es: ",mul) #Imprime el resultado de la operación
        elif int(operador) == 4:
            print("Realiza División de:",num1, "/",num2) #Mensaje de lo que se va ahacer
            div = num1 / num2 #Realiza la operación
            print("El resultado de la resta es: ",div) #Imprime el resultado de la operación
