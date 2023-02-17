"""
    #Soluciones
    #Nombre: Fernando AVV
    #Fecha: 14/02/2023
    #Descripción: Clases heredadas
"""
class Persona: #Clase persona
    __nombre = None #Creación de la variable __nombre
    __edad = None #Creación de la variable __edad
    
    def __init__ (self): #Función init llamada a la clase
        print("Persona") #Imprime persona
    
    def setNombre(self,nombre): #Función set perimite modificar el valor
        self.__nombre = nombre #Modifica nombre

class Alumno(Persona): #Alumno hereda persona
    __nombre = None  #Creación de la variable __nombre
    __matricula = None  #Creación de la variable __matricula
    def __init__ (self): #Función init llamada a la clase
        super().__init__() #Llamada a la superclase
        print("Alumno") #imprime alumno

objeto_persona = Persona() #llama a la función persona
objeto_alumno = Alumno() #llama a la función alumno


print(dir(objeto_persona)) #Muestra los metodos de la clase
print(dir(objeto_alumno)) #Muestra los metodos de la clase
