class Persona: #Clase Persona

    __nombre = None #Creación de la variable __nombre
    __edad = None  #Creación de la variable __edad

    def __init__(self) -> None: #Constructor de la clase Persona
        print("Constructor persona") #Imprme el constructor

    def setNombre(self, nombre:str): #Metodo para modificar el valor de la variable
        self.__nombre = nombre #asigna el valor de nombre a la variable
    
    def getNombre(self)-> str: #Metodo para rempazar el valor de la variable 
        return self.__nombre #Regresa el valor de la variable 
