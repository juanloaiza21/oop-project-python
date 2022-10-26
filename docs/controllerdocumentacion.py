from materia import main as matController # importar el metodo main del modulo materia para ser ejecutado por el nombre de matController
from historia_academica import main as acadHistory # importar el metodo main del modulo historia_academica para ser ejecutado por el nombre de acadHistory
from estudiante import main as estudent # importar el metodo main del modulo estudiante para ser ejecutado por el nombre de estudent
from table_creator import main as dbCreator# importar el metodo main del modulo table_creator para ser ejecutado por el nombre de dbCreator

def main(): #se define la funcion prinsipal de control
    dbCreator()#se ejecutara el metodo main importado del modulo table_creator para entrar al mismo
    while True: #generar un ciclo para permanecer en la aplicacion independientemente de la entrada del usuario a excepcion de la opcion salir
        validator = True #creacion del boleano para realiza la comprobacion que se realizo una entrada correcta por parte del usuario
        while validator: #generar un ciclo con la funcion de  ingresar y verificar la entrada del usuario, el cual solo se rompera cuando la entrada del usuario es valida
            try: #sentecia que se desea ejecutar sin presencia de ningun tipo de error
                selector = input("Para entrar a 'materia' presione 1, para entrar en 'historia academica' presione 2, para entrar en 'estudiante' presione 3, para salir presione 4. ") 
                #mensaje para el usuario sobre sus opcciones validas de entrada y entrada del mismo 
                selector = int(selector) #verificacion de que la entrada es un numero
                validator = False #cambiar el valor del boleano para finalizar el ciclo que pide la entrada del usuario 
                while (selector!=1 and selector!=2 and selector!=3 and selector !=4): #generar el ciclo de verificacion de que la entradad es uno de los valores validos
                    selector = input(f"{selector} no es valido ")#en caso de que la entrada no se un valor valido se generara un mensaje de no valides y se pedira nuevamente la entrada
                    selector = int(selector) #verificacion de que la entrada es un numero
            except ValueError:  #sentecia que se ejecuta en caso se presencia de algun error
                print("input invalido") #genrar mensaje de entrada invalida
                validator = True #cambiar el valor del boleano para que el ciclo de ingresar y verificar entrada del usuario continue 
        if selector==1:#sentencia en caso que la entrada del usuario sea 1
            matController()#con 1 como la entrada del usuario se ejecutara el metodo main importado del modulo materia para entrar al mismo
        elif selector==2:#sentencia en caso que la entrada del usuario sea 2
            acadHistory()#con 2 como la entrada del usuario se ejecutara el metodo main importado del modulo historia_academica para entrar al mismo
        elif selector==3:#sentencia en caso que la entrada del usuario sea 3
            estudent()#con 3 como la entrada del usuario se ejecutara el metodo main importado del modulo estudiante para entrar al mismo
        elif selector==4:#sentencia en caso que la entrada del usuario sea 4
            break;#con 4 como la entrada del usuario se rompera el ciclo prinsipal y asi salir del programa
