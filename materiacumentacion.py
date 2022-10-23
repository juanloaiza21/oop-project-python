from multiprocessing.sharedctypes import Value
import sqlite3 as sql#importar sqlite3 por el nombre sql
from decouple import config#importar config de decouple
DB = config('DB_NAME')#se determina una variable para referirse a la base de datos

#Crea tablas manualmente, automatizar
def createTeable():#definicion del metodo para crear la tabla de datos
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        conn = sql.connect(DB)#se genera la conexion con la base de datos 
        cursor = conn.cursor()#se inserta un cursor para la insercion de los datos que estaran presente en tabla materia de la base de datos
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
        #se pasa la instruccion a la base de datos de crear la tabla materia en caso de no existir con las subtablas codigo ,nombre ,facultad ,departamento ,idioma ,creditos y su respectivo tipo de entrada
        #codigo esta declarada como prymary key al ser el dato identificador por no poder repetirse en ningun caso
        conn.commit();#se verifican que los cambios en la base de datos son validos
        conn.close();#se cierra la conexion con la base de datos
    except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
        print(e)#mensaje del error que se presenta

 #Inserta la materia
def insertRow(codigo: int, nombre: str, facultad: str, departamento: str, idioma: str, creditos: int):
    #definicion del metodo para insertar los datos de la materia con sus variables y su respectivo tipo de variable para la verificacion como parametros
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        conn = sql.connect(DB)#se genera la conexion con la base de datos 
        cursor = conn.cursor()#se inserta un cursor para la insercion de los datos a la tabla materia de la base de datos
        instruction = f"INSERT INTO materias values({codigo}, '{nombre}', '{facultad}', '{departamento}', '{idioma}', {creditos})"
        #se determina la instruccion de insetar los valores de codigo ,nombre ,facultad ,departamento ,idioma ,creditos a la tabla materia
        cursor.execute(instruction)#se pasa la instruccion con el cursor para insertar los datos
        conn.commit();#se verifican que los cambios en la base de datos son validos
        conn.close();#se cierra la conexion con la base de datos
    except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
        print (e)#mensaje del error que se presenta

    
#Pide input por teclado a tráves de consola de los datos, en versión gráfica desaparece
#TODO validar ints, strings y floats
def rowGetter():#definicion del metodo para pedir la entrada del usuario de cada uno de los datos de la tabla materia
    while True:#ciclo generado para verificar que los datos ingresados sean validos
        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
            codigo = input('Codigo de la materia: ')#determinar el codigo de la materia mediante el input del usuario
            while True:#ciclo generado para verificar que el codigo es valida
                try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error              
                    codigo = codigo.ljust(10)#especifica la cantidad maxima de caracteres que puede ingresar el usario para la variable codigo
                    codigo = int(codigo)#determinar si la entrada del usuario es un numero
                    break#romper el ciclo de verificar que el codigo es valida
                except:#sentecia que se ejecuta en caso de que el codigo no es valida
                    print("input invalido")#generar mensaje de entrada invalida
                    codigo = input('Codigo de la materia: ')#determinar el codigo de la materia mediante el input del usuario nuevamente
            nombre = input('Nombre de la materia: ')#determinar la nombre de la materia mediante el input del usuario
            facultad = input('Facultad que dicta la materia: ')#determinar la facultad de la materia mediante el input del usuario
            departamento = input('Departamento que dicta la materia: ')#determinar el departamento de la materia mediante el input del usuario
            creditos = input('Creditos de la materia: ')#determinar los creditos de la materia mediante el input del usuario
            while True:#ciclo generado para verificar que el numero de creditos es valido
                try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error                  
                    creditos = int(creditos)#determinar si la entrada del usuario es un numero
                    break#romper el ciclo de verificar que el numero de creditos es valido
                except:#sentecia que se ejecuta en caso de que el numero de creditos no es valido
                    print("input invalido")#generar mensaje de entrada invalida
                    creditos = input('creditos de la materia: ')#determinar el numero de creditos de la materia mediante el input del usuario nuevamente
            idioma = input('Idioma en que se dicta la materia: ')#determinar el idioma de la materia mediante el input del usuario
            return (codigo, nombre.upper(), facultad.upper(), departamento.upper(), idioma.upper(), creditos)
            #retorna los datos ingresados por el usuario , en caso de ser un string utilizando el metodo upper() el cual devuelve la misma cadena de caracteres pero en mayusculas
        except ValueError:#sentecia que se ejecuta en caso de que la algun dato sea invalido y no sea detectado
            print("Dato(s) invalido(s), codigo y creditos son numeros enteros")#generar mensaje de entradas invalidas


#pide varias veces los datos
def batchRowGetter():#definicion del metodo para pedir la entrada del usuario de cada uno de los datos de la tabla materia varias veces
    result = []#se crea un lista para el almcenamiento de todos los datos que ingrese el usuario
    secret_runner = "1"#esablecer la variable que sirve para mantener el ciclo que pide los datos varias vece
    counter = 0#establecer el contador que sirve para controlar el numero de veces que el usuario a ingresado datos
    while True: #generar el ciclo que pide los datos varias veces
        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error            
            codigo = input('Codigo de la materia: ')#determinar el codigo de la materia mediante el input del usuario
            while True:#ciclo generado para verificar que el codigo es valida
                try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error                
                    codigo = codigo.ljust(10)#especifica la cantidad maxima de caracteres que puede ingresar el usario para la variable codigo
                    codigo = int(codigo)#determinar si la entrada del usuario es un numero
                    break#romper el ciclo de verificar que el codigo es valida
                except:#sentecia que se ejecuta en caso de que el codigo no es valida
                    print("input invalido")#generar mensaje de entrada invalida
                    codigo = input('Codigo de la materia: ')#determinar el codigo de la materia mediante el input del usuario nuevamente
            nombre = input('Nombre de la materia: ')#determinar la nombre de la materia mediante el input del usuario
            facultad = input('Facultad que dicta la materia: ')#determinar la facultad de la materia mediante el input del usuario
            departamento = input('Departamento que dicta la materia: ')#determinar el departamento de la materia mediante el input del usuario
            creditos = input('Creditos de la materia: ')#determinar los creditos de la materia mediante el input del usuario
            while True:#ciclo generado para verificar que el numero de creditos es valido
                try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error                  
                    creditos = int(creditos)#determinar si la entrada del usuario es un numero
                    break#romper el ciclo de verificar que el numero de creditos es valido
                except:#sentecia que se ejecuta en caso de que el numero de creditos no es valido
                    print("input invalido")#generar mensaje de entrada invalida
                    creditos = input('creditos de la materia: ')#determinar el numero de creditos de la materia mediante el input del usuario nuevamente
            idioma = input('Idioma en que se dicta la materia: ')#determinar el idioma de la materia mediante el input del usuario
            result.append((codigo, nombre.upper(), facultad.upper(), departamento.upper(), idioma.upper(), creditos))
            #agregar a la lista los datos ingresados por el usuario, en caso de ser un string utilizando el metodo upper() el cual devuelve la misma cadena de caracteres pero en mayusculas
            runner=input('Digite 1 si desea continuar, digite cualquier otra tecla si no. ')#controlador de la continuacion del ciclo por parte de la entrada del usuario
            counter+=1#agregarle una unidad al contador de datos ingresados
            if runner != secret_runner:#sentencia de verificacion para continuar o no el ciclo
                break #como no se desea continuar el ciclo se rompera en esta sentencia
        except ValueError:#sentecia que se ejecuta en caso de que la algun dato sea invalido y no sea detectado
            print("Dato(s) invalido(s), codigo y creditos son numeros enteros")#generar mensaje de entradas invalidas
    print (f"Usted ha insertado {counter} datos, los cuales son: {result}")#mensaje par el usuario de la cantidad de datos ingresados y cuales son
    return result#retornar todos los datos que ingreso el usuario

#Leer todos datos
def readAllRows():#definir el método que se encarga de leer los datos al momento que se el usuario desee ver información
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        conn = sql.connect(DB)#se genera la conexion con la base de datos 
        cursor = conn.cursor()#se inserta un cursor para la busqueda de los datos de la tabla materia de la base de datos
        instruction = f"SELECT * from materias"#se determina la intruccion de seleccionar los elementos de la tabla materia
        cursor.execute(instruction)#se pasa la instruccion con el cursor para la busqueda de los datos-------------------------------------------
        datos = cursor.fetchall()#utilizamos el metodo fetchall para obtener todas las filas de datos de golpe
        conn.commit();#se verifican que los cambios en la base de datos son validos
        conn.close();#se cierra la conexion con la base de datos
        print(datos);#mensaje de los datos de la tabla materia
    except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
        print (e)#mensaje del error que se presenta

#Acá se puede filtrar los datos bajo una condición 
def searchByFilter(fieldName, fieldValue):#definir el método que se encarga de leer los datos por medio de un filtro al momento que se el usuario desee ver información especifica
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        conn = sql.connect(DB)#se genera la conexion con la base de datos 
        cursor = conn.cursor()#se inserta un cursor para la busqueda de los datos de la tabla materia de la base de datos
        instruction = f"SELECT * from materias WHERE {fieldName}={fieldValue}"#se determina la intruccion de seleccionar los elementos de la tabla materia de acuerdo al filtro seleccionado
        cursor.execute(instruction)#se pasa la instruccion con el cursor para la busqueda de los datos-------------------------------------------------------
        datos = cursor.fetchall()#utilizamos el metodo fetchall para obtener todas las filas de datos de golpe
        conn.commit();#se verifican que los cambios en la base de datos son validos
        conn.close();#se cierra la conexion con la base de datos
        print(datos);#mensaje de los datos espesificados de la tabla materia
    except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
        print (e)#mensaje del error que se presenta

#Batch write, escribe multiples lineas de datos a la vez
def batchInsertRow(dataList):#definicion del metedo para insertar multiples cantidades de datos ingesados por el usuario
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        conn = sql.connect(DB)#se genera la conexion con la base de datos 
        cursor = conn.cursor()#se inserta un cursor para la insercion de los datos de la tabla materia de la base de datos
        instruction = f"INSERT INTO materias values(?, ?, ?, ?, ?, ?)"
        #se determina la instruccion de insetar todos los valores ingresados por el usuario
        cursor.executemany(instruction, dataList)#se pasa la instruccion con el cursor para insertar los multiples datos por medio del parametro el cual son todos los datos ingresados por el usuario
        conn.commit();#se verifican que los cambios en la base de datos son validos
        conn.close();#se cierra la conexion con la base de datos
    except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
        print (e)#mensaje del error que se presenta 
    
#Read order, ordena los datos de mayor a menor según el campo que le pidamos :p
def readOrdered(field: str):#definicion del metedo para ordenar los datos de la tabla materia por medio de un filtro
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        conn = sql.connect(DB)#se genera la conexion con la base de datos 
        cursor = conn.cursor()#se inserta un cursor para la actualizacion de los datos de la tabla materia de la base de datos
        instruction = f"SELECT * from materias ORDER BY {field} DESC" #Si le quitamos el DESC se ordenara de menor a mayor, "DESC" viene de DESCENDING
        #se determina la instruccion de seleccionar todos los valores ingresados por el usuario mediante el friltro
        cursor.execute(instruction)#se pasa la instruccion con el cursor para seleccionar los multiples datos por medio del parametro dado
        datos = cursor.fetchall()#utilizamos el metodo fetchall para obtener todas las filas de datos de golpe
        conn.commit();#se verifican que los cambios en la base de datos son validos
        conn.close();#se cierra la conexion con la base de datos
        print(datos);#mensaje de los datos requeridos por el usuario ordenados de forma desendente
    except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
        print (e)#mensaje del error que se presenta 

#Actualizar datos en un determinado campo de alguna materia
"""Actualizar materia en diseño lógico."""
def update(fieldOnChange: str, dataOnChange, code: int):#definicion del metedo para actualizar los datos de la tabla materia por medio de la clave primaria
    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
        conn = sql.connect(DB)#se genera la conexion con la base de datos 
        cursor = conn.cursor()#se inserta un cursor para la actualizacion de los datos de la tabla materia de la base de datos
        try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
            dataOnChange= int(dataOnChange)#comprobacion de que el parametro ingresado es un numero 
            instruction = f"UPDATE materias SET '{fieldOnChange}'={dataOnChange} WHERE codigo={code}"#Comando de actualización en SQL
        except ValueError:#sentecia que se ejecuta en caso de que se desee actualizar un string
            instruction = f"UPDATE materias SET '{fieldOnChange}'='{dataOnChange}' WHERE codigo={code}" #Comando de actualización en SQL
        finally:#sentencia que se ejecutara finalizando este proceso
            cursor.execute(instruction)#se pasa la instruccion con el cursor para actualiza los datos por medio del parametro dado
            conn.commit();#se verifican que los cambios en la base de datos son validos
            conn.close();#se cierra la conexion con la base de datos
            print ('Datos actualizados de forma correcta')#mensaje para el usuario
    except sql.Error as e:#sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
        print (e)#mensaje del error que se presenta




#---------------------------------------------------------------Función principal---------------------------------------------------------------------------------#
def main():#definicion del metodo controldor del modulo materia
    
    while True:
        #Revisa si va a añadir datos, leer o actualizar, metodo reutilizable, verifica que el input sea correcto
        validator = True#creacion del boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
        while validator:#generar un ciclo en la tabla de datos materia con la funcion de ingresar y verificar la entrada del usuario, el cual solo se rompera cuando la entrada del usuario es valida
            try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                selector = input("Si desea añadir datos ingrese '1' y enter. Si desea actualizar el idioma presione '2' y enter. si desea obtener información ingrese '3' y enter, para salir presione 4 y enter. ")
                #mensaje para el usuario sobre sus opcciones validas de entrada y entrada del mismo 
                selector = int(selector)#verificacion de que la entrada es un numero
                validator = False#cambiar el valor del boleano para finalizar el ciclo que pide la entrada del usuario 
                while(selector!=1 and selector !=2 and selector !=3 and selector !=4):#generar el ciclo de verificacion de que la entradad es uno de los valores validos
                    selector = input(f"{selector} no es una opción valida, por favor digite una opcion valida ")#en caso de que la entrada no se un valor valido se generara un mensaje de no valides y se pedira nuevamente la entrada
                    selector = int(selector)#verificacion de que la entrada es un numero
            except ValueError:#sentecia que se ejecuta en caso de algun tipo de error 
                print("Input invalido")#genrar mensaje de entrada invalida
                validator = True#cambiar el valor del boleano para que el ciclo de ingresar y verificar entrada del usuario no continue 
        #-------------------------------------------Creación de materias---------------------------------------------------------------------------#
        if selector ==1:#sentencia en caso que la entrada del usuario sea 1
            validator = True#creacion del boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
            while validator:#generar un ciclo en la tabla de datos materia con la funcion de ingresar y verificar la entrada del usuario
                try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                    pointer = input("Si desea solo añadir una materia digite '1' y luego enter, si desea registrar multiples datos digite '2' y luego enter. ")
                    #mensaje para el usuario sobre sus opcciones validas de entrada y entrada del mismo 
                    pointer = int(pointer)#verificacion de que la entrada es un numero
                    validator = False#cambiar el valor del boleano para finalizar el ciclo que pide la entrada del usuario 
                    while(pointer!=1 and pointer !=2):#generar el ciclo de verificacion de que la entradad es uno de los valores validos
                        pointer = input(f"{pointer} no es una opción valida, por favor digite una opcion valida ")#en caso de que la entrada no se un valor valido se generara un mensaje de no valides y se pedira nuevamente la entrada
                        pointer = int(pointer)#verificacion de que la entrada es un numero
                except ValueError:#sentecia que se ejecuta en caso de algun tipo de error 
                    print("Input invalido")#generar mensaje de entrada invalida
                    validator = True#cambiar el valor del boleano para que el ciclo de ingresar y verificar entrada del usuario continue 
        #Primer caso del input de escritura, un solo dato
            if int(pointer)==1:#sentencia en caso que la entrada pointed del usuario sea 1, por lo tanto desea añadir solo una materia
                data = rowGetter()#llamar al metodo que pide input por teclado a tráves de consola de los datos
                insertRow(data[0], data[1], data[2], data[3], data[4], data[5])#llamar al metodo que inserta el estudiante en la base de datos
                print("Datos insertados: ",data)#mensaje para el usuario con los datos ingresados
        #Segundo caso, múltiples datos
            elif(int(pointer)==2):#sentencia en caso que la entrada pointed del usuario sea 2, por lo tanto desea añadir multiples materias
                data = batchRowGetter()#llamar al metodo que pide input por teclado a tráves de consola de los datos varias veces
                batchInsertRow(data)#llamar al metodo que inserta todas los estudiantes que a ingresado el usuario en la base de datos e internamenete da el mensaje al usuario
        #-----------------------------------------------------------------------------------------------------------------------------------------#

        #---------------------------------------------------------------Actualizar datos-----------------------------------------------------------#
        elif(int(selector)==2):#sentencia en caso que la entrada del usuario sea 2
            validator = True#creacion del boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
            while validator:#generar un ciclo en la tabla de datos estudiante con la funcion de ingresar y verificar la entrada del usuario
                try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                    code = input("Escriba el codigo que quiere actualizar ")#entrada del codigo o clave primaria del estudiante que se desea actualizr
                    code = int(code)#verificacion de que la entrada es un numero
                    validator = False#cambiar el valor del boleano para finalizar el ciclo que pide la entrada del usuario 
                except ValueError:#sentecia que se ejecuta en caso de algun tipo de error 
                    print("Input invalido")#generar mensaje de entrada invalida
                    validator = True#cambiar el valor del boleano para que el ciclo de ingresar y verificar entrada del usuario continue 
            dataOnchange = input(f"Escriba el valor con el cual quiere modificar el campo {'idioma'} de la materia con codigo{code} ")#entrada del usuario del nuevo idioma que desea actualizar
            try:#en caso de que la entrada es un numero
                dataOnchange = int(dataOnchange)#examinar el valor
            except:#en caso de que la entrada es un string
                dataOnchange.lower()#en caso de que la entrada es un string
            finally:# sentencia que se ejecutara al finalizar el proceso
                update('idioma', dataOnchange, code)#se llama a la funcion encargada para que genere la acualizacion

        #------------------------------------------------------------------------------------------------------------------------------------------#

        #----------------------------------------------------------------Leer datos---------------------------------------------------------------#
        elif selector==3:#sentencia en caso que la entrada del usuario sea 3
            order = int(input("Si desea ordenar por código oprima 1  y enter, si no oprima 2 y enter."))
            #mensaje para el usuario sobre sus opcciones validas de entrada y entrada del mismo 
            #Verifica si el input es correcto
            while(order!=1 and order !=2):#generar el ciclo de verificacion de que la entradad es uno de los valores validos
                order = int(input(f"{selector} no es una opción valida, por favor digite una opcion valida ")) #en caso de que la entrada no se un valor valido se generara un mensaje de no valides y se pedira nuevamente la entrada
            if(order==1):#sentencia en caso que la entrada del usuario sea 1
                while True:#ciclo generado para verificar que la entrada del usuario es valida y leer los datos
                    try:#sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        field = int(input('Escriba el codigo de la materia '))#entrada del usuario del codigo de una materia ya existente
                        print(searchByFilter('codigo', field))#mensaje para el usuario sobre la informacion requerida mediante el llamado a al metodo de leer datos
                        break#romper el ciclo de verificar que la entrada del usuario
                    except ValueError:#sentecia que se ejecuta en caso de algun tipo de error 
                        print(f"{field} invalido")#generar mensaje de entrada invalida 
            elif order==2:
                readAllRows()
        #-----------------------------------------------------------------------------------------------------------------------------------------#
        elif selector ==4:#sentencia en caso que la entrada del usuario sea 4
            break;#con 4 como la entrada del usuario se rompera el ciclo prinsipal y asi salir a la pantalla del controlador
