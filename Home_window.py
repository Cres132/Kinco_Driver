from digitalclock import DigitalClock
from PyQt5.QtWidgets import QComboBox, QStyleFactory, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtGui import QFont
import Home_backend


class Ui_Home_Window(object):
    names_list = []

    def quit(self):
        sys.exit(app.exec())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Kinco_Driver")
        MainWindow.resize(600, 500)
        MainWindow.setFixedSize(MainWindow.size())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 420, 100, 50))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 420, 100, 50))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 420, 100, 50))
        self.pushButton_3.setObjectName("pushButton_3")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 25, 331, 25))


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 75, 361, 25))


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 125, 211, 25))


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 175, 100, 25))



        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 225, 100, 25))


        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 275, 200, 25))


        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 325, 200, 25))


        self.Text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_edit.setGeometry(QtCore.QRect(20, 50, 200, 25))


        self.Text_edit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_edit_1.setGeometry(QtCore.QRect(20, 150, 200, 25))


        self.Text_edit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_edit_2.setGeometry(QtCore.QRect(20, 200, 200, 25))


        self.Text_edit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_edit_3.setGeometry(QtCore.QRect(20, 250, 200, 25))


        self.Text_edit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_edit_4.setGeometry(QtCore.QRect(20, 300, 200, 25))


        self.Text_edit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_edit_5.setGeometry(QtCore.QRect(20, 350, 200, 25))

        self.Method_choice = QtWidgets.QComboBox(self.centralwidget)
        self.Method_choice.setGeometry(QtCore.QRect(20, 100, 200, 25))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Home"))
        self.pushButton.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_2.setText(_translate("MainWindow", "Standard"))
        self.pushButton_2.clicked.connect(Home_backend.Homing.standard_homing())
        self.pushButton_3.setText(_translate("MainWindow", "start"))


        self.label.setText(_translate("MainWindow", "Home offset"))
        self.label_2.setText(_translate("MainWindow", "Homing method:"))
        self.label_3.setText(_translate("MainWindow", "Homing speed swtitch"))
        self.label_4.setText(_translate("MainWindow", "Homing speed zero"))
        self.label_5.setText(_translate("MainWindow", "Homing power on"))
        self.label_6.setText(_translate("MainWindow", "Homing acceleration"))
        self.label_7.setText(_translate("MainWindow", "Homing current"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    Home_Window = QtWidgets.QMainWindow()
    ui = Ui_Home_Window()
    ui.setupUi(Home_Window)
    Home_Window.show()
    sys.exit(app.exec_())

