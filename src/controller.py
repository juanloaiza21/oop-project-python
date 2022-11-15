#Modulos de control
from materia import Materia
from historia_academica import AcadHistory
from estudiante import Estudiante
from table_creator import TableGen
from ranking import Ranking
from decouple import config

#DB
DB = config('DB_NAME')

#Instanciamiento
miMateria = Materia(DB)
miEstudiante = Estudiante(DB)
miRanking = Ranking(DB)
miTables = TableGen(DB)
miHistoria = AcadHistory(DB)

def main():
    NoneType = type(None)
    miTables.main()
    while True:
        validator = True
        while validator:
            try:
                selector = input( #Este input debe ser un número entero en el rango de 1 a 5, si no lo es, se repite
                    """
                    ¡Bienvenido al programa de gestión de notas!
                    1. Para entrar a 'materia'.
                    2. Para entrar en 'historia academica'.
                    3. Para entrar en 'estudiante'. 
                    4. Para ver el top de estudiante. 
                    5. Para salir. 
                    """
                    )
                selector = int(selector)
                validator = False
                while (selector!=1 and selector!=2 and selector!=3 and selector !=4 and selector!=5):
                    selector = input(f"{selector} no es valido ")
                    selector = int(selector)
            except ValueError:
                print("input invalido")
                validator = True
        if selector==1:
            miMateria.main()
        elif selector==2:
            miHistoria.main()
        elif selector==3:
            miEstudiante.main()
        elif selector==4:
            miRanking.main()
        elif selector==5:
            break;

