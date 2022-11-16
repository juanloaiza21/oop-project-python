#TODO all module
import sqlite3 as sql#importar sqlite3 por el nombre sql
from decouple import config#importar config de decouple
import datetime#importar datetime para el manejo de fechas
from console_utils import Console#importar el objeto Console de console_utils

class Estudiante(Console):#declaramos el objeto Estudiante con la herencia console importada de console_utils para la visualizacion estetica de los datos
    def __init__(self, db: str)->None:#deinir el metodo iniciador del objeto con la variables pretinentes
        self.__db = db #definimos self.__db como db para referirnos dentro del objeto y se pone como privada        
        self.__identificacion:int = None#definimos self.__identificacion como tipo None pues todavia no se determian el valor de la variable y se pone como privada
        self.__nombre: str = None#definimos self.__nombre comotipo None pues todavia no se determian el valor de la variable y se pone como privada
        self.__apellido: str = None#definimos self.__apellido como tipo None pues todavia no se determian el valor de la variable y se pone como privada
        self.__carrera: str = None#definimos self.__carrera como tipo None pues todavia no se determian el valor de la variable y se pone como privada
        self.__fechanacimiento: str = None#definimos self.__fechanacimiento como tipo None pues todavia no se determian el valor de la variable y se pone como privada
        self.__fechaingreso: str = None#definimos self.__fechaingreso como tipo None pues todavia no se determian el valor de la variable y se pone como privada
        self.__procedencia: str = None#definimos self.__procedencia como tipo None pues todavia no se determian el valor de la variable y se pone como privada
        self.__correoeletronico: str = None#definimos self.__correoeletronico como tipo None pues todavia no se determian el valor de la variable y se pone como privada
        self.__cantidadmatriculas: int = None#definimos  self.__cantidadmatriculas como tipo None pues todavia no se determian el valor de la variable y se pone como privada
    def identificacionsetter(self,identificacion: int) ->None:#definimos el metodo set para pder guardar el valor de la variable privada identificacion
        self.__identificacion = identificacion# se guarda el valor de identificacion en self.__identificacion
    
    def apellidosetter(self,apellido: str) ->None:#definimos el metodo set para pdoer guardar el valor de la variable privada apellido
        self.__apellido = apellido# se guarda el valor de apellido en self.__apellido
    
    def nombresetter(self,nombre: str) ->None:#definimos el metodo set para poder guardar el valor de la variable privada nombre
        self.__nombre = nombre# se guarda el valor de nombre en self.__nombre
    
    def carrerasetter(self,carrera: str) ->None:#definimos el metodo set para poder guardar el valor de la variable privada carrera
        self.__carrera = carrera# se guarda el valor de carrera en self.__carrera

    def fechanacimientosetter(self,fechanacimiento: int) ->None:#definimos el metodo set para poder guardar el valor de la variable privada fechanacimiento
        self.__fechanacimiento = fechanacimiento# se guarda el valor de fechanacimiento en self.__fechanacimiento

    def fechaingresosetter(self,fechaingreso: int) ->None:#definimos el metodo set para poder guardar el valor de la variable privada fechaingreso
        self.__fechaingreso = fechaingreso# se guarda el valor de fechaingreso en self.__fechaingreso

    def procedenciasetter(self,procedencia: str) ->None:#definimos el metodo set para poder guardar el valor de la variable privada procedencia
        self.__procedencia = procedencia# se guarda el valor de procedencia en self.__procedencia

    def correoeletronicosetter(self,correoeletronico: str) ->None:#definimos el metodo set para poder guardar el valor de la variable privada correoeletronico
        self.__correoeletronico = correoeletronico# se guarda el valor de correoeletronico en self.__correoeletronico

    def cantidadmatriculassetter(self,cantidadmatriculas: int) ->None:#definimos el metodo set para poder guardar el valor de la variable privada cantidadmatriculas
        self.__cantidadmatriculas = cantidadmatriculas# se guarda el valor de cantidadmatriculas en self.__cantidadmatriculas
    
    def cantidadmatriculassetter(self,multidata) ->None:#definimos el metodo set para poder guardar el valor de la variable privada multidata
        self.__multidata = multidata# se guarda el valor de multidata en self.__multidata
#-----------------------------------------------------------------------------------------------
    def identificaciongetter(self)->int:#definimos el metodo get para obtener el valor de la variable privada identificacion
        return self.__identificacion#retorna el valor de self.__identificacion
    
    def apellidogetter(self)->str:#definimos el metodo get para obtener el valor de la variable privada apellido
        return self.__apellido#retorna el valor de self.__apellido
    
    def nombregetter(self)->str:#definimos el metodo get para obtener el valor de la variable privada nombre
        return self.__nombre #retorna el valor de self.__nombre
    
    def carreragetter(self)->str:#definimos el metodo get para obtener el valor de la variable privada carrera
        return self.__carrera #retorna el valor de self.__carrera

    def fechanacimientogetter(self)->str:#definimos el metodo get para obtener el valor de la variable privada fechanacimiento
        return self.__fechanacimiento#retorna el valor de self.__fechanacimiento

    def fechaingresogetter(self)->str:#definimos el metodo get para obtener el valor de la variable privada fechaingreso
        return self.__fechaingreso#retorna el valor de self.__fechaingreso

    def procedenciagetter(self)->str:#definimos el metodo get para obtener el valor de la variable privada procedencia
        return self.__procedencia#retorna el valor de self.__procedencia

    def correoeletronicogetter(self)->str:#definimos el metodo get para obtener el valor de la variable privada correoeletronico
        return self.__correoeletronico#retorna el valor de self.__correoeletronico

    def cantidadmatriculasgetter(self)->int:#definimos el metodo get para obtener el valor de la variable privada cantidadmatriculas
        return self.__cantidadmatriculas #retorna el valor de self.__cantidadmatriculas
    def multidatagetter(self):#definimos el metodo get para obtener el valor de la variable privada multidata
        return self.__multidata#retorna el valor de self.__multidata
    #Inserta la materia
    def __insertRow(self):
        #definicion del metodo para insertar los datos de la materia guardados en la clase
        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__db)#se genera la conexion con la base de datos 
            cursor = conn.cursor()#se inserta un cursor para la insercion de los datos a la tabla estudiante de la base de datos
            instruction = f"INSERT INTO estudiante values({self.__identificacion}, '{self.__nombre}', '{self.__apellido}', '{self.__carrera}', '{self.__fechanacimiento}', '{self.__fechaingreso}','{self.__procedencia}','{self.__correoeletronico}','{self.__cantidadmatriculas}')"
            #se determina la instruccion de insetar los valores de identificacion ,nombre ,apellido ,carrera ,fechanacimiento ,procedencia ,correoeletronico ,cantidadmatriculas a la tabla estudiante por medio de su referencia en la clase
            cursor.execute(instruction)#se pasa la instruccion con el cursor para insertar los datos---------------------------------------------------------------------
            conn.commit();#se verifican que los cambios en la base de datos son validos
            conn.close();#se cierra la conexion con la base de datos
        except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print (e)#mensaje del error que se presenta

    #Pide input por teclado a tráves de consola de los datos, en versión gráfica desaparece
    def __rowGetter(self):#definicion del metodo para pedir la entrada del usuario de cada uno de los datos de la tabla estudiante
        #TODO hacer que la fecha sea DD/MM/AA
        while True:#ciclo generado para verificar que los datos ingresados sean validos
            try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                identificacion = input('numero de identificacion del estudiante: ')#determinar la identificacion del estudiante mediante el input del usuario
                identificacion = identificacion.ljust(10)#especifica la cantidad maxima de caracteres que puede ingresar el usario para la variable identificacion
                while True:#ciclo generado para verificar que la identificacion es valida
                    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        identificacion = int(identificacion)#determinar si la entrada del usuario es un numero
                        break#romper el ciclo de verificar que la identificacion es valida
                    except:#sentecia que se ejecuta en caso de que la identificacion no es valida
                        print("input invalido")#generar mensaje de entrada invalida
                        self.__identificacion = input('numero de identificacion del estudiante: ')#determinar la identificacion del estudiante mediante el input del usuario nuevamente
                        self.__identificacion = identificacion.ljust(10)  #especifica la cantidad maxima de caracteres que puede ingresar el usario para la variable identificacion              
                self.__nombre = input('Nombre del estudiante: ')#determinar el nombre del estudiante mediante el input del usuario
                self.__apellido = input('apellido del estudiante: ')#determinar el apellido del estudiante mediante el input del usuario
                self.__carrera = input('nomrbre de la carrera: ')#determinar la carrera del estudiante mediante el input del usuario
                self.__fechanacimiento = input('fecha de nacimiento del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')#determinar la fecha de nacimiento del estudiante mediante el input del usuario con una epesificacion de formato
                while True:#ciclo generado para verificar que la fecha de nacimiento es valida
                    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        fechanacimientoreal=datetime.datetime.strptime(fechanacimiento,'%d/%m/%Y')#verificamos si la entrada del usuaro se encuentra en el formato indicado mediante la funcion strptime de datatime
                        break#romper el ciclo de verificar que la fecha de nacimiento es valida
                    except:#sentecia que se ejecuta en caso de que la fecha de nacimiento no es valida
                        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                            fechanacimientoreal=datetime.datetime.strptime(fechanacimiento,'%Y/%m/%d')#verificamos si la entrada del usuaro se encuentra en el formato indicado mediante la funcion strptime de datatime
                            break#romper el ciclo de verificar que la fecha de nacimiento es valida
                        except:#sentecia que se ejecuta en caso de que la fecha de nacimiento no es valida
                            print("formato invalido")#generar mensaje de entrada invalida
                            self.__fechanacimiento = input('fecha de nacimiento del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')#determinar la fecha de nacimiento del estudiante mediante el input del usuario con una epesificacion de formato nuevamente
                self.__fechaingreso = input('fecha de ingreso del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')#determinar la fecha de ingreso del estudiante mediante el input del usuario con una epesificacion de formato
                while True:#ciclo generado para verificar que la fecha de ingreso es valida
                    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        fechanacimientoreal2=datetime.datetime.strptime(self.__fechaingreso,'%d/%m/%Y')#verificamos si la entrada del usuaro se encuentra en el formato indicado mediante la funcion strptime de datatime
                        break#romper el ciclo de verificar que la fecha de ingreso es valida
                    except:#sentecia que se ejecuta en caso de que la fecha de ingreso no es valida
                        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                            fechanacimientoreal=datetime.datetime.strptime(self.__fechaingreso,'%Y/%m/%d')#verificamos si la entrada del usuaro se encuentra en el formato indicado mediante la funcion strptime de datatime
                            break#romper el ciclo de verificar que la fecha de ingreso es valida
                        except:#sentecia que se ejecuta en caso de que la fecha de ingreso no es valida
                            print("formato invalido")#generar mensaje de entrada invalida
                            fechanacimiento = input('fecha de ingreso del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')#determinar la fecha de ingreso del estudiante mediante el input del usuario con una epesificacion de formato nuevamente
                self.__procedencia = input('procedencia del estudiante: ')#determinar la procedencia del estudiante mediante el input del usuario
                self.__correoeletronico = input('corre oeletronico del estudiante: ')#determinar el correo eletronico del estudiante mediante el input del usuario
                self.__cantidadmatriculas = input('cantidad de matriculas del estudiante: ')#determinar la cantidad de matriculas del estudiante mediante el input del usuario
                while True:#ciclo generado para verificar que la cantidad de matriculas es valida
                    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        self.__cantidadmatriculas = int(self.__cantidadmatriculas)#determinar si la entrada del usuario es un numero
                        break#romper el ciclo de verificar que la cantidad de matriculas es valida
                    except:#sentecia que se ejecuta en caso de que la cantidad de matriculas no es valida
                        print("input invalido")#generar mensaje de entrada invalida
                        self.__cantidadmatriculas = input('cantidad de matriculas del estudiante: ')#determinar la cantidad de matriculas del estudiante mediante el input del usuario nuevamente
                if (self.__identificacion is None and self.__nombre is None and self.__apellido is None and self.__carrera is None and self.__fechanacimiento is None and self.__fechaingreso is None and self.__procedencia is None and self.__correoeletronico is None and self.__cantidadmatriculas is None):
                    print("Algun dato es vacio, por favor envie todos los datos.")#mensaje de inexistencia de datos al usuario
                else:
                    break
            except ValueError:#sentecia que se ejecuta en caso de que la algun dato seainvalido y no sea detectado
                print('Value error, cantidad de matriculas e identificacion son numeros enteros')#generar mensaje de entradas invalidas

    #pide varias veces los datos
    def __batchRowGetter(self):#definicion del metodo para pedir la entrada del usuario de cada uno de los datos de la tabla estudiante varias veces
        result = []#se crea un lista para el almcenamiento de todos los datos que ingrese el usuario
        secret_runner = "1"#esablecer la variable que sirve para mantener el ciclo que pide los datos varias veces
        counter = 0#establecer el contador que sirve para controlar el numero de veces que el usuario a ingresado datos
        while True: #generar el ciclo que pide los datos varias veces
            try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                identificacion = input('numero de identificacion del estudiante: ')#determinar la identificacion del estudiante mediante el input del usuario
                identificacion = identificacion.ljust(10)#especifica la cantidad maxima de caracteres que puede ingresar el usario para la variable identificacion
                while True:#ciclo generado para verificar que la identificacion es valida
                    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        identificacion = int(identificacion)#determinar si la entrada del usuario es un numero
                        break#romper el ciclo de verificar que la identificacion es valida
                    except:#sentecia que se ejecuta en caso de que la identificacion no es valida
                        print("input invalido")#generar mensaje de entrada invalida
                        identificacion = input('numero de identificacion del estudiante: ')#determinar la identificacion del estudiante mediante el input del usuario nuevamente
                        identificacion = identificacion.ljust(10)   #especifica la cantidad maxima de caracteres que puede ingresar el usario para la variable identificacion                    
                nombre = input('Nombre del estudiante: ')#determinar el nombre del estudiante mediante el input del usuario
                apellido = input('apellido del estudiante: ')#determinar el apellido del estudiante mediante el input del usuario
                carrera = input('nomrbre de la carrera: ')#determinar la carrera del estudiante mediante el input del usuario
                fechanacimiento = input('fecha de nacimiento del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')#determinar la fecha de nacimiento del estudiante mediante el input del usuario con una epesificacion de formato
                while True:#ciclo generado para verificar que la fecha de nacimiento es valida
                    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        fechanacimientoreal=datetime.datetime.strptime(fechanacimiento,'%d/%m/%Y')#verificamos si la entrada del usuaro se encuentra en el formato indicado mediante la funcion strptime de datatime
                        break#romper el ciclo de verificar que la fecha de nacimiento es valida
                    except:#sentecia que se ejecuta en caso de que la fecha de nacimiento no es valida
                        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                            fechanacimientoreal=datetime.datetime.strptime(fechanacimiento,'%Y/%m/%d')#verificamos si la entrada del usuaro se encuentra en el formato indicado mediante la funcion strptime de datatime
                            break#romper el ciclo de verificar que la fecha de nacimiento es valida
                        except:#sentecia que se ejecuta en caso de que la fecha de nacimiento no es valida
                            print("formato invalido")#generar mensaje de entrada invalida
                            fechanacimiento = input('fecha de nacimiento del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')#determinar la fecha de nacimiento del estudiante mediante el input del usuario con una epesificacion de formato nuevamente
                fechaingreso = input('fecha de ingreso del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')#determinar la fecha de ingreso del estudiante mediante el input del usuario con una epesificacion de formato
                while True:#ciclo generado para verificar que la fecha de ingreso es valida
                    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        fechanacimientoreal2=datetime.datetime.strptime(fechaingreso,'%d/%m/%Y')#verificamos si la entrada del usuaro se encuentra en el formato indicado mediante la funcion strptime de datatime
                        break#romper el ciclo de verificar que la fecha de ingreso es valida
                    except:#sentecia que se ejecuta en caso de que la fecha de ingreso no es valida
                        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                            fechanacimientoreal=datetime.datetime.strptime(fechaingreso,'%Y/%m/%d')#verificamos si la entrada del usuaro se encuentra en el formato indicado mediante la funcion strptime de datatime
                            break#romper el ciclo de verificar que la fecha de ingreso es valida
                        except:#sentecia que se ejecuta en caso de que la fecha de ingreso no es valida
                            print("formato invalido")#generar mensaje de entrada invalida
                            fechanacimiento = input('fecha de ingreso del estudiante (formato DD/MM/AAAA,AAAA/MM/DD): ')#determinar la fecha de ingreso del estudiante mediante el input del usuario con una epesificacion de formato nuevamente
                procedencia = input('procedencia del estudiante: ')#determinar la procedencia del estudiante mediante el input del usuario
                correoeletronico = input('corre oeletronico del estudiante: ')#determinar el correo eletronico del estudiante mediante el input del usuario
                cantidadmatriculas = input('cantidad de matriculas del estudiante: ')#determinar la cantidad de matriculas del estudiante mediante el input del usuario
                while True:#ciclo generado para verificar que la cantidad de matriculas es valida
                    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        cantidadmatriculas = int(cantidadmatriculas)#determinar si la entrada del usuario es un numero
                        break#romper el ciclo de verificar que la cantidad de matriculas es valida
                    except:#sentecia que se ejecuta en caso de que la cantidad de matriculas no es valida
                        print("input invalido")#generar mensaje de entrada invalida
                        cantidadmatriculas = input('cantidad de matriculas del estudiante: ')#determinar la cantidad de matriculas del estudiante mediante el input del usuario nuevamente
                result.append((identificacion, nombre, apellido, carrera, fechanacimiento, fechaingreso, procedencia, correoeletronico, cantidadmatriculas))
                #agregar a la lista los datos ingresados por el usuario espesificando si es un entero o un string, en caso de ser un string utilizando el metodo upper() el cual devuelve la misma cadena de caracteres pero en mayusculas
                runner=input('Digite 1 si desea continuar, digite cualquier otra tecla si no. ')#controlador de la continuacion del ciclo por parte de la entrada del usuario
                counter+=1#agregarle una unidad al contador de datos ingresados
                if runner != secret_runner:#sentencia de verificacion para continuar o no el ciclo
                    break #como no se desea continuar el ciclo se rompera en esta sentencia
            except ValueError:#sentecia que se ejecuta en caso de que la algun dato seainvalido y no sea detectado
                    print('Value error, cantidad de matriculas e identificacion son numeros enteros')#generar mensaje de entradas invalidas
        print (f"Usted ha insertado {counter} datos, los cuales son: {result}")#mensaje par el usuario de la cantidad de datos ingresados y cuales son 
        return result#retornar todos los datos que ingreso el usuario

    #Leer todos datos
    def readAllRows(self):#definir el método que se encarga de leer los datos al momento que se el usuario desee ver información
        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__DB)#se genera la conexion con la base de datos 
            cursor = conn.cursor()#se inserta un cursor para la busqueda de los datos de la tabla estudiante de la base de datos
            instruction = f"SELECT * from estudiante"#se determina la intruccion de seleccionar los elementos de la tabla estudiante
            cursor.execute(instruction)#se pasa la instruccion con el cursor para la busqueda de los datos----------------------------------------------
            datos = cursor.fetchall()#utilizamos el metodo fetchall para obtener todas las filas de datos de golpe
            conn.commit();#se verifican que los cambios en la base de datos son validos
            conn.close()#se cierra la conexion con la base de datos
            print(datos);#mensaje de los datos de la tabla estudiante
        except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print (e)#mensaje del error que se presenta

    #Acá se puede filtrar los datos bajo una condición 
    def searchByFilter(self,fieldName, fieldValue):#definir el método que se encarga de leer los datos por medio de un filtro al momento que se el usuario desee ver información especifica
        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__DB)#se genera la conexion con la base de datos 
            cursor = conn.cursor()#se inserta un cursor para la busqueda de los datos de la tabla estudiante de la base de datos
            instruction = f"SELECT * from estudiante WHERE {fieldName}={fieldValue}"#se determina la intruccion de seleccionar los elementos de la tabla estudiante de acuerdo al filtro seleccionado
            cursor.execute(instruction)#se pasa la instruccion con el cursor para la busqueda de los datos------------------------------
            datos = cursor.fetchall()#utilizamos el metodo fetchall para obtener todas las filas de datos de golpe
            conn.commit();#se verifican que los cambios en la base de datos son validos
            conn.close()#se cierra la conexion con la base de datos
            print(datos);#mensaje de los datos espesificados de la tabla estudiante
        except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print (e)#mensaje del error que se presenta   

    #Batch write, escribe multiples lineas de datos a la vez
    def __batchInsertRow(self,dataList):#definicion del metedo para insertar multiples cantidades de datos ingesados por el usuario
        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__DB)#se genera la conexion con la base de datos 
            cursor = conn.cursor()#se inserta un cursor para la insercion de los datos de la tabla estudiante de la base de datos
            instruction = f"INSERT INTO estudiante values(?, ?, ?, ?, ?, ?, ?, ?, ?)"
            #se determina la instruccion de insetar todos los valores ingresados por el usuario
            cursor.executemany(instruction, dataList)#se pasa la instruccion con el cursor para insertar los multiples datos por medio del parametro el cual son todos los datos ingresados por el usuario
            conn.commit();#se verifican que los cambios en la base de datos son validos
            conn.close();#se cierra la conexion con la base de datos
        except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print (e)#mensaje del error que se presenta 

    #Read order, ordena los datos de mayor a menor según el campo que le pidamos 
    def readOrdered(self,field: str):#definicion del metedo para ordenar los datos de la tabla estudiante por medio de un filtro
        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__DB)#se genera la conexion con la base de datos 
            cursor = conn.cursor()#se inserta un cursor para la actualizacion de los datos de la tabla estudiante de la base de datos
            instruction = f"SELECT * from estudiante ORDER BY '{field}' DESC" #Si le quitamos el DESC se ordenara de menor a mayor, "DESC" viene de DESCENDING
            #se determina la instruccion de seleccionar todos los valores ingresados por el usuario mediante el friltro
            cursor.execute(instruction)#se pasa la instruccion con el cursor para seleccionar los multiples datos por medio del parametro dado
            datos = cursor.fetchall()#utilizamos el metodo fetchall para obtener todas las filas de datos de golpe
            conn.commit();#se verifican que los cambios en la base de datos son validos
            conn.close();#se cierra la conexion con la base de datos
            print(datos);#mensaje de los datos requeridos por el usuario ordenados de forma desendente
        except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print (e)#mensaje del error que se presenta 

    #Actualizar datos en un determinado campo de algun estudiante
    """Actualizar materia en diseño lógico."""
    def __update(self,fieldOnChange: str, dataOnChange, iden: int):#definicion del metedo para actualizar los datos de la tabla estudiante por medio de la clave primaria
        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__DB)#se genera la conexion con la base de datos 
            cursor = conn.cursor()#se inserta un cursor para la actualizacion de los datos de la tabla estudiante de la base de datos
            try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                dataOnChange= int(dataOnChange)#comprobacion de que el parametro ingresado es un numero 
                instruction = f"UPDATE estudiante SET '{fieldOnChange}'={dataOnChange} WHERE identificacion={iden}"#Comando de actualización en SQL
            except ValueError:#sentecia que se ejecuta en caso de que se desee actualizar un string
                instruction = f"UPDATE estudiante SET '{fieldOnChange}'='{dataOnChange}' WHERE identificacion={iden}"#Comando de actualización en SQL
            finally:#sentencia que se ejecutara finalizando este proceso
                cursor.execute(instruction)#se pasa la instruccion con el cursor para actualiza los datos por medio del parametro dado
                conn.commit();#se verifican que los cambios en la base de datos son validos
                conn.close();#se cierra la conexion con la base de datos
                print ('Datos actualizados de forma correcta')#mensaje para el usuario
        except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print (e)#mensaje del error que se presenta



    def main(self):#definicion del metodo controldor del modulo estudiante
        
        while True:#sentencia del ciclo prinsipal de la tabla estudiante
            #Revisa si va a añadir datos, leer o actualizar, metodo reutilizable, verifica que el input sea correcto
            validator = True#creacion del boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
            while validator:#generar un ciclo en la tabla de datos estudiante con la funcion de ingresar y verificar la entrada del usuario, el cual solo se rompera cuando la entrada del usuario es valida
                try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                    selector = input(
                    """Bienvendio a estudiante
                    1. Agregar datos. 
                    2. Para actualizar.
                    3. Para obtener información. 
                    4. Para salir. 
                    """
                    )
                    #mensaje para el usuario sobre sus opcciones validas de entrada y entrada del mismo 
                    selector = int(selector)#verificacion de que la entrada es un numero
                    validator = False#cambiar el valor del boleano para finalizar el ciclo que pide la entrada del usuario 
                    while(selector!=1 and selector !=2 and selector !=3 and selector !=4):#generar el ciclo de verificacion de que la entradad es uno de los valores validos
                        selector = input(f"{selector} no es una opción valida, por favor digite una opcion valida ")#en caso de que la entrada no se un valor valido se generara un mensaje de no valides y se pedira nuevamente la entrada
                        selector = int(selector)#verificacion de que la entrada es un numero
                except ValueError:#sentecia que se ejecuta en caso de algun tipo de error 
                    print("Input invalido")#genrar mensaje de entrada invalida
                    validator = True#cambiar el valor del boleano para que el ciclo de ingresar y verificar entrada del usuario no continue 
    
            #-------------------------------------------Creación de estudiante---------------------------------------------------------------------------#
    
            if selector ==1:#sentencia en caso que la entrada del usuario sea 1
                self.clearConsole()#llamar al metodo para limpiar la consola
                validator = True#creacion del boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
                while validator:#generar un ciclo en la tabla de datos estudiante con la funcion de ingresar y verificar la entrada del usuario
                    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        pointer = input(
                        """
                        1. Para un añadir estudiante. 
                        2. Para añadir multiples estudiantes. 
                        """)
                        #mensaje para el usuario sobre sus opcciones validas de entrada y entrada del mismo 
                        pointer = int(pointer)#verificacion de que la entrada es un numero
                        validator = False#cambiar el valor del boleano para finalizar el ciclo que pide la entrada del usuario 
                        while(pointer!=1 and pointer !=2):#generar el ciclo de verificacion de que la entradad es uno de los valores validos
                            pointer = input(f"{pointer} no es una opción valida, por favor digite una opcion valida ")#en caso de que la entrada no se un valor valido se generara un mensaje de no valides y se pedira nuevamente la entrada
                            pointer = int(pointer)#verificacion de que la entrada es un numero
                    except ValueError:#sentecia que se ejecuta en caso de algun tipo de error 
                        print("Input invalido")#generar mensaje de entrada invalida
                        validator = True #cambiar el valor del boleano para que el ciclo de ingresar y verificar entrada del usuario continue 
            #Primer caso del input de escritura, un solo dato
                if int(pointer)==1:#sentencia en caso que la entrada pointed del usuario sea 1, por lo tanto desea añadir solo una materia
                    self.__rowGetter()#llamar al metodo que pide input por teclado a tráves de consola de los datos
                    self.__insertRow()
                    data = [self.__identificacion, self.__nombre, self.__apellido, self.__carrera, self.__fechanacimiento, self.__fechaingreso, self.__procedencia, self.__correoeletronico, self.__cantidadmatriculas]
                    print("Datos insertados: ")#llamar al metodo que inserta el estudiante en la base de datos
                    self.tableEstudiante([data])#lamar al metodo para generar el mensaje para el usuario con los datos ingresados
            #Segundo caso, múltiples datos
                elif(int(pointer)==2):#sentencia en caso que la entrada pointed del usuario sea 2, por lo tanto desea añadir multiples estudiantes
                    data = self.__batchRowGetter()#llamar al metodo que pide input por teclado a tráves de consola de los datos varias veces
                    self.__batchInsertRow(data)#llamar al metodo que inserta todas los estudiantes que a ingresado el usuario en la base de datos e internamenete da el mensaje al usuario


            #---------------------------------------------------------------Actualizar datos-----------------------------------------------------------#
            elif(int(selector)==2):#sentencia en caso que la entrada del usuario sea 2
                validator = True#creacion del boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
                while validator:#generar un ciclo en la tabla de datos estudiante con la funcion de ingresar y verificar la entrada del usuario
                    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        #TODO verificar que el estudiante exista
                        iden = input("Escriba el numero de identificacion del estudiante que quiere actualizar ")#entrada del identificaor o clave primaria del estudiante que se desea actualizr
                        iden = int(iden)#verificacion de que la entrada es un numero
                        validator = False#cambiar el valor del boleano para finalizar el ciclo que pide la entrada del usuario 
                    except ValueError:#sentecia que se ejecuta en caso de algun tipo de error 
                        print("Input invalido")#generar mensaje de entrada invalida
                        validator = True#cambiar el valor del boleano para que el ciclo de ingresar y verificar entrada del usuario continue 
                dataOnchange = int(input(f"Escriba el nuevo valor de matricula "))#entrada del usuario del nuevo valor que desea actualizar
                while True: #ciclo generado para verificar que la actualizacion es valida
                    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        dataOnchange = int(dataOnchange)#verificar que la entrada es un numero
                        self.__update('cantidadmatriculas', dataOnchange, iden)#se llama a la funcion encargada para que genere la acualizacion
                        break#romper el ciclo de verificar que la actualizacion es valida
                    except ValueError:#sentecia que se ejecuta en caso de algun tipo de error
                        print(f'{dataOnchange} invalido')# mensaje de actualizacion invalida

            #------------------------------------------------------------------------------------------------------------------------------------------#

            #----------------------------------------------------------------Leer datos---------------------------------------------------------------#
            elif selector==3:#sentencia en caso que la entrada del usuario sea 3
                while True: #ciclo generado para verificar que la entrada del usuario es valida
                    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        selector = int(input("Para ver sus datos escriba el numero de la identificacion "))#entrada del usuario de la identificacion de un estudiante existente
                        self.searchByFilter('identificacion', selector)#se llama a la funcion encargada para que lea los datos y mande el mensaje al usuario
                        break#romper el ciclo de verificar que la entrada del usuario es valida
                    except ValueError:#sentecia que se ejecuta en caso de algun tipo de error
                        print("dato inválido")# mensaje de indentificacion invalida

                
            #-----------------------------------------------------------------------------------------------------------------------------------------#
            elif selector ==4:#sentencia en caso que la entrada del usuario sea 4
                break;#con 4 como la entrada del usuario se rompera el ciclo prinsipal y asi salir a la pantalla del controlador
