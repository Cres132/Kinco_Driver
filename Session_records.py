from digitalclock import DigitalClock
from PyQt5.QtWidgets import QComboBox, QStyleFactory, QMainWindow,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtGui import QFont
import Admin_backend
import traceback
import sqlite3
import sys
import SessionControl


class Ui_Session_records_Window(QWidget):
    session_name=" "	
    def quit(self):
        sys.exit(app.exec_())    
    
    #tworzenie obiektow okna rejsetrow 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Name")
        MainWindow.setFixedSize(250, 150)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 15, 300, 25))
        self.label.setObjectName("label") 
        
        self.sessions= QtWidgets.QComboBox(self.centralwidget)
        self.sessions.setGeometry(QtCore.QRect(25, 50, 200, 25))
        
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 90 , 75, 25))
        self.pushButton_1.setObjectName("pushButton_7")        
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 90 , 75, 25))
        self.pushButton_2.setObjectName("pushButton_7") 
       

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

		
	#trzeba dodac wiecej zabezpieczen	
    def proceed_callback(self,MainWindow):
        try:
            SessionControl.session_name=self.sessions.currentText()
            self.ui = SessionControl.Ui_SessionControl_Window()
            self.ui.setupUi(self.ui)
            self.ui.show()     		
        
            self.close()
        except Exception:
            traceback.print_exc()
        
    def read_sessions(self):		
        tables_names=[]
        con = sqlite3.connect('Sessions.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor() 
        tables=con.execute('SELECT name FROM sqlite_master where type="table"')    
        for name in tables:
            tables_names.append(name[0])
        print(tables_names)
        self.sessions.addItems(tables_names)
        con.commit()
        
    def session_selected(self,MainWindow):
        self.session_name=self.sessions.currentText()
        
    def retranslateUi(self, MainWindow):	
        self.read_sessions();	
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Choose session"))
	    
        self.label.setText(_translate("MainWindow", "Choose  session to Open"))
        self.pushButton_1.setText(_translate("MainWindow", "Exit"))
        self.pushButton_1.clicked.connect(self.close)	  
	      
        self.pushButton_2.setText(_translate("MainWindow", "Open"))
        self.pushButton_2.clicked.connect(self.proceed_callback)
                
        self.sessions.currentTextChanged.connect(self.session_selected)
       
#funkcja startowa okna uzywana do testowania
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    ui = Ui_Session_records_Window()
    ui.setupUi(ui)
    ui.show()
    sys.exit(app.exec_())
