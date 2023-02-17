"""
    #Soluciones
    #Nombre: Fernando AVV
    #Fecha: 13/02/2023
    #Descripción: Clase persona
"""
class Persona: #Se crea la clase Persona
    __nombre = None #Variable __nombre
    __email = None #Variable __email

    def __init__ (self): #Constructor de la clase persona
        print("Persona: ") #Imprime texto
    
    def setNombre(self,nombre): #Función set
        self.__nombre = nombre #Modifica nombre
    
    def getNombre(self): #Función get
        return self.__nombre #Retorna __nombre
    
    def setEmail(self,email): #Función set 
        self.__email = email #Mustra nombre
    
    def getEmail(self):  #Función get
        return self.__email #Retorna __email
    
dejah = Persona() #Persona
dejah.setNombre('Dejah') #Set permite modificar
print(dejah.getNombre()) #Get permite mostrar
dejah.setEmail('dejah@utectulancingo.edu.mx') #Set permite modificar
print(dejah.getEmail()) #Get permite mostrar

john=Persona() #Crea otra persona
print(john.getNombre()) #Imprime nombre que es None

carthoris = Persona() #Crea otra persona
carthoris.setNombre("Carthoris") #Modifica el nombre
print(carthoris.getNombre()) # Imprime el nombre
carthoris.setEmail('carthoris@utectulancingo.edu.mx') #Set permite modificar
print(carthoris.getEmail()) #Get permite mostrar

nando = Persona() #Crea otra persona
nando.setNombre("Nando") #Modifica el nombre
print(nando.getNombre()) #Imprime el nombre
nando.setEmail("Nando@gmail.com") #Modifica el email
print(nando.getEmail()) #Imprime el email
