"""
    #Programa 6
    #Nombre: Fernando AVV
    #Fecha: 30/01/2023
    #Descripción: Aplicación que permite calcular el area y el perimetro de un triangulo
"""
print("----------------------------------------")
print("Ingrese 1 si el triangulo es Equilátero")
print("Ingrese 2 si el triangulo es Isósceles")
print("Ingrese 3 si el triangulo es Escaleno")
print("----------------------------------------")
tipo = input("Ingrese el tipo de triangulo: ")

if tipo == "":
  print("Campo vacío")
else:
  if tipo == "1":
    print("Triangulo Equilátero")
    a = float(input("Ingresa el valor de a (lado): "))
    h = float(input("Ingresa el valor de h (altura): "))
    print("___________________________________")
    per = a*3
    print("El perímetro es: " , a , "* 3 =",per)
    area = (a*h)/2
    print("El área es: ",a,"*",h,"/2 =",area)
  else:
    if tipo == "2":
      print("Triangulo Isósceles")
      a = float(input("Ingresa el valor de a (hipotenusa): "))
      b = float(input("Ingresa el valor de b (base): "))
      h = float(input("Ingresa el valor de h (altura): "))
      print("___________________________________")
      per = a*2+b
      print("El perímetro es: " , a , "* 2 +", b, "=" ,per)
      area = (b*h)/2
      print("El área es: ",b,"*",h,"/2 =",area)
    else:
      if tipo == "3":
        print("Triangulo Escaleno")
        print("Triangulo Isósceles")
        a = float(input("Ingresa el valor de a (lado): "))
        b = float(input("Ingresa el valor de b (base): "))
        c = float(input("Ingresa el valor de c (lado): "))
        h = float(input("Ingresa el valor de h (altura): "))
        print("___________________________________")
        per = a+b+c
        print("El perímetro es: " , a , "+", b ,"+", c, "=" ,per)
        area = (b*h)/2
        print("El área es: ",b,"*",h,"/2 =",area)
      else:
        print("Caracter no valido")
