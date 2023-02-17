"""
    #Programa 4
    #Nombre: Fernando AVV
    #Fecha: 26/01/2023
    #Descripción: Suma de dos número utiliznado dos variables en (format)
"""

numero1 = 10 #primera variable
numero2 = 5 #segunda variable

print("{}+{}={}". format(numero1, numero2, numero1 + numero2)) #sentencia que imprime 10+5=15

print("{n1}+{n2}={suma}". format(n1=numero1, n2=numero2, suma =numero1+numero2)) #sentencia que imprime 10+5=15

print("{n2}+{n2}={n2}". format(n1=numero1, n2=numero2, suma =numero1+numero2)) #sentencia que imprime 5+5=5
"""
    No se puede cambiar las variables que estan entre {} no se pueden repetir
"""

print("{numero1}+{numero2}={suma}". format(numero1=numero1, numero2=numero2, suma =numero1+numero2)) #sentencia que imprime 10+5=15 pero con una forma diferente de resolverlo

