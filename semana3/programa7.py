"""
    #Programa 7
    #Nombre: Fernando AVV
    #Fecha: 31/01/2023
    #Descripción: Aplicación que permite cacular el area de un círculo y un cuadrado
"""
print("Ingresa un número") #Imprime texto
print("Ingresa 1 si tu figura es un círculo")#Imprime texto
print("Ingresa 2 si tu figura es un cuadrado")#Imprime texto

tipo = input("Ingresa número: ") #Pide el tipo de figura 

if tipo == "": #condiciona si el campo esta vacío
  print("Ingresa un valor") #Si el campo esta vacío imprime un mensaje de alerta
else: #Condición SiNo
  if tipo == "1": #condiciona que el valor de tipo sea 1 
    print("Figura CÍRCULO") # si el valor es 1 va a imprimir un mensaje 
    radio = float(input("Ingrese el tamaño del radio: ")) #pide el tamaño del radio
    area = 3.1416 * radio**2 # cacula el área
    per=2*3.1416*radio # calcula el perímetro
    print("El área de un círculo de: ",radio, "de radio es: ",area)# imprime el valor del área
    print("El perímetro de un círculo de: ",radio, " de radio es:", per) #Imprime el valor del perímetro
  else: #Condición SiNo
    if tipo == "2": #condiciona que el tipo sea 2
      print("Figura CUADRADO") # si el valor es 2 se imprime un mensaje 
      lado = float(input("Ingrese el tamaño del lado: ")) #Pide el tamaño de el lado del cuadrado
      area = lado*lado #Calcula el área
      per=lado*4 #Calcula el perímetro
      print("El área de un cuadrado de: ",lado, "como tamaño de un lado es: ",area) #imprime el valor del área
      print("El perímetro de un cuadrado de: ",lado, " como tamaño del lado es: ", per)#Imprime el valor del perímetro
    else: #Condición SiNo
      print("Caracter no valido") #Imprime un mensaje de alerta
  