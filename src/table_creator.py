#Creador de tablas
from materia import createTeable as materiaTable
from historia_academica import createTeable as acadHistoryTable
from estudiante import createTeable as estudianteTable
#Modulos
import sqlite3 as sql
from decouple import config

DB = config('DB_NAME')

#Crea base de datos
def createrDB():
    try:
        conn = sql.connect(DB);
        conn.commit();
        conn.close();
    except sql.Error as e:
        print(e)

def main():
    createrDB()
    materiaTable()
    estudianteTable()
    acadHistoryTable()
