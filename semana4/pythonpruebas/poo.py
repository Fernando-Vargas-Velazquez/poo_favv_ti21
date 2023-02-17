"""
    #Soluciones
    #Nombre: Fernando AVV
    #Fecha: 14/02/2023
    #Descripción: Clases heredadas
"""
class Persona: #Clase persona
    __nombre = None #Creación de la varable __nombre
    __edad = None #Creación de la varable __edad
    
    def __init__ (self): #Función init llamada a la clase
        print("Persona") #Imprime persona
    
    def setNombre(self,nombre): #Función set
        self.__nombre = nombre #Modifica nombre
    
    def getNombre(self): #Función get
        return self.__nombre #Retorna __nombre
    
    def setEdad(self,edad): #Función set
        self.__edad = edad #Modifica Edad
    
    def getEdad(self): #Función get
        return self.__edad #Retorna __Edad

class Alumno(Persona): #Alumno hereda persona
    __nombre = None #Creación de la varable __nombre
    __matricula = None #Creación de la varable __matricula
    def __init__ (self): #Función init llamada a la clase
        super().__init__() #Llamada a la superclase
        print("Alumno") #imprime alumno
    
    def setNombre(self,nombre): #Función set
        self.__nombre = nombre #Modifica nombre
    
    def getNombre(self): #Función get
        return self.__nombre #Retorna __nombre
    
    def setMatricula(self,matricula): #Función set
        self.__matricula = matricula #Modifica matricula
    
    def getMatricula(self): #Función get
        return self.__matricula #Retorna __matricula

class Profesor(Persona): #Creación de la clase Profesor que hereda de la clase Persona
    __no_nomina = None #Creación de la variable __no_nomina
    def __init__ (self): #Función init llamada a la clase
        super().__init__() #Llamada a la superclase
        print("Profesor") #Imprime mensaje
    
    def setNoNomina(self,no_nomina): #Función set
        self.__no_nomina = no_nomina #Modifica nomina
    
    def getNoNomina(self): #Función get
        return self.__no_nomina #Retorna __no_nomina

    
class Coordinador(Persona): #Cración de la clase Coordinador que hereda de la clase Persona
    __no_nomina = None #Creación de la varable __no_nomina
    __carrera_a_cargo = None #Creación de la varable __carrera_a_cargo
    def __init__ (self): #Función init llamada a la clase
        super().__init__() #Llamada a la superclase
        print("Coordinador") #Imprime mensaje

    def setNoNomina(self,no_nomina): #Función set
        self.__no_nomina = no_nomina #Modifica nomina
    
    def getNoNomina(self): #Función get
        return self.__no_nomina #Retorna __no_nomina

    def setCarreraCargo(self,carrera_a_cargo): #Función set 
	    self.__carrera_a_cargo = carrera_a_cargo #Modifica el valor de la variable
    
    def getCarreraCargo(self): #Función get
	    return self.__carrera_a_cargo #Retorna el valor de la variable
	


objeto_persona = Persona() #llama a la función persona
objeto_alumno = Alumno() #llama a la función alumno
objeto_profesor = Profesor() #llama a la función profesor
objeto_cordinador = Coordinador() #llama a la función coordinador

print(dir(objeto_persona)) #Muestra las funciones de cada objeto
print(dir(objeto_alumno)) #Muestra las funciones de cada objeto
print(dir(objeto_profesor)) #Muestra las funciones de cada objeto
print(dir(objeto_cordinador)) #Muestra las funciones de cada objeto
