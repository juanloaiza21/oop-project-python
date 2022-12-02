import os

#Modulo para la creación de tablas en consola y ordenar la informacion
from prettytable import PrettyTable

class Console: #Crea la clase "Console"
    #Funcion para limpiar la consola
    def clearConsole(self):
        command = 'clear' #Para sistemas linux
        if os.name in ('nt', 'dos'):  # En caso de que este corriendo sobre windows
            command = 'cls'
        os.system(command) #Ejecución comando

    #Tabla para materias
    def tableMaterias(self, data): #Data va a ser una lista de tuplas de tamaño 6, coumpuesta tanto por STR como por INT
        my_table = PrettyTable() #llamado al modulo de tablas en consola
        my_table.field_names = ["CODIGO", "NOMBRE", "FACULTAD", "DEPARTAMENTO", "IDIOMA", "CREDITOS"] #Nombre de los campos
        for i in range(len(data)):
            my_table.add_row(data[i])
        print(my_table)

    #Tabla de historia academica
    def tableHistoriaAcad(self, data): #Data va a ser una lista de tuplas de tamaño = 5, compuesta en su totalidad por INT
        my_table = PrettyTable() #llamado al modulo de tablas en consola
        my_table.field_names = ["ID", "CODIGO MATERIA", "ID ESTUDIANTE", "NOTA", "CREDITOS"] #Nombre de los campos
        for i in range(len(data)):
            my_table.add_row(data[i])
        print(my_table)

    #Tabla Estudiante
    def tableEstudiante(self, data): #Data va a ser una lista de tuplas. con tamaño = 9, compuesto por INT y STRINGS, tal como estan en la BD
        my_table = PrettyTable() #llamado al modulo de tablas en consola
        my_table.field_names = ["IDENTIFICACION", "NOMBRE", "APELLIDO", "CARRERA", "FECHA NACIMIENTO", "FECHA INGRESO", "PROCEDENCIA", "CORREO ELECTRONICO", "CANTIDAD DE MATRICULAS"] #Nombre de los campos
        for i in range(len(data)):
            my_table.add_row(data[i])
        print(my_table)


    #Tabla de historia academica
    def tableRanking(self, data): #Data va a ser una lista de tuplas, cada tupla será de un tamaño = 2, ambos datos seran int
        my_table = PrettyTable() #llamado al modulo de tablas en consola
        my_table.field_names = ["ID", "NOMBRE", "APELLIDO","PROMEDIO", "CREDITOS"] #Nombre de los campos
        for i in range(len(data)):
            my_table.add_row(data[i])
        print(my_table)
