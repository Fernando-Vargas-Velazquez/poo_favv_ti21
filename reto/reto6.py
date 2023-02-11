"""
    #Soluciones
    #Nombre: Fernando AVV
    #Fecha: 10/02/2023
    #Descripción: Aplica descuentos dados dados por el usuario
"""
precio = int(input("Ingrese precio del producto: ")) #Ingresa el precio del producto
por = int(input("Ingresa el descuento que quiere realizar: ")) #Ingresa el descuento
des = (precio * por) / 100 #Calcula el descuento
total = precio - des #Calcula el total
print("El precio del producto es: $", precio) #Imprime mensaje
print("Se aplico el:",por,"% de descuento") #Imprime mensaje
print("El descuento es de: $",des)
print("El precio final del producto es :$", total) #Imprime mensaje
