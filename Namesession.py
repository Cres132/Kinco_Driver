from digitalclock import DigitalClock
from PyQt5.QtWidgets import QComboBox, QStyleFactory, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtGui import QFont
import Admin_backend
import traceback

class Ui_NameSession_Window(object):
    session_name=" "	
    def quit(self):
        sys.exit(app.exec())       
    
    #tworzenie obiektow okna rejsetrow 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Name")
        MainWindow.setFixedSize(200, 150)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 5, 180, 25))
        self.label.setObjectName("label") 
        
        self.session_name_box = QtWidgets.QTextEdit(self.centralwidget)
        self.session_name_box.setGeometry(QtCore.QRect(10, 50, 180, 25))
        
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 90 , 75, 25))
        self.pushButton_1.setObjectName("pushButton_7")        
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 90 , 75, 25))
        self.pushButton_2.setObjectName("pushButton_7") 

        
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        	
    def deafult_callback(self,event):
        session_name=" "
        Admin_backend.button_callbacks.savesession_buttton_callback(session_name) 
		
	#trzeba dodac wiecej zabezpieczen	
    def save_name_callback(self,event):
        try:
            session_name=self.session_name_box.toPlainText()
            Admin_backend.button_callbacks.savesession_buttton_callback(session_name)  
        except Exception:
            traceback.print_exc()
			
    def retranslateUi(self, MainWindow):		
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Name new session"))
	    
        self.label.setText(_translate("MainWindow", "Choose name for session"))
        
        self.pushButton_1.setText(_translate("MainWindow", "deafult"))
        self.pushButton_1.clicked.connect(self.deafult_callback)	  
	      
        self.pushButton_2.setText(_translate("MainWindow", "Save name"))
        self.pushButton_2.clicked.connect(self.save_name_callback)
       
#funkcja startowa okna uzywana do testowania
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    Register_Window = QtWidgets.QMainWindow()
    ui = Ui_NameSession_Window()
    ui.setupUi(Register_Window)
    Register_Window.show()
    sys.exit(app.exec_())
