# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ITlea\OneDrive\Bureau\Projet_PFA\AddCar\login-form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(394, 500)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 380, 480))
        self.widget.setStyleSheet("background-color:rgba(16,16,16,255);\n"
"border-radius:20px;\n"
"")
        self.widget.setObjectName("widget")
        self.t1 = QtWidgets.QLineEdit(self.widget)
        self.t1.setGeometry(QtCore.QRect(10, 240, 361, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.t1.setFont(font)
        self.t1.setStyleSheet("background-color:rgba(47,49,52,200);\n"
"color:rgb(255,255,255);\n"
"border-radius:2px;\n"
"padding-left:10px;\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"padding-bottom:3px;")
        self.t1.setObjectName("t1")
        self.t2 = QtWidgets.QLineEdit(self.widget)
        self.t2.setGeometry(QtCore.QRect(10, 290, 361, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.t2.setFont(font)
        self.t2.setStyleSheet("background-color:rgba(47,49,52,200);\n"
"color:rgb(255,255,255);\n"
"border-radius:2px;\n"
"padding-left:10px;\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"padding-bottom:3px;")
        self.t2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.t2.setObjectName("t2")
        self.b1 = QtWidgets.QPushButton(self.widget)
        self.b1.setGeometry(QtCore.QRect(10, 340, 361, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setStyleSheet("QPushButton#b1{\n"
"background-color:rgb(255,191,16);\n"
"color:rgb(0,0,0);\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton#b1:pressed{\n"
"background-color:rgb(255,255,16);\n"
"\n"
"\n"
"}")
        self.b1.setObjectName("b1")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(150, 70, 91, 111))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255,191,16);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(140, 400, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255,191,16);")
        self.label_2.setObjectName("label_2")
        self.b2 = QtWidgets.QPushButton(self.widget)
        self.b2.setGeometry(QtCore.QRect(125, 430, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setStyleSheet("QPushButton#b2{\n"
"background-color:rgb(255,191,16);\n"
"color:rgb(0,0,0);\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton#b2:pressed{\n"
"background-color:rgb(255,255,16);\n"
"\n"
"\n"
"}")
        self.b2.setObjectName("b2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.t1.setPlaceholderText(_translate("Form", "Enter your username"))
        self.t2.setPlaceholderText(_translate("Form", "Enter your password"))
        self.b1.setText(_translate("Form", "L o g i n"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", "New user Sign Up"))
        self.b2.setText(_translate("Form", "R e g i s t e r  N o w"))