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
                FOREIGN KEY(code_materia) REFERENCES materias(codigo)
                )"""
        );
        conn.commit();
        conn.close();
    except sql.Error as e:
        print(e)

#----------------------------------------------------------------Inserta las notas de la materia-------------------------------------------------------------------

def insertRow(codigo: int, id_estudiante: int, score: float):
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        #TODO creditos automaticos
        creditos=5
        instruction = f"INSERT INTO acadhistory(code_materia, id_estudiante, nota, creditos_cursados) VALUES ({codigo},{id_estudiante}, {score}, {creditos})"
        cursor.execute(instruction)
        conn.commit();
        conn.close();
    except sql.Error as e:
        print (e)

#Lector del input por parte del usuario
#TODO validar ints, strings y floats
def rowGetter():
    print("El codigo de la materia y el Id del estudiante deben existir, si no, habra error")
    codigo = input('Codigo de la materia: ')
    codigo = codigo.ljust(10)
    idEstudiante = input('Id del estudiante ')
    #TODO validacion en caso de que la nota aun no este sea 0
    nota = input('Nota del estudiante ')
    return (int(codigo), int(idEstudiante), float(nota))

#TODO validar ints, strings y floats
def batchRowGetter():
    result = []
    secret_runner = "1"
    counter = 0
    while True: 
        print("El codigo de la materia y el Id del estudiante deben existir, si no, habra error")
        codigo = input('Codigo de la materia: ')
        codigo = codigo.ljust(10)
        idEstudiante = input('Id del estudiante ')
        #TODO validacion en caso de que la nota aun no este sea 0
        nota = input('Nota del estudiante ')
        result.append(int(codigo), int(idEstudiante), float(nota))
        runner=input('Digite 1 si desea continuar, digite cualquier otra tecla si no. ')
        counter+=1
        if runner != secret_runner:
            break 
    print (f"Usted ha insertado {counter} datos, los cuales son: {result}")
    return result
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------Lector del modulo de historia academica----------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------Controlador principal----------------------------------------------------------------------------#
def main():
    pass
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#