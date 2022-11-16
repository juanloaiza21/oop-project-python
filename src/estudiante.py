from datetime import datetime
import sqlite3 as sql
import datetime
from console_utils import Console


class estudiante(Console):
    def __init__(self, db: str)->None:
        self.__db = db            
        self.__identificacion:int = None
        self.__nombre: str = None
        self.__apellido: str = None
        self.__carrera: str = None
        self.__fechanacimiento: str = None
        self.__fechaingreso: str = None
        self.__procedencia: str = None
        self.__correoeletronico: str = None
        self.__cantidadmatriculas: int = None
        self.__multidata=[]

        def identificacionsetter(self,identificacion: int) ->None:
        self.__identificacion = identificacion
    
    def apellidosetter(self,apellido: str) ->None:
        self.__apellido = apellido
    
    def nombresetter(self,nombre: str) ->None:
        self.__nombre = nombre
    
    def carrerasetter(self,carrera: str) ->None:
        self.__carrera = carrera

    def fechanacimientosetter(self,fechanacimiento: int) ->None:
        self.__fechanacimiento = fechanacimiento

    def fechaingresosetter(self,fechaingreso: int) ->None:
        self.__fechaingreso = fechaingreso

    def procedenciasetter(self,procedencia: str) ->None:
        self.__procedencia = procedencia

    def correoeletronicosetter(self,correoeletronico: str) ->None:
        self.__correoeletronico = correoeletronico

    def cantidadmatriculassetter(self,cantidadmatriculas: int) ->None:
        self.__cantidadmatriculas = cantidadmatriculas
    
    def cantidadmatriculassetter(self,multidata) ->None:
        self.__multidata = multidata
#-----------------------------------------------------------------------------------------------
    def identificaciongetter(self)->int:
        return self.__identificacion
    
    def apellidogetter(self)->str:
        return self.__apellido
    
    def nombregetter(self)->str:
        return self.__nombre 
    
    def carreragetter(self)->str:
        return self.__carrera

    def fechanacimientogetter(self)->str:
        return self.__fechanacimiento

    def fechaingresogetter(self)->str:
        return self.__fechaingreso

    def procedenciagetter(self)->str:
        return self.__procedencia

    def correoeletronicogetter(self)->str:
        return self.__correoeletronico

    def cantidadmatriculasgetter(self)->int:
        return self.__cantidadmatriculas 
    def multidatagetter(self):
        return self.__multidata
    #Inserta la materia
    def __insertRow(self):
        try:
            conn = sql.connect(self.__db)
            cursor = conn.cursor()
            instruction = f"INSERT INTO estudiante values({self.__carrera}, '{self.__nombre}', '{self.__apellido}', '{self.__fechanacimiento}', '{self.__fechaingreso}', '{self.__procedencia}','{self.__correoeletronico}','{self.__cantidadmatriculas}','{self.__identificacion}')"
            cursor.execute(instruction)
            conn.commit();
            conn.close();
        except sql.Error as e:
            print (e)

    #Pide input por teclado a tráves de consola de los datos, en versión gráfica desaparece
    def __rowGetter(self):
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
                correoeletronico = input('correo eletronico del estudiante: ')
                while True:
                    try:
                        cantidadmatriculas = input('cantidad de matriculas del estudiante: ')
                        cantidadmatriculas = int(cantidadmatriculas)
                        break
                    except:
                        print("input invalido")
                if not (identificacion and nombre and apellido and carrera and fechanacimiento and fechaingreso and procedencia and correoeletronico and cantidadmatriculas):
                    print("Algun dato es vacio, por favor envie todos los datos.")
                else:
                    estudiante.cantidadmatriculassetter(cantidadmatriculas)
                    estudiante.correoeletronicosetter(correoeletronico.upper())
                    estudiante.procedenciasetter(procedencia.upper())
                    estudiante.fechaingresosetter(fechaingreso)
                    estudiante.fechanacimientosetter(fechanacimiento)
                    estudiante.carrerasetter(carrera.upper())
                    estudiante.nombresetter(nombre.upper())
                    estudiante.identificacionsetter(identificacion)
                    estudiante.apellidosetter(apellido.upper())
                    break
                    #return (identificacion, nombre.upper(), apellido.upper(), carrera.upper(), fechanacimiento.isoformat(), fechaingreso.isoformat(), procedencia.upper(),correoeletronico.upper(),cantidadmatriculas)
            except ValueError:
                print('Value error, cantidad de matriculas e identificacion son numeros enteros')

    #pide varias veces los datos
    def __batchRowGetter(self):
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
                if not (identificacion and nombre and apellido and carrera and fechanacimiento and fechaingreso and procedencia and correoeletronico and cantidadmatriculas):
                    print("Algun dato es vacio, por favor envie todos los datos.")
                else:    
                    self.__multidata.append((identificacion, nombre.upper(), apellido.upper(), carrera.upper(), fechanacimiento.isoformat(), fechaingreso.isoformat(), procedencia.upper(), correoeletronico.upper(), cantidadmatriculas))
                    runner=input('Digite 1 si desea continuar, digite cualquier otra tecla si no. ')
                    counter+=1
                    if runner != secret_runner:
                        break 
            except ValueError:
                    print('Value error, cantidad de matriculas e identificacion son numeros enteros')
        print (f"Usted ha insertado {counter} datos, los cuales son:")
        self.tableEstudiante(self.__multidata)
        return self.__multidata

    #Leer todos datos
    def readAllRows(self):
        try:
            conn = sql.connect(self.__db)
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
    def searchByFilter(self,fieldName, fieldValue):
        try:
            conn = sql.connect(self.__db)
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
    def __batchInsertRow(self,dataList):
        try:
            conn = sql.connect(self.__db)
            cursor = conn.cursor()
            instruction = f"INSERT INTO estudiante values(?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.executemany(instruction, dataList)
            conn.commit();
            conn.close();
        except sql.Error as e:
            print (e)   

    #Read order, ordena los datos de mayor a menor según el campo que le pidamos 
    def readOrdered(self,field: str):
        try:
            conn = sql.connect(self.__db)
            cursor = conn.cursor()
            instruction = f"SELECT * from estudiante ORDER BY '{field}' DESC" #Si le quitamos el DESC se ordenara de menor a mayor, "DESC" viene de DESCENDING
            cursor.execute(instruction)
            datos = cursor.fetchall()
            conn.commit();
            conn.close()
            self.tableMaterias(datos);
        except sql.Error as e:
            print (e) 

    #Actualizar datos en un determinado campo de algun estudiante
    """Actualizar materia en diseño lógico."""
    def __update(self,fieldOnChange: str, dataOnChange, iden: int):
        try:
            conn = sql.connect(self.__db)
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
                    self.__rowGetter()
                    self.__insertRow()
                    data = [self.__identificacion, self.__nombre, self.__apellido, self.__carrera, self.__fechanacimiento, self.__fechaingreso, self.__procedencia, self.__correoeletronico, self.__cantidadmatriculas]
                    print("Datos insertados: ")
                    self.tableEstudiante([data])
            #Segundo caso, múltiples datos
                elif(int(pointer)==2):
                    data = self.__batchRowGetter()
                    self.__batchInsertRow(data)
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
                        self.__update('cantidadmatriculas', dataOnchange, iden)
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
