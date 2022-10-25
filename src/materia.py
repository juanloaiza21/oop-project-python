from cgitb import text
import sqlite3 as sql
from decouple import config
from console_utils import clearConsole
from console_utils import tableMaterias
DB = config('DB_NAME')

#Crea tablas manualmente, automatizar
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

    
#Pide input por teclado a tráves de consola de los datos, en versión gráfica desaparece
#TODO validar ints, strings y floats
def rowGetter():
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
            if not(codigo and nombre and facultad and departamento and idioma and creditos):
                print("Por favor llene todos los campos")
            else:
                return (codigo, nombre.upper(), facultad.upper(), departamento.upper(), idioma.upper(), creditos)
        except ValueError:
            print("Dato(s) invalido(s), codigo y creditos son numeros enteros")


#pide varias veces los datos
def batchRowGetter():
    result = []
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
            if not(codigo and nombre and facultad and departamento and idioma and creditos):
                print("Por favor llene todos los campos")
            else:
                result.append((codigo, nombre.upper(), facultad.upper(), departamento.upper(), idioma.upper(), creditos))
                runner=input('Digite 1 si desea continuar, digite cualquier otra tecla si no. ')
                counter+=1
            if runner != secret_runner:
                break 
        except ValueError:
            print("Dato(s) invalido(s), codigo y creditos son numeros enteros")
    print (f"Usted ha insertado {counter} datos, los cuales son: ")
    tableMaterias(result)
    return result


#Leer todos datos
def readAllRows():
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
def searchByFilter(fieldName, fieldValue):
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
def batchInsertRow(dataList):
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        instruction = f"INSERT INTO materias values(?, ?, ?, ?, ?, ?)"
        cursor.executemany(instruction, dataList) #Enviar varios datos a la vez
        conn.commit();
        conn.close();
    except sql.Error as e:
        print (e)
    

#Read order, ordena los datos de mayor a menor según el campo que le pidamos :p
def readOrdered(field: str):
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        instruction = f"SELECT * from materias ORDER BY {field} DESC" #Si le quitamos el DESC se ordenara de menor a mayor, "DESC" viene de DESCENDING
        cursor.execute(instruction)
        datos = cursor.fetchall()
        conn.commit();
        conn.close()
        tableMaterias(datos);
    except sql.Error as e:
        print (e)

#Actualizar datos en un determinado campo de alguna materia
"""Actualizar materia en diseño lógico."""
def update(fieldOnChange: str, dataOnChange, code: int):
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
#Calcula el promedio de un campo n
def promedio():
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
#TODO revisar
def main():
    #TODO
    while True:
        #validador inicial
        while True:
            try:
                selector = input("Para añadir una materia presione 1, para actualizar el idioma presione 2, para leer datos presione 3. Para salir presione otro numero. ")
                selector = int(selector)
                break
            except ValueError:
                print("valor invalido")
        #Añadir materia
        if selector == 1:
            while True:
                while True:
                    try:
                        subselector = int(input("Si desea añadir una materia presione 1, si desea añadir una materia sin recibir los datos presione 2, si desea añadir multiples materias presione 3, para salir cualquier otro numero "))
                        break
                    except ValueError:
                        print("valor invalido")
                #Añadir una sola materia
                if subselector == 1:
                    data = rowGetter()
                    insertRow(data[0], data[1], data[2], data[3], data[4], data[5])
                    tableMaterias([data])
                    break
                #Añadir materia sin que se vean los datos
                elif subselector==2:
                    data = rowGetter()
                    insertRow(data[0], data[1], data[2], data[3], data[4], data[5])
                    break
                #Añadir multiples materias
                elif subselector==3:
                    data = batchRowGetter()
                    batchInsertRow(data)
                    break
                else:
                    break
        #Actualizar idioma
        if selector == 2:
            while True:
                try:
                    codigo = int(input("Seleccione el codigo de la materia "))
                    break
                except ValueError:
                    print('Valor invalido')
            while True:
                idioma = input("Escriba el nuevo idioma ")
                if (type(idioma)!=str):
                    print('Ingrese un valor')
                else:
                    break
            update('idioma', idioma, codigo)
        #Leer datos
        if selector == 3:
                while True:
                    clearConsole()
                    try:
                        subselector = int(input("Si desea ver todas las materias presione 1, si desea buscar por codigos presione 2, para salir otro numero" ))
                        break
                    except ValueError:
                        print("valor invalido")
            #Ver todas las materias
                if(subselector == 1):
                    tableMaterias(readAllRows())
            #Ver materias por codigos
                if(subselector == 2):
                    while True:
                        try:
                            codigo = int(input("Escriba el codigo de la materia que quiere ver "))
                            break
                        except ValueError:
                            print("valor invalido")
                    tableMaterias( searchByFilter('codigo', codigo))
        else:
            break