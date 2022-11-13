from cgitb import text
import sqlite3 as sql
from decouple import config
from console_utils import Console
DB = config('DB_NAME')


def createTeable():
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        cursor.execute(
        """CREATE TABLE IF NOT EXISTS materias (
            codigo INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            facultad TEXT NOT NULL,
            departamento TEXT NOT NULL,
            idioma TEXT NOT NULL,
            creditos INTEGER NOT NULL
                    )"""
        );
        conn.commit();
        conn.close();
    except sql.Error as e:
        print(e)

class Materia(Console):

    #Constructor function
    def __init__(self) -> None:
        self.__codigo:int = None;
        self.__nombre:str = None;
        self.__facultad:str = None;
        self.__departamento:str = None;
        self.__idioma:str = None;
        self.__creditos:int = None;
        self.__multidata = []        

#--------------------------------------------------------------------------------------SETTERS--------------------------------------------------------------------------#         
    def codigoSetter(self, codigo: int) ->None:
        self.__codigo = codigo;
    
    def creditosSetter(self, creditos: int) ->None:
        self.__creditos = creditos;
    
    def nombreSetter(self, nombre: str) ->None:
        self.__nombre = nombre;
    
    def facultadSetter(self, facultad: str) ->None:
        self.__facultad = facultad;
    
    def departamentoSetter(self, departamento: str) ->None:
        self.__departamento = departamento;

    def idiomaSetter(self, idioma: str) ->None:
        self.__idioma = idioma;
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------GETTERS---------------------------------------------------------------------------#
    def codigoGetter(self) ->int:
        return self.__codigo
    
    def creditosGetter(self) ->int:
        return self.__creditos
    
    def nombreGetter(self) ->str:
        return self.__nombre
    
    def facultadGetter(self) ->str:
        return self.__facultad
    
    def departamentoGetter(self) ->str:
        return self.__departamento

    def idiomaGetter(self) ->str:
        return self.__idioma;
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #Inserta la materia
    def __insertRow(self):
        try:
            conn = sql.connect(DB)
            cursor = conn.cursor()
            instruction = f"INSERT INTO materias values({self.__codigo}, '{self.__nombre}', '{self.__facultad}', '{self.__departamento}', '{self.__idioma}', {self.__creditos})"
            cursor.execute(instruction)
            conn.commit();
            conn.close();
        except sql.Error as e:
            print (e)

        
    #Pide input por teclado a tráves de consola de los datos, en versión gráfica desaparece
    #Pide input por teclado y retorna una tupla de tamaño = 6, que contiene todos los datos de materias a ser insertados
    def __rowGetter(self)->None:
        while True:
            try: 
                codigo = input('Codigo de la materia: ')
                codigo = codigo.ljust(10)
                codigo = int(codigo)
                nombre = input('Nombre de la materia: ')
                facultad = input('Facultad que dicta la materia: ')
                departamento = input('Departamento que dicta la materia: ')
                creditos = input('Creditos de la materia: ')
                creditos = int(creditos)
                idioma = input('Idioma en que se dicta la materia: ')
                if(codigo is None and nombre is None and facultad is None and departamento is None and idioma is None and creditos is None):
                    print("Por favor llene todos los campos")
                else:
                    self.codigoSetter(codigo)
                    self.nombreSetter(nombre.upper())
                    self.facultadSetter(facultad.upper())
                    self.departamentoSetter(departamento.upper())
                    self.idiomaSetter(idioma.upper())
                    self.creditosSetter(creditos)
                    break
            except ValueError:
                print("Dato(s) invalido(s), codigo y creditos son numeros enteros")


    #pide varias veces los datos
    #Pide input por teclado y retorna una lista de tuplas de tamaño = 6, que contiene todos los datos de materias a ser insertados
    def __batchRowGetter(self):
        secret_runner = "1"
        counter = 0
        while True: 
            try:
                codigo = input('Codigo de la materia: ')
                codigo = codigo.ljust(10)
                codigo = int(codigo)
                nombre = input('Nombre de la materia: ')
                facultad = input('Facultad que dicta la materia: ')
                departamento = input('Departamento que dicta la materia: ')
                creditos = input('Creditos de la materia: ')
                creditos = int(creditos)
                idioma = input('Idioma en que se dicta la materia: ')
                if(codigo is None and nombre is None and facultad is None and departamento is None and idioma is None and creditos is None):
                    print("Por favor llene todos los campos")
                else:
                    self.__multidata.append((codigo, nombre.upper(), facultad.upper(), departamento.upper(), idioma.upper(), creditos))
                    runner=input('Digite 1 si desea continuar, digite cualquier otra tecla si no. ')
                    counter+=1
                if runner != secret_runner:
                    break 
            except ValueError:
                print("Dato(s) invalido(s), codigo y creditos son numeros enteros")
        print (f"Usted ha insertado {counter} datos, los cuales son: ")
        self.tableMaterias(self.__multidata)
        return self.__multidata


    #Leer todos datos
    #Retorna una lista de tuplas tamaño = 6 con todos los datos en la DB referentes a materias
    def __readAllRows(self):
        try:
            conn = sql.connect(DB)
            cursor = conn.cursor()
            instruction = f"SELECT * from materias"
            cursor.execute(instruction)
            datos = cursor.fetchall()
            conn.commit();
            conn.close()
            return (datos);
        except sql.Error as e:
            print (e)

    #Acá se puede filtrar los datos bajo una condición 
    #Pide los datos para filtrarlos bajo alguna condición, puede ser cualquier tipo de dato
    #Retorna lista de tuplas con tamaño = 6 con todos los datos de las materias que hagan match con la busqueda
    #Publico para el uso en historia academica 
    def searchByFilter(self, fieldName, fieldValue):
        try:
            conn = sql.connect(DB)
            cursor = conn.cursor()
            instruction = f"SELECT * from materias WHERE {fieldName}={fieldValue}"
            cursor.execute(instruction)
            datos = cursor.fetchall()
            conn.commit();
            conn.close()
            return datos;
        except sql.Error as e:
            print (e)

    #Batch write, escribe multiples lineas de datos a la vez
    #Recibe como datos la salida de batch row getter
    def __batchInsertRow(self, dataList):
        try:
            conn = sql.connect(DB)
            cursor = conn.cursor()
            instruction = f"INSERT INTO materias values(?, ?, ?, ?, ?, ?)"
            cursor.executemany(instruction, self.__multidata) #Enviar varios datos a la vez
            conn.commit();
            conn.close();
        except sql.Error as e:
            print (e)
        

    #Read order, ordena los datos de mayor a menor según el campo que le pidamos :p
    #Imprime los datos en forma de tablita
    #Método público para el uso en otros lugares
    def readOrdered(self, field: str):
        try:
            conn = sql.connect(DB)
            cursor = conn.cursor()
            instruction = f"SELECT * from materias ORDER BY {field} DESC" #Si le quitamos el DESC se ordenara de menor a mayor, "DESC" viene de DESCENDING
            cursor.execute(instruction)
            datos = cursor.fetchall()
            conn.commit();
            conn.close()
            self.tableMaterias(datos);
        except sql.Error as e:
            print (e)

    #Actualizar datos en un determinado campo de alguna materia
    """Actualizar materia en diseño lógico."""
    #Pide el fieldOnChange como un string, la data puede ser cualquier tipo de dato, y la identificación que responde al nombre code
    #Retorna un mensaje de felicitación si todo fue correcto
    def __update(self, fieldOnChange: str, dataOnChange, code: int):
        try:
            conn = sql.connect(DB)
            cursor = conn.cursor()
            try:
                dataOnChange= int(dataOnChange)
                instruction = f"UPDATE materias SET '{fieldOnChange}'={dataOnChange} WHERE codigo={code}"
            except ValueError:
                instruction = f"UPDATE materias SET '{fieldOnChange}'='{dataOnChange}' WHERE codigo={code}" #Comando de actualización en SQL
            finally:
                cursor.execute(instruction)
                conn.commit();
                conn.close()
                print ('Datos actualizados de forma correcta')
        except sql.Error as e:
            print (e)

    #---------------------------------------------------------------------------------------------IMPORTANT calcular promedios de una tabla------------------------------------------------------------------------------------------
    #Calcula el promedio de un campo, en este caso de creditos
    def __promedio(self):
        try:
            conn = sql.connect(DB)
            cursor = conn.cursor()
            instruction = f"SELECT count(*) FROM materias" #Comando de contar campos en SQL
            cursor.execute(instruction)
            cantidad=cursor.fetchall()
            instruction = f"SELECT sum(creditos) FROM materias" #Comando de sumar campos en SQL
            cursor.execute(instruction)
            suma=cursor.fetchall()
            conn.commit();
            conn.close()
            print("Promedio creditos ", suma[0][0]/cantidad[0][0])
        except sql.Error as e:
            print (e)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    #---------------------------------------------------------------Función principal---------------------------------------------------------------------------------#

    def main(self):
        #TODO
        while True:
            #validador inicial
            while True:
                try:
                    selector = input(
                    """
                    Bienvenido a materia
                    1. Añadir materia.
                    2. Actualizar idioma. 
                    3. Leer datos. 
                    Para salir presione otro numero.  
                    """)
                    selector = int(selector)
                    break
                except ValueError:
                    print("valor invalido")
            #Añadir materia
            if selector == 1:
                while True:
                    while True:
                        try:
                            subselector = input(
                                """
                                1. Para añadir una sola materia.
                                2. Añadir materia sin recibir datos. 
                                3. Para añadir múltiples materias.
                                Para salir cualquier otro numero.  
                                """)
                            subselector = int(subselector)
                            break
                        except ValueError:
                            print("valor invalido")
                    #Añadir una sola materia
                    if subselector == 1:
                        self.__rowGetter()
                        self.__insertRow()
                        self.tableMaterias([self.codigoGetter(), self.nombreGetter(), self.facultadGetter(), self.departamentoGetter(), self.idiomaGetter(),self.creditosGetter])
                        break
                    #Añadir materia sin que se vean los datos
                    elif subselector==2:
                        self.__rowGetter()
                        self.__insertRow()
                        break
                    #Añadir multiples materias
                    elif subselector==3:
                        self.__batchRowGetter()
                        self.__batchInsertRow
                        break
                    else:
                        break
            #Actualizar idioma
            if selector == 2:
                while True:
                    try:
                        codigo = input("Seleccione el codigo de la materia ")
                        codigo = int(codigo)
                        break
                    except ValueError:
                        print('Valor invalido')
                while True:
                    idioma = input("Escriba el nuevo idioma ")
                    if (type(idioma)!=str):
                        print('Ingrese un valor')
                    else:
                        break
                self.__update('idioma', idioma, codigo)
            #Leer datos
            if selector == 3:
                    while True:
                        self.clearConsole()
                        try:
                            subselector = input(
                                """
                                1. Si desea ver todas las materias.
                                2. Para bsucar con el código.
                                Cualquier otro número para salir
                                """ 
                                )
                            subselector=int(subselector)
                            break
                        except ValueError:
                            print("valor invalido")
                #Ver todas las materias
                    if(subselector == 1):
                        self.tableMaterias(self.__readAllRows())
                #Ver materias por codigos
                    if(subselector == 2):
                        while True:
                            try:
                                codigo = input("Escriba el codigo de la materia que quiere ver: ")
                                codigo = int(codigo)
                                break
                            except ValueError:
                                print("valor invalido")
                        self.tableMaterias( self.searchByFilter('codigo', codigo))
            else:
                break