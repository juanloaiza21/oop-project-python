#TODO all module
import sqlite3 as sql
from time import sleep
from decouple import config
from materia import readOrdered as allMaterias

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
#Crear historia academica en documentación
def insertRow(codigo: int, id_estudiante: int, score: float = 0.0):
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
    selector = input("¿Desea agregar nota? 1. Si. 2. No")
    if selector ==1:
        nota = input('Nota del estudiante ')
    else:
        nota = 0
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
        for i in range(numeroMaterias-1):
            sumaNotas += data[i][3]
        return sumaNotas/numeroMaterias
    except:
        print("Try again")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------Metodo de actualizacion--------------------------------------------------------------------------#
def update(fieldOnChange: str, dataOnChange, code: int):
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        try:
            dataOnChange= int(dataOnChange)
            instruction = f"UPDATE acadhistory SET '{fieldOnChange}'={dataOnChange} WHERE codigo={code}"
        except ValueError:
            instruction = f"UPDATE acadhistory SET '{fieldOnChange}'='{dataOnChange}' WHERE codigo={code}" #Comando de actualización en SQL
        finally:
            cursor.execute(instruction)
            conn.commit();
            conn.close()
            print ('Datos actualizados de forma correcta')
    except sql.Error as e:
        print (e)
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
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------Controlador principal----------------------------------------------------------------------------#
def main():
    #TODO print historia academica como una tabla xd
    while True: 
        validator = True
        while validator:
            try:
                selector=input("Si desea crear añadir una materia aprete 1. Si desea actualizar datos o una nota en una materia ya registrada aprete 2. Si desea consultar sus notas o su promedio aprete 3. si desea eliminar alguna materia aprete 4. Para salir, cualquier otra tecla.")
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
                    selector=input("Para añadir una materia debe escribir el documento del estudiante (ya registrado) y  el codigo de una materia existente. ¿Desea ver que materias hay disponibles? 1.Si. 2.No");
                    selector = int(selector)
                    if (selector !=1 and selector !=2):
                        print(f"{selector} es invalido")
                    elif selector == 1:
                        allMaterias('codigo')
                        sleep(2.5)
                        print('A continuación va a inscribir una materia ')
                        data = rowGetter()
                        insertRow(data)
                        print("Datos añadidos correctamente");
                    elif selector == 2:
                        print('A continuación va a inscribir una materia ')
                        data = rowGetter()
                        insertRow(data)
                        print("Datos añadidos correctamente")
                        break;
                except ValueError:
                    print (f"{selector} es invalido")
        elif selector == 2:
            pass
        elif selector == 3: 
            pass
        elif selector == 4:
            pass
        else:
            break

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

main()