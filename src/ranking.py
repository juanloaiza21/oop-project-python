from types import NoneType
from estudiante import Estudiante
from historia_academica import AcadHistory
from console_utils import Console

class Ranking(Console):
#Busca todos los ids de la tabla estudiante y los guarda en una lista y devuelve esta lsita
    def __init__(self, db):
        self.__db = db
        self.__estudiante = Estudiante(self.__db)
        self.__acadHistory = AcadHistory(self.__db)
    
    def __idsList(self):
        ids =[]
        data = self.__estudiante.readAllRows() #Data de todos los estudiantes
        for x in range(len(data)):
            ids.append(data[x][0]) #Acomoda los ids en lista
        return ids

    #Devuelve el promedio junto a quien le pertenece
    def __promsCalculator(self, data):
        proms = []
        for i in range(len(data)):
            datos = self.__acadHistory.acadHistoryById(data[i])
            promedy =self.__acadHistory.prom(datos)
            if type(promedy)==NoneType:
                promedy = 0.0
            proms.append({data[i]:promedy}) #Organiza los datos como un diccionario y almacena este diccionario en una lista
        return proms #Devuelve una lista de diccionarios con las notas y sus respectivos dueños

    #Convierte la lista de dictionarios en una lista de tuplas ordenadas
    def __dictToTuple(self, data):
        result = []
        for i in range(len(data)):
            result.append(data[i].popitem())
        return result

    def main(self):
        data = self.__idsList()
        promsList = self.__promsCalculator(data)
        dataToOrder=self.__dictToTuple(promsList)
        self.tableRanking(sorted(dataToOrder, key=lambda x: x[1], reverse=True)) #Ordena e imprime la lista de tuplas en orden descendente de acuerdo a la nota que estara siempre en indes = 1
