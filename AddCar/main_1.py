import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector as con
import subprocess



class LoginApp(QDialog):
    def __init__(self) :
        super(LoginApp,self).__init__()
        loadUi("login-form.ui",self)
        self.b1.clicked.connect(self.login)
        self.b2.clicked.connect(self.show_reg)

    

    def login(self):
        un = self.t1.text()
        pw = self.t2.text()
        db = con.connect(host="localhost", user="root", password="", db="addcar") 
        cursor= db.cursor()
        cursor.execute("select * from userlist where username='"+ un +"' and password ='"+ pw +"'")
        result = cursor.fetchone() 
        self.t1.setText("")
        self.t2.setText("") 

        if result:
            QMessageBox.information(self,"Login Output","Your login successful !!!")
            subprocess.Popen(['python', 'main.py'])
            quit("main_1.py")
        else: 
            QMessageBox.information(self,"Login Output","Invalid user !! Register for new user !!!")


    def show_reg(self):
        widget.setCurrentIndex(1)


class RegApp(QDialog):
    def __init__(self) :
        super(RegApp,self).__init__()
        loadUi("register-form.ui",self)
        self.b3.clicked.connect(self.reg)
        self.b4.clicked.connect(self.show_login)

    def reg(self):
        un = self.t3.text()
        pw = self.t4.text()
        em = self.t5.text()
        ph = self.t6.text()

        db = con.connect(host="localhost", user="root", password="", db="addcar")
        cursor = db.cursor()
        cursor.execute("select * from userlist where username='"+ un +"' and password ='"+ pw +"'")
        result = cursor.fetchone()

        if result:
            QMessageBox.information(self,"Login form","The user already registred, Try another username")
        else:
            cursor.execute("insert into userlist values('"+ un +"','"+ pw +"','"+ em +"','"+ ph +"')")
            db.commit()
            QMessageBox.information(self,"Login form","The user registered successfully, You can login now!!")
            self.t3.setText("")
            self.t4.setText("")
            self.t5.setText("")
            self.t6.setText("")
            widget.setCurrentIndex(0)


    
    def show_login(self):
        widget.setCurrentIndex(0)
            

        


app =QApplication(sys.argv)    
widget = QtWidgets.QStackedWidget()
loginform = LoginApp()
registrationform = RegApp()
widget.addWidget(loginform)
widget.addWidget(registrationform)
widget.setCurrentIndex(0)
widget.setFixedWidth(400)
widget.setFixedHeight(500)

widget.show()

app.exec_()




