#Modulos de control
from materia import main as matController
from historia_academica import main as acadHistory
from estudiante import main as estudent
from table_creator import main as dbCreator
from ranking import main as rankingGen

def main():
    dbCreator()
    while True:
        validator = True
        while validator:
            try:
                selector = input(
                    """
                    ¡Bienvenido al programa de gestión de notas!
                    1. Para entrar a 'materia'.
                    2. Para entrar en 'historia academica'.
                    3. Para entrar en 'estudiante'. 
                    4. Para ver el top de estudiante presione 4. 
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
            matController()
        elif selector==2:
            acadHistory()
        elif selector==3:
            estudent()
        elif selector==4:
            rankingGen()
        elif selector==5:
            break;

