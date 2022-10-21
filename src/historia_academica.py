#TODO all module
import sqlite3 as sql
from decouple import config

DB = config('DB_NAME')

#Crea base de datos, hay que hacer que verifique si ya existe
def createrDB():
    try:
        conn = sql.connect(DB);
        conn.commit();
        conn.close();
    except sql.Error as e:
        print(e)

#Crea tablas manualmente, automatizar; TODO generar modulo que cree toda la DB y meterlo en el controlador como primer paso al correr la app
def createTeable():
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS acadhistory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code_materia  INTEGER,
                id_estudiante INTEGER,
                nota REAL,
                creditos_cursados INTEGER,
                FOREIGN KEY(id_estudiante) REFERENCES estudiante(identificacion),
                FOREIGN KEY(code_materia) REFERENCES materias(codigo),
                FOREIGN KEY(creditos_cursados) REFERENCES materias(creditos)
                )"""
        );
        conn.commit();
        conn.close();
    except sql.Error as e:
        print(e)


createTeable()
#----------------------------------------------------------------Controlador principal----------------------------------------------------------------------------#
def main():
    pass
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#