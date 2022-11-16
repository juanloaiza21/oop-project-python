#Modulos
import sqlite3 as sql #importar el modulo sqlite3 como sql

class TableGen: #creacion de la clase TableGen

    def __init__(self, db)->None: #definir la funcion que inicializa los atributos
        self.__db = db #base de datos

    def __estudianteTable(self)->None: #define la funcion privada de la tabla de los estudiante
        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__db) #conexion a la base de datos
            cursor = conn.cursor() #se inserta un cursor para la insercion de datos
            cursor.execute(
                    """CREATE TABLE IF NOT EXISTS estudiante (
                        identificacion INTEGER PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        apellido TEXT NOT NULL,
                        carrera TEXT NOT NULL,
                        fechanacimiento TEXT NOT NULL,
                        fechaingreso TEXT NOT NULL,
                        procedencia TEXT NOT NULL,
                        correoeletronico TEXT NOT NULL,
                        cantidadmatriculas INTEGER NOT NULL
                        )"""
                ); #creacion de la tabla
            conn.commit(); #se verifican que los cambios en la base de datos son validos
            conn.close(); #se cierra la conexion con la base de datos
        except sql.Error as e: #sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print(e) #mensaje del error que se presenta

    def __materiaTable(self)->None: #define la funcion privada de la tabla de materias
        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__db) #conexion a la base de datos
            cursor = conn.cursor() #se inserta un cursor para la insercion de datos
            cursor.execute(
            """CREATE TABLE IF NOT EXISTS materias (
                codigo INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                facultad TEXT NOT NULL,
                departamento TEXT NOT NULL,
                idioma TEXT NOT NULL,
                creditos INTEGER NOT NULL
                        )"""
            ); #creacion de la tabla
            conn.commit(); #se verifican que los cambios en la base de datos son validos
            conn.close(); #se cierra la conexion con la base de datos
        except sql.Error as e: #Sentencia que se ejecuta en caso de error
            print(e) #Mensaje presentado en caso de error

    def __acadHistoryTable(self)->None: #define la funcion privada de la tabla de historia academica
        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__db) #Conexion a la base de datos
            cursor = conn.cursor()  #Se inserta un cursor para la insercion de datos
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS acadhistory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code_materia  INTEGER NOT NULL,
                    id_estudiante INTEGER NOT NULL,
                    nota REAL,
                    creditos_cursados INTEGER,
                    FOREIGN KEY(id_estudiante) REFERENCES estudiante(identificacion),
                    FOREIGN KEY(code_materia) REFERENCES materias(codigo)
                    )"""   #Creacion de la tabla
            );
            conn.commit();#Se verifican los cambios en la base de datos
            conn.close(); # se cierra la conexion con la base de datos
        except sql.Error as e: #Sentencia que se ejecuta en caso de error
            print(e) #Mensaje presentado en caso de error

    #Crea base de datos
    def __createrDB(self)->None: #define la funcion privada de la creacion de base de datos
        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__db); #Conexion a la base de datos
            conn.commit(); #Se verifican los cambios en la base de datos
            conn.close(); # se cierra la conexion con la base de datos
        except sql.Error as e: #Sentencia que se ejecuta en caso de error
            print(e) #Mensaje presentado en caso de error

    def main(self)->None: #definicion del metodo controldor del modulo table_creator
        self.__createrDB() #atributo privado de la creacion de base de datos
        self.__materiaTable() #atributo privado de la tabla materia
        self.__estudianteTable() #atributo privado de la tabla estudiante 
        self.__acadHistoryTable() #atributo privado de la tabla historia academica
