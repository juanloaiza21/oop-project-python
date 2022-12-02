#TODO all module
import sqlite3 as sql
from time import sleep
from decouple import config
from materia import Materia
from console_utils import Console

#DB
DB = config('DB_NAME')

miMateria = Materia(DB)
miConsola = Console()

class AcadHistory(Console):

    def __init__(self, db):
        self.__db = db
        self.__idMateria: int = None
        self.__codigo: int = None
        self.__idEstudiante: int = None
        self.__score: float = None
        self.__creditos: int = None

    #--------------------------------------------------------------------------Setters---------------------------------------------------------------------------------
    def __idMateriaSetter(self, idMateria: int)->None:
        self.__idMateria = idMateria

    def __codigoSetter(self, codigo: int)->None:
        self.__codigo = codigo

    def __idEstudianteSetter(self, idEstudiante: int)->None:
        self.__idEstudiante = idEstudiante

    def __scoreSetter(self, score: float)->None:
        self.__score = score

    def __creditosSetter(self, creditos: int)->None:
        self.__creditos = creditos
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #--------------------------------------------------------------------------Getters---------------------------------------------------------------------------------
    def __idMateriaGetter(self)->int:
        return self.__idMateria

    def __codigoGetter(self)->int:
        return self.__codigo

    def __idEstudianteGetter(self)->int:
        return self.__idEstudiante

    def __scoreGetter(self)->float:
        return self.__score

    def __creditosGetter(self)->int:
        return self.__creditos
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------Inserta las notas de la materia-------------------------------------------------------------------

    def __creditsRef(self):
        try:
            data = miMateria.searchByFilter('codigo', self.__codigo)
            self.__creditosSetter(data[0][5]) #Retorna el codigo de la materia junto a los creditos
        except:  
            print("Codigo de la materia inexistente") #En caso de no existir materia se ejecuta la siguiente linea

    #Crear historia academica en documentación
    def __insertRow(self):
        try:
            conn = sql.connect(self.__db) #Conexion a la base de datos
            conn.execute('PRAGMA foreign_keys = ON') #Valida las llaves extranjeras, es decir la existencia del estudiante o la amteria, si no existe da error
            cursor = conn.cursor() #llamado a la funcion de filtro de materias
            self.__creditsRef()
            instruction = f"INSERT INTO acadhistory(code_materia, id_estudiante, nota, creditos_cursados) VALUES ({self.__codigo},{self.__idEstudiante}, {self.__score}, {self.__creditos})" #Da la instruccion de insertar datos en la base de datos
            cursor.execute(instruction)#Ejecucion de la instruccion
            conn.commit();
            conn.close(); #Cierre de la conexion a la base de datos
            print("Datos añadidos: ") #Muestra en pantalla los datos añadidos
            data = (0,self.__codigo, self.__idEstudiante, self.__score, self.__creditos)
            miConsola.tableHistoriaAcad([data])
        except sql.Error as e:
            print (e)  #En caso de error se debe verificar la existencia de los datos
            print('Probablemente no exista el estudiante o la materia, revise por favor los datos que ingreso y vuelva a intentar. Si sí existen, es que primero debe eliminar la materia, para que se actualice con los nuevos datos')

    #Lector del input por parte del usuario
    #TODO add here setters
    def __rowGetter(self):
        while True:
            try:
                print("El codigo de la materia y el Id del estudiante deben existir, si no, habra error") #Aclaracion para evitar posibles errores en el programa
                codigo = input('Codigo de la materia: ') #El usuario ingresa el codigo
                codigo = codigo.ljust(10) #El codigo no puede tener mas de 10 caracteres
                idEstudiante = input('Id del estudiante ') #Se ingresa el Id del estudiante
                selector = input("""
                ¿Desea agregar nota? 
                1. Si. 
                2. No.
                """) #El usuario decide entr3e insertar o no insertar nota
                selector = int(selector)
                if selector ==1: #Si el usuario selecciona 1 podra insertar la nota
                    nota = input('Nota del estudiante ')
                else: #en caso de no insertar nota aparecera como 0.0
                    nota = 0.0
                self.__scoreSetter(float(nota)) #se transforma la nota en un dato tipo float
                self.__idEstudianteSetter(int(idEstudiante)) #se transforma el Id del estudiante en un dato tipo int
                self.__codigoSetter(int(codigo)) #se transforma el codigo en un dato tipo int
                break
            except ValueError: #En caso de error dira que los datos son invalidos
                print("Dato(s) invalido")

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #----------------------------------------------------------------Lector del modulo de historia academica----------------------------------------------------------#

    #Esta función debe traer todos las notas de un id
    def acadHistoryById(self, idd = None):
        try:
            conn = sql.connect(self.__db) #Conexion a la base de datos
            cursor = conn.cursor()
            if idd == None:
                idd = self.__idEstudiante
            instruction = f"SELECT * from acadhistory WHERE id_estudiante={idd} ORDER BY nota DESC" #da la instruccion de buscar las notas en la base de datos
            cursor.execute(instruction) #Ejecuta la instruccion de buscar las notas
            datos = cursor.fetchall()
            conn.commit(); 
            conn.close()
            return datos; #retorna los datos obtenidos con el fetchall
        except sql.Error as e:
            print (e)

    #Esta función calcula el promedio
    def prom (self, data):
        try:
            numeroMaterias = len(data)
            sumaNotas = 0
            for i in range(numeroMaterias): #toma todas las notas
                sumaNotas += data[i][3]
            return sumaNotas/numeroMaterias #saca el promedio de las notas basado en la cantidad de materias
        except:
            print("Try again") #En caso de error imprimira "Intenta otra vez"
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #----------------------------------------------------------------Metodo de actualizacion--------------------------------------------------------------------------#
    def __update(self, fieldOnChange: str):
        try:
            conn = sql.connect(self.__db) #conexion a la base de datos
            cursor = conn.cursor()
            instruction = f"UPDATE acadhistory SET '{fieldOnChange}'={self.__score} WHERE code_materia={self.__codigo} AND id_estudiante={self.__idEstudiante}" #Da la instruccion de actualizar
            cursor.execute(instruction) #Ejecuta la instruccion de actualizacion
            conn.commit();
            conn.close() #se cierra la conexxion
            print ('Datos actualizados de forma correcta') #Informa la correcta actualizacion de datos
        except sql.Error as e:
            print (e)

    #TODO add setters
    def __rowUpdateGetter(self):
        while True:
            try:
                print("El codigo de la materia y el Id del estudiante deben existir, si no, habra error")#Aclaracion para evitar que el programa tenga errores
                codigo = input('Codigo de la materia: ')#El usuario ingresa el codigo
                codigo = codigo.ljust(10)#El codigo no puede tener mas de 10 caracteres
                idEstudiante = input('Id del estudiante ')#El usuario ingresa el id
                nota = input('Nota del estudiante ')#El usuario ingresa la nota
                codigo = int(codigo)
                idEstudiante = int(idEstudiante)
                nota = float(nota)
                self.__codigoSetter(codigo)
                self.__idEstudianteSetter(idEstudiante)
                self.__scoreSetter(nota)
                break
                #retorna los datos insertados como datos tipo int y float
            except ValueError:
                print("Dato(s) invalido") #En caso de que los datos sean incorrectos saldra este mensaje

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #----------------------------------------------------------------Metodo de borrado--------------------------------------------------------------------------------#
    def __deleteRow(self):
        try:
            conn = sql.connect(self.__db) #Conexxion a la base de datos
            cursor = conn.cursor()
            instruction = f"DELETE FROM acadhistory WHERE code_materia={self.__codigo} AND id_estudiante={self.__idEstudiante}" #Comando de delete en SQL un solo dato
            cursor.execute(instruction) #Ejecuta la instruccion de borrado
            conn.commit();
            conn.close() #Cierre de conexion a la base de datos
            print ('Datos actualizados de forma correcta') #Mensaje en caso de no hbaer error en la actualizacion
        except sql.Error as e:
            print (e)

    #TODO add setter
    def __rowDeleteGetter(self):
        try:
            print("El codigo de la materia y el Id del estudiante deben existir, si no, habra error")#Aclaracion para prevenir errores en el programa
            codigo = input('Codigo de la materia: ') #El usuario ingresa el codigo
            codigo = codigo.ljust(10) #El codigo ingresado no puede tener mas de 10 caracteres
            idEstudiante = input('Id del estudiante ') #El usuario ingresa el id
            self.__codigo = int(codigo)
            self.__idEstudiante = int(idEstudiante) #Retorna codigo e id
        except ValueError:
            print("Dato(s) invalido") #En caso de insertar datos incorrectos se imprime este mensaje
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #funcion que hace suma de creditos
    def creditss(self, id: int):
        try:
            conn = sql.connect(self.__db) #Conexxion a la base de datos
            cursor = conn.cursor()
            instruction = f"SELECT sum(creditos_cursados) FROM acadhistory WHERE id_estudiante = {id}" #Comando de delete en SQL un solo dato
            cursor.execute(instruction) #Ejecuta la instruccion de borrado
            result = cursor.fetchall()
            conn.commit();
            conn.close() #Cierre de conexion a la base de datos
            return result[0][0]
        except sql.Error as e:
            print (e)
    #Funcion que cuenta las amterias cursadas
    def materiass(self, id: int):
        try:
            conn = sql.connect(self.__db) #Conexxion a la base de datos
            cursor = conn.cursor()
            instruction = f"SELECT count(creditos_cursados) FROM acadhistory WHERE id_estudiante = {id}" #Comando de delete en SQL un solo dato
            cursor.execute(instruction) #Ejecuta la instruccion de borrado
            result = cursor.fetchall()
            conn.commit();
            conn.close() #Cierre de conexion a la base de datos
            return result[0][0]
        except sql.Error as e:
            print (e)

    #----------------------------------------------------------------Controlador principal----------------------------------------------------------------------------#
    def main(self):
        #TODO print historia academica como una tabla 
        while True: 
            validator = True
            while validator:
                try:
                    selector=input(
                    """
                    Bienvenido a historia academica
                    1. Si desea añadir una materia. 
                    2. Si desea actualizar una nota en una materia ya registrada. 
                    3. Si desea consultar sus notas o su promedio. 
                    4. Si desea eliminar alguna materia. 
                    Para salir, cualquier otra tecla.
                    """)
                    #El usuario decide que desea realizar en el programa
                    selector =int(selector) #trensforma la seleccion del usuario para poder hacer una validacion
                    if (selector!=1 and selector !=2 and selector !=3 and selector !=4 and selector !=5):
                        print(f"{selector} es un valor invalido")#En caso de que el usuario seleccione una opcion que no sea parte de las expuestas por el programa saldra este mensaje de error
                    else:
                        validator = False
                except ValueError:
                    print(f"{selector} es un valor invalido")
            if selector == 1: #ejecucion en caso de que la seleccion del usuario sea 1
                validator = True
                while validator:
                    # TODO Se arma bucle infinito en 1
                    try:
                        miConsola.clearConsole()
                        selectorr=input(
                        """
                        Para añadir una materia debe escribir el documento del estudiante (ya registrado) y  el codigo de una materia existente. 
                        ¿Desea ver que materias hay disponibles? 
                        1.Si. 
                        2.No.  
                        """); #da la opcion de ver las materias existentes en la base de datos
                        selectorr = selectorr
                        if selectorr == "1": #En caso de querer ver las materias se ejecuta las siguientes lineas
                            miMateria.readOrdered('codigo')
                            sleep(2.5)
                            print('A continuación va a inscribir una materia ')
                            self.__rowGetter()
                            self.__insertRow() 
                            validator = False
                        elif selectorr == "2": #En caso de no querer ver las materias se ejecutan las siguientes lineas
                            print('A continuación va a inscribir una materia ')
                            self.__rowGetter()
                            self.__insertRow()
                            validator = False
                    except ValueError:
                        print (f"{selector} es invalido") #Error en caso de no insertar una opcion disponible
            elif selector == 2: #ejecucion en caso de que la seleccion del usuario sea 2
                while True:
                    try:
                        miConsola.clearConsole()
                        print("Para actualizar la nota de una materia debe escribir el documento del estudiante y el codigo de la materia. Claramene la nota tambien");
                        data = self.__rowUpdateGetter() #se ejecuta la funcion de update
                        self.__update('nota')
                        break
                    except:
                        print ("Unexpected error") #mensaje en caso de error
            elif selector == 3: #ejecucion en caso de que la seleccion del usuario sea 3
                while True:
                    try:
                        miConsola.clearConsole()
                        selector=input(
                        """
                        1. Si desea ver su promedio. 
                        2. Si desea ver todas sus notas. 
                        """);
                        selector = int(selector)
                        if (selector !=1 and selector !=2):
                            print(f"{selector} es invalido") #Validacion de la opcion insertada
                        elif selector == 1: #Ejecucion en caso de la opcion 1
                            while True:
                                try:
                                    idd = input("Ingrese el documento del estudiante ")
                                    idd = int(idd)
                                    data = self.acadHistoryById(idd) #se ejecuta la funcion de historia academica
                                    promedio = self.prom(data) #Saca el promedio de las notas
                                    print("Su promedio es: ", promedio)
                                    break
                                except ValueError:
                                    print(f"{idd} es invalido")
                            break
                        elif selector == 2: #Ejecucion en caso de la opcion 2
                            while True:
                                try:
                                    idd = input("Ingrese el documento del estudiante ")
                                    idd = int(idd) #solicita el id de estudiante y lo convierte 
                                    data = self.acadHistoryById(idd)
                                    print("Sus notas son: ") #muestra las notas del estudiante
                                    miConsola.tableHistoriaAcad(data) 
                                    break
                                except ValueError:
                                    print(f"{idd} es invalido") #error en caso de que el id sea incorrecto
                            break
                    except ValueError:
                        print (f"{selector} es invalido") #error en caso de que la seleccion sea incorrecta
            elif selector == 4: #ejecucion en caso de que la seleccion del usuario sea 4
                while True:
                    miConsola.clearConsole()
                    data = self.__rowDeleteGetter() #se ejecuta la funcion de borrado
                    self.__deleteRow()
                    break;
            else:
                break

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
