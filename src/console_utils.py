import os

#Modulo para la creación de tablas en consola y ordenar la informacion
from prettytable import PrettyTable


#Funcion para limpiar la consola
def clearConsole():
    command = 'clear' #Para sistemas linux
    if os.name in ('nt', 'dos'):  # En caso de que este corriendo sobre windows
        command = 'cls'
    os.system(command) #Ejecución comando

#Tabla para materias
def tableMaterias(data):
    my_table = PrettyTable() #llamado al modulo de tablas en consola
    my_table.field_names = ["CODIGO", "NOMBRE", "FACULTAD", "DEPARTAMENTO", "IDIOMA", "CREDITOS"] #Nombre de los campos
    for i in range(len(data)):
        my_table.add_row(data[i])
    print(my_table)

#Tabla de historia academica
def tableHistoriaAcad(data):
    my_table = PrettyTable() #llamado al modulo de tablas en consola
    my_table.field_names = ["ID", "CODIGO MATERIA", "ID ESTUDIANTE", "NOTA", "CREDITOS"] #Nombre de los campos
    for i in range(len(data)):
        my_table.add_row(data[i])
    print(my_table)

#Tabla Estudiante
def tableEstudiante(data):
    my_table = PrettyTable() #llamado al modulo de tablas en consola
    my_table.field_names = ["IDENTIFICACION", "NOMBRE", "APELLIDO", "CARRERA", "FECHA NACIMIENTO", "FECHA INGRESO", "PROCEDENCIA", "CORREO ELECTRONICO", "CANTIDAD DE MATRICULAS"] #Nombre de los campos
    for i in range(len(data)):
        my_table.add_row(data[i])
    print(my_table)


#Tabla de historia academica
def tableRanking(data):
    my_table = PrettyTable() #llamado al modulo de tablas en consola
    my_table.field_names = ["ID", "PROMEDIO"] #Nombre de los campos
    for i in range(len(data)):
        my_table.add_row(data[i])
    print(my_table)