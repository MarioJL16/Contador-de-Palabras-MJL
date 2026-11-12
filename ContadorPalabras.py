import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        #CARGA DE NUESTRA VISTA
        uic.loadUi("contadorPalabras.ui",self)
        self.btnContar.clicked.connect(self.ContarPalabras)
        
    def ContarPalabras(self):
        
        #Recuperar texto (check)
        texto = self.edtCaracteres.text()
        
        #Separar palabras (check)
        textoSeparado = texto.split()
        print(textoSeparado)
        
        #Contar palabras
        #Contar caracteres
        print("Papu")
        
app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec())