class Ui_MainWindow(object):#declaramos la clase Ui_MainWindow que contendrá las propiedades de la ventana emergente
    def setupUi(self, MainWindow):#definimos el método encargado de generar la interfaz
        MainWindow.setObjectName("MainWindow") #se designa el nombre del objeto 
        MainWindow.resize(800, 600)
        self.FrmRanking = QtWidgets.QWidget(MainWindow)
        self.FrmRanking.setObjectName("FrmRanking") #se designa el nombre del objeto de FrmRanking
        self.TblRanking = QtWidgets.QTableWidget(self.FrmRanking)#utilizamos la clase para hacer referencia que se usara una tabala
        self.TblRanking.setGeometry(QtCore.QRect(-10, 0, 811, 591)) #estipular los rangos de la tabla a crear
        self.TblRanking.setObjectName("TblRanking")#definimos otro objeto con el nombre TblRanking el cual representa la tabla creada
        self.TblRanking.setColumnCount(6)#definicion de la cantidad de columnas de TblRanking
        self.TblRanking.setRowCount(0) )#definicion de la cantidad de filas de TblRanking
        item = QtWidgets.QTableWidgetItem() #definimos el objeto item de la clase QTableWidgetItem
        self.TblRanking.setHorizontalHeaderItem(0, item) #determinamos una columna y el índice de esta
        item = QtWidgets.QTableWidgetItem()#definimos el objeto item de la clase QTableWidgetItem
        self.TblRanking.setHorizontalHeaderItem(1, item) #determinamos una columna y el índice de esta
        item = QtWidgets.QTableWidgetItem()#definimos el objeto item de la clase QTableWidgetItem
        self.TblRanking.setHorizontalHeaderItem(2, item) #determinamos una columna y el índice de esta
        item = QtWidgets.QTableWidgetItem()#definimos el objeto item de la clase QTableWidgetItem
        self.TblRanking.setHorizontalHeaderItem(3, item) #determinamos una columna y el índice de esta
        item = QtWidgets.QTableWidgetItem()#definimos el objeto item de la clase QTableWidgetItem
        self.TblRanking.setHorizontalHeaderItem(4, item) #determinamos una columna y el índice de esta
        item = QtWidgets.QTableWidgetItem()#definimos el objeto item de la clase QTableWidgetItem
        self.TblRanking.setHorizontalHeaderItem(5, item) #determinamos una columna y el índice de esta
        MainWindow.setCentralWidget(self.FrmRanking) #sentencia para definir los cambios como propios de la clase
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22)) #estipular los rangos del menubar en la interfas
        self.menubar.setObjectName("menubar") #se designa el nombre del objeto de menubar
        MainWindow.setMenuBar(self.menubar) #sentencia para definir los cambios como propios de la clase
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar") #se designa el nombre del objeto de statusbar
        MainWindow.setStatusBar(self.statusbar) #sentencia para definir los cambios como propios de la clase


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))#estipular la ubicación donde se hará el cambio
        item = self.TblRanking.horizontalHeaderItem(0) #definimos el odjeto para referirnos a la celda con el índice 0
        item.setText(_translate("MainWindow", "ID")) #cambiamos la propiedad del objeto para que muestre la palabra ID
        item = self.TblRanking.horizontalHeaderItem(1) #definimos el odjeto para referirnos a la celda con el índice 1
        item.setText(_translate("MainWindow", "Nombre"))#cambiamos la propiedad del objeto para que muestre la palabra Nombre
        item = self.TblRanking.horizontalHeaderItem(2) #definimos el odjeto para referirnos a la celda con el índice 2
