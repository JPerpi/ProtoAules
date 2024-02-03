import sys, os
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from recursos_rc import *

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
ui_path = os.path.join(os.path.dirname(__file__), "Screeens/login_aules.ui")
window = loader.load(ui_path, None)
window.show()
app.exec()
