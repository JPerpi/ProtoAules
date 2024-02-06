# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_aules.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QWidget)
import ProtoAules.recursos_rc as recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(834, 588)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.FrameAules = QFrame(self.centralwidget)
        self.FrameAules.setObjectName(u"FrameAules")
        self.FrameAules.setGeometry(QRect(10, 80, 623, 77))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.FrameAules.sizePolicy().hasHeightForWidth())
        self.FrameAules.setSizePolicy(sizePolicy1)
        self.FrameAules.setMaximumSize(QSize(15000, 150))
        self.horizontalLayout_2 = QHBoxLayout(self.FrameAules)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(225, 75, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.FrameAules)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMaximumSize(QSize(350, 300))
        self.label_2.setStyleSheet(u"border-image: url(:/prefijoNuevo/png/logo_aules.png);")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(225, 75, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.LogoIdiomes = QFrame(self.centralwidget)
        self.LogoIdiomes.setObjectName(u"LogoIdiomes")
        self.LogoIdiomes.setGeometry(QRect(20, 10, 640, 52))
        sizePolicy1.setHeightForWidth(self.LogoIdiomes.sizePolicy().hasHeightForWidth())
        self.LogoIdiomes.setSizePolicy(sizePolicy1)
        self.LogoIdiomes.setMaximumSize(QSize(1500, 90))
        self.horizontalLayout = QHBoxLayout(self.LogoIdiomes)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.LogoIdiomes)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMaximumSize(QSize(400, 500))
        self.label.setStyleSheet(u"border-image: url(:/prefijoNuevo/png/logo gen.png);")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(400, 50, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.LogoIdiomes)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(35, 30))
        self.pushButton.setStyleSheet(u"border-image: url(:/prefijoNuevo/png/esp.png);")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.LogoIdiomes)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(35, 30))
        self.pushButton_3.setStyleSheet(u"border-image: url(:/prefijoNuevo/png/val.png);")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.LogoIdiomes)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(35, 30))
        self.pushButton_2.setStyleSheet(u"border-image: url(:/prefijoNuevo/png/ingles.png);")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 160, 889, 185))
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(1500, 185))
        self.frame.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(153, 193, 241);")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 30, 101, 21))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 70, 91, 22))
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(350, 30, 221, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(350, 70, 221, 30))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(400, 110, 121, 31))
        self.pushButton_4.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(98, 160, 234);")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(720, 160, 161, 22))
        font = QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 360, 131, 21))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(370, 490, 111, 41))
        self.textEdit.setStyleSheet(u"border-image: url(:/prefijoNuevo/png/Europa.png);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 834, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label.setText("")
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Recuperar contrase\u00f1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Per a l'alumnat", None))
    # retranslateUi

