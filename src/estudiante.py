from datetime import datetime
import sqlite3 as sql
from decouple import config
import datetime
from console_utils import Console

DB = config('DB_NAME')

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

class Estudiante(Console):
    def __init__(self)->None:
        pass            
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
    #Retorna todos los datos del estudiante en forma de tupla con tamaño = 9.
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
                #Validador fecha nacimiento
                while True:
                    try:
                        fechanacimiento = input('fecha de nacimiento del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ') #Fecha en formato ISO 8601
                        fechanacimiento=datetime.datetime.strptime(fechanacimiento,'%d/%m/%Y')#Fecha en formato ISO 8601
                        break
                    except:
                        try:
                            fechanacimiento=datetime.datetime.strptime(fechanacimiento,'%Y/%m/%d')#Fecha en formato ISO 8601
                            break
                        except:
                            print("formato invalido")
                #Validador fecha ingreso
                while True:
                    try:
                        fechaingreso = input('fecha de ingreso del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')#Fecha en formato ISO 8601
                        fechaingreso=datetime.datetime.strptime(fechaingreso,'%d/%m/%Y')#Fecha en formato ISO 8601
                        break
                    except:
                        try:
                            fechaingreso=datetime.datetime.strptime(fechaingreso,'%Y/%m/%d')#Fecha en formato ISO 8601
                            break
                        except:
                            print("formato invalido")
                procedencia = input('procedencia del estudiante: ')
                correoeletronico = input('correo eletronico del estudiante: ')
                while True:
                    try:
                        cantidadmatriculas = input('cantidad de matriculas del estudiante: ')
                        cantidadmatriculas = int(cantidadmatriculas)
                        break
                    except:
                        print("input invalido")
                if (identificacion is None and nombre is None and apellido is None and carrera is None and fechanacimiento is None and fechaingreso is None and procedencia is None and correoeletronico is None and cantidadmatriculas is None):
                    print("Algun dato es vacio, por favor envie todos los datos.")
                else:
                    return (identificacion, nombre.upper(), apellido.upper(), carrera.upper(), fechanacimiento.isoformat(), fechaingreso.isoformat(), procedencia.upper(),correoeletronico.upper(),cantidadmatriculas)
            except ValueError:
                print('Value error, cantidad de matriculas e identificacion son numeros enteros')

    #pide varias veces los datos
    #Retorna retorna una lista de tuplas con todos los datos de cada estudiante estudiante, tuplas con tamaño= 9.
    def batchRowGetter(self):
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
            #Validador fecha nacimiento
                while True:
                    try:
                        fechanacimiento = input('fecha de nacimiento del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')
                        fechanacimiento=datetime.datetime.strptime(fechanacimiento,'%d/%m/%Y')
                        break
                    except:
                        try:
                            fechanacimiento=datetime.datetime.strptime(fechanacimiento,'%Y/%m/%d')
                            break
                        except:
                            print("formato invalido")
                #Validador fecha ingreso
                while True:
                    try:
                        fechaingreso = input('fecha de ingreso del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')
                        fechaingreso=datetime.datetime.strptime(fechaingreso,'%d/%m/%Y')
                        break
                    except:
                        try:
                            fechaingreso=datetime.datetime.strptime(fechaingreso,'%Y/%m/%d')
                            break
                        except:
                            print("formato invalido")
                procedencia = input('procedencia del estudiante: ')
                correoeletronico = input('corre oeletronico del estudiante: ')
                while True:
                    try:
                        cantidadmatriculas = input('cantidad de matriculas del estudiante: ')
                        cantidadmatriculas = int(cantidadmatriculas)
                        break
                    except:
                        print("input invalido")
                if (identificacion is None and nombre is None and apellido is None and carrera is None and fechanacimiento is None and fechaingreso is None and procedencia is None and correoeletronico is None and cantidadmatriculas is None):
                    print("Algun dato es vacio, por favor envie todos los datos.")
                else:    
                    result.append((identificacion, nombre.upper(), apellido.upper(), carrera.upper(), fechanacimiento.isoformat(), fechaingreso.isoformat(), procedencia.upper(), correoeletronico.upper(), cantidadmatriculas))
                    runner=input('Digite 1 si desea continuar, digite cualquier otra tecla si no. ')
                    counter+=1
                    if runner != secret_runner:
                        break 
            except ValueError:
                    print('Value error, cantidad de matriculas e identificacion son numeros enteros')
        print (f"Usted ha insertado {counter} datos, los cuales son:")
        self.tableEstudiante(result)
        return result

    #Leer todos datos
    #Retorna una lista de tuplas tamaño = 9 con los datos del estudiante
    def readAllRows():
        try:
            conn = sql.connect(DB)
            cursor = conn.cursor()
            instruction = f"SELECT * from estudiante"
            cursor.execute(instruction)
            datos = cursor.fetchall()
            conn.commit();
            conn.close()
            return(datos);
        except sql.Error as e:
            print (e)

    #Acá se puede filtrar los datos bajo una condición 
    #Field by name puede ser cualquier tipo de dato, igual que field value, no poseen validaciones ya que están siendo usados especificamente.
    #Retorna una lista de tuplas tamaño = 9 que contiene los datos del estudiante que hace match con los datos pedidos
    def searchByFilter(self, fieldName, fieldValue):
        try:
            conn = sql.connect(DB)
            cursor = conn.cursor()
            instruction = f"SELECT * from estudiante WHERE {fieldName}={fieldValue}"
            cursor.execute(instruction)
            datos = cursor.fetchall()
            conn.commit();
            conn.close()
            self.tableEstudiante(datos);
        except sql.Error as e:
            print (e)   

    #Batch write, escribe multiples lineas de datos a la vez
    #Recibe los datos de BatchRowGetter
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
    #Retorna una lista de tuplas tamaño = 9 que contiene los datos de los estudiantes de manera ordenada según el campo que siemrpe será un string
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
    #Pide el fieldOnChange como un string, la data puede ser cualquier tipo de dato, y la identificación que responde al nombre iden
    #Retorna un mensaje de felicitación si todo fue correcto
    def update(self, fieldOnChange: str, dataOnChange, iden: int):
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

    def main(self):
        NoneType = type(None)
        while True:
            #Revisa si va a añadir datos, leer o actualizar, metodo reutilizable, verifica que el input sea correcto
            validator = True
            while validator:
                try:
                    selector = input(
                    """Bienvendio a estudiante
                    1. Agregar datos. 
                    2. Para actualizar.
                    3. Para obtener información. 
                    4. Para salir. 
                    """
                    )
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
                self.clearConsole()
                validator = True
                while validator:
                    try:
                        pointer = input(
                        """
                        1. Para un añadir estudiante. 
                        2. Para añadir multiples estudiantes. 
                        """)
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
                    data = self.rowGetter()
                    self.insertRow(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
                    print("Datos insertados: ")
                    self.tableEstudiante([data])
            #Segundo caso, múltiples datos
                elif(int(pointer)==2):
                    data = self.batchRowGetter()
                    self.batchInsertRow(data)
            #-----------------------------------------------------------------------------------------------------------------------------------------#

            #---------------------------------------------------------------Actualizar datos-----------------------------------------------------------#
            elif(int(selector)==2):
                validator = True
                self.clearConsole()
                while validator:
                    try:
                        #TODO verificar que el estudiante exista
                        iden = input("Escriba el numero de identificacion del estudiante que quiere actualizar ")
                        iden = int(iden)
                        validator = False
                    except ValueError:
                        print("Input invalido")
                        validator = True
                dataOnchange = input(f"Escriba el nuevo valor de matricula ")
                dataOnchange = int(dataOnchange)
                while True: 
                    try:
                        dataOnchange = int(dataOnchange)
                        self.update('cantidadmatriculas', dataOnchange, iden)
                        break
                    except ValueError:
                        print(f'{dataOnchange} invalido')

            #------------------------------------------------------------------------------------------------------------------------------------------#

            #----------------------------------------------------------------Leer datos---------------------------------------------------------------#
            elif selector==3:
                while True: 
                    try:
                        selector = input("Para ver sus datos escriba el numero de la identificacion: ")
                        selector = int(selector)
                        self.searchByFilter('identificacion', selector)
                        break
                    except ValueError:
                        print("dato inválido")

                
            #-----------------------------------------------------------------------------------------------------------------------------------------#
            elif selector ==4:
                break;

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------#