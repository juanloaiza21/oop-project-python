import sqlite3 as sql;
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

#Crea tablas manualmente, automatizar
def createTeable():
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE materias (
                codigo integer PRIMARY KEY,
                nombre text,
                facultad text,
                departamento text,
                idioma text,
                creditos integer
                )"""
        );
        conn.commit();
        conn.close();
    except sql.Error as e:
        print(e)
    
#Inserta la materia
def insertRow(codigo: int, nombre: str, facultad: str, departamento: str, idioma: str, creditos: str):
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        instruction = f"INSERT INTO materias values({codigo}, '{nombre}', '{facultad}', '{departamento}', '{idioma}', {creditos})"
        cursor.execute(instruction)
        conn.commit();
        conn.close();
    except sql.Error as e:
        print (e)

    

def rowGetter():
    codigo = input('Codigo de la materia: ')
    codigo = codigo.ljust(10)
    nombre = input('Nombre de la materia: ')
    facultad = input('Facultad que dicta la materia: ')
    departamento = input('Departamento que dicta la materia: ')
    creditos = input('Creditos de la materia: ')
    idioma = input('Idioma en que se dicta la materia: ')
    return (int(codigo), nombre, facultad, departamento, idioma, int(creditos))
    
#Verifica tabla y DB, ejecuta QUERY
def main():
    #Verifica si existe el archivo.db SOTISFICAR TODO
    createrDB()
    # Verifica si existe la tabla    SOTISFICAR TODO
    createTeable()
    #DONE entra la data y luego la inserta
    data = rowGetter()
    insertRow(data[0], data[1], data[2], data[3], data[4], data[5])
    print(data)

main()