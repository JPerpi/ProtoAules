from PySide6.QtWidgets import *


class DialogoPersonalizado(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Dialogo personalizado")

        self.visi_button=QPushButton('Visibilitat')
        self.editar_button=QPushButton('Editar')
        self.esborrar_button=QPushButton('Esborrar')

        self.editar_button.clicked.connect(self.dialeg_guardar)

        
        self.layout_dialogo = QVBoxLayout()
        self.layout_dialogo.addWidget(self.visi_button)
        self.layout_dialogo.addWidget(self.esborrar_button)
        self.layout_dialogo.addWidget(self.editar_button)
        self.setLayout(self.layout_dialogo)


        
    def dialeg_guardar(self):
            finestra_dialeg = QFileDialog.getOpenFileName(
                self, caption="Obrir fitxer...", dir=".",
                filter="Documents de text (*.txt);;Documents PDF (*.pdf)",
                selectedFilter="Documents de text (*.txt)")
            fitxer = finestra_dialeg[0]
        

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        

        self.setWindowTitle("Aplicación con diálogo personalizado")

        boton = QPushButton("Editar")
        boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(boton)

    def mostrar_dialogo(self):
        
        ventana_dialogo = DialogoPersonalizado(self)
       
        ventana_dialogo.exec()
        
        


app = QApplication([])

ventana_principal = VentanaPrincipal()
ventana_principal.show()

app.exec()
