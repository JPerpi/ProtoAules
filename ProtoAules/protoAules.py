import sys
import os

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtUiTools import QUiLoader
from recursos_rc import *
import firebase_admin
from firebase_admin import credentials, firestore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Base de datos Firebase
        cred_path = os.path.join(os.path.dirname(
            __file__), "resources/credential.json")

        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

        # Inicializar el cargador de UI
        loader = QUiLoader()

        # Cargar pantallas
        self.login_screen = loader.load(os.path.join(
            os.path.dirname(__file__), "Screens/login_aules.ui"), self)
        self.alumne_ini = loader.load(os.path.join(
            os.path.dirname(__file__), "Screens/inici_alumne.ui"), self)
        self.profe_ini = loader.load(os.path.join(
            os.path.dirname(__file__), "Screens/inici_professor.ui"), self)

        # Añadir pantallas
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        # 0
        self.stacked_widget.addWidget(self.login_screen)
        # 1
        self.stacked_widget.addWidget(self.alumne_ini)
        # 2
        self.stacked_widget.addWidget(self.profe_ini)

        self.setCentralWidget(self.stacked_widget)

        # Eventos navegación
        self.login_screen.button_login.clicked.connect(self.accio_login)
        self.alumne_ini.sortir.clicked.connect(self.show_login)
        self.profe_ini.sortir.clicked.connect(self.show_login)

        # Volver al login
    def show_login(self):
        self.stacked_widget.setCurrentIndex(0)

    def accio_login(self):

       # Professor
        nombre_user = self.login_screen.username.text()
        if not (len(nombre_user) >= 2 and nombre_user[-1].isalpha() and nombre_user[:-1].isalnum()):
            users_db = self.db.collection("usuarios")
            query = users_db.where(field_path="username",
                                   op_string="==", value=nombre_user)
            result = query.get()
            if result:
                # comp_pass
                pass_user = self.login_screen.password.text()
                users_db = self.db.collection("usuarios")
                query = users_db.where(
                    field_path="password", op_string="==", value=pass_user)
                result_pass = query.get()
                if result_pass:
                    self.stacked_widget.setCurrentIndex(1)
                else:
                    msg_error = "El nombre de usuario o contraseña son incorrectos."
                    QMessageBox.information(
                        self, "Error al iniciar sesión", msg_error)

        # Alumne
        else:
            users_db = self.db.collection("usuarios")
            query = users_db.where(field_path="username",
                                   op_string="==", value=nombre_user)
            result = query.get()
            if result:
                # comp_pass
                pass_user = self.login_screen.password.text()
                users_db = self.db.collection("usuarios")
                query = users_db.where(
                    field_path="password", op_string="==", value=pass_user)
                result_pass = query.get()
                if result_pass:
                    self.stacked_widget.setCurrentIndex(2)
                else:
                    msg_error = "El nombre de usuario o contraseña son incorrectos."
                    QMessageBox.information(
                        self, "Error al iniciar sesión", msg_error)


def main():
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()