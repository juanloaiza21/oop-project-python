from estudiante import Estudiante #importar Estudiante del modulo estudiante
from historia_academica import AcadHistory #importar AcadHistory del modulo historia_academica
from console_utils import Console #importar Console del modulo console_utils

class Ranking(Console): #creacion de la clase ranking
#Busca todos los ids de la tabla estudiante y los guarda en una lista y devuelve esta lsita
    def __init__(self, db): #funcion que inicializa los atributos
        self.__db = db #base de datos
        self.__estudiante = Estudiante(self.__db) #atributo Estudiante
        self.__acadHistory = AcadHistory(self.__db) #atributo AcadHistory
    
    def __idsList(self): #definir la funcion privada idsList
        ids =[] #creacion de una lista para ids
        data = self.__estudiante.readAllRows() #Data de todos los estudiantes
        for x in range(len(data)): #cantidad de caracteres de la informacion de los estudiantes
            element = data[x]
            ids.append((element[0], element[1], element[2])) #Acomoda los ids en lista
        return ids #devuelve la lista de ids

    #Devuelve el promedio junto a quien le pertenece
    def __promsCalculator(self, data): #definir la funcion privada promsCalculator
        proms = [] #creacion de una lista para promedios
        for i in range(len(data)): #cantidad de caracteres de la informacion de los promedios
            datos = self.__acadHistory.acadHistoryById(data[i][0]) #data de los id estudiantes #Donde 3 es nota, 4 creditos
            promedy =self.__acadHistory.prom(datos) #data de los promedios
            if promedy is None: #instancia en caso de que el promedio no exista
                promedy = 0.0 #el promedio es igual a 0.0
                creditos = 0
                cantidadMaterias = 0
            else:
                creditos = self.__acadHistory.creditss(data[i][0])
                cantidadMaterias = self.__acadHistory.materiass(data[i][0])
            proms.append({data[i]: (promedy, creditos, cantidadMaterias)}) #Organiza los datos como un diccionario y almacena este diccionario en una lista
        return proms #Devuelve una lista de diccionarios con las notas y sus respectivos dueños

        #Convierte la lista de dictionarios en una lista de tuplas ordenadas
    def __dictToTuple(self, data): #definir la funcion privada dictToTuple
        result = [] #creacion de una lista para resultados
        for i in range(len(data)): #cantidad de caracteres de la informacion 
            result.append(data[i].popitem()) #agrega la data a la lista
        return result #devuelve la lista de tuplas ordenadas

    def __tupleUnion(self, data):
        result = []
        for i in range(len(data)):
            element = data[i]
            subelement = element[0] + element[1]
            result.append(subelement)
        return result 

    #Metodo para usar en la parte gráfica
    def dataUnprint(self):
        print("Entra")
        data = self.__idsList() #data del metodo privado de ids de los estudiantes
        proms = self.__promsCalculator(data)
        dataToOrder=self.__dictToTuple(proms) #data de la lista de tuplas en orden
        tuples = self.__tupleUnion(dataToOrder)
        return sorted(tuples, key=lambda x: x[3], reverse=True)

    def main(self): #definir el metodo controlador del modulo ranking
        data = self.__idsList() #data del metodo privado de ids de los estudiantes
        proms = self.__promsCalculator(data)
        dataToOrder=self.__dictToTuple(proms) #data de la lista de tuplas en orden
        tuples = self.__tupleUnion(dataToOrder)
        self.tableRanking(sorted(tuples, key=lambda x: x[3], reverse=True)) #Ordena e imprime la lista de tuplas en orden descendente de acuerdo a la nota que estara siempre en indes = 1


data = Ranking("DBTEST.db")
print(data.dataUnprint())