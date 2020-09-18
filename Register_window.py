from digitalclock import DigitalClock
from PyQt5.QtWidgets import QComboBox, QStyleFactory, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtGui import QFont
import Admin_backend
import Interpretation

class Ui_Register_Window(object):
    Register_name = []
    Register_status = []
    Register_count=0
    def quit(self):
        Register_name = []
        Register_status = []
        sys.exit(app.exec())
		
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Kinco_Driver")
        MainWindow.resize(600, 550)

        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")  


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 500, 25))
        self.label.setFont(QFont('Arial', 10))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 25, 500, 25))
        self.label_2.setFont(QFont('Arial', 10))

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 500, 25))
        self.label_3.setFont(QFont('Arial', 10))

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 75, 500, 25))
        self.label_4.setFont(QFont('Arial', 10))


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 500, 25))
        self.label_5.setFont(QFont('Arial', 10))

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 125, 500, 25))
        self.label_6.setFont(QFont('Arial', 10))

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 500, 25))    
        self.label_7.setFont(QFont('Arial', 10))

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 175, 500, 25))
        self.label_8.setFont(QFont('Arial', 10))

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 200, 500, 25))
        self.label_9.setFont(QFont('Arial', 10))

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 225, 500, 25))
        self.label_10.setFont(QFont('Arial', 10))        

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 250, 500, 25))
        self.label_11.setFont(QFont('Arial', 10))


        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 275, 500, 25))
        self.label_12.setFont(QFont('Arial', 10))

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 300, 500, 25))
        self.label_13.setFont(QFont('Arial', 10))
        
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 325, 500, 25))
        self.label_14.setFont(QFont('Arial', 10))
        
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 350, 500, 25))
        self.label_15.setFont(QFont('Arial', 10))

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(10, 375, 500, 25))
        self.label_16.setFont(QFont('Arial', 10))

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(10, 400, 500, 25))
        self.label_17.setFont(QFont('Arial', 10))        

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(10, 425, 500, 25))
        self.label_18.setFont(QFont('Arial', 10))

        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(10, 450, 500, 25))
        self.label_19.setFont(QFont('Arial', 10))

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(10, 475, 500, 25))
        self.label_20.setFont(QFont('Arial', 10))
        
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(10, 500, 500, 25))
        self.label_21.setFont(QFont('Arial', 10))
        
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(10, 500, 500, 25))
        self.label_22.setFont(QFont('Arial', 10))
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 500, 100, 25))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(10, 500, 100, 25))
        self.pushButton2.setObjectName("pushButton")
        
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
    def next_registers(self, MainWindow):
        Register_count=self.Register_count
        Register_name=self.Register_name
        Register_status=self.Register_status
        while(len(self.Register_name)<60):
           Register_name.append([""])
           Register_status.append("")
        if(Register_count<1):
            Register_count=(Register_count+1)*20
            print(Register_status)
            print(Register_name)
            self.label.setText(str(Register_name[Register_count+0][0]+':'+Register_status[Register_count+0]))
            self.label_2.setText(str(Register_name[Register_count+1][0]+':'+Register_status[Register_count+1]))
            self.label_3.setText(str(Register_name[Register_count+2][0]+':'+Register_status[Register_count+2]))
            self.label_4.setText(str(Register_name[Register_count+3][0]+':'+Register_status[Register_count+3]))
            self.label_5.setText(str(Register_name[Register_count+4][0]+':'+Register_status[Register_count+4]))
            self.label_6.setText(str(Register_name[Register_count+5][0]+':'+Register_status[Register_count+5]))
            self.label_7.setText(str(Register_name[Register_count+6][0]+':'+Register_status[Register_count+6]))
            self.label_8.setText(str(Register_name[Register_count+7][0]+':'+Register_status[Register_count+7]))
            self.label_9.setText(str(Register_name[Register_count+8][0]+':'+Register_status[Register_count+8]))
            self.label_10.setText(str(Register_name[Register_count+9][0]+':'+Register_status[Register_count+9]))
            self.label_11.setText(str(Register_name[Register_count+10][0]+':'+Register_status[Register_count+10]))
            self.label_12.setText(str(Register_name[Register_count+11][0]+':'+Register_status[Register_count+11]))
            self.label_13.setText(str(Register_name[Register_count+12][0]+':'+Register_status[Register_count+12]))
            self.label_14.setText(str(Register_name[Register_count+13][0]+':'+Register_status[Register_count+13]))
            self.label_15.setText(str(Register_name[Register_count+14][0]+':'+Register_status[Register_count+14]))
            self.label_16.setText(str(Register_name[Register_count+15][0]+':'+Register_status[Register_count+15]))
            self.label_17.setText(str(Register_name[Register_count+16][0]+':'+Register_status[Register_count+16]))
            self.label_18.setText(str(Register_name[Register_count+17][0]+':'+Register_status[Register_count+17]))
            self.label_19.setText(str(Register_name[Register_count+18][0]+':'+Register_status[Register_count+18]))
            self.label_20.setText(str(Register_name[Register_count+19][0]+':'+Register_status[Register_count+19]))
            self.Register_count=int(Register_count/20)
            print(Register_count)
            
    def prev_registers(self, MainWindow):
        Register_count=self.Register_count
        Register_name=self.Register_name
        Register_status=self.Register_status
        if(Register_count>0):
            Register_count=(Register_count-1)*20
            self.label.setText(str(Register_name[Register_count+0][0]+':'+Register_status[Register_count+0]))
            self.label_2.setText(str(Register_name[Register_count+1][0]+':'+Register_status[Register_count+1]))
            self.label_3.setText(str(Register_name[Register_count+2][0]+':'+Register_status[Register_count+2]))
            self.label_4.setText(str(Register_name[Register_count+3][0]+':'+Register_status[Register_count+3]))
            self.label_5.setText(str(Register_name[Register_count+4][0]+':'+Register_status[Register_count+4]))
            self.label_6.setText(str(Register_name[Register_count+5][0]+':'+Register_status[Register_count+5]))
            self.label_7.setText(str(Register_name[Register_count+6][0]+':'+Register_status[Register_count+6]))
            self.label_8.setText(str(Register_name[Register_count+7][0]+':'+Register_status[Register_count+7]))
            self.label_9.setText(str(Register_name[Register_count+8][0]+':'+Register_status[Register_count+8]))
            self.label_10.setText(str(Register_name[Register_count+9][0]+':'+Register_status[Register_count+9]))
            self.label_11.setText(str(Register_name[Register_count+10][0]+':'+Register_status[Register_count+10]))
            self.label_12.setText(str(Register_name[Register_count+11][0]+':'+Register_status[Register_count+11]))
            self.label_13.setText(str(Register_name[Register_count+12][0]+':'+Register_status[Register_count+12]))
            self.label_14.setText(str(Register_name[Register_count+13][0]+':'+Register_status[Register_count+13]))
            self.label_15.setText(str(Register_name[Register_count+14][0]+':'+Register_status[Register_count+14]))
            self.label_16.setText(str(Register_name[Register_count+15][0]+':'+Register_status[Register_count+15]))
            self.label_17.setText(str(Register_name[Register_count+16][0]+':'+Register_status[Register_count+16]))
            self.label_18.setText(str(Register_name[Register_count+17][0]+':'+Register_status[Register_count+17]))
            self.label_19.setText(str(Register_name[Register_count+18][0]+':'+Register_status[Register_count+18]))
            self.label_20.setText(str(Register_name[Register_count+19][0]+':'+Register_status[Register_count+19]))           
            self.Register_count=int(Register_count/20)
   
    def retranslateUi(self, MainWindow):
       Admin_backend.message_sending.check_connection()
       self.Register_name = Interpretation.Status_registers
       self.Register_status = Interpretation.Status_registers_message
       Register_name=self.Register_name
       Register_status=self.Register_status 
       while(len(self.Register_name)<60):
           Register_name.append([""])
           Register_status.append("")    
       print(Interpretation.Status_registers_message)
       iter_temp=0
       _translate = QtCore.QCoreApplication.translate
       MainWindow.setWindowTitle(_translate("MainWindow", "Registers"))
       self.label.setText(_translate("MainWindow", str(Register_name[0][0]+':'+Register_status[0])))
       self.label_2.setText(_translate("MainWindow", str(Register_name[1][0]+':'+Register_status[1])))
       self.label_3.setText(_translate("MainWindow", str(Register_name[2][0]+':'+Register_status[2])))
       self.label_4.setText(_translate("MainWindow", str(Register_name[3][0]+':'+Register_status[3])))
       self.label_5.setText(_translate("MainWindow", str(Register_name[4][0]+':'+Register_status[4])))
       self.label_6.setText(_translate("MainWindow", str(Register_name[5][0]+':'+Register_status[5])))
       self.label_7.setText(_translate("MainWindow", str(Register_name[6][0]+':'+Register_status[6])))
       self.label_8.setText(_translate("MainWindow", str(Register_name[7][0]+':'+Register_status[7])))
       self.label_9.setText(_translate("MainWindow", str(Register_name[8][0]+':'+Register_status[8])))
       self.label_10.setText(_translate("MainWindow", str(Register_name[9][0]+':'+Register_status[9])))
       self.label_11.setText(_translate("MainWindow", str(Register_name[10][0]+':'+Register_status[10])))
       self.label_12.setText(_translate("MainWindow", str(Register_name[11][0]+':'+Register_status[11])))
       self.label_13.setText(_translate("MainWindow", str(Register_name[12][0]+':'+Register_status[12])))
       self.label_14.setText(_translate("MainWindow", str(Register_name[13][0]+':'+Register_status[13])))
       self.label_15.setText(_translate("MainWindow", str(Register_name[14][0]+':'+Register_status[14])))
       self.label_16.setText(_translate("MainWindow", str(Register_name[15][0]+':'+Register_status[15])))
       self.label_17.setText(_translate("MainWindow", str(Register_name[16][0]+':'+Register_status[16])))
       self.label_18.setText(_translate("MainWindow", str(Register_name[17][0]+':'+Register_status[17])))
       self.label_19.setText(_translate("MainWindow", str(Register_name[18][0]+':'+Register_status[18])))
       self.label_20.setText(_translate("MainWindow", str(Register_name[19][0]+':'+Register_status[19])))
       self.pushButton.setText(_translate("MainWindow", "next"))
       self.pushButton.clicked.connect(self.next_registers)
       self.pushButton2.setText(_translate("MainWindow", "prev"))
       self.pushButton2.clicked.connect(self.prev_registers)
       print(self.Register_name)

       
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    Register_Window = QtWidgets.QMainWindow()
    ui = Ui_Register_Window()
    ui.setupUi(Register_Window)
    Register_Window.show()
    sys.exit(app.exec_())

