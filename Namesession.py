from digitalclock import DigitalClock
from PyQt5.QtWidgets import QComboBox, QStyleFactory, QMainWindow,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtGui import QFont
import Admin_backend
import traceback

class Ui_NameSession_Window(QWidget):
    session_name=" "	
     
    
    #tworzenie obiektow okna rejsetrow 
    def setupUi(self, Widget):
        Widget.setObjectName("Name")
        Widget.setFixedSize(200, 150)
        
        self.centralwidget = QtWidgets.QWidget(Widget)
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

        

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        	
    def deafult_callback(self,event):
        session_name=" "
        Admin_backend.button_callbacks.savesession_buttton_callback(session_name) 
        self.close()
 	
    def save_name_callback(self,event):
        try:       
            print(event)
            session_name=self.session_name_box.toPlainText()
            Admin_backend.button_callbacks.savesession_buttton_callback(session_name)  
            self.close()

        except Exception:
            session_name=" "
            Admin_backend.button_callbacks.savesession_buttton_callback(session_name) 
            self.close()
			
    def retranslateUi(self, Widget):		
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Name new session"))
	    
        self.label.setText(_translate("Widget", "Choose name for session"))
        
        self.pushButton_1.setText(_translate("Widget", "deafult"))
        self.pushButton_1.clicked.connect(self.deafult_callback)	  
	      
        self.pushButton_2.setText(_translate("MWidget", "Save name"))
        self.pushButton_2.clicked.connect(self.save_name_callback)
       
#funkcja startowa okna uzywana do testowania
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    ui=Ui_NameSession_Window()
    ui.setupUi(ui)
    ui.show()
    sys.exit(app.exec_())
