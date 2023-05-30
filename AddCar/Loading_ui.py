from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Splash(object):
    def setupUi(self, Splash):
        Splash.setObjectName("Splash")
        Splash.resize(1000, 610)
        self.centralwidget = QtWidgets.QWidget(Splash)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(749, 576, 241, 20))
        self.label_3.setStyleSheet("font: 75 10pt \"MS Sans Serif\";\n"
"color:rgb(26, 26, 26)")
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(180, 470, 661, 41))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    \n"
"    background-color: rgb(102, 102, 102);\n"
"    color: rgb(200, 200, 200);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(166, 166, 166, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 520, 181, 31))
        self.label_2.setStyleSheet("font: 75 14pt \"Oswald\";\n"
"color: rgb(26, 26, 26);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1071, 611))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\ITlea\\OneDrive\\Bureau\\Projet_PFA\\AddCar\\Icon/1234.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.progressBar.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        Splash.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash)
        QtCore.QMetaObject.connectSlotsByName(Splash)

    def retranslateUi(self, Splash):
        _translate = QtCore.QCoreApplication.translate
        Splash.setWindowTitle(_translate("Splash", "MainWindow"))
        self.label_3.setText(_translate("Splash", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#1a1a1a;\">Créer Par</span><span style=\" font-weight:600;\"> : </span><span style=\" font-weight:600; color:#1a1a1a;\">Salaheddine Sahnoune</span></p></body></html>"))
        self.label_2.setText(_translate("Splash", "Téléchargement..."))
