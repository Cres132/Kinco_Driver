from digitalclock import DigitalClock
from PyQt5.QtWidgets import QComboBox,QStyleFactory,QMainWindow,QMessageBox ,QWidget,QVBoxLayout,QLabel,QCheckBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtGui import QFont
import Constants
import Admin_backend
import Home_window
import Register_window
import traceback
import Namesession
import Session_records
import Current_position

#klasa odpowiedzialna za tworzenia okna admina 
class Ui_GuestWindow(object):
	#tworzenie zmienncyh tymczasowych
    names_list=[]
    Readed_registers=[]
    Responded_messages_list=[]
    #zakoncz dzialanie programu po zamknieciu okna
    def quit(self):
        sys.exit(app.exec())
    #tworzenie obiektow okna admina
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Kinco_Driver")
        MainWindow.resize(800, 450)
        MainWindow.setFixedSize(MainWindow.size())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 280, 100, 60))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 280, 100, 60))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 280, 100, 60))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 280, 100, 60))
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(725, 120, 50, 25))
        self.pushButton_6.setObjectName("pushButton_5")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 280, 100, 60))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(650, 120, 50, 25))
        self.pushButton_8.setObjectName("pushButton_7")
        
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(50, 15, 120, 25))
        self.pushButton_9.setObjectName("pushButton_7")        
        
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(200, 15, 130, 25))
        self.pushButton_10.setObjectName("pushButton_7")   
        
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(350, 15, 130, 25))
        self.pushButton_11.setObjectName("pushButton_7")  

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(500, 15, 130, 25))
        self.pushButton_12.setObjectName("pushButton_7")         
         
        self.scrollAreaWidgetContents = QtWidgets.QWidget() 
        self.scrollArea2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea2.setGeometry(QtCore.QRect(50, 150, 701, 100))
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setObjectName("scrollArea")

        self.scrollArea2WidgetContents = QtWidgets.QWidget()
        self.scrollArea2WidgetContents.setGeometry(QtCore.QRect(0, 0, 699, 99))
        self.scrollArea2WidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea2.setWidget(self.scrollArea2WidgetContents)
        self.scrollArea2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setWidget(self.scrollAreaWidgetContents)



        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 350, 211, 25))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 75, 100, 25))
        self.label_4.setObjectName("label_3")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 100, 25))
        self.label_5.setObjectName("label_3")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 50, 110, 25))

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(230, 50, 140, 25))
        
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(380, 50, 140, 25))

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(530, 50, 130, 25))
        
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(680, 50, 80, 25))
    

        
        self.coordination_box_y = QtWidgets.QTextEdit(self.centralwidget)
        self.coordination_box_y.setGeometry(QtCore.QRect(120, 110, 80, 25))
               
        self.coordination_box_x = QtWidgets.QTextEdit(self.centralwidget)
        self.coordination_box_x.setGeometry(QtCore.QRect(120, 75, 80, 25))
		
        self.acceleration_box_x = QtWidgets.QTextEdit(self.centralwidget)
        self.acceleration_box_x.setGeometry(QtCore.QRect(260, 75, 80, 25))
        
        self.decceleration_box_x = QtWidgets.QTextEdit(self.centralwidget)
        self.decceleration_box_x.setGeometry(QtCore.QRect(400, 75, 80, 25))
        
        self.velocity_box_x = QtWidgets.QTextEdit(self.centralwidget)
        self.velocity_box_x.setGeometry(QtCore.QRect(540, 75, 80, 25))        
      	
        self.acceleration_box_y = QtWidgets.QTextEdit(self.centralwidget)
        self.acceleration_box_y.setGeometry(QtCore.QRect(260, 110, 80, 25))
        
        self.decceleration_box_y = QtWidgets.QTextEdit(self.centralwidget)
        self.decceleration_box_y.setGeometry(QtCore.QRect(400, 110, 80, 25))
        
        self.velocity_box_y = QtWidgets.QTextEdit(self.centralwidget)
        self.velocity_box_y.setGeometry(QtCore.QRect(540, 110, 80, 25)) 

    
        self.positioning_choice = QtWidgets.QComboBox(self.centralwidget)
        self.positioning_choice.setGeometry(QtCore.QRect(650, 75, 100, 25))


        self.responded_messages2 = QWidget()
        self.vbox2 = QVBoxLayout()
        #podzielenie okna na czesc z menu i czesc z obiektami
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #dodanie zegara na dole okna
        self.DigitalClock = DigitalClock(self.centralwidget)
        self.DigitalClock.setGeometry(QtCore.QRect(570, 375, 130, 21))
        self.retranslateUi(MainWindow) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
                
    #funkcja pobiera aktualna date    
    def getDate(self):
        date = QDate.currentDate()
        return date.toString(Qt.DefaultLocaleLongDate)
    
 
    #callback przcisku home do zaimplementopwania
    def Home_window(self):
        self.window = QMainWindow()
        self.Home_ui = Home_window.Ui_Home_Window()
        self.Home_ui.setupUi(self.window)
        self.window.show()
    #callback przycisku register uruchamia okno rejsetru
    def Register_window(self):
        #odpytaj serwomechnizm o stan jego rejestrow
        connection_result=Admin_backend.message_sending.check_connection()
        if (connection_result==0):
           self.window = QMainWindow()
           self.Register_ui = Register_window.Ui_Register_Window()
           self.Register_ui.setupUi(self.window)
           self.window.show()        
        else:
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Critical)
            self.msgbox.setText("Check connection")
            self.msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.msgbox.show()
    #callback przycisku test wykonuje test serwomechnizmow a w razie
    #problemow wyswietla informacje o bledzie    
     
    def Test_clicked(self):
		#wywolaj metode wykoujaca test
        result=Admin_backend.moving.do_test()    
        #wyswietl informacje czy test sie powiodl    
        if(result!=0):
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Critical)
            self.msgbox.setText("Test Error")
            self.msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.msgbox.show()
        else:
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Information)            
            self.msgbox.setText("Test completed succesful")
            self.msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.msgbox.show()
			 
    #funkcja odpowiedzialna za porusznie sie serwomechanizmow    		
    def Move_clicked(self):
        result=0
        try:
			#pobierz wartosci o ruchu podane przez uzytkownika i zapisz
			#w odpowienich zmiennych klasy asmin_backend
            Admin_backend.moving.position_x=int(self.coordination_box_x.toPlainText())
            Admin_backend.moving.position_y=int(self.coordination_box_y.toPlainText()) 
            Admin_backend.moving.zero=self.positioning_choice.currentText()                   
        except Exception:
            traceback.print_exc()
            result=6   
            #jesli aktualnie program nie namesession_ui wykonuje ruchu
        Admin_backend.move_deafult_flag[0]=1
        #wyswietl informacje o statusie ruchu 
        if(result!=6):               
            result=Admin_backend.moving.do_move()
        self.msgbox = QMessageBox()
        self.msgbox.setIcon(QMessageBox.Critical)
        if(result==1):
            self.msgbox.setText("wrong type of message")
        elif(result==2):
             self.msgbox.setText("one of value out of limit")
        elif(result==3):
            self.msgbox.setText("one of value out of limit")
        elif(result==4):
            self.msgbox.setText("Check connection")
        elif(result==5):
            self.msgbox.setText("Move Error")
        elif(result==6):
            self.msgbox.setText("Invalid input data")
        else:
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Information)            
            self.msgbox.setText("Move completed succesful")
            self.msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgbox.show() 
 	



        
    def savepoint_callback(self):
        Admin_backend.button_callbacks.savepoint_button_callback()
        object = QLabel('Unit1:'+str(Admin_backend.Position_save_info[0])+'     '+'Unit2:'+str(Admin_backend.Position_save_info[1]))
        self.vbox2.addWidget(object)	
        self.responded_messages2.setLayout(self.vbox2)			
        self.scrollArea2.setWidget(self.responded_messages2)
        

   
    def previous_callback(self):
        saved_coor=Admin_backend.button_callbacks.previous_buttton_callback()
        self.coordination_box_x.setText(str(saved_coor[0]))
        self.coordination_box_y.setText(str(saved_coor[1]))
	
    def next_callback(self):
        saved_coor=Admin_backend.button_callbacks.next_buttton_callback()
        self.coordination_box_x.setText(str(saved_coor[0]))
        self.coordination_box_y.setText(str(saved_coor[1]))
	
    def savesession_callback(self):
        self.namesession_ui = Namesession.Ui_NameSession_Window()
        self.namesession_ui.setupUi(self.namesession_ui)
        self.namesession_ui.show()     		
        
        
    def readsession_callback(self):
        self.readsession_ui = Session_records.Ui_Session_records_Window()
        self.readsession_ui.setupUi(self.readsession_ui)
        self.readsession_ui.show()     	
    
    def error_reset_callback(self):
        result=Admin_backend.button_callbacks.error_reset()
        if(result!=0): 
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Critical)        
            self.msgbox.setText("Reset error")
            
    def session_movement_callback(self):        
        self.currentPosition_ui = Current_position.Ui_current_position_window()
        self.currentPosition_ui.setupUi(self.currentPosition_ui)
        self.currentPosition_ui.show()   

        
			

    #funkcja uruchamiana przy starcie okna przypsiujaca wartosci oknu 
    #gui oraz deklarujaca callbacki
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kinco Driver"))
        self.pushButton.setText(_translate("MainWindow", "Home"))
        self.pushButton.clicked.connect(self.Home_window)
        self.pushButton_2.setText(_translate("MainWindow", "Save point"))
        self.pushButton_2.clicked.connect(self.savepoint_callback)
        self.pushButton_3.setText(_translate("MainWindow", "Previous"))
        self.pushButton_3.clicked.connect(self.previous_callback)
        self.pushButton_4.setText(_translate("MainWindow", "Next"))
        self.pushButton_4.clicked.connect(self.next_callback)
        self.pushButton_6.setText(_translate("MainWindow", "test"))
        self.pushButton_6.clicked.connect(self.Test_clicked)
        self.pushButton_7.setText(_translate("MainWindow", "Save session"))
        self.pushButton_7.clicked.connect(self.savesession_callback)
        self.pushButton_8.setText(_translate("MainWindow", "Move"))
        self.pushButton_8.clicked.connect(self.Move_clicked)
        self.pushButton_9.setText(_translate("MainWindow", "Registers_status"))
        self.pushButton_9.clicked.connect(self.Register_window)
        self.pushButton_10.setText(_translate("MainWindow", "Read Session"))
        self.pushButton_10.clicked.connect(self.readsession_callback)
        self.pushButton_11.setText(_translate("MainWindow", "Reset Error"))
        self.pushButton_11.clicked.connect(self.error_reset_callback)
        self.pushButton_12.setText(_translate("MainWindow", "Session Movement"))
        self.pushButton_12.clicked.connect(self.session_movement_callback)
        self.positioning_choice.addItems(Admin_backend.Positioning_values)
        self.label_3.setText(_translate("MainWindow", self.getDate() ))
        self.label_4.setText(_translate("MainWindow", "X Coordinate:"))
        self.label_5.setText(_translate("MainWindow", "Y Coordinate:"))
        self.label_11.setText(_translate("MainWindow", "Position(inc):"))
        self.label_12.setText(_translate("MainWindow", "Acceleration(rp/s^2):"))
        self.label_13.setText(_translate("MainWindow", "Deceleration(rp/s^2):"))
        self.label_14.setText(_translate("MainWindow", "Velocity(rpm):"))
        self.label_15.setText(_translate("MainWindow", "Zero:"))
        self.DigitalClock.setStyleSheet('background-color: black',)
        self.acceleration_box_x.setDisabled(True)          
        self.decceleration_box_x.setDisabled(True)  
        self.velocity_box_x.setDisabled(True)       	
        self.acceleration_box_y.setDisabled(True)  
        self.decceleration_box_y.setDisabled(True)          
        self.velocity_box_y.setDisabled(True) 
        self.Register_window()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_GuestWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

