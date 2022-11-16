from types import NoneType #importar NoneType del modulo types
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
            ids.append(data[x][0]) #Acomoda los ids en lista
        return ids #devuelve la lista de ids

    #Devuelve el promedio junto a quien le pertenece
    def __promsCalculator(self, data): #definir la funcion privada promsCalculator
        proms = [] #creacion de una lista para promedios
        for i in range(len(data)): #cantidad de caracteres de la informacion de los promedios
            datos = self.__acadHistory.acadHistoryById(data[i]) #data de los id estudiantes
            promedy =self.__acadHistory.prom(datos) #data de los promedios
            if type(promedy)==NoneType: 
                promedy = 0.0
            proms.append({data[i]:promedy}) #Organiza los datos como un diccionario y almacena este diccionario en una lista
        return proms #Devuelve una lista de diccionarios con las notas y sus respectivos dueños

    #Convierte la lista de dictionarios en una lista de tuplas ordenadas
    def __dictToTuple(self, data): #definir la funcion privada dictToTuple
        result = [] #creacion de una lista para resultados
        for i in range(len(data)): #cantidad de caracteres de la informacion 
            result.append(data[i].popitem()) #agrega la data a la lista
        return result #devuelve la lista de tuplas ordenadas

    def main(self): #definir el metodo controlador del modulo ranking
        data = self.__idsList() #data del metodo privado de ids de los estudiantes
        promsList = self.__promsCalculator(data) #data del metodo privado de promedios
        dataToOrder=self.__dictToTuple(promsList) #data de la lista de tuplas en orden
        self.tableRanking(sorted(dataToOrder, key=lambda x: x[1], reverse=True)) #Ordena e imprime la lista de tuplas en orden descendente de acuerdo a la nota que estara siempre en indes = 1
