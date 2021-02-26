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

#klasa odpowiedzialna za tworzenia okna admina 
class Ui_MainWindow(object):
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
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(MainWindow.size())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 450, 100, 60))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 450, 100, 60))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 450, 100, 60))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 450, 100, 60))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 55, 50, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(725, 300, 50, 25))
        self.pushButton_6.setObjectName("pushButton_5")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 450, 100, 60))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(650, 300, 50, 25))
        self.pushButton_8.setObjectName("pushButton_7")
        
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 5, 120, 25))
        self.pushButton_9.setObjectName("pushButton_7")        
        
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(630, 5, 120, 25))
        self.pushButton_10.setObjectName("pushButton_7")   
        
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(630, 40, 120, 25))
        self.pushButton_11.setObjectName("pushButton_7")  

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 140, 701, 100))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 100, 699, 99))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.scrollArea2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea2.setGeometry(QtCore.QRect(50, 330, 701, 100))
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setObjectName("scrollArea")

        self.scrollArea2WidgetContents = QtWidgets.QWidget()
        self.scrollArea2WidgetContents.setGeometry(QtCore.QRect(0, 0, 699, 99))
        self.scrollArea2WidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea2.setWidget(self.scrollArea2WidgetContents)
        self.scrollArea2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setWidget(self.scrollAreaWidgetContents)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 5, 331, 25))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(125, 5, 361,25))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 530, 211, 25))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 265, 100, 25))
        self.label_4.setObjectName("label_3")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 295, 100, 25))
        self.label_5.setObjectName("label_3")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(375, 5, 70, 25))
        self.label_6.setObjectName("label_3")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 5, 100, 25))
        self.label_7.setObjectName("label_3")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setFont(QFont('Arial', 12))
        self.label_8.setGeometry(QtCore.QRect(40, 70, 500, 60))
        self.label_8.setObjectName("label_3")

        self.label_9 = QtWidgets.QLabel(self.scrollArea)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 500, 25))
        self.label_9.setObjectName("label_3")



        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 245, 110, 25))

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(230, 245, 140, 25))
        
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(380, 245, 140, 25))

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(530, 245, 130, 25))
        
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(680, 245, 80, 25))
        
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(10, 245, 80, 25))
        
        self.deafult_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.deafult_checkbox.move(70,250)
        
        self.coordination_box_y = QtWidgets.QTextEdit(self.centralwidget)
        self.coordination_box_y.setGeometry(QtCore.QRect(120, 295, 80, 25))
               
        self.coordination_box_x = QtWidgets.QTextEdit(self.centralwidget)
        self.coordination_box_x.setGeometry(QtCore.QRect(120, 265, 80, 25))
		
        self.acceleration_box_x = QtWidgets.QTextEdit(self.centralwidget)
        self.acceleration_box_x.setGeometry(QtCore.QRect(260, 265, 80, 25))
        
        self.decceleration_box_x = QtWidgets.QTextEdit(self.centralwidget)
        self.decceleration_box_x.setGeometry(QtCore.QRect(400, 265, 80, 25))
        
        self.velocity_box_x = QtWidgets.QTextEdit(self.centralwidget)
        self.velocity_box_x.setGeometry(QtCore.QRect(540, 265, 80, 25))        
      	
        self.acceleration_box_y = QtWidgets.QTextEdit(self.centralwidget)
        self.acceleration_box_y.setGeometry(QtCore.QRect(260, 295, 80, 25))
        
        self.decceleration_box_y = QtWidgets.QTextEdit(self.centralwidget)
        self.decceleration_box_y.setGeometry(QtCore.QRect(400, 295, 80, 25))
        
        self.velocity_box_y = QtWidgets.QTextEdit(self.centralwidget)
        self.velocity_box_y.setGeometry(QtCore.QRect(540, 295, 80, 25))
        
        self.Message_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.Message_edit.setGeometry(QtCore.QRect(375, 55, 100, 25))
        
        self.Message_edit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Message_edit2.setGeometry(QtCore.QRect(125, 55, 100, 25))
        
        self.Message_edit3 = QtWidgets.QTextEdit(self.centralwidget)
        self.Message_edit3.setGeometry(QtCore.QRect(250, 55, 100, 25))

        self.unit_choice = QtWidgets.QComboBox(self.centralwidget)
        self.unit_choice.setGeometry(QtCore.QRect(50, 25, 50, 25))
        
        self.positioning_choice = QtWidgets.QComboBox(self.centralwidget)
        self.positioning_choice.setGeometry(QtCore.QRect(650, 265, 100, 25))

        self.function_choice = QtWidgets.QComboBox(self.centralwidget)
        self.function_choice.setGeometry(QtCore.QRect(125, 25, 100, 25))

        self.register_choice = QtWidgets.QComboBox(self.centralwidget)
        self.register_choice.setGeometry(QtCore.QRect(250, 25, 100, 25))

        self.message_choice = QtWidgets.QComboBox(self.centralwidget)
        self.message_choice.setGeometry(QtCore.QRect(375, 25, 100, 25))
        
        self.responded_messages = QWidget()
        self.vbox = QVBoxLayout()
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
        self.DigitalClock.setGeometry(QtCore.QRect(570, 553, 130, 21))
        self.retranslateUi(MainWindow) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #callback przycisku send obsugujacy wysylanie wiadomosci do serwomechanizmow
    def send_message(self):
		#wczytaj wartosci nazwy rejestru, funkcji, jednostki, oraz 
		#wysylanej wiadomosci podanych przez uzytkownika.
        function_choosed=self.function_choice.currentText()
        Admin_backend.message_sending.Register=self.register_choice.currentText()
        Admin_backend.message_sending.Unit=self.unit_choice.currentText()  
        Admin_backend.message_sending.message=self.Message_edit.toPlainText()
        #jesli wybrane jest czytanie z rejestru
        if(function_choosed=='read'):			
			#wywolaj funkcje czytajaca z rejestr
            result=Admin_backend.message_sending.read_register()
            #zapisz do tabeli odebrana wiadomosc 
            if (result==0):
                self.Responded_messages_list.append(Admin_backend.Register_respond[len(Admin_backend.Register_respond)-1])
                object = QLabel(self.Responded_messages_list[len(self.Responded_messages_list)-1])
                self.vbox.addWidget(object)	
                self.responded_messages.setLayout(self.vbox)			
                self.scrollArea.setWidget(self.responded_messages)
                #wyczysc zmienna z wczytaneym rejestrem
            else: 
                self.msgbox = QMessageBox()
                self.msgbox.setIcon(QMessageBox.Critical)
                self.msgbox.setText("check connection") 
                self.msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                self.msgbox.show()  
            Admin_backend.Register_respond=[]
        elif(function_choosed=='write'):
			#jesli wybrana funkcja jest pisanie do rejestru wywolaj 
			#metode piszaca do rejestru
            result=Admin_backend.message_sending.write_register()
            #korzystajac z flagi podniesionej przez wywolana funkcje 
            #wyswietl informacji o bledzie podczas wysylania wiadomosci 
            if(result!=0):
                self.msgbox = QMessageBox()
                self.msgbox.setIcon(QMessageBox.Critical)
                if(result==1):
                    self.msgbox.setText("wrong type of message")
                elif(result==2):
                    self.msgbox.setText("value of message out of limit")
                elif(result==3):
                    self.msgbox.setText("value of message out of limit")
                else:
                    self.msgbox.setText("Check connection")
                self.msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                self.msgbox.show()                
            #wyswietl wczytane informacje z nowo zapisanego rejsetru
            self.Responded_messages_list.append(Admin_backend.Register_respond[len(Admin_backend.Register_respond)-1])
            object = QLabel(self.Responded_messages_list[len(self.Responded_messages_list)-1])
            self.vbox.addWidget(object)	
            self.responded_messages.setLayout(self.vbox)			
            self.scrollArea.setWidget(self.responded_messages)
            #wyzeroj zmienne kontrolne
            Admin_backend.Register_respond=[]

        
    #funkcja pobiera aktualna date    
    def getDate(self):
        date = QDate.currentDate()
        return date.toString(Qt.DefaultLocaleLongDate)
    
    #callback wybrania wartosci okienka unit zapisuje wybrana zmienna do 
    #odpowiedniego zmiennej w klasie admin_backend
    def unit_selected(self, value):
        if(int(value)==1):
            Admin_backend.unit_choice=0
        else:
            Admin_backend.unit_choice=1
            print("to dziala")
            
    #callback wybrania wartosci okienka function zapisuje wybrana zmienna 
    #do odpowiedniego zmiennej w klasie admin_backend i wczytuje mozliwe
    #wartosci okienka nazw rejestrow
    def Function_selected(self, value):
        self.register_choice.clear()
        Admin_backend.function_value=value
        names_list=Admin_backend.comboboxes.registers_names()
        self.register_choice.addItems(names_list)
        Admin_backend.registers_names_list=[]
        self.Message_edit2.setText(value)
        
    #callback wybrania wartosci okienka nazwy rejsestru zapisuje wybrana 
    #zmienna do odpowiedniego zmiennej w klasie admin_backend i wczytuje
    #mozliwe wartosci okienka mozliwych wiadomosci
    def name_selected(self, value):
        self.message_choice.clear()
        Admin_backend.register_name_value=value
        messages_list=Admin_backend.comboboxes.messages_names()
        self.message_choice.addItems(messages_list)
        Admin_backend.message_names_list=[]
        if(Admin_backend.label_text!=[]):
            self.label_8.setText(Admin_backend.label_text[0])
            Admin_backend.label_text=[]
        self.Message_edit3.setText(value)  
          
    #callback wybrania wartosci okienka wiadomosci zapisuje wybrana 
    #zmienna do odpowiedniego zmiennej w klasie admin_backend i wyswietla
    #podpwiedz do danej wiadomosci
    def message_selected(self, value):
        Admin_backend.message_name_value = value
        print(Admin_backend.label_text)
        Admin_backend.comboboxes.message_description()
        if(Admin_backend.label_text!=[]):
            self.label_8.setText(Admin_backend.label_text[0])
            Admin_backend.label_text=[]
        value=self.message_choice.currentText()
        print(value)
        if value!='inc' and value!='RPM' and value!='AMP' and value!='number' and value!='rp/s^2':
            self.Message_edit.setText(value)	
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
        if(Admin_backend.move_deafult_flag[0]==0):
            try:
				#zapisz wczytane uzytkownika informacje o ruchu 
				#do odpowiednich zmienncyh klasy admin_backend
                Admin_backend.moving.acceleration_x=round(163.84*int(self.acceleration_box_x.toPlainText()))
                Admin_backend.moving.decceleration_x=round(163.84*int(self.decceleration_box_x.toPlainText()))
                Admin_backend.moving.velocity_x=round(2730*int(self.velocity_box_x.toPlainText()))
                Admin_backend.moving.acceleration_y=round(163.84*int(self.acceleration_box_y.toPlainText()))
                Admin_backend.moving.decceleration_y=round(163.84*int(self.decceleration_box_y.toPlainText()))
                Admin_backend.moving.velocity_y=round(2730*int(self.velocity_box_x.toPlainText()))
                Admin_backend.moving.zero=self.positioning_choice.currentText()
            except Exception:
                traceback.print_exc()
                result=6
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

    #Callback checkboxu wylacza mozliwosc dodawania swoich wartosci do 
    #ruchu oprocz wspolrzednych    
    def deafult_checkbox_clicked(self , state):
        Admin_backend.move_deafult_flag=[]	
        if str(state) == "True": 		
            self.acceleration_box_x.setDisabled(True)          
            self.decceleration_box_x.setDisabled(True)  
            self.velocity_box_x.setDisabled(True)       	
            self.acceleration_box_y.setDisabled(True)  
            self.decceleration_box_y.setDisabled(True)          
            self.velocity_box_y.setDisabled(True)       
            Admin_backend.move_deafult_flag.append(1)
        else: 		
            self.acceleration_box_x.setDisabled(False)          
            self.decceleration_box_x.setDisabled(False)  
            self.velocity_box_x.setDisabled(False)       	
            self.acceleration_box_y.setDisabled(False)  
            self.decceleration_box_y.setDisabled(False)          
            self.velocity_box_y.setDisabled(False)  
            Admin_backend.move_deafult_flag.append(0)  

        
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
        self.pushButton_5.setText(_translate("MainWindow", "Send"))
        self.pushButton_5.clicked.connect(self.send_message)
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
        self.positioning_choice.addItems(Admin_backend.Positioning_values)
        self.deafult_checkbox.clicked.connect(self.deafult_checkbox_clicked)
        self.unit_choice.addItems(Constants.units)
        self.unit_choice.currentTextChanged.connect(self.unit_selected)
        self.function_choice.currentTextChanged.connect(self.Function_selected)
        self.function_choice.addItems(Constants.function_select)
        self.register_choice.currentTextChanged.connect(self.name_selected)
        self.message_choice.currentTextChanged.connect(self.message_selected)
        self.label.setText(_translate("MainWindow", "Unit:"))
        self.label_2.setText(_translate("MainWindow", "Function:"))
        self.label_3.setText(_translate("MainWindow", self.getDate() ))
        self.label_4.setText(_translate("MainWindow", "X Coordinate:"))
        self.label_5.setText(_translate("MainWindow", "Y Coordinate:"))
        self.label_6.setText(_translate("MainWindow", "Message:"))
        self.label_7.setText(_translate("MainWindow", "Register Name:"))
        self.label_9.setText(_translate("MainWindow", " "))
        self.label_11.setText(_translate("MainWindow", "Position(inc):"))
        self.label_12.setText(_translate("MainWindow", "Acceleration(rp/s^2):"))
        self.label_13.setText(_translate("MainWindow", "Deceleration(rp/s^2):"))
        self.label_14.setText(_translate("MainWindow", "Velocity(rpm):"))
        self.label_15.setText(_translate("MainWindow", "Zero:"))
        self.label_16.setText(_translate("MainWindow", "Deafult:"))
        self.DigitalClock.setStyleSheet('background-color: black',)
        self.Register_window()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

