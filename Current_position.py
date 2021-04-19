from digitalclock import DigitalClock
from PyQt5.QtWidgets import QComboBox, QStyleFactory, QMainWindow,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtGui import QFont
import Admin_backend
import traceback
import pylab

time1=[]
time2=[]
movement1=[]	
movement2=[]

class Ui_current_position_window(QWidget):     
    
    #tworzenie obiektow okna rejsetrow 
    def setupUi(self, Widget):
        Widget.setObjectName("Name")
        Widget.setFixedSize(300, 150)
        
        self.centralwidget = QtWidgets.QWidget(Widget)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 5, 250, 25))
        self.label.setObjectName("label") 
        
        self.units= QtWidgets.QComboBox(self.centralwidget)
        self.units.setGeometry(QtCore.QRect(25, 50, 200, 25))
        
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 90 , 75, 25))
        self.pushButton_1.setObjectName("pushButton_7")        
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 90 , 75, 25))
        self.pushButton_2.setObjectName("pushButton_7")        

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)      
   

    
    def deafult_callback(self,event): 
        self.close()
 	
    def open_movement_window_callback(self,event):
        try:
            print(time1)
            print(movement1)
            print(time2)
            print(movement2)
            x=[]
            iter1=0
            if self.units.currentText()=="Unit 1":
                pylab.plot(time1,movement1)
                pylab.title("Unit 1 Movement")
                pylab.grid(True)
                pylab.show()
            else:                    
                pylab.plot(time2,movement2)
                pylab.title("Unit 2 Movement")
                pylab.grid(True)
                pylab.show()
            self.close()
        except Exception:
            traceback.print_exc()

			
    def retranslateUi(self, Widget):		
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Watch movement"))
        self.units.addItem("Unit 1")
        self.units.addItem("Unit 2")
        self.label.setText(_translate("Widget", "Choose unit to track movement"))
        
        self.pushButton_1.setText(_translate("Widget", "exit"))
        self.pushButton_1.clicked.connect(self.deafult_callback)	  
	      
        self.pushButton_2.setText(_translate("Widget", "display"))
        self.pushButton_2.clicked.connect(self.open_movement_window_callback)
       
#funkcja startowa okna uzywana do testowania
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    ui=Ui_current_position_window()
    ui.setupUi(ui)
    ui.show()
    sys.exit(app.exec_())


