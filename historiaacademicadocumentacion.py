TODO all module
import sqlite3 as sql#importar sqlite3 por el nombre sql
from time import sleep#importar sleep de time para poder tener un manejo de tiempo
from decouple import config#importar config de decouple
from materia import readOrdered as allMaterias # importar el metodo readOrdered del modulo materia para ser ejecutado por el nombre de allMaterias
from materia import searchByFilter as materiasFilter# importar el metodo searchByFilter del modulo materia para ser ejecutado por el nombre de materiasFilter
from console_utils import clearConsole, tableHistoriaAcad# importar el metodo tableHistoriaAcad y clearConsole del modulo console_utils 

DB = config('DB_NAME')#se determina una variable para referirse a la base de datos


#Crea tablas manualmente, automatizar; TODO generar modulo que cree toda la DB y meterlo en el controlador como primer paso al correr la app
def createTeable():#definicion del metodo para crear la tabla de datos
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        conn = sql.connect(DB)#se genera la conexion con la base de datos 
        cursor = conn.cursor()#se inserta un cursor para la insercion de los datos que estaran presente en tabla acadhistory de la base de datos
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS acadhistory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code_materia  INTEGER NOT NULL,
                id_estudiante INTEGER NOT NULL,
                nota REAL,
                creditos_cursados INTEGER,
                FOREIGN KEY(id_estudiante) REFERENCES estudiante(identificacion),
                FOREIGN KEY(code_materia) REFERENCES materias(codigo)
                )"""
        );
        #se pasa la instruccion a la base de datos de crear la tabla acadhistory en caso de no existir con las subtablas id ,code_materia ,id_estudiante ,nota ,creditos_cursados y su respectivo tipo de entrada
        #id esta declarada como prymary key al ser el dato identificador por no poder repetirse en ningun caso
        conn.commit();#se verifican que los cambios en la base de datos son validos
        conn.close();#se cierra la conexion con la base de datos
    except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
        print(e)#mensaje del error que se presenta

#----------------------------------------------------------------Inserta las notas de la materia-------------------------------------------------------------------

def creditsRef(idMateria: int):#definicion del metodo para retornar la infromacion de los creditos de las materias
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        data = materiasFilter('codigo', idMateria)#llamamos al metodo de idMaterias importado de materias para filtrar la informacion deseada y la determina en una variable
        return data[0][5]#retorna un dato en espesifico de los datos
    except:#sentecia que se ejecuta en caso de que Codigo de la materia inexistente
        print("Codigo de la materia inexistente")#mensaje al usuario de entrada invalida

#Crear historia academica en documentación
def insertRow(codigo: int, id_estudiante: int, score: float):
    #definicion del metodo para insertar los datos de la historia academica con sus variables y su respectivo tipo de variable para la verificacion como parametros
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        conn = sql.connect(DB)#se genera la conexion con la base de datos 
        conn.execute('PRAGMA foreign_keys = ON') #Valida las llaves extranjeras, es decir la existencia del estudiante o la amteria, si no existe da error
        cursor = conn.cursor()#se inserta un cursor para la insercion de los datos a la tabla acadhistory de la base de datos
        creditos= creditsRef(codigo)#llamamos el metodo para retornar la infromacion de los creditos de las materias y referirlo a una variable
        instruction = f"INSERT INTO acadhistory(code_materia, id_estudiante, nota, creditos_cursados) VALUES ({codigo},{id_estudiante}, {score}, {creditos})"
        #se determina la instruccion de insetar los valores de id ,code_materia ,id_estudiante ,nota ,creditos_cursados a la tabla acadhistory
        cursor.execute(instruction)#se pasa la instruccion con el cursor para insertar los datos----------------------
        conn.commit();#se verifican que los cambios en la base de datos son validos
        conn.close();#se cierra la conexion con la base de datos
        print("Datos añadidos: ")#mensaje para el usuario
        tableHistoriaAcad([(0,codigo, id_estudiante, score, creditos)])#muestra los datos insertados en consola con el metodo importadp de console_utils de forma mas estetica
    except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
        print (e)#mensaje del error que se presenta
        print('Probablemente no exista el estudiante o la materia, revise por favor los datos que ingreso y vuelva a intentar. Si sí existen, es que primero debe eliminar la materia, para que se actualice con los nuevos datos')
        #mensaje para el usuario sobre su posible dato invalido
#Lector del input por parte del usuario
def rowGetter():#definicion del metodo para pedir la entrada del usuario de cada uno de los datos de la tabla acadhistory
    while True:#ciclo generado para verificar que los datos ingresados sean validos
        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
            print("El codigo de la materia y el Id del estudiante deben existir, si no, habra error")#mensaje de instrucciones para llenar los datos
            codigo = input('Codigo de la materia: ')#determinar el Codigo de la materia ya existente mediante el input del usuario
            codigo = codigo.ljust(10)#especifica la cantidad maxima de caracteres que puede ingresar el usario para la variable codigo
            idEstudiante = input('Id del estudiante ')#determinar el Id del estudiante ya existente mediante el input del usuario
            selector = int(input("¿Desea agregar nota? 1. Si. 2. No"))#determinar la desicion de ingresar nota o no mediante el input del usuario
            if selector ==1:#sentencia en caso que la entrada del usuario sea 1
                nota = input('Nota del estudiante ')#entrada del usario del float de nota del estudiante
            else:#sentencia en caso que la entrada del usuario sea 2 o cualquier otra
                nota = 0.0#determinacion del float de nota del estudiante
            nota = float(nota)#verificacion que la entrada del usuario de la variable nota es un float
            idEstudiante = int(idEstudiante)#verificacion que la entrada del usuario de la variable idEstudiante es un entero
            codigo = int(codigo)#verificacion que la entrada del usuario de la variable codigo es un entero
            return (codigo, idEstudiante, nota)#retorna los datos ingresados por el usuario para funcionar como parametro en otros metodos
        except ValueError:#sentecia que se ejecuta en caso de algun tipo de error 
            print("Dato(s) invalido")#mensaje al usuario de entrada invalida

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------Lector del modulo de historia academica----------------------------------------------------------#

#Esta función debe traer todos las notas de un id
def acadHistoryById(id: int):#definicion del metodo para pedir la informacion del modulo de historia academica de un estudiante
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        conn = sql.connect(DB)#se genera la conexion con la base de datos 
        cursor = conn.cursor()#se inserta un cursor para la seleccionar los datos a la tabla acadhistory de la base de datos
        instruction = f"SELECT * from acadhistory WHERE id_estudiante={id} ORDER BY nota DESC"
        #se determina la instruccion de seleccionar los valores donde id_estudiante debe ser igual al parametro ingresado
        cursor.execute(instruction)#se pasa la instruccion con el cursor para insertar los datos----------------------
        datos = cursor.fetchall()#utilizamos el metodo fetchall para obtener todas las filas de datos de golpe
        conn.commit();#se verifican que los cambios en la base de datos son validos
        conn.close()#se cierra la conexion con la base de datos
        return datos;#retorna la informacion del modulo de historia academica de un estudiante 
    except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
        print (e)#mensaje del error que se presenta

#Esta función calcula el promedio
def prom (data):#definicion del metodo que calcula el promedipo de un estudiante con las materias del estudiante como parametro
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        numeroMaterias = len(data)#se determina una variable a la longitud de los datos ingresados a la funcion
        sumaNotas = 0#se termina un valor por defecto a las notas del estudiante
        for i in range(numeroMaterias):#se genera un ciclo para que calcule el promedio
            sumaNotas += data[i][3]#se suman todas las notas de las materias del estudiante
        return sumaNotas/numeroMaterias#se retorna el calculo del promedio
    except:#sentecia que se ejecuta en caso de algun tipo de error 
        print("Try again")#mensaje para el usuario
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------Metodo de actualizacion--------------------------------------------------------------------------#
def update(fieldOnChange: str, dataOnChange, code: int, dataOnChange2: int):#definicion del metedo para actualizar los datos de la tabla acadhistory por medio de la clave primaria
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        conn = sql.connect(DB)#se genera la conexion con la base de datos 
        cursor = conn.cursor()#se inserta un cursor para la actualizar los datos a la tabla acadhistory de la base de datos
        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
            dataOnChange= float(dataOnChange)#verificacion de que el parametro del metodo en caso de que sea un float
            instruction = f"UPDATE acadhistory SET '{fieldOnChange}'={dataOnChange} WHERE code_materia={dataOnChange2} AND id_estudiante={code}"
            #se determina la instruccion de actualizar el valor deseado donde id_estudiante debe ser igual al parametro ingresado y code_materia debe ser igual al parametro ingresado
        except ValueError:
            instruction = f"UPDATE acadhistory SET '{fieldOnChange}'='{dataOnChange}' WHERE code_materia={code} AND id_estudiante={dataOnChange2}" #Comando de actualización en SQL
            #se determina la instruccion de actualizar el valor deseado donde id_estudiante debe ser igual al parametro ingresado y code_materia debe ser igual al parametro ingresado
        finally:#sentencia que se desea ejecuatar al finalizar este proceso
            cursor.execute(instruction)#se pasa la instruccion con el cursor para actualizar los datos
            conn.commit();#se verifican que los cambios en la base de datos son validos
            conn.close()#se cierra la conexion con la base de datos
            print ('Datos actualizados de forma correcta')#mensaje para el usuario
    except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
        print (e)#mensaje del error que se presenta

def rowUpdateGetter():
    while True:
        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
            print("El codigo de la materia y el Id del estudiante deben existir, si no, habra error")#mensaje de instrucciones para llenar los datos
            codigo = input('Codigo de la materia: ')#determinar el Codigo de la materia ya existente mediante el input del usuario
            codigo = codigo.ljust(10)#especifica la cantidad maxima de caracteres que puede ingresar el usario para la variable codigo
            idEstudiante = input('Id del estudiante ')#determinar el Id del estudiante ya existente mediante el input del usuario
            nota = input('Nota del estudiante ')#entrada del usario del float de nota del estudiante
            return (int(codigo), int(idEstudiante), float(nota))#retorna los datos ingresados por el usuario para funcionar como parametro en otra funcion
        except ValueError:#sentecia que se ejecuta en caso de algun tipo de error 
            print("Dato(s) invalido")#mensaje al usuario de entrada invalida

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------Metodo de borrado--------------------------------------------------------------------------------#
def deleteRow(code: int, studentId: int):#definicion del metodo de eliminacion de la materia de un estudiante en espesifico
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        conn = sql.connect(DB)#se genera la conexion con la base de datos 
        cursor = conn.cursor()#se inserta un cursor para la eliminacion de los datos a la tabla acadhistory de la base de datos
        instruction = f"DELETE FROM acadhistory WHERE code_materia={code} AND id_estudiante={studentId}" #Comando de delete en SQL un solo dato
        #se determina la instruccion de actualizar el valor deseado donde id_estudiante debe ser igual al parametro ingresado y code_materia debe ser igual al parametro ingresado
        cursor.execute(instruction)#se pasa la instruccion con el cursor para eliminar los datos
        conn.commit();#se verifican que los cambios en la base de datos son validos
        conn.close()#se cierra la conexion con la base de datos
        print ('Datos actualizados de forma correcta')#mensaje para el usuario
    except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
        print (e)#mensaje del error que se presenta

def rowDeleteGetter():#definicion del metodo para los parametros para la eliminacion de una materia de un estudiante en espesifico 
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        print("El codigo de la materia y el Id del estudiante deben existir, si no, habra error")#mensaje de instrucciones para llenar los datos
        codigo = input('Codigo de la materia: ')#determinar el Codigo de la materia ya existente mediante el input del usuario
        codigo = codigo.ljust(10)#especifica la cantidad maxima de caracteres que puede ingresar el usario para la variable codigo
        idEstudiante = input('Id del estudiante ')#determinar el Id del estudiante ya existente mediante el input del usuario
        return (int(codigo), int(idEstudiante))#retorna los datos ingresados por el usuario para funcionar como parametro en otra funcion
    except ValueError:#sentecia que se ejecuta en caso de algun tipo de error 
        print("Dato(s) invalido")#mensaje al usuario de entrada invalida
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------Controlador principal----------------------------------------------------------------------------#
def main():#definicion del metodo controldor del modulo acadhistory
    while True: #sentencia del ciclo prinsipal de la tabla acadhistory
        validator = True#creacion del boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
        while validator:#generar un ciclo en la tabla de datos acadhistory con la funcion de ingresar y verificar la entrada del usuario, el cual solo se rompera cuando la entrada del usuario es valida
            try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                selector=input("Si desea crear añadir una materia aprete 1. Si desea actualizar una nota en una materia ya registrada aprete 2. Si desea consultar sus notas o su promedio aprete 3. si desea eliminar alguna materia aprete 4. Para salir, cualquier otra tecla.")
                #mensaje para el usuario sobre sus opcciones validas de entrada y entrada del mismo 
                selector =int(selector)#verificacion de que la entrada es un numero
                if (selector!=1 and selector !=2 and selector !=3 and selector !=4 and selector !=5):#sentencia de verificacion de que la entradad es uno de los valores validos
                    print(f"{selector} es un valor invalido")#mensaje al usuario de entrada invalida
                else:
                    validator = False#cambiar el valor del boleano para que el ciclo de ingresar y verificar entrada del usuario no continue 
            except ValueError:#sentecia que se ejecuta en caso de algun tipo de error 
                print(f"{selector} es un valor invalido")#mensaje al usuario de entrada invalida
        if selector == 1:#sentencia en caso que la entrada del usuario sea 1
            validator = True#creacion del boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
            while validator:#generar un ciclo con la funcion de ingresar y verificar la entrada del usuario
                # TODO Se arma bucle infinito en 1
                try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                    clearConsole()#llamar al metodo para limpiar la consola, metodo estetico
                    selectorr=input("Para añadir una materia debe escribir el documento del estudiante (ya registrado) y  el codigo de una materia existente. ¿Desea ver que materias hay disponibles? 1.Si. 2.No");
                    #mensaje para el usuario sobre sus opcciones validas de entrada y entrada del mismo 
                    if selectorr == "1":#sentencia en caso que la entrada del usuario sea 1
                        allMaterias('codigo')#llamar al metodo importado de materias para ordenar por el filtro ingresado
                        sleep(2.5)#descanso del programa
                        print('A continuación va a inscribir una materia ')#mensaje para el usuario
                        data = rowGetter()#llamar al metodo para pedir la entrada del usuario de cada uno de los datos de la tabla acadhistory
                        insertRow(data[0], data[1], data[2])#llamar al metodo para insertar los datos de la historia academica con lso datos de data
                        validator = False#cambiar el valor del boleano para que el ciclo de ingresar y verificar entrada del usuario no continue 
                    elif selectorr == "2":#sentencia en caso que la entrada del usuario sea 2
                        print('A continuación va a inscribir una materia ')#mensaje para el usuario
                        data = rowGetter()#llamar al metodo para pedir la entrada del usuario de cada uno de los datos de la tabla acadhistory
                        insertRow(data[0], data[1], data[2])#llamar al metodo para insertar los datos de la historia academica con lso datos de data
                        validator = False#cambiar el valor del boleano para que el ciclo de ingresar y verificar entrada del usuario no continue 
                except ValueError:#sentecia que se ejecuta en caso de algun tipo de error 
                    print (f"{selector} es invalido")#mensaje al usuario de entrada invalida
        elif selector == 2:#sentencia en caso que la entrada del usuario sea 2
            while True:#generar un ciclo con la funcion de ingresar y verificar la entrada del usuario
                try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                    clearConsole()#llamar al metodo para limpiar la consola, metodo estetico
                    print("Para actualizar la nota de una materia debe escribir el documento del estudiante y el codigo de la materia. Claramene la nota tambien");
                    #mensaje para el usuario sobre sus opcciones validas de entrada y entrada del mismo 
                    data = rowUpdateGetter()#llamar al metodo para pedir la entrada del usuario de cada uno de los datos a actualizar de la tabla acadhistory
                    update('nota', data[2], data[1], data[0])#llamar al metodo update para actualizar los datos ingresados
                    break#romper el ciclo de ingresar y verificar la entrada del usuario
                except:#sentecia que se ejecuta en caso de algun tipo de error 
                    print ("Unexpected error")#mensaje al usuario de entrada invalida
        elif selector == 3:#sentencia en caso que la entrada del usuario sea 3
            while True:#generar un ciclo con la funcion de ingresar y verificar la entrada del usuario
                try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                    clearConsole()#llamar al metodo para limpiar la consola, metodo estetico
                    selector=input("Si desea ver su promedio aprete 1. Si desea ver todas sus notas aprete 2.");
                    #mensaje para el usuario sobre sus opcciones validas de entrada y entrada del mismo 
                    selector = int(selector)#verificacion de que la entrada es un numero
                    if (selector !=1 and selector !=2):#sentencia de verificacion de que la entradad es uno de los valores validos
                        print(f"{selector} es invalido")#mensaje al usuario de entrada invalida
                    elif selector == 1:#sentencia en caso que la entrada del usuario sea 1
                        while True:#generar un ciclo con la funcion de ingresar y verificar la entrada del usuario
                            try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                                idd = int(input("Ingrese el documento del estudiante "))#entrada del usuario de la llave primaria de un estudiante
                                data = acadHistoryById(idd)#llamamos al metodo que toma las materias de un estudinate con su llave primaria
                                promedio = prom(data)#llamamos al metodo que calcula el promedio por medio de la materias del estudiante
                                print("Su promedio es: ", promedio)#menaje para el usuario sobre su informacion
                                break#romper el ciclo de ingresar y verificar la entrada del usuario
                            except ValueError:#sentecia que se ejecuta en caso de algun tipo de error 
                                print(f"{idd} es invalido")#mensaje al usuario de entrada invalida
                    elif selector == 2:#sentencia en caso que la entrada del usuario sea 1
                       while True:#generar un ciclo con la funcion de ingresar y verificar la entrada del usuario
                            try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                                clearConsole()#llamar al metodo para limpiar la consola, metodo estetico
                                idd = int(input("Ingrese el documento del estudiante "))#entrada del usuario de la llave primaria de un estudiante
                                data = acadHistoryById(idd)#llamamos al metodo que toma las materias de un estudinate con su llave primaria
                                print("Sus notas son: ")#mensaje para el usuario sobre la infromacion pedida
                                tableHistoriaAcad(data)#metodo estetico para la visualizacion de las notas
                                break#romper el ciclo de ingresar y verificar la entrada del usuario
                            except ValueError:#sentecia que se ejecuta en caso de algun tipo de error
                                print(f"{idd} es invalido")#mensaje al usuario de entrada invalida
                    break#romper el ciclo de ingresar y verificar la entrada del usuario
                except ValueError:#sentecia que se ejecuta en caso de algun tipo de error
                    print (f"{selector} es invalido")#mensaje al usuario de entrada invalida
        elif selector == 4:#sentencia en caso que la entrada del usuario sea 4
            while True:
                clearConsole()#llamar al metodo para limpiar la consola, metodo estetico
                data = rowDeleteGetter()#llamamos al metodo para los parametros para la eliminacion de una materia de un estudiante en espesifico 
                deleteRow(data[0], data[1])#llamamos al metodo de eliminacion de la materia de un estudiante en espesifico
                break;
        else:#sentencia en caso que la entrada del usuario sea una diferente a sus opciones
            break#salir del mudulo acadhistory

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
