import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import RegresionLineal as myRL

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import (QTableWidgetItem,QTableWidget)




qtCreatorFile = "ui_principal.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnCargarDatos.clicked.connect(self.getxls)
        self.btnGraficar.clicked.connect(self.plot)
        self.cmbEstadistica.currentTextChanged.connect(self.estadisticas)
        self.btnEntrenar.clicked.connect(self.regresionLineal)
        self.btnCalcular.clicked.connect(self.regresionLineal_Prueba)
        
       
    def getxls(self):
        self.cmbX.clear()
        self.cmbY.clear()
        self.cmbX2.clear()
        self.cmbY2.clear()
        self.cmbEstadistica.clear()
        self.txtResultados.setText("")
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'ABRIR ARCHIVO', 'D:/Maestria/base de datos y conocimiento/RegresionLineal PyQt5/data')
        if filePath != "":
            
            self.df=pd.read_csv(str(filePath))
            self.cmbX.addItems(list(self.df.columns.values))
            self.cmbY.addItems(list(self.df.columns.values))

            self.cmbX2.addItems(list(self.df.columns.values))
            self.cmbY2.addItems(list(self.df.columns.values))
            
            # LLENAR LA TABLA
            self.tblDatos.clearContents()
            columnas=int(self.df.shape[1])
            filas=int(self.df.shape[0])
            self.tblDatos.setVerticalHeaderLabels(('Row 1', 'Row 2', 'Row 3'))
            self.tblDatos.setRowCount(filas)
            self.tblDatos.setColumnCount(columnas)
            
            self.tblDatos2.setVerticalHeaderLabels(('Row 1', 'Row 2', 'Row 3'))
            self.tblDatos2.setRowCount(filas)
            self.tblDatos2.setColumnCount(columnas)

            for c in range(0,columnas):
                for f in range(0,filas):
                    dato=str(self.df.iloc[f,c])
                    self.tblDatos.setItem(f,c,QTableWidgetItem(dato))
                    self.tblDatos2.setItem(f,c,QTableWidgetItem(dato))

    def plot (self):
        x=self.df[str(self.cmbX.currentText())]
        y=self.df[str(self.cmbY.currentText())]
        plt.plot(x,y)
        plt.show()
                
    def estadisticas(self):
        text = str(self.cmbEstadistica.currentText())
        if(text!=''):
            estad_st=str(self.cmbEstadistica.currentText())+str(self.df[self.cmbEstadistica.currentText()].describe())
            self.txtResultados.setText(estad_st)
    
    def regresionLineal(self):
        x=self.df[str(self.cmbX2.currentText())]
        y=self.df[str(self.cmbY2.currentText())]
        rl=myRL.regresionLineal()
        rl.plot_recta(x,y)
        self.txtB0.setText(str(rl.b0))
        self.txtB1.setText(str(rl.b1))
    
    def regresionLineal_Prueba(self):
        b0=float(self.txtB0.setText(str(rl.b0)))
        b1=float(self.txtB1.setText(str(rl.b1)))
        x=float(self.txtX.)
        


        
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()