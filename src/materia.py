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

        
    #Pide input por teclado a tráves de consola de los datos, en versión gráfica desaparece
    #Pide input por teclado y retorna una tupla de tamaño = 6, que contiene todos los datos de materias a ser insertados
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
    #Pide input por teclado y retorna una lista de tuplas de tamaño = 6, que contiene todos los datos de materias a ser insertados
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
    #Retorna una lista de tuplas tamaño = 6 con todos los datos en la self.__db referentes a materias
    def __readAllRows(self):
        try:
            conn = sql.connect(self.__db)
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
    #Pide los datos para filtrarlos bajo alguna condición, puede ser cualquier tipo de dato
    #Retorna lista de tuplas con tamaño = 6 con todos los datos de las materias que hagan match con la busqueda
    #Publico para el uso en historia academica 
    def searchByFilter(self, fieldName, fieldValue):
        try:
            conn = sql.connect(self.__db)
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
    #Recibe como datos la salida de batch row getter
    def __batchInsertRow(self):
        try:
            conn = sql.connect(self.__db)
            cursor = conn.cursor()
            instruction = f"INSERT INTO materias values(?, ?, ?, ?, ?, ?)"
            cursor.executemany(instruction, self.__multidata) #Enviar varios datos a la vez
            conn.commit();
            conn.close();
        except sql.Error as e:
            print (e)
        

    #Read order, ordena los datos de mayor a menor según el campo que le pidamos :p
    #Imprime los datos en forma de tablita
    #Método público para el uso en otros lugares
    def readOrdered(self, field: str):
        try:
            conn = sql.connect(self.__db)
            cursor = conn.cursor()
            instruction = f"SELECT * from materias ORDER BY {field} DESC" #Si le quitamos el DESC se ordenara de menor a mayor, "DESC" viene de DESCENDING
            cursor.execute(instruction)
            datos = cursor.fetchall()
            conn.commit();
            conn.close()
            self.tableMaterias(datos);
        except sql.Error as e:
            print (e)

    #Actualizar datos en un determinado campo de alguna materia
    """Actualizar materia en diseño lógico."""
    #Pide el fieldOnChange como un string, la data puede ser cualquier tipo de dato, y la identificación que responde al nombre code
    #Retorna un mensaje de felicitación si todo fue correcto
    def __update(self, fieldOnChange: str, dataOnChange, code: int):
        try:
            conn = sql.connect(self.__db)
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
    #Calcula el promedio de un campo, en este caso de creditos
    def __promedio(self):
        try:
            conn = sql.connect(self.__db)
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

    def main(self):
        #TODO
        while True:
            #validador inicial
            while True:
                try:
                    selector = input(
                    """
                    Bienvenido a materia
                    1. Añadir materia.
                    2. Actualizar idioma. 
                    3. Leer datos. 
                    Para salir presione otro numero.  
                    """)
                    selector = int(selector)
                    break
                except ValueError:
                    print("valor invalido")
            #Añadir materia
            if selector == 1:
                while True:
                    while True:
                        try:
                            subselector = input(
                                """
                                1. Para añadir una sola materia.
                                2. Añadir materia sin recibir datos. 
                                3. Para añadir múltiples materias.
                                Para salir cualquier otro numero.  
                                """)
                            subselector = int(subselector)
                            break
                        except ValueError:
                            print("valor invalido")
                    #Añadir una sola materia
                    if subselector == 1:
                        self.__rowGetter()
                        self.__insertRow()
                        data = (self.__codigo, self.__nombre, self.__facultad, self.__departamento, self.__idioma,self.__creditos)
                        self.tableMaterias([data])
                        break
                    #Añadir materia sin que se vean los datos
                    elif subselector==2:
                        self.__rowGetter()
                        self.__insertRow()
                        break
                    #Añadir multiples materias
                    elif subselector==3:
                        self.__batchRowGetter()
                        self.__batchInsertRow()
                        break
                    else:
                        break
            #Actualizar idioma
            if selector == 2:
                while True:
                    try:
                        codigo = input("Seleccione el codigo de la materia ")
                        codigo = int(codigo)
                        break
                    except ValueError:
                        print('Valor invalido')
                while True:
                    idioma = input("Escriba el nuevo idioma ")
                    if (type(idioma)!=str):
                        print('Ingrese un valor')
                    else:
                        break
                self.__update('idioma', idioma, codigo)
            #Leer datos
            if selector == 3:
                    while True:
                        self.clearConsole()
                        try:
                            subselector = input(
                                """
                                1. Si desea ver todas las materias.
                                2. Para bsucar con el código.
                                Cualquier otro número para salir
                                """ 
                                )
                            subselector=int(subselector)
                            break
                        except ValueError:
                            print("valor invalido")
                #Ver todas las materias
                    if(subselector == 1):
                        self.tableMaterias(self.__readAllRows())
                #Ver materias por codigos
                    if(subselector == 2):
                        while True:
                            try:
                                codigo = input("Escriba el codigo de la materia que quiere ver: ")
                                codigo = int(codigo)
                                break
                            except ValueError:
                                print("valor invalido")
                        self.tableMaterias( self.searchByFilter('codigo', codigo))
            else:
                break
