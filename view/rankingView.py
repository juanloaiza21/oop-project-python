# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ranking.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.FrmRanking = QtWidgets.QWidget(MainWindow)
        self.FrmRanking.setObjectName("FrmRanking")
        self.TblRanking = QtWidgets.QTableWidget(self.FrmRanking)
        self.TblRanking.setGeometry(QtCore.QRect(-10, 0, 811, 591))
        self.TblRanking.setObjectName("TblRanking")
        self.TblRanking.setColumnCount(6)
        self.TblRanking.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TblRanking.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TblRanking.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TblRanking.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TblRanking.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TblRanking.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TblRanking.setHorizontalHeaderItem(5, item)
        MainWindow.setCentralWidget(self.FrmRanking)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.TblRanking.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.TblRanking.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.TblRanking.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.TblRanking.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Materias"))
        item = self.TblRanking.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Créditos"))
        item = self.TblRanking.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Promedio"))
