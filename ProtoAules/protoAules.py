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


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Inicialitzar el carregador de UI
        loader = QUiLoader()
        
        self.setMinimumSize(1151, 795)
        
        self.nombre_user=""
        self.nombre_assignatura=""

        # Carregar pantalles:
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
        self.alumne_ini.notes.clicked.connect(self.informeAlumne)

        #Funcions pantalla profe:
        self.profe_ini.llista.clicked.connect(self.show_llista)
        self.profe_ini.Notes.clicked.connect(self.informeProfe)
        
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
        self.llistaScreen.notes.clicked.connect(self.informeProfe)
        self.llistaAlumnes=[]
        self.agafarNoms()
        self.llistaScreen.cursos.clicked.connect(self.show_cursos)
        self.llistaScreen.al1.setText(self.llistaAlumnes[0])
        self.llistaScreen.qbAsis1.setChecked(True)
        self.llistaScreen.qbret1.stateChanged.connect(lambda state: self.retras_state_changed(state, 1))
        self.llistaScreen.qbfal1.stateChanged.connect(lambda state: self.falta_state_changed(state, 1))
        self.llistaScreen.al2.setText(self.llistaAlumnes[1])
        self.llistaScreen.qbAsis2.setChecked(True)
        self.llistaScreen.qbret2.stateChanged.connect(lambda state: self.retras_state_changed(state, 2))
        self.llistaScreen.qbfal2.stateChanged.connect(lambda state: self.falta_state_changed(state, 2))
        self.llistaScreen.al3.setText(self.llistaAlumnes[2])
        self.llistaScreen.qbAsis3.setChecked(True)
        self.llistaScreen.qbret3.stateChanged.connect(lambda state: self.retras_state_changed(state, 3))
        self.llistaScreen.qbfal3.stateChanged.connect(lambda state: self.falta_state_changed(state, 3))

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
        base_path= os.path.dirname(__file__)
        pass_user = self.login_screen.password.text() 
       
        if not self.nombre_user[-1].isalpha():
            
            with open(os.path.join(base_path,"resources/alumnes.json")) as json_file:
                    data = json.load(json_file)
            for usuario in data:
                if usuario["username"] == self.nombre_user and usuario["password"] == pass_user:    
                    self.stacked_widget.setCurrentIndex(1)
                    return

            msg_error = "El nombre de usuario o contraseña son incorrectos."
            QMessageBox.information(self, "Error al iniciar sesión", msg_error)
        else:
            with open(os.path.join(base_path,"resources/professors.json")) as json_file:
                    data2 = json.load(json_file)
            for usuario in data2:
                if usuario["username"] == self.nombre_user and usuario["password"] == pass_user:
                    self.nombre_assignatura=usuario["asignatura"]
                    self.profe_ini.cursos_2.setItemText(0,self.nombre_assignatura)
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
        json_path= os.path.join(base_path,"resources/alumnes.json")
        f = open(json_path)

        datos=json.load(f)
        for alumne in datos:
            if alumne["username"]== self.nombre_user:

                data2=json.dumps(alumne)
                

                df=pd.read_json(data2)

                tarta_matplotlib = df.plot.bar(y=['Notes'], ylabel="")
                tarta_datapane = dp.Plot(tarta_matplotlib)

                report = dp.Report(tarta_datapane)
                report_path = os.path.join(base_path, "resources/Informe alumne.html")
                report.save(path=report_path, open=True)
        f.close()

    def informeProfe(self):

        base_path= os.path.dirname(__file__)
        json_path= os.path.join(base_path,"resources/professors.json")
        f = open(json_path)

        datos=json.load(f)
        for professor in datos:
            if professor["username"]== self.nombre_user:

                data2=json.dumps(professor)
                

                df=pd.read_json(data2)

                tarta_matplotlib = df.plot.bar(y=['alumnes'], ylabel="")
                tarta_datapane = dp.Plot(tarta_matplotlib)

                report = dp.Report(tarta_datapane)
                report_path = os.path.join(base_path, "resources/Informe professor.html")
                report.save(path=report_path, open=True)
            f.close()
    
    def agafarNoms(self):
        base_path= os.path.dirname(__file__)
        json_path= os.path.join(base_path,"resources/alumnes.json")
        f = open(json_path)
        datos=json.load(f)
        for alumne in datos:
        
            self.llistaAlumnes.append(alumne["Nombre"])
        return self.llistaAlumnes
        f.close()

    def agafarAssignatura(self):
        base_path= os.path.dirname(__file__)
        json_path= os.path.join(base_path,"resources/professors.json")
        f = open(json_path)
        datos=json.load(f)
        for profe in datos:
            if profe["username"]== self.nombre_user:
                self.nombre_assignatura= profe["asignatura"]
                print(self.nombre_assignatura)
        f.close()

    def retras_state_changed(self, state,alumno):
        if state == 2:  # 2 es el estado de marcado
            all_checkboxes = {
                1: [self.llistaScreen.qbAsis1, self.llistaScreen.qbret1, self.llistaScreen.qbfal1],
                2: [self.llistaScreen.qbAsis2, self.llistaScreen.qbret2, self.llistaScreen.qbfal2],
                3: [self.llistaScreen.qbAsis3, self.llistaScreen.qbret3, self.llistaScreen.qbfal3]
            }
            current_checkboxes = all_checkboxes[alumno]
            for checkbox in current_checkboxes:
                if checkbox.isChecked() and checkbox is not self.sender():
                    checkbox.setChecked(False)

    def falta_state_changed(self, state, alumno):
        if state == 2:  # 2 es el estado de marcado
            all_checkboxes = {
                1: [self.llistaScreen.qbAsis1, self.llistaScreen.qbret1, self.llistaScreen.qbfal1],
                2: [self.llistaScreen.qbAsis2, self.llistaScreen.qbret2, self.llistaScreen.qbfal2],
                3: [self.llistaScreen.qbAsis3, self.llistaScreen.qbret3, self.llistaScreen.qbfal3]
            }
            current_checkboxes = all_checkboxes[alumno]
            for checkbox in current_checkboxes:
                if checkbox.isChecked() and checkbox is not self.sender():
                    checkbox.setChecked(False)
    
    def asistencia_state_changed(self, state,alumno):
        if state == 2:  # 2 es el estado de marcado
            all_checkboxes = {
                1: [self.llistaScreen.qbAsis1, self.llistaScreen.qbret1, self.llistaScreen.qbfal1],
                2: [self.llistaScreen.qbAsis2, self.llistaScreen.qbret2, self.llistaScreen.qbfal2],
                3: [self.llistaScreen.qbAsis3, self.llistaScreen.qbret3, self.llistaScreen.qbfal3]
            }
            current_checkboxes = all_checkboxes[alumno]
            for checkbox in current_checkboxes:
                if checkbox.isChecked() and checkbox is not self.sender():
                    checkbox.setChecked(False)
    

def main():
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()