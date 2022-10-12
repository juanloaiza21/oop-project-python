import sqlite3 as sql
from decouple import config

DB = config('DB_NAME')


"""A la larga este será el módulo de materias"""

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

    
#Pide input por teclado a tráves de consola de los datos, en versión gráfica desaparece
def rowGetter():
    codigo = input('Codigo de la materia: ')
    codigo = codigo.ljust(10)
    nombre = input('Nombre de la materia: ')
    facultad = input('Facultad que dicta la materia: ')
    departamento = input('Departamento que dicta la materia: ')
    creditos = input('Creditos de la materia: ')
    idioma = input('Idioma en que se dicta la materia: ')
    return (int(codigo), nombre.upper(), facultad.upper(), departamento.upper(), idioma.upper(), int(creditos))

#pide varias veces los datos
def batchRowGetter():
    result = []
    secret_runner = "1"
    counter = 0
    while True: 
        codigo = input('Codigo de la materia: ')
        codigo = codigo.ljust(10)
        nombre = input('Nombre de la materia: ')
        facultad = input('Facultad que dicta la materia: ')
        departamento = input('Departamento que dicta la materia: ')
        creditos = input('Creditos de la materia: ')
        idioma = input('Idioma en que se dicta la materia: ')
        result.append((int(codigo), nombre, facultad, departamento, idioma, int(creditos)))
        runner=input('Digite 1 si desea continuar, digite cualquier otra tecla si no. ')
        counter+=1
        if runner != secret_runner:
            break 
    print (f"Usted ha insertado {counter} datos, los cuales son: {result}")
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
        print(datos);
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
        print(datos);
    except sql.Error as e:
        print (e)

#Batch write, escribe multiples lineas de datos a la vez
def batchInsertRow(dataList):
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        instruction = f"INSERT INTO materias values(?, ?, ?, ?, ?, ?)"
        cursor.executemany(instruction, dataList)
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
        print(datos);
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

#---------------------------------------------------------------Métodos DELETE, no se usan acá pero no sobran TODO eliminarlos--------------------------------------#
def deleteRow(code: int):
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        instruction = f"DELETE FROM materias WHERE codigo={code}" #Comando de delete en SQL un solo dato
        cursor.execute(instruction)
        conn.commit();
        conn.close()
        print ('Datos actualizados de forma correcta')
    except sql.Error as e:
        print (e)

def deleteAll():
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        instruction = f"DELETE * FROM materias" #Comando de delete all en SQL
        cursor.execute(instruction)
        conn.commit();
        conn.close()
        print ('Datos actualizados de forma correcta')
    except sql.Error as e:
        print (e)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------Función principal---------------------------------------------------------------------------------#
def main():
    
    while True:
        #Verifica si existe el archivo.db SOTISFICAR TODO
        createrDB()
        # Verifica si existe la tabla    SOTISFICAR TODO
        createTeable()
        #Revisa si va a añadir datos, leer o actualizar, metodo reutilizable, verifica que el input sea correcto
        validator = True
        while validator:
            try:
                selector = input("Si desea añadir datos ingrese '1' y enter. Si desea actualizar datos presione '2' y enter. si desea obtener información ingrese '3' y enter, para salir presione 4 y enter. ")
                selector = int(selector)
                validator = False
                while(selector!=1 and selector !=2 and selector !=3 and selector !=4):
                    selector = input(f"{selector} no es una opción valida, por favor digite una opcion valida ")
                    selector = int(selector)
            except ValueError:
                print("Input invalido")
                validator = True
        #-------------------------------------------Creación de materias---------------------------------------------------------------------------#
        if selector ==1:
            validator = True
            while validator:
                try:
                    pointer = input("Si desea solo añadir una materia digite '1' y luego enter, si desea registrar multiples datos digite '2' y luego enter. ")
                    pointer = int(pointer)
                    validator = False
                    while(pointer!=1 and pointer !=2):
                        pointer = input(f"{pointer} no es una opción valida, por favor digite una opcion valida ")
                        pointer = int(pointer)
                except ValueError:
                    print("Input invalido")
                    validator = True
        #Primer caso del input de escritura, un solo dato
            if int(pointer)==1:
                data = rowGetter()
                insertRow(data[0], data[1], data[2], data[3], data[4], data[5])
                print("Datos insertados: ",data)
        #Segundo caso, múltiples datos
            elif(int(pointer)==2):
                data = batchRowGetter()
                batchInsertRow(data)
        #-----------------------------------------------------------------------------------------------------------------------------------------#

        #---------------------------------------------------------------Actualizar datos-----------------------------------------------------------#
        elif(int(selector)==2):
            validator = True
            while validator:
                try:
                    code = input("Escriba el codigo que quiere actualizar ")
                    code = int(code)
                    validator = False
                except ValueError:
                    print("Input invalido")
                    validator = True
            field = input("""Escriba por el campo que quiere actualizar, recuerde que los campos son
                    codigo,
                    nombre
                    facultad,
                    departamento,
                    idioma,
                    creditos
            """)
            dataOnchange = input(f"Escriba el valor con el cual quiere modificar el campo {field.lower()} de la materia con codigo{code} ")
            try:
                dataOnchange = int(dataOnchange)
            except:
                dataOnchange.lower()
            finally:
                update(field, dataOnchange, code)

        #------------------------------------------------------------------------------------------------------------------------------------------#

        #----------------------------------------------------------------Leer datos---------------------------------------------------------------#
        elif selector==3:
            order = int(input("Si desea ordenar por algun campo en particular oprima 1  y enter, si no oprima 2 y enter. EL ORDEN SIEMPRE SERA DESCENDETE "))
            #Verifica si el input es correcto
            while(order!=1 and order !=2):
                order = int(input(f"{selector} no es una opción valida, por favor digite una opcion valida "))
            if(order==1):
                field = input("""Escriba por el campo que quiere filtrar, recuerde que los campos son
                    codigo,
                    nombre
                    facultad,
                    departamento,
                    idioma,
                    creditos
                """)
                readOrdered(field.lower())
            elif order==2:
                readAllRows()
        #-----------------------------------------------------------------------------------------------------------------------------------------#
        elif selector ==4:
            break;