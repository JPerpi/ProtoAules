import sys
import os
import json
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox,QMenu, QFileDialog
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtUiTools import QUiLoader
from recursos_rc import *
import pandas as pd 
import datapane as dp 
import matplotlib


#import firebase_admin
#from firebase_admin import credentials, firestore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Base de datos Firebase
        #      cred_path = os.path.join(os.path.dirname(
        #         __file__), "resources/credential.json")
        #
        #       cred = credentials.Certificate(cred_path)
        #      firebase_admin.initialize_app(cred)
        #     self.db = firestore.client()

        # Inicialitzar el carregador de UI
        loader = QUiLoader()
        self.nombre_user=""
        # Cargar pantallas:
        self.login_screen = loader.load(os.path.join(
            os.path.dirname(__file__), "Screens/login_aules.ui"), self)
        self.alumne_ini = loader.load(os.path.join(
            os.path.dirname(__file__), "Screens/inici_alumne.ui"), self)
        self.profe_ini = loader.load(os.path.join(
            os.path.dirname(__file__), "Screens/inici_professor.ui"), self)
        self.llistaScreen=loader.load(os.path.join(
            os.path.dirname(__file__), "Screens/llista_alumnes.ui"), self)

        # Afegir pantalles:
        self.stacked_widget = QtWidgets.QStackedWidget(self)
       
        self.stacked_widget.addWidget(self.login_screen) # 0
        self.stacked_widget.addWidget(self.alumne_ini) # 1
        self.stacked_widget.addWidget(self.profe_ini) # 2
        self.stacked_widget.addWidget(self.llistaScreen) # 3

        self.setCentralWidget(self.stacked_widget)

        # Events navegació:
        self.login_screen.button_login.clicked.connect(self.accio_login)
        self.profe_ini.sortir.clicked.connect(self.show_login)
        self.profe_ini.llista.clicked.connect(self.show_llista)
        self.alumne_ini.sortir.clicked.connect(self.show_login)
        self.llistaScreen.sortir.clicked.connect(self.show_login)        

        #Funcions login:
        self.login_screen.password.returnPressed.connect(self.accio_login)

        #Funcions pantalla alumne:

        #Funcions pantalla profe:
        self.profe_ini.llista.clicked.connect(self.show_llista)
        self.profe_ini.ico1.setVisible(False)
        
        menu=QMenu(self)
        act1=QAction("Pujar tramessa",self)
        act1.triggered.connect(self.obrir_fitxer)
        act2=QAction("Editar tramessa",self)
        act3=QAction("Eliminar tramessa",self)
        menu.addAction(act1)
        menu.addAction(act2)
        menu.addAction(act3)
        self.profe_ini.tool_profesor.setMenu(menu)
        self.profe_ini.tool_profesor2.setMenu(menu)

        #Funcions pantalla llistaAlumnes:
        self.llistaScreen.cursos.clicked.connect(self.show_cursos)

    # Anar al login
    def show_login(self):
        self.stacked_widget.setCurrentIndex(0)
        self.login_screen.password.clear()
        self.login_screen.username.clear()
        self.login_screen.username.setFocus()

    # Anar a llistaAlumnes
    def show_llista(self):
        self.stacked_widget.setCurrentIndex(3)

    # Anar a cursos
    def show_cursos(self):
        self.stacked_widget.setCurrentIndex(2)

    #Comprobació d'inici de sessió
    def accio_login(self):

        self.nombre_user = self.login_screen.username.text() 
       
        pass_user = self.login_screen.password.text() 
       
        if not self.nombre_user[-1].isalpha():
            
            with open('alumnes.json') as json_file:
                    data = json.load(json_file)
            for usuario in data:
                if usuario["username"] == self.nombre_user and usuario["password"] == pass_user:    
                    self.stacked_widget.setCurrentIndex(1)
                    return

            msg_error = "El nombre de usuario o contraseña son incorrectos."
            QMessageBox.information(self, "Error al iniciar sesión", msg_error)
        else:
            with open('professors.json') as json_file:
                    data2 = json.load(json_file)
            for usuario in data2:
                if usuario["username"] == self.nombre_user and usuario["password"] == pass_user:
                    self.stacked_widget.setCurrentIndex(2)
                    return
                    
            msg_error = "El nombre de usuario o contraseña son incorrectos."
            QMessageBox.information(self, "Error al iniciar sesión", msg_error)

    def obrir_fitxer(self):
        # El ,_ es una forma de separar los valores
        path_doc,_=QFileDialog.getOpenFileName(self, "Seleccionar Archivo","","Archivos de Texto(*.txt);;Archivos PDF(*.pdf)")
        if path_doc:
            doc_nom=os.path.basename(path_doc)
            self.profe_ini.label.setText(doc_nom)
    
    def informeAlumne(self):

        base_path= os.path.dirname(__file__)
        json_path= os.path.join(base_path,"alumnes.json")
        f = open(json_path)

        datos=json.load(f)
        for alumne in datos:
            if alumne["username"]== self.nombre_user:

                data2=json.dumps(alumne)
                print(data2)

                df=pd.read_json(data2)

                tarta_matplotlib = df.plot.bar(y=['Notes'], ylabel="")
                tarta_datapane = dp.Plot(tarta_matplotlib)

                report = dp.Report(tarta_datapane)
                report_path = os.path.join(base_path, "json.html")
                report.save(path=report_path, open=True)
        f.close()

    # Per a canviar la icona depenent del tipus d'arxiu
    def canvi_icona(self):
        archivo = self.label.text().split(": ")[1]
        if archivo.endswith(".txt"):
            self.ico1.setText("Hola soc un txt")
        elif archivo.endswith(".pdf"):
            self.ico1.setText("Hola soc un pdf")
        else:
            self.ico1.setText("Hola soc un random")

def main():
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()