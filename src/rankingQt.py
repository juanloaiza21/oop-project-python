from ranking import Ranking
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
                    
   
#Main Window
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 - QTableWidget'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
   
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
   
        self.createTable()
   
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
   
        #Show window
        self.show()
   
    #Create table
    def createTable(self):
        rank = Ranking("DBTEST.db")
        data = rank.dataUnprint()

        self.tableWidget = QTableWidget()
        self.title = "POO FINAL G1-G1"
        self.tableWidget.setColumnCount(6)  
        self.tableWidget.setRowCount(len(data))

        self.tableWidget.setHorizontalHeaderLabels(["Codigo","Nombre", "Apellido", "Promedio", "Materias", "Creditos"]) 

        #Imprimir datos
        for i in range(len(data)):
            element = data[i]
            self.tableWidget.setItem(i,0, QTableWidgetItem(str(element[0])))
            self.tableWidget.setItem(i,1, QTableWidgetItem(str(element[1])))
            self.tableWidget.setItem(i,2, QTableWidgetItem(str(element[2])))
            self.tableWidget.setItem(i,3, QTableWidgetItem(str(element[3])))
            self.tableWidget.setItem(i,4, QTableWidgetItem(str(element[4])))
            self.tableWidget.setItem(i,5, QTableWidgetItem(str(element[5])))            

    
        #Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())