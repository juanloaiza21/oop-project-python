import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from ranking import Ranking


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        
    def headerData(self, p_int, Qt_Orientation, role=None):
        if role == Qt.DisplayRole and Qt_Orientation==Qt.Horizontal:
            header = [ "ID", "NOMBRE", "APELLIDO", "PROMEDIO", "CREDITOS", "MATERIAS"]
            return header[p_int]
        else:
            return QtCore.QAbstractTableModel.headerData(self, p_int, Qt_Orientation, role)        

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._ranking = Ranking("DBTEST.db")

        self.table = QtWidgets.QTableView()

        data = self._ranking.dataUnprint()

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()