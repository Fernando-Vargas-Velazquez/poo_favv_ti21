"""
    #Soluciones
    #Nombre: Fernando AVV
    #Fecha: 13/02/2023
    #Descripción: Clase alumno
"""
class Alumno: #Creación de la clase Alumno
    __nombre = None #Cración de la variable __nombre
    __matricula = None #Cración de la variable __matricula
    __carrera = None #Cración de la variable __carrera

    def __init__ (self):  #Constructor de la clase alumno
        print("Alumno: ") #Imprime texto
    
    def setNombre(self,nombre): #Función set permite modificar el valor
        self.__nombre = nombre #Modifica nombre
    
    def getNombre(self): #Función get permite remplazar el valor
        return self.__nombre #Retorna __nombre
    
    def setMatricula(self,matricula): #Función set permite modificar el valor
        self.__matricula = matricula #Modifica el valor de la variable
    
    def getMatricula(self):  #Función get permite remplazar el valor
        return self.__matricula #Retorna el valor de la variable
    
    def setCarrera(self,carrera): #Función set permite modificar el valor
        self.__carrera = carrera #Modifica el valor de la variable
    
    def getCarrera(self):  #Función get permite remplazar el valor
        return self.__carrera #Retorna el valor de la variable

dejah = Alumno() #Alumno
dejah.setNombre('Nando') #Set permite modificar
print(dejah.getNombre()) #Get permite mostrar
dejah.setMatricula('1722110121') #Set permite modificar
print(dejah.getMatricula()) #Get permite mostrar
dejah.setCarrera('TI Desarrollo de software') #Modifica el valor de la variable
print(dejah.getCarrera()) #Muestra el valor de la variable