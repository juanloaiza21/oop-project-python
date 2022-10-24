#TODO all module
import sqlite3 as sql
from time import sleep
from decouple import config
from materia import readOrdered as allMaterias
from materia import searchByFilter as materiasFilter
from console_utils import clearConsole, tableHistoriaAcad

DB = config('DB_NAME')

#Crea tablas manualmente, automatizar; TODO generar modulo que cree toda la DB y meterlo en el controlador como primer paso al correr la app
def createTeable():
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS acadhistory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code_materia  INTEGER NOT NULL UNIQUE,
                id_estudiante INTEGER NOT NULL,
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

def creditsRef(idMateria: int):
    try:
        data = materiasFilter('codigo', idMateria)
        return data[0][5]
    except:
        print("Codigo de la materia inexistente")

#Crear historia academica en documentación
def insertRow(codigo: int, id_estudiante: int, score: float):
    try:
        conn = sql.connect(DB)
        conn.execute('PRAGMA foreign_keys = ON') #Valida las llaves extranjeras, es decir la existencia del estudiante o la amteria, si no existe da error
        cursor = conn.cursor()
        creditos= creditsRef(codigo)
        instruction = f"INSERT INTO acadhistory(code_materia, id_estudiante, nota, creditos_cursados) VALUES ({codigo},{id_estudiante}, {score}, {creditos})"
        cursor.execute(instruction)
        conn.commit();
        conn.close();
        print("Datos añadidos: ")
        tableHistoriaAcad([(codigo, id_estudiante, score, creditos)])
        sleep(2.5)
    except sql.Error as e:
        print (e)
        print('Probablemente no exista el estudiante o la materia, revise por favor los datos que ingreso y vuelva a intentar. Si sí existen, es que primero debe eliminar la materia, para que se actualice con los nuevos datos')

#Lector del input por parte del usuario
def rowGetter():
    while True:
        try:
            print("El codigo de la materia y el Id del estudiante deben existir, si no, habra error")
            codigo = input('Codigo de la materia: ')
            codigo = codigo.ljust(10)
            idEstudiante = input('Id del estudiante ')
            selector = int(input("¿Desea agregar nota? 1. Si. 2. No"))
            if selector ==1:
                nota = input('Nota del estudiante ')
            else:
                nota = 0
            nota = float(nota)
            idEstudiante = int(idEstudiante)
            codigo = int(codigo)
            if not (codigo and idEstudiante and nota):
                print('Algun valor esta vacio, por favor envie todos los datos')
            else:
                return (codigo, idEstudiante, nota)
        except ValueError:
            print("Dato(s) invalido")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------Lector del modulo de historia academica----------------------------------------------------------#

#Esta función debe traer todos las notas de un id
def acadHistoryById(id: int):
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        instruction = f"SELECT * from acadhistory WHERE id_estudiante={id} ORDER BY nota DESC"
        cursor.execute(instruction)
        datos = cursor.fetchall()
        conn.commit();
        conn.close()
        return datos;
    except sql.Error as e:
        print (e)

#Esta función calcula el promedio
def prom (data):
    try:
        numeroMaterias = len(data)
        sumaNotas = 0
        for i in range(numeroMaterias):
            sumaNotas += data[i][3]
        return sumaNotas/numeroMaterias
    except:
        print("Try again")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------Metodo de actualizacion--------------------------------------------------------------------------#
def update(fieldOnChange: str, dataOnChange, code: int, dataOnChange2: int):
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        try:
            dataOnChange= float(dataOnChange)
            instruction = f"UPDATE acadhistory SET '{fieldOnChange}'={dataOnChange} WHERE code_materia={dataOnChange2} AND id_estudiante={code}"
        except ValueError:
            instruction = f"UPDATE acadhistory SET '{fieldOnChange}'='{dataOnChange}' WHERE code_materia={code} AND id_estudiante={dataOnChange2}" #Comando de actualización en SQL
        finally:
            cursor.execute(instruction)
            conn.commit();
            conn.close()
            print ('Datos actualizados de forma correcta')
    except sql.Error as e:
        print (e)

def rowUpdateGetter():
    while True:
        try:
            print("El codigo de la materia y el Id del estudiante deben existir, si no, habra error")
            codigo = input('Codigo de la materia: ')
            codigo = codigo.ljust(10)
            idEstudiante = input('Id del estudiante ')
            nota = input('Nota del estudiante ')
            if not(codigo and idEstudiante and nota):
                print("Asegurese de enviar todos los datos")
            else:
                return (int(codigo), int(idEstudiante), float(nota))
        except ValueError:
            print("Dato(s) invalido")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------Metodo de borrado--------------------------------------------------------------------------#
def deleteRow(code: int, studentId: int):
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        instruction = f"DELETE FROM acadhistory WHERE code_materia={code} AND id_estudiante={studentId}" #Comando de delete en SQL un solo dato
        cursor.execute(instruction)
        conn.commit();
        conn.close()
        print ('Datos actualizados de forma correcta')
    except sql.Error as e:
        print (e)

def rowDeleteGetter():
    try:
        print("El codigo de la materia y el Id del estudiante deben existir, si no, habra error")
        codigo = input('Codigo de la materia: ')
        codigo = codigo.ljust(10)
        idEstudiante = input('Id del estudiante ')
        if not(codigo and idEstudiante):
            print("Asegurese de enviar todos los datos")
        else:
            return (int(codigo), int(idEstudiante))
    except ValueError:
        print("Dato(s) invalido")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------Controlador principal----------------------------------------------------------------------------#
def main():
    #TODO print historia academica como una tabla xd
    while True: 
        validator = True
        while validator:
            try:
                selector=input("Si desea crear añadir una materia aprete 1. Si desea actualizar una nota en una materia ya registrada aprete 2. Si desea consultar sus notas o su promedio aprete 3. si desea eliminar alguna materia aprete 4. Para salir, cualquier otra tecla.")
                selector =int(selector)
                if (selector!=1 and selector !=2 and selector !=3 and selector !=4):
                    print(f"{selector} es un valor invalido")
                else:
                    validator = False
            except ValueError:
                print(f"{selector} es un valor invalido")
        if selector == 1:
            while True:
                try:
                    clearConsole()
                    selector=input("Para añadir una materia debe escribir el documento del estudiante (ya registrado) y  el codigo de una materia existente. ¿Desea ver que materias hay disponibles? 1.Si. 2.No");
                    selector = int(selector)
                    if (selector !=1 and selector !=2):
                        print(f"{selector} es invalido")
                    elif selector == 1:
                        allMaterias('codigo')
                        sleep(2.5)
                        print('A continuación va a inscribir una materia ')
                        data = rowGetter()
                        insertRow(data[0], data[1], data[2])
                        break;
                    elif selector == 2:
                        print('A continuación va a inscribir una materia ')
                        data = rowGetter()
                        insertRow(data[0], data[1], data[2])
                        break;
                except ValueError:
                    print (f"{selector} es invalido")
        elif selector == 2:
            while True:
                try:
                    clearConsole()
                    print("Para actualizar la nota de una materia debe escribir el documento del estudiante y el codigo de la materia. Claramene la nota tambien");
                    data = rowUpdateGetter()
                    update('nota', data[2], data[1], data[0])
                    break
                except:
                    print ("Unexpected error")
        elif selector == 3: 
            while True:
                try:
                    clearConsole()
                    selector=input("Si desea ver su promedio aprete 1. Si desea ver todas sus notas aprete 2.");
                    selector = int(selector)
                    if (selector !=1 and selector !=2):
                        print(f"{selector} es invalido")
                    elif selector == 1:
                        while True:
                            try:
                                idd = int(input("Ingrese el documento del estudiante "))
                                data = acadHistoryById(idd)
                                promedio = prom(data)
                                print("Su promedio es: ", promedio)
                                break
                            except ValueError:
                                print(f"{idd} es invalido")
                    elif selector == 2:
                       while True:
                            try:
                                clearConsole()
                                idd = int(input("Ingrese el documento del estudiante "))
                                data = acadHistoryById(idd)
                                print("Sus notas son: ")
                                tableHistoriaAcad(data)
                                break
                            except ValueError:
                                print(f"{idd} es invalido")
                    break
                except ValueError:
                    print (f"{selector} es invalido")
        elif selector == 4:
            while True:
                clearConsole()
                data = rowDeleteGetter()
                deleteRow(data[0], data[1])
                break;
        else:
            break

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
