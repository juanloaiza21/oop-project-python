#Modulos
import sqlite3 as sql

class TableGen:

    def __init__(self, db)->None:
        self.__db = db

    def __estudianteTable(self)->None:
        try:
            conn = sql.connect(self.__db)
            cursor = conn.cursor()
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
                );
            conn.commit();
            conn.close();
        except sql.Error as e:
            print(e)

    def __materiaTable(self)->None:
        try:
            conn = sql.connect(self.__db)
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

    def __acadHistoryTable(self)->None:
        try:
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
    def __createrDB(self)->None:
        try:
            conn = sql.connect(self.__db);
            conn.commit();
            conn.close();
        except sql.Error as e:
            print(e)

    def main(self)->None:
        self.__createrDB()
        self.__materiaTable()
        self.__estudianteTable()
        self.__acadHistoryTable()
