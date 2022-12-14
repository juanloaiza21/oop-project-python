from cgitb import text #se importa text del modulo cgitb
import sqlite3 as sql #importar sqlite3 por el nombre sql
from console_utils import Console #se importa Console del module console_utils

class Materia(Console): #se crea la clase materia

    #Constructor function
    def __init__(self, db) -> None: #inicializa los atributos
        self.__codigo:int = None; #atributo de codigo
        self.__nombre:str = None; #atributo de nombre
        self.__facultad:str = None; #atributo de facultad
        self.__departamento:str = None; #atributo de departamento
        self.__idioma:str = None; #atributo de idioma
        self.__creditos:int = None; #atributo de creditos
        self.__multidata = []; #lista donde se guardaran los datos
        self.__db = db; #base de datos para inicializar las clases        

#--------------------------------------------------------------------------------------SETTERS--------------------------------------------------------------------------#         
    def codigoSetter(self, codigo: int) ->None: #se establece el valor de codigo
        self.__codigo = codigo; #variable privada de codigo
    
    def creditosSetter(self, creditos: int) ->None: #se establece el valor de creditos
        self.__creditos = creditos; #variable privada de creditos
    
    def nombreSetter(self, nombre: str) ->None: #se establece el valor de nombre
        self.__nombre = nombre; #variable privada de nombre
    
    def facultadSetter(self, facultad: str) ->None: #se establece el valor de facultad
        self.__facultad = facultad; #variable privada de facultad
    
    def departamentoSetter(self, departamento: str) ->None: #se establece el valor de departamento
        self.__departamento = departamento; #variable privada de departamento

    def idiomaSetter(self, idioma: str) ->None: #se establece el valor de idioma
        self.__idioma = idioma; #variable privada de idioma
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------GETTERS---------------------------------------------------------------------------#
    def codigoGetter(self) ->int: #se obtiene el valor de codigo
        return self.__codigo #devuelve el valor privado de codigo
    
    def creditosGetter(self) ->int: #se obtiene el valor de creditos
        return self.__creditos #devuelve el valor privado de creditos
    
    def nombreGetter(self) ->str: #se obtiene el valor de nombre
        return self.__nombre #devuelve el valor privado de nombre
    
    def facultadGetter(self) ->str: #se obtiene el valor de facultad
        return self.__facultad #devuelve el valor privado de facultad
    
    def departamentoGetter(self) ->str: #se obtiene el valor de departamento
        return self.__departamento #devuelve el valor privado de departamento

    def idiomaGetter(self) ->str: #se obtiene el valor de idioma
        return self.__idioma; #devuelve el valor privado de idioma
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #Inserta la materia
    def __insertRow(self): #define el metodo privado
        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__db) #se genera la conexion con la base de datos
            cursor = conn.cursor() #se inserta un cursor para la insercion de los datos que estaran presente en tabla materia de la base de datos
            instruction = f"INSERT INTO materias values({self.__codigo}, '{self.__nombre}', '{self.__facultad}', '{self.__departamento}', '{self.__idioma}', {self.__creditos})"
            cursor.execute(instruction) #se pasa la instruccion a la base de datos de crear la tabla materia en caso de no existir con las subtablas codigo ,nombre ,facultad ,departamento ,idioma ,creditos y su respectivo tipo de entrada
            conn.commit(); #se verifican que los cambios en la base de datos son validos
            conn.close(); #se cierra la conexion con la base de datos
        except sql.Error as e: #sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print (e) #mensaje del error que se presenta

        
    #Pide input por teclado a tr??ves de consola de los datos, en versi??n gr??fica desaparece
    #Pide input por teclado y retorna una tupla de tama??o = 6, que contiene todos los datos de materias a ser insertados
    def __rowGetter(self)->None: #define el metodo privado
        while True: #ciclo generado para verificar que los datos ingresados sean validos
            try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
                codigo = input('Codigo de la materia: ') #determinar el codigo de la materia mediante el input del usuario
                codigo = codigo.ljust(10) #especifica la cantidad maxima de caracteres que puede ingresar el usario para la variable codigo
                codigo = int(codigo) #determinar si la entrada del usuario es un numero
                nombre = input('Nombre de la materia: ') #determinar el nombre de la materia mediante el input del usuario
                facultad = input('Facultad que dicta la materia: ') #determinar el nombre de la facultad mediante el input del usuario
                departamento = input('Departamento que dicta la materia: ') #determinar el nombre del departamento mediante el input del usuario
                creditos = input('Creditos de la materia: ') #determinar el numero de creditos mediante el input del usuario
                creditos = int(creditos) #verifica que el input sea un entero
                idioma = input('Idioma en que se dicta la materia: ') #determinar el idioma mediante el input del usuario
                if(codigo is None and nombre is None and facultad is None and departamento is None and idioma is None and creditos is None):
                    print("Por favor llene todos los campos") #verifica que todos los datos hayan sido colocados, y si no es asi imprime el mensaje
                else: #sentencia en caso de que todos los datos hayan sido colocados
                    self.codigoSetter(codigo)
                    self.nombreSetter(nombre.upper())
                    self.facultadSetter(facultad.upper())
                    self.departamentoSetter(departamento.upper())
                    self.idiomaSetter(idioma.upper())
                    self.creditosSetter(creditos)
                    break #rompe el ciclo
            except ValueError: #sentecia que se ejecuta en caso de que la algun dato sea invalido y no sea detectado
                print("Dato(s) invalido(s), codigo y creditos son numeros enteros") #generar mensaje de entradas invalidas


    #pide varias veces los datos
    #Pide input por teclado y retorna una lista de tuplas de tama??o = 6, que contiene todos los datos de materias a ser insertados
    def __batchRowGetter(self): #define el metodo privado
        secret_runner = "1" #establece la variable que sirve para mantener el ciclo que pide los datos varias veces
        counter = 0 #establecer el contador que sirve para controlar el numero de veces que el usuario a ingresado datos
        while True: #generar el ciclo que pide los datos varias veces
            try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
                codigo = input('Codigo de la materia: ') #determinar el codigo de la materia mediante el input del usuario
                codigo = codigo.ljust(10) #especifica la cantidad maxima de caracteres que puede ingresar el usuario para la variable codigo
                codigo = int(codigo) #determinar si la entrada del usuario es un numero
                nombre = input('Nombre de la materia: ') #determinar el nombre de la materia mediante el input del usuario
                facultad = input('Facultad que dicta la materia: ') #determinar el nombre de la facultad mediante el input del usuario
                departamento = input('Departamento que dicta la materia: ') #determinar el nombre del departamento mediante el input del usuario
                creditos = input('Creditos de la materia: ') #determinar el numero de creditos mediante el input del usuario
                creditos = int(creditos) #verifica que el input sea un entero
                idioma = input('Idioma en que se dicta la materia: ') #determinar el idioma mediante el input del usuario
                if(codigo is None and nombre is None and facultad is None and departamento is None and idioma is None and creditos is None):
                    print("Por favor llene todos los campos") #verifica que todos los datos hayan sido colocados, y si no es asi imprime el mensaje
                else: #sentencia en caso de que todos los datos hayan sido colocados
                    self.__multidata.append((codigo, nombre.upper(), facultad.upper(), departamento.upper(), idioma.upper(), creditos)) #agregar a la lista los datos ingresados por el usuario, en caso de ser un string utilizando el metodo upper()
                    runner=input('Digite 1 si desea continuar, digite cualquier otra tecla si no. ') #controlador de la continuacion del ciclo por parte de la entrada del usuario
                    counter+=1 #agregarle una unidad al contador de datos ingresados
                if runner != secret_runner: #sentencia de verificacion para continuar o no el ciclo
                    break #como no se desea continuar el ciclo se rompera en esta sentencia
            except ValueError: #sentecia que se ejecuta en caso de que la algun dato sea invalido y no sea detectado
                print("Dato(s) invalido(s), codigo y creditos son numeros enteros") #generar mensaje de entradas invalidas
        print (f"Usted ha insertado {counter} datos, los cuales son: ") #mensaje para el usuario de la cantidad de datos ingresados y cuales son
        self.tableMaterias(self.__multidata) #llama al metodo encargado de las tablas que contienen los datos
        return self.__multidata #retornar todos los datos que ingreso el usuario


    #Leer todos datos
    #Retorna una lista de tuplas tama??o = 6 con todos los datos en la self.__db referentes a materias
    def __readAllRows(self): #define el metodo privado
        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__db) #se genera la conexion con la base de datos 
            cursor = conn.cursor() #se inserta un cursor para la busqueda de los datos de la tabla materia de la base de datos
            instruction = f"SELECT * from materias" #se determina la intruccion de seleccionar los elementos de la tabla materia
            cursor.execute(instruction) #se pasa la instruccion con el cursor para la busqueda de los datos
            datos = cursor.fetchall() #utilizamos el metodo fetchall para obtener todas las filas de datos de golpe
            conn.commit(); #se verifican que los cambios en la base de datos son validos
            conn.close() #se cierra la conexion con la base de datos
            return (datos); #devuelve los datos de la tabla materia
        except sql.Error as e: #sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print (e) #mensaje del error que se presenta

    #Ac?? se puede filtrar los datos bajo una condici??n 
    #Pide los datos para filtrarlos bajo alguna condici??n, puede ser cualquier tipo de dato
    #Retorna lista de tuplas con tama??o = 6 con todos los datos de las materias que hagan match con la busqueda
    #Publico para el uso en historia academica 
    def searchByFilter(self, fieldName, fieldValue): #definir el m??todo que se encarga de leer los datos por medio de un filtro al momento que se el usuario desee ver informaci??n especifica
        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__db) #se genera la conexion con la base de datos
            cursor = conn.cursor() #se inserta un cursor para la busqueda de los datos de la tabla materia de la base de datos
            instruction = f"SELECT * from materias WHERE {fieldName}={fieldValue}" #se determina la intruccion de seleccionar los elementos de la tabla materia de acuerdo al filtro seleccionado
            cursor.execute(instruction) #se pasa la instruccion con el cursor para la busqueda de los datos
            datos = cursor.fetchall() #utilizamos el metodo fetchall para obtener todas las filas de datos de golpe
            conn.commit(); #se verifican que los cambios en la base de datos son validos
            conn.close() #se cierra la conexion con la base de datos
            return datos; #devuelve los datos de la tabla materia
        except sql.Error as e: #sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print (e) #mensaje del error que se presenta

    #Batch write, escribe multiples lineas de datos a la vez
    #Recibe como datos la salida de batch row getter
    def __batchInsertRow(self): #definicion del metodo privado para insertar multiples cantidades de datos ingesados por el usuario
        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__db) #se genera la conexion con la base de datos 
            cursor = conn.cursor() #se inserta un cursor para la insercion de los datos de la tabla materia de la base de datos
            instruction = f"INSERT INTO materias values(?, ?, ?, ?, ?, ?)" #se determina la instruccion de insetar todos los valores ingresados por el usuario
            cursor.executemany(instruction, self.__multidata) #Enviar varios datos a la vez
            conn.commit(); #se verifican que los cambios en la base de datos son validos
            conn.close(); #se cierra la conexion con la base de datos
        except sql.Error as e: #sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print (e) #mensaje del error que se presenta
        

    #Read order, ordena los datos de mayor a menor seg??n el campo que le pidamos :p
    #Imprime los datos en forma de tablita
    #M??todo p??blico para el uso en otros lugares
    def readOrdered(self, field: str): #definicion del metedo para ordenar los datos de la tabla materia por medio de un filtro
        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__db) #se genera la conexion con la base de datos 
            cursor = conn.cursor() #se inserta un cursor para la actualizacion de los datos de la tabla materia de la base de datos
            instruction = f"SELECT * from materias ORDER BY {field} DESC" #Si le quitamos el DESC se ordenara de menor a mayor, "DESC" viene de DESCENDING
            cursor.execute(instruction) #se pasa la instruccion con el cursor para seleccionar los multiples datos por medio del parametro dado
            datos = cursor.fetchall() #utilizamos el metodo fetchall para obtener todas las filas de datos de golpe
            conn.commit(); #se verifican que los cambios en la base de datos son validos
            conn.close() #se cierra la conexion con la base de datos
            self.tableMaterias(datos); #se llama al metodo que contiene los datos en forma de tabalas
        except sql.Error as e: #sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print (e) #mensaje del error que se presenta

    #Actualizar datos en un determinado campo de alguna materia
    """Actualizar materia en dise??o l??gico."""
    #Pide el fieldOnChange como un string, la data puede ser cualquier tipo de dato, y la identificaci??n que responde al nombre code
    #Retorna un mensaje de felicitaci??n si todo fue correcto
    def __update(self, fieldOnChange: str, dataOnChange, code: int): #definicion del metodo privado para actualizar los datos de la tabla materia por medio de la clave primaria
        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__db) #se genera la conexion con la base de datos
            cursor = conn.cursor() #se inserta un cursor para la actualizacion de los datos de la tabla materia de la base de datos
            try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
                dataOnChange= int(dataOnChange) #comprobacion de que el parametro ingresado es un numero 
                instruction = f"UPDATE materias SET '{fieldOnChange}'={dataOnChange} WHERE codigo={code}" #Comando de actualizaci??n en SQL
            except ValueError: #sentecia que se ejecuta en caso de que se desee actualizar un string
                instruction = f"UPDATE materias SET '{fieldOnChange}'='{dataOnChange}' WHERE codigo={code}" #Comando de actualizaci??n en SQL
            finally: #sentencia que se ejecutara finalizando este proceso
                cursor.execute(instruction) #se pasa la instruccion con el cursor para actualiza los datos por medio del parametro dado
                conn.commit(); #se verifican que los cambios en la base de datos son validos
                conn.close() #se cierra la conexion con la base de datos
                print ('Datos actualizados de forma correcta') #mensaje para el usuario
        except sql.Error as e: #sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print (e) #mensaje del error que se presenta

    #---------------------------------------------------------------------------------------------IMPORTANT calcular promedios de una tabla------------------------------------------------------------------------------------------
    #Calcula el promedio de un campo, en este caso de creditos
    def __promedio(self): #definicion del metodo privado para calcular el promedio de un campo
        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
            conn = sql.connect(self.__db) #se genera la conexion con la base de datos
            cursor = conn.cursor() #se inserta un cursor para la actualizacion de los datos de la tabla materia de la base de datos
            instruction = f"SELECT count(*) FROM materias" #Comando de contar campos en SQL
            cursor.execute(instruction) #se pasa la instruccion con el cursor para seleccionar los campos
            cantidad=cursor.fetchall() #utilizamos el metodo fetchall para obtener todas las filas de datos de golpe
            instruction = f"SELECT sum(creditos) FROM materias" #Comando de sumar campos en SQL
            cursor.execute(instruction) #se pasa la instruccion con el cursor para seleccionar la suma de los campos
            suma=cursor.fetchall() #utilizamos el metodo fetchall para obtener todas las filas de datos de golpe
            conn.commit(); #se verifican que los cambios en la base de datos son validos
            conn.close() #se cierra la conexion con la base de datos
            print("Promedio creditos ", suma[0][0]/cantidad[0][0]) #mensaje para el usuario con el promedio de creditos
        except sql.Error as e: #sentecia que se ejecuta en caso de algun tipo de error y determinar una variable para referirse al mismo
            print (e) #mensaje del error que se presenta
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    #---------------------------------------------------------------Funci??n principal---------------------------------------------------------------------------------#

    def main(self): #definicion del metodo controlador del modulo materia
        #TODO
        while True:#Revisa si va a a??adir datos, actualizar idioma o leer datos, metodo reutilizable, verifica que el input sea correcto
            #validador inicial
            while True: #creacion del boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
                try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
                    selector = input(
                    """
                    Bienvenido a materia
                    1. A??adir materia.
                    2. Actualizar idioma. 
                    3. Leer datos. 
                    Para salir presione otro numero.  
                    """)  #mensaje para el usuario sobre sus opciones validas de entrada y entrada del mismo 
                    selector = int(selector) #verificacion de que la entrada es un numero
                    break #se rompe el ciclo
                except ValueError: #sentecia que se ejecuta en caso de algun tipo de error
                    print("valor invalido") #genera mensaje de entrada invalida
            #A??adir materia
            if selector == 1: #sentencia en caso que la entrada del usuario sea 1
                while True: #creacion del boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
                    while True: #creacion del boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
                        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
                            subselector = input(
                                """
                                1. Para a??adir una sola materia.
                                2. A??adir materia sin recibir datos. 
                                3. Para a??adir m??ltiples materias.
                                Para salir cualquier otro numero.  
                                """) #mensaje para el usuario sobre sus opciones validas de entrada y entrada del mismo 
                            subselector = int(subselector) #verificacion de que la entrada es un numero
                            break #se rompe el ciclo
                        except ValueError: #sentecia que se ejecuta en caso de algun tipo de error
                            print("valor invalido") #genera mensaje de entrada invalida
                    #A??adir una sola materia
                    if subselector == 1: #sentencia en caso que la entrada del usuario en el subselector sea 1
                        self.__rowGetter() #llamar al metodo privado que pide input por teclado a tr??ves de consola de los datos
                        self.__insertRow() #llamar al metodo privado que inserta la materia en la base de datos
                        data = (self.__codigo, self.__nombre, self.__facultad, self.__departamento, self.__idioma,self.__creditos) #actualizacion de los datos
                        self.tableMaterias([data]) #llamado al metodo para ver los datos en la tabla
                        break #rompe el ciclo
                    #A??adir materia sin que se vean los datos
                    elif subselector==2: #sentencia en caso que la entrada del usuario en el subselector sea 2
                        self.__rowGetter() #llamar al metodo privado que pide input por teclado a tr??ves de consola de los datos
                        self.__insertRow() #llamar al metodo privado que pide input por teclado a tr??ves de consola de los datos
                        break #rompe el ciclo
                    #A??adir multiples materias
                    elif subselector==3: #sentencia en caso que la entrada del usuario en el subselector sea 3
                        self.__batchRowGetter() #llamar al metodo privado que pide input por teclado a tr??ves de consola de los datos varias veces
                        self.__batchInsertRow() #llamar al metodo que inserta todas las materias que a ingresado el usuario en la base de datos e internamenete da el mensaje al usuario
                        break #rompe el ciclo
                    else: #sentencia en caso de que la entrada fuera un numero distinto
                        break #rompe el ciclo
            #Actualizar idioma
            if selector == 2: #sentencia en caso que la entrada del usuario sea 2
                while True: #creacion del ciclo boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
                    try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
                        codigo = input("Seleccione el codigo de la materia ") #entrada del codigo o clave primaria de la materia que se desea actualizar
                        codigo = int(codigo) #verificacion de que la entrada es un numero
                        break #rompe el ciclo
                    except ValueError: #sentecia que se ejecuta en caso de algun tipo de error 
                        print('Valor invalido') #generar mensaje de entrada invalida
                while True: #creacion del ciclo boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
                    idioma = input("Escriba el nuevo idioma ") #entrada del nuevo idioma que desea actualizar
                    if (type(idioma)!=str): #sentencia en caso de que la entrada no sea un str
                        print('Ingrese un valor') #mensaje para el usuario 
                    else: #sentencia en caso de que la entrada sea un str
                        break #rompe el ciclo
                self.__update('idioma', idioma, codigo) # metodo privado que actualiza el idioma
            #Leer datos
            if selector == 3: #sentencia en caso que la entrada del usuario sea 3
                    while True: #creacion del ciclo boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
                        self.clearConsole() #metodo que limpiara la consola
                        try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
                            subselector = input(
                                """
                                1. Si desea ver todas las materias.
                                2. Para bsucar con el c??digo.
                                Cualquier otro n??mero para salir
                                """ 
                                ) #mensaje para el usuario sobre sus opciones validas de entrada y entrada del mismo
                            subselector=int(subselector) #verifica que la entrada sea un entero
                            break #rompe el ciclo
                        except ValueError: #sentecia que se ejecuta en caso de algun tipo de error 
                            print("valor invalido") #generar mensaje de entrada invalida
                #Ver todas las materias
                    if(subselector == 1): #sentencia en caso que la entrada del usuario sea 1
                        self.tableMaterias(self.__readAllRows()) #metodo privado que muestra todas las materias en una tabla
                #Ver materias por codigos
                    if(subselector == 2): #sentencia en caso que la entrada del usuario sea 2
                        while True: #creacion del ciclo boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
                            try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
                                codigo = input("Escriba el codigo de la materia que quiere ver: ") #mensaje que le pedira al usuario la clave o codigo de la materia
                                codigo = int(codigo) #verifica que la entrada sea un entero
                                break #rompe el ciclo
                            except ValueError: #sentecia que se ejecuta en caso de algun tipo de error
                                print("valor invalido") #generar mensaje de entrada invalida
                        self.tableMaterias( self.searchByFilter('codigo', codigo)) #metodo que muestra las materias por codigos
            else: #sentencia en caso de que la entrada no sea una de las mencionadas
                break #rompe el ciclo
