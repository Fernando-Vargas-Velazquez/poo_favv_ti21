"""
    #Programa 6
    #Nombre: Fernando AVV
    #Fecha: 30/01/2023
    #Descripción: Aplicación que permite calcular el area y el perimetro de un triangulo
"""
print("----------------------------------------") #Imprime texto
print("Ingrese 1 si el triangulo es Equilátero") #Imprime texto
print("Ingrese 2 si el triangulo es Isósceles") #Imprime texto
print("Ingrese 3 si el triangulo es Escaleno") #Imprime texto
print("----------------------------------------") #Imprime texto
tipo = input("Ingrese el tipo de triangulo: ") #Pide el tipo de triangulo

if tipo == "": #Condiciona si el campo esta vacío
  print("Campo vacío") #Imprime texto
else: #Condición sino
  if tipo == "1": #Condiciona si el campo es 1 
    print("Triangulo Equilátero") #Imprime texto
    a = float(input("Ingresa el valor de a (lado): ")) #Pide el valor de su lado
    h = float(input("Ingresa el valor de h (altura): ")) #Pide el valor de su altura
    print("___________________________________") #Imprime texto
    per = a*3 #Calcula el perímetro
    print("El perímetro es: " , a , "* 3 =",per) #Imprime el valor de perímetro
    area = (a*h)/2 #Calcula el área
    print("El área es: ",a,"",h,"/2 =",area) #Imprime el valor de área
  else: #Condición sino
    if tipo == "2": #Condiciona si el campo es 2
      print("Triangulo Isósceles") #Imprime texto
      a = float(input("Ingresa el valor de a (hipotenusa): ")) #Pide el valor de la hipotenusa 
      b = float(input("Ingresa el valor de b (base): ")) #Pide el valor de la base
      h = float(input("Ingresa el valor de h (altura): ")) #Pide el valor de la altura 
      print("___________________________________") #Imprime texto
      per = a*2+b #Calcula el perímetro
      print("El perímetro es: " , a , "* 2 +", b, "=" ,per) #Imprime el perímetro
      area = (b*h)/2 #Calcula el área
      print("El área es: ",b,"*",h,"/2 =",area) #Imprime el área
    else: #Condición sino
      if tipo == "3": #Condiciona si el campo es 3
        print("Triangulo Escaleno") #Imprime texto
        a = float(input("Ingresa el valor de a (lado): ")) #Pide el valor del lado
        b = float(input("Ingresa el valor de b (base): ")) #Pide el valor de la base
        c = float(input("Ingresa el valor de c (lado): ")) #Pide el valor del lado
        h = float(input("Ingresa el valor de h (altura): ")) #Pide el valor de altura
        print("___________________________________") #Imprime texto
        per = a+b+c #Calcula el perímetro
        print("El perímetro es: " , a , "+", b ,"+", c, "=" ,per) # Imprime el valor de el perímetro
        area = (b*h)/2 #Calcula el área
        print("El área es: ",b,"*",h,"/2 =",area) #Imprime el valor del área
      else: #Condición sino
        print("Caracter no valido") #Imprime una alerta
