from unittest import result
from estudiante import readAllRows
from historia_academica import prom, acadHistoryById
from console_utils import tableRanking

def idsList():
    ids =[]
    data = readAllRows()
    for x in range(len(data)):
        ids.append(data[x][0])
    return ids

#Devuelve el promedio junto a quien le pertenece
def promsCalculator(data):
    proms = []
    for i in range(len(data)):
        datos = acadHistoryById(data[i])
        proms.append({data[i]:prom(datos)})
    return proms

def dictToTuple(data):
    result = []
    for i in range(len(data)):
        result.append(data[i].popitem())
    return result


def main():
    data = idsList()
    promsList = promsCalculator(data)
    dataToOrder=dictToTuple(promsList)
    tableRanking(sorted(dataToOrder, key=lambda x: x[1], reverse=True))