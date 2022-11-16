#Modulos de control
from materia import Materia # importar el metodo main del modulo materia para ser ejecutado por el nombre de Materia
from historia_academica import AcadHistory # importar el metodo main del modulo historia_academica para ser ejecutado por el nombre de AcadHistory
from estudiante import Estudiante # importar el metodo main del modulo estudiante para ser ejecutado por el nombre de Estudiante
from table_creator import TableGen # importar el metodo main del modulo table_creator para ser ejecutado por el nombre de TableGen
from ranking import Ranking # importar el metodo main del modulo ranking para ser ejecutado por el nombre de Ranking
from decouple import config # importar el metodo main del modulo decouple para ser ejecutado por el nombre de config

#DB
DB = config('DB_NAME')

#Instanciamiento
miMateria = Materia(DB)
miEstudiante = Estudiante(DB)
miRanking = Ranking(DB)
miTables = TableGen(DB)
miHistoria = AcadHistory(DB)

def main(): #se define la funcion prinsipal de control
    NoneType = type(None)
    miTables.main()
    while True: #generar un ciclo para permanecer en la aplicacion independientemente de la entrada del usuario a excepcion de la opcion salir
        validator = True #creacion del boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
        while validator: #generar un ciclo con la funcion de  ingresar y verificar la entrada del usuario, el cual solo se rompera cuando la entrada del usuario es valida
            try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
                selector = input( #Este input debe ser un número entero en el rango de 1 a 5, si no lo es, se repite
                    """
                    ¡Bienvenido al programa de gestión de notas!
                    1. Para entrar a 'materia'.
                    2. Para entrar en 'historia academica'.
                    3. Para entrar en 'estudiante'. 
                    4. Para ver el top de estudiante. 
                    5. Para salir. 
                    """
                    )
                selector = int(selector) #verificacion de que la entrada es un numero
                validator = False #cambiar el valor del boleano para finalizar el ciclo que pide la entrada del usuario 
                while (selector!=1 and selector!=2 and selector!=3 and selector !=4 and selector!=5): #generar el ciclo de verificacion de que la entrada es uno de los valores validos
                    selector = input(f"{selector} no es valido ") #en caso de que la entrada no se un valor valido se generara un mensaje de no valides y se pedira nuevamente la entrada
                    selector = int(selector) #verificacion de que la entrada es un numero
            except ValueError:#sentecia que se ejecuta en caso se presencia de algun error
                print("input invalido") #generar mensaje de entrada invalida
                validator = True #cambiar el valor del boleano para que el ciclo de ingresar y verificar entrada del usuario continue 
        if selector==1: #sentencia en caso que la entrada del usuario sea 1
            miMateria.main() #con 1 como la entrada del usuario se ejecutara el metodo main importado del modulo materia para entrar al mismo
        elif selector==2: #sentencia en caso que la entrada del usuario sea 2
            miHistoria.main() #con 2 como la entrada del usuario se ejecutara el metodo main importado del modulo historia_academica para entrar al mismo
        elif selector==3: #sentencia en caso que la entrada del usuario sea 3
            miEstudiante.main() #con 3 como la entrada del usuario se ejecutara el metodo main importado del modulo estudiante para entrar al mismo
        elif selector==4: #sentencia en caso que la entrada del usuario sea 4
            miRanking.main() #con 4 como la entrada del usuario se ejecutara el metodo main importado del modulo ranking para entrar al mismo
        elif selector==5: #sentencia en caso que la entrada del usuario sea 5
            break; #con 5 como la entrada del usuario se rompera el ciclo prinsipal y asi salir del programa

