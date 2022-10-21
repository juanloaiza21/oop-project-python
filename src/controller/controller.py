#Modulos de control
from modules.materia import main as matController
from modules.historia_academica import main as acadHistory
from modules.estudiante import main as estudent
from modules.table_creator import main as dbCreator

def main():
    dbCreator()
    while True:
        validator = True
        while validator:
            try:
                selector = input("Para entrar a 'materia' presione 1, para entrar en 'historia academica' presione 2, para entrar en 'estudiante' presione 3, para salir presione 4. ")
                selector = int(selector)
                validator = False
                while (selector!=1 and selector!=2 and selector!=3 and selector !=4):
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
            break;

