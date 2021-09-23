from digitalclock import DigitalClock
from PyQt5.QtWidgets import QComboBox, QStyleFactory, QMainWindow,QWidget, QListWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtGui import QFont
import Admin_backend
import sqlite3
import sys
import traceback

session_name=" "
class Ui_SessionControl_Window(QWidget):
	
    def quit(self):
        sys.exit(app.exec())       
    
    #tworzenie obiektow okna rejsetrow 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Name")
        MainWindow.setFixedSize(400, 300)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.PointList = QtWidgets.QListWidget(self.centralwidget)
        self.PointList.setGeometry(QtCore.QRect(10, 20, 380, 200))
        
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 260 , 75, 25))
        self.pushButton_1.setObjectName("pushButton_7")        
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 260 , 75, 25))
        self.pushButton_2.setObjectName("pushButton_7") 
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 260 , 75, 25))
        self.pushButton_3.setObjectName("pushButton_7")        
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 260 , 75, 25))
        self.pushButton_4.setObjectName("pushButton_7") 
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def deafult_callback(self,event):
        session_name=" "
        
 
    def read_points(self):
        try:
            con = sqlite3.connect('Sessions.db')
            con.row_factory = sqlite3.Row
            cur = con.cursor() 
            query='SELECT * FROM  %s'%session_name
            cur.execute(query)
            Points= cur.fetchall()
            for point in Points:
                self.PointList.addItem("x="+str(point[1])+"    "+"y="+str(point[2]))
            print(session_name)

            con.commit()
        except Exception:
            traceback.print_exc()	
			
	#trzeba dodac wiecej zabezpieczen	
    def save_name_callback(self,event):
        try:
            session_name=self.session_name_box.toPlainText()
             
        except Exception:
            traceback.print_exc()
			
    def retranslateUi(self, MainWindow):		
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Session Control"))
        
        self.pushButton_1.setText(_translate("MainWindow", "Delete"))
        #self.pushButton_1.clicked.connect(self.delete_callback)	  
	      
        self.pushButton_2.setText(_translate("MainWindow", "Add"))
        #self.pushButton_2.clicked.connect(self.save_name_callback)
        
        self.pushButton_3.setText(_translate("MainWindow", "Move"))
        #self.pushButton_3.clicked.connect(self.e_callback)	  
	      
        self.pushButton_4.setText(_translate("MainWindow", "Edit"))
        #self.pushButton_4.clicked.connect(self.save_name_callback)
        
        self.read_points()
       
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
