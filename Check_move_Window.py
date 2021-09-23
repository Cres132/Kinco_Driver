from digitalclock import DigitalClock
from PyQt5.QtWidgets import QComboBox, QStyleFactory, QMainWindow,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QFont
import sqlite3
import Admin_backend
import Admin_ui
import Interpretation
import traceback
import sys
import time

class Ui_Check_move_Window(QWidget):
    Unit_name=""
    unit_position=""         
    #tworzenie obiektow okna rejsetrow 
    def setupUi(self, Widget):
		
        Widget.setObjectName("Current move")
        Widget.setFixedSize(300, 150)

        self.centralwidget = QtWidgets.QWidget(Widget)
        self.centralwidget.setObjectName("centralwidget")       
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 300, 25)) 
        
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(60, 60 , 120, 40))     

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        	
    def quit(self): 
        self.close()
        
    def update_label(self,label):
        self.label.setText(label)
                  
    def Cancel_move_callback(self):
        Admin_backend.stop_thread=1       		      
        self.close()		
			
    def retranslateUi(self, Widget):  
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Current move"))
	    
        self.label.setText(_translate("Widget", "starting..."))
        
        self.pushButton_1.setText(_translate("Widget", "cancel move"))
        self.pushButton_1.clicked.connect(self.Cancel_move_callback)	   
              
    def closeEvent(self, event):
        print("zamkniete")

#funkcja startowa okna uzywana do testowania
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Check_move_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
