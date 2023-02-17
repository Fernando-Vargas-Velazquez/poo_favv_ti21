from persona import Persona #Importa del archivo persona.py la clase Persona

class Alumno(Persona): #Crea la clase alumno y hereda de la clase Persona

    def __init__(self) -> None: #Constructor de la clase alumno
        super().__init__() #Llama al constructor de la clase Persona
        print("Constructor alumno") #Muestra un mensaje

objeto_alumno = Alumno() #Crea un objeto de la clase alumno e invoca al constructor de a clase persona
objeto_alumno.setNombre("Dejah") #Asigana el valor a la variable
print(objeto_alumno.getNombre()) #Imprima el valor de la variable
