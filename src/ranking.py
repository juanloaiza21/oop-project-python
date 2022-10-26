from types import NoneType
from estudiante import readAllRows
from historia_academica import prom, acadHistoryById
from console_utils import tableRanking

#Busca todos los ids de la tabla estudiante y los guarda en una lista y devuelve esta lsita
def idsList():
    ids =[]
    data = readAllRows() #Data de todos los estudiantes
    for x in range(len(data)):
        ids.append(data[x][0]) #Acomoda los ids en lista
    return ids

#Devuelve el promedio junto a quien le pertenece
def promsCalculator(data):
    proms = []
    for i in range(len(data)):
        datos = acadHistoryById(data[i])
        promedy =prom(datos)
        if type(promedy)==NoneType:
            promedy = 0.0
        proms.append({data[i]:promedy}) #Organiza los datos como un diccionario y almacena este diccionario en una lista
    return proms #Devuelve una lista de diccionarios con las notas y sus respectivos dueños

#Convierte la lista de dictionarios en una lista de tuplas ordenadas
def dictToTuple(data):
    result = []
    for i in range(len(data)):
        result.append(data[i].popitem())
    return result

def main():
    data = idsList()
    promsList = promsCalculator(data)
    dataToOrder=dictToTuple(promsList)
    tableRanking(sorted(dataToOrder, key=lambda x: x[1], reverse=True)) #Ordena e imprime la lista de tuplas en orden descendente de acuerdo a la nota que estara siempre en indes = 1
