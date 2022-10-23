#TODO all module
import sqlite3 as sql
from decouple import config
import datetime

DB = config('DB_NAME')

#Crea tablas manualmente, automatizar
def createTeable():
    try:
        conn = sql.connect(DB)
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


        
#Inserta la materia
def insertRow(identificacion : int, nombre: str, apellido: str, carrera: str, fechanacimiento: str, fechaingreso: str, procedencia: str, correoeletronico: str, cantidadmatriculas: int):
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        instruction = f"INSERT INTO estudiante values({identificacion}, '{nombre}', '{apellido}', '{carrera}', '{fechanacimiento}', '{fechaingreso}','{procedencia}','{correoeletronico}','{cantidadmatriculas}')"
        cursor.execute(instruction)
        conn.commit();
        conn.close();
    except sql.Error as e:
        print (e)

#Pide input por teclado a tráves de consola de los datos, en versión gráfica desaparece
def rowGetter():
    #TODO hacer que la fecha sea DD/MM/AA
    while True:
        try:
            identificacion = input('numero de identificacion del estudiante: ')
            identificacion = identificacion.ljust(10)
            while True:
                try:
                    identificacion = int(identificacion)
                    break
                except:
                    print("input invalido")
                    identificacion = input('numero de identificacion del estudiante: ')
                    identificacion = identificacion.ljust(10)                
            nombre = input('Nombre del estudiante: ')
            apellido = input('apellido del estudiante: ')
            carrera = input('nomrbre de la carrera: ')
            fechanacimiento = input('fecha de nacimiento del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')
            while True:
                try:
                    fechanacimientoreal=datetime.datetime.strptime(fechanacimiento,'%d/%m/%Y')
                    break
                except:
                    try:
                        fechanacimientoreal=datetime.datetime.strptime(fechanacimiento,'%Y/%m/%d')
                        break
                    except:
                        print("formato invalido")
                        fechanacimiento = input('fecha de nacimiento del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')
            fechaingreso = input('fecha de ingreso del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')
            while True:
                try:
                    fechanacimientoreal2=datetime.datetime.strptime(fechaingreso,'%d/%m/%Y')
                    break
                except:
                    try:
                        fechanacimientoreal=datetime.datetime.strptime(fechaingreso,'%Y/%m/%d')
                        break
                    except:
                        print("formato invalido")
                        fechanacimiento = input('fecha de ingreso del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')
            procedencia = input('procedencia del estudiante: ')
            correoeletronico = input('corre oeletronico del estudiante: ')
            cantidadmatriculas = input('cantidad de matriculas del estudiante: ')
            while True:
                try:
                    cantidadmatriculas = int(cantidadmatriculas)
                    break
                except:
                    print("input invalido")
                    cantidadmatriculas = input('cantidad de matriculas del estudiante: ')
            return (identificacion, nombre.upper(), apellido.upper(), carrera.upper(), fechanacimiento.upper(), fechaingreso.upper(), procedencia.upper(),correoeletronico.upper(),cantidadmatriculas)
        except ValueError:
            print('Value error, cantidad de matriculas e identificacion son numeros enteros')

#pide varias veces los datos
def batchRowGetter():
    result = []
    secret_runner = "1"
    counter = 0
    while True: 
        try:
            identificacion = input('numero de identificacion del estudiante: ')
            identificacion = identificacion.ljust(10)
            while True:
                try:
                    identificacion = int(identificacion)
                    break
                except:
                    print("input invalido")
                    identificacion = input('numero de identificacion del estudiante: ')
                    identificacion = identificacion.ljust(10)                
            nombre = input('Nombre del estudiante: ')
            apellido = input('apellido del estudiante: ')
            carrera = input('nomrbre de la carrera: ')
            fechanacimiento = input('fecha de nacimiento del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')
            while True:
                try:
                    fechanacimientoreal=datetime.datetime.strptime(fechanacimiento,'%d/%m/%Y')
                    break
                except:
                    try:
                        fechanacimientoreal=datetime.datetime.strptime(fechanacimiento,'%Y/%m/%d')
                        break
                    except:
                        print("formato invalido")
                        fechanacimiento = input('fecha de nacimiento del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')
            fechaingreso = input('fecha de ingreso del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')
            while True:
                try:
                    fechanacimientoreal2=datetime.datetime.strptime(fechaingreso,'%d/%m/%Y')
                    break
                except:
                    try:
                        fechanacimientoreal=datetime.datetime.strptime(fechaingreso,'%Y/%m/%d')
                        break
                    except:
                        print("formato invalido")
                        fechanacimiento = input('fecha de ingreso del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')
            procedencia = input('procedencia del estudiante: ')
            correoeletronico = input('corre oeletronico del estudiante: ')
            cantidadmatriculas = input('cantidad de matriculas del estudiante: ')
            while True:
                try:
                    cantidadmatriculas = int(cantidadmatriculas)
                    break
                except:
                    print("input invalido")
                    cantidadmatriculas = input('cantidad de matriculas del estudiante: ')
            result.append((identificacion, nombre, apellido, carrera, fechanacimiento, fechaingreso, procedencia, correoeletronico, cantidadmatriculas))
            runner=input('Digite 1 si desea continuar, digite cualquier otra tecla si no. ')
            counter+=1
            if runner != secret_runner:
                break 
        except ValueError:
                print('Value error, cantidad de matriculas e identificacion son numeros enteros')
    print (f"Usted ha insertado {counter} datos, los cuales son: {result}")
    return result

#Leer todos datos
def readAllRows():
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        instruction = f"SELECT * from estudiante"
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
        instruction = f"SELECT * from estudiante WHERE {fieldName}={fieldValue}"
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
        instruction = f"INSERT INTO estudiante values(?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.executemany(instruction, dataList)
        conn.commit();
        conn.close();
    except sql.Error as e:
        print (e)   

#Read order, ordena los datos de mayor a menor según el campo que le pidamos 
def readOrdered(field: str):
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        instruction = f"SELECT * from estudiante ORDER BY '{field}' DESC" #Si le quitamos el DESC se ordenara de menor a mayor, "DESC" viene de DESCENDING
        cursor.execute(instruction)
        datos = cursor.fetchall()
        conn.commit();
        conn.close()
        print(datos);
    except sql.Error as e:
        print (e) 

#Actualizar datos en un determinado campo de algun estudiante
"""Actualizar materia en diseño lógico."""
def update(fieldOnChange: str, dataOnChange, iden: int):
    try:
        conn = sql.connect(DB)
        cursor = conn.cursor()
        try:
            dataOnChange= int(dataOnChange)
            instruction = f"UPDATE estudiante SET '{fieldOnChange}'={dataOnChange} WHERE identificacion={iden}"
        except ValueError:
            instruction = f"UPDATE estudiante SET '{fieldOnChange}'='{dataOnChange}' WHERE identificacion={iden}" #Comando de actualización en SQL
        finally:
            cursor.execute(instruction)
            conn.commit();
            conn.close()
            print ('Datos actualizados de forma correcta')
    except sql.Error as e:
        print (e)

def main():
    
    while True:
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
        #-------------------------------------------Creación de estudiante---------------------------------------------------------------------------#
        if selector ==1:
            validator = True
            while validator:
                try:
                    pointer = input("Si desea solo añadir un estudiante digite '1' y luego enter, si desea registrar multiples estudiantes digite '2' y luego enter. ")
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
                insertRow(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
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
                    #TODO verificar que el estudiante exista
                    iden = input("Escriba el numero de identificacion del estudiante que quiere actualizar ")
                    iden = int(iden)
                    validator = False
                except ValueError:
                    print("Input invalido")
                    validator = True
            dataOnchange = int(input(f"Escriba el nuevo valor de matricula "))
            while True: 
                try:
                    dataOnchange = int(dataOnchange)
                    update('cantidadmatriculas', dataOnchange, iden)
                    break
                except ValueError:
                    print(f'{dataOnchange} invalido')

        #------------------------------------------------------------------------------------------------------------------------------------------#

        #----------------------------------------------------------------Leer datos---------------------------------------------------------------#
        elif selector==3:
            while True: 
                try:
                    selector = int(input("Para ver sus datos escriba el numero de la identificacion "))
                    searchByFilter('identificacion', selector)
                    break
                except ValueError:
                    print("dato inválido")

            
        #-----------------------------------------------------------------------------------------------------------------------------------------#
        elif selector ==4:
            break;

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
