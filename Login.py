
import sys
import sqlite3
from Admin_ui import *
from Guest_ui import *
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMessageBox,QLabel, QGridLayout ,QComboBox,\
    QMainWindow

class window(QWidget):

    def __init__(self, parent=None):
        super(window,self).__init__(parent)
        self.interfejs()

    def new_window(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def new_window2(self):
        self.window1 = QMainWindow()
        self.ui2 = Ui_MainWindow1()
        self.ui2.setupUi(self.window1)
        self.window1.show()



    def login(self):
        nadawca = self.sender()

        try:
            templist1=[]
            text1 = self.user.text()
            text2 = self.password.text()
            text3 = self.cb.currentText()

            if text3=="Guest":
                self.close()
                self.new_window2()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                users_database = sqlite3.connect('users.db')
                users_database.row_factory = sqlite3.Row
                user_cursor = users_database.cursor()
                user_cursor.execute(""" SELECT * FROM users """)
                fun=user_cursor.fetchall()
                for f in fun:
                    usercheck=f['user']
                    passwordcheck=f['password']
                    if usercheck==text1:
                        if passwordcheck==text2:
                            if text3 == "Admin":

                                self.close()
                                self.new_window()
                            else:
                                msg.setText("haslo nie tego ale blisko")
                                msg.exec_()
                        else:
                            msg.setText("haslo nie tego ale blisko")
                            msg.exec_()
                    else:
                        msg.setText("haslo nie tego")
                        msg.exec_()

        except ValueError:
            print("nope")

    def keyPressEvent(self, event): # Działanie przycisków Esc i Enter
        if event.key() == QtCore.Qt.Key_Escape:
            sys.exit()
        elif event.key() == QtCore.Qt.Key_Return:
            self.login()

    def interfejs(self):
        op1=QLabel("Użytkownik:")
        op2=QLabel("Hasło:")
        ukladT = QGridLayout()
        self.user = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password) # hasło nie jest widoczne przy wpisywaniu
        self.cb = QComboBox()
        self.cb.addItem("Admin")
        self.cb.addItem("Guest")
        ukladT.addWidget(op1, 1, 0)
        ukladT.addWidget(op2, 3, 0)
        ukladT.addWidget(self.user, 2, 0)
        ukladT.addWidget(self.password, 4, 0)
        ukladT.addWidget(self.cb, 0, 0)
        zaloguj = QPushButton("Zaloguj", self)
        anuluj = QPushButton("Anuluj", self)
        ukladT.addWidget(zaloguj,5,0)
        ukladT.addWidget(anuluj, 5, 1)
        self.setLayout(ukladT)
        self.resize(400, 200)
        self.setWindowTitle("Okno logowania")
        self.show()
        zaloguj.clicked.connect(self.login)
        anuluj.clicked.connect(sys.exit)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    okno = window()
    sys.exit(app.exec_())
