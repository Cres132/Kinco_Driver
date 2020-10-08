from digitalclock import DigitalClock
from PyQt5.QtWidgets import QComboBox,QStyleFactory,QMainWindow,QMessageBox ,QWidget,QVBoxLayout,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtGui import QFont
import Constants
import Admin_backend
import Home_window
import Register_window
class Ui_GuestWindow(object):
    names_list=[]
    Readed_registers=[]
    Responded_messages_list=[]
    def quit(self):
        sys.exit(app.exec())

    def setup_guest_Ui(self, MainWindow):
        MainWindow.setObjectName("Kinco_Driver")
        MainWindow.resize(800, 400)
        MainWindow.setFixedSize(MainWindow.size())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 250, 100, 60))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 250, 100, 60))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 250, 100, 60))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 250, 100, 60))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(725, 245, 50, 25))
        self.pushButton_6.setObjectName("pushButton_5")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 250, 100, 60))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(360, 90, 50, 25))
        self.pushButton_8.setObjectName("pushButton_7")
        
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 5, 120, 25))
        self.pushButton_9.setObjectName("pushButton_7")
        
        self.coordination_box_x = QtWidgets.QTextEdit(self.centralwidget)
        self.coordination_box_x.setGeometry(QtCore.QRect(100, 90, 100, 25))


        self.scrollArea2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea2.setGeometry(QtCore.QRect(50, 130, 701, 100))
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setObjectName("scrollArea")

        self.scrollArea2WidgetContents = QtWidgets.QWidget()
        self.scrollArea2WidgetContents.setGeometry(QtCore.QRect(0, 0, 699, 99))
        self.scrollArea2WidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea2.setWidget(self.scrollArea2WidgetContents)


        # Date
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 330, 211, 25))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 60, 100, 25))
        self.label_4.setObjectName("label_3")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 60, 100, 25))
        self.label_5.setObjectName("label_3")


        self.label_10 = QtWidgets.QLabel(self.scrollArea2)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 500, 25))
        self.label_10.setObjectName("label_3")

        self.coordination_box_y = QtWidgets.QTextEdit(self.centralwidget)
        self.coordination_box_y.setGeometry(QtCore.QRect(250, 90, 100, 25))


        self.responded_messages = QWidget()
        self.vbox = QVBoxLayout()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.DigitalClock = DigitalClock(self.centralwidget)
        self.DigitalClock.setGeometry(QtCore.QRect(570, 353, 130, 21))
        self.retranslateUi(MainWindow) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        
    def getDate(self):
        date = QDate.currentDate()
        return date.toString(Qt.DefaultLocaleLongDate)
    
    def Home_window(self):
        self.window = QMainWindow()
        self.Home_ui = Home_window.Ui_Home_Window()
        self.Home_ui.setupUi(self.window)
        self.window.show()

    def Register_window(self):
        self.window = QMainWindow()
        self.Register_ui = Register_window.Ui_Register_Window()
        self.Register_ui.setupUi(self.window)
        self.window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kinco Driver"))
        self.pushButton.setText(_translate("MainWindow", "Home"))
        self.pushButton.clicked.connect(self.Home_window)
        self.pushButton_2.setText(_translate("MainWindow", "Save point"))
        self.pushButton_3.setText(_translate("MainWindow", "previous"))
        self.pushButton_4.setText(_translate("MainWindow", "next"))
        self.pushButton_7.setText(_translate("MainWindow", "Save session"))
        self.pushButton_8.setText(_translate("MainWindow", "move"))
        self.pushButton_9.setText(_translate("MainWindow", "Registers_status"))
        self.pushButton_9.clicked.connect(self.Register_window)
        self.label_3.setText(_translate("MainWindow", self.getDate() ))
        self.label_4.setText(_translate("MainWindow", "X Coordinate:"))
        self.label_5.setText(_translate("MainWindow", "Y Coordinate:"))
        self.DigitalClock.setStyleSheet('background-color: black',)
        self.Register_window()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    GuestWindow = QtWidgets.QMainWindow()
    ui = Ui_GuestWindow()
    ui.setup_guest_Ui(GuestWindow)
    GuestWindow.show()
    sys.exit(app.exec_())

