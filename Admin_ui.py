from digitalclock import DigitalClock
from PyQt5.QtWidgets import QComboBox,QStyleFactory,QMainWindow,QMessageBox ,QWidget,QVBoxLayout,QLabel,QCheckBox,QTableWidget,QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer,QObject, QThread, pyqtSignal
from PyQt5.QtGui import QFont
from time import sleep 
import Constants
import Admin_backend
import Home_window
import Register_window
import traceback
import Namesession
import Session_records
import Current_position
import Check_move_Window
import serwervxi
import socket

Table=[]
Point_table=0
check_window=0	
table_end=0
#klasa odpowiedzialna za tworzenia okna admina 
class Ui_MainWindow(object):
	#tworzenie zmienncyh tymczasowych
    current_unit=0
    names_list=[]
    Readed_registers=[]
    Responded_messages_list=[]
    #zakoncz dzialanie programu po zamknieciu okna
    
    def quit(self):
        sys.exit(app.exec())
    #tworzenie obiektow okna admina
   
    def setupUi(self, MainWindow):
        serwervxi.Listen_connection.listen()
        MainWindow.setObjectName("Kinco_Driver")
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(MainWindow.size())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 475, 100, 60))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 475, 100, 60))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 475, 100, 60))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 475, 100, 60))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 55, 50, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(725, 300, 50, 25))
        self.pushButton_6.setObjectName("pushButton_5")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 475, 100, 60))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(650, 300, 50, 25))
        self.pushButton_8.setObjectName("pushButton_7")
        
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 5, 120, 25))
        self.pushButton_9.setObjectName("pushButton_7")        
        
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(630, 440, 130, 25))
        self.pushButton_10.setObjectName("pushButton_7")   
        
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(630, 40, 130, 25))
        self.pushButton_11.setObjectName("pushButton_7")  

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(630, 70, 130, 25))
        self.pushButton_12.setObjectName("pushButton_7") 
        
        
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(630, 100, 130, 25))
        self.pushButton_13.setObjectName("pushButton_7") 
        
        
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(630, 5, 130, 25))
        self.pushButton_14.setObjectName("pushButton_7") 
        
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

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(50, 530, 300, 60))
        
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
        self.table = QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 330, 760, 100))
        self.table.setColumnCount(3)
        self.table.setRowCount(1000)
        self.table.setColumnWidth(0,235)
        self.table.setColumnWidth(1,235)
        self.table.setColumnWidth(2,235)
        self.table.setHorizontalHeaderLabels(['Position X','Position Y','name'])
        self.table.resizeRowsToContents() 
        self.table.setMinimumWidth(720)
        self.table.setMinimumHeight(100)
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
        Admin_backend.stop_thread=0
        self.check_window()
        self.testTask()      

    def check_window(self):
        global check_window	  	
        check_window=Check_move_Window.Ui_Check_move_Window()
        print(check_window)
        self.ui = check_window
        check_window.setupUi(self.ui)
        check_window.show()
        	
    def moveTask(self):        
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.moving = Admin_backend.moving()
        # Step 4: Move worker to the thread
        self.moving.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.moving.do_move)
        self.moving.finished.connect(self.thread.quit)
        self.moving.finished.connect(self.moving.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.moving.progress2.connect(self.update_move_window)
        self.moving.progress.connect(self.show_messagebox)
        self.moving.progress3.connect(self.update_unit)
        self.moving.stop_current_thread.connect(self.thread.quit)

        # Step 6: Start the thread
        self.thread.start()	
        self.pushButton_5.setEnabled(False)
        self.thread.finished.connect( lambda: self.pushButton_5.setEnabled(True))
        self.pushButton_6.setEnabled(False)
        self.thread.finished.connect( lambda: self.pushButton_6.setEnabled(True))
        self.pushButton_8.setEnabled(False)
        self.thread.finished.connect(lambda: self.pushButton_8.setEnabled(True) )     
        
        	 
        #funkcja odpowiedzialna za porusznie sie serwomechanizmow   		

    def update_unit(self,unit):
        self.current_unit=unit
            
    def testTask(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.moving = Admin_backend.moving()
        # Step 4: Move worker to the thread
        self.moving.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.moving.do_test)
        self.moving.finished.connect(self.thread.quit)
        self.moving.finished.connect(self.moving.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.moving.progress2.connect(self.update_move_window)
        self.moving.progress3.connect(self.update_unit)        
        self.moving.progress.connect(self.show_messagebox2)
        self.moving.stop_current_thread.connect(self.thread.quit)
        
        # Step 6: Start the thread
        self.thread.start()	
        self.pushButton_5.setEnabled(False)
        self.thread.finished.connect(lambda: self.pushButton_5.setEnabled(True))
        self.pushButton_6.setEnabled(False)
        self.thread.finished.connect(lambda: self.pushButton_6.setEnabled(True))
        self.pushButton_8.setEnabled(False)
        self.thread.finished.connect(lambda: self.pushButton_8.setEnabled(True))          
        	 
        #funkcja odpowiedzialna za porusznie sie serwomechanizmow 
    def apimoveTask(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.moving = Admin_backend.moving()
        # Step 4: Move worker to the thread
        self.moving.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.moving.do_test)
        self.moving.finished.connect(self.thread.quit)
        self.moving.finished.connect(self.moving.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)        
        # Step 6: Start the thread
        self.thread.start()	
          
    def update_move_window(self,point):
        global check_window	
        curr_text=""
        if self.current_unit==1:
            curr_text="x"
        else:
            curr_text="y"    
        uplabel=("current position of axis "+curr_text+" : "+str(point))
        Check_move_Window.Ui_Check_move_Window.update_label(check_window,uplabel)
           
    def show_messagebox(self,result):
        self.msgbox = QMessageBox()
        self.msgbox.setIcon(QMessageBox.Critical)
        global check_window
        check_window.close()
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
    
    def show_messagebox2(self,result):
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
            
    def api_move(self,x,y,x_vel,y_vel,X_acc,y_acc,x_dec,y_dec,positioning,deafult):
        result=0
        try:
			#pobierz wartosci o ruchu podane przez uzytkownika i zapisz
			#w odpowienich zmiennych klasy asmin_backend
            Admin_backend.moving.position_x=x
            Admin_backend.moving.position_y=y 
            Admin_backend.moving.zero=positioning                  
        except Exception:
            traceback.print_exc()
            result=6
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Critical)                 
            self.msgbox.setText("Invalid input data")
            self.msgbox.show() 
            #jesli aktualnie program nie namesession_ui wykonuje ruchu
        if(deafult==0):
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
                self.msgbox = QMessageBox()
                self.msgbox.setIcon(QMessageBox.Critical)                 
                self.msgbox.setText("Invalid input data")
                self.msgbox.show() 
        else:
            Admin_backend.move_deafult_flag[0]=1         
        #wyswietl informacje o statusie ruchu 
        if(result!=6):
            Admin_backend.stop_thread=0 
            self.check_window()             
            self.apimoveTask()          
            
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
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Critical)                 
            self.msgbox.setText("resultInvalid input data")
            self.msgbox.show() 
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
                self.msgbox = QMessageBox()
                self.msgbox.setIcon(QMessageBox.Critical)                 
                self.msgbox.setText("Invalid input data")
                self.msgbox.show() 
         
        #wyswietl informacje o statusie ruchu 
        if(result!=6):
            Admin_backend.stop_thread=0 
            self.check_window()             
            self.moveTask()           
       

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
        global table_end
        global Table
        Admin_backend.button_callbacks.savepoint_button_callback()
        item1=QTableWidgetItem(str(Admin_backend.Position_save_info[0]))
        item2=QTableWidgetItem(str(Admin_backend.Position_save_info[1]))
        item3=QTableWidgetItem("Default name "+str(table_end))
        self.table.setItem(table_end,0,item1)
        self.table.setItem(table_end,1,item2)
        self.table.setItem(table_end,2,item3)
        self.table.selectRow(table_end)
        table_end=table_end+1        
   
    def previous_callback(self):
        saved_coor=Admin_backend.button_callbacks.previous_buttton_callback()
        self.coordination_box_x.setText(str(saved_coor[0]))
        self.coordination_box_y.setText(str(saved_coor[1]))
        if(Admin_backend.current_point>-1):
            self.table.selectRow(Admin_backend.current_point)	
            
    def next_callback(self):
        saved_coor=Admin_backend.button_callbacks.next_buttton_callback()
        self.coordination_box_x.setText(str(saved_coor[0]))
        self.coordination_box_y.setText(str(saved_coor[1]))
        if(Admin_backend.current_point<1000):
            self.table.selectRow(Admin_backend.current_point)	
	
    def savesession_callback(self):
        global Table
        global table_end
        Table=[[0 for x in range(self.table.columnCount())]for y in range(table_end)]
        for i in range(self.table.columnCount()):			
            for k in range(table_end):
                print([k,i])
                print(self.table.item(k,i).text())
                Table[k][i]=self.table.item(k,i).text()
        Admin_backend.Points=Table
        self.namesession_ui = Namesession.Ui_NameSession_Window()
        self.namesession_ui.setupUi(self.namesession_ui)
        self.namesession_ui.show()     		
        
        
    def readsession_callback(self):				
        self.thread = QThread()
        self.readsession_ui = Session_records.Ui_Session_records_Window()
        self.readsession_ui.moveToThread(self.thread)
        self.readsession_ui.setupUi(self.readsession_ui)
        self.thread.started.connect(self.readsession_ui.show)
        self.readsession_ui.finished.connect(self.update_table )
        self.readsession_ui.finished.connect(self.thread.quit)
        self.readsession_ui.finished.connect(self.readsession_ui.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()      	


        
    def update_table(self):
        try:
            global table_end    
            Points=Admin_backend.New_points
            counter=0
            print(Points)
            self.table.clear()
            Admin_backend.Saved_points=[]          
            for point in Points:
                Admin_backend.Saved_points.append([str(point[1]),str(point[2])]) 
                Admin_backend.current_point=(len(Admin_backend.Saved_points))-1
                item1=QTableWidgetItem(str(point[1]))
                item2=QTableWidgetItem(str(point[2]))
                item3=QTableWidgetItem(str(point[3]))
                self.table.setItem(counter,0,item1)
                self.table.setItem(counter,1,item2)
                self.table.setItem(counter,2,item3)
                counter=counter+1
            table_end=counter
            Admin_backend.current_point=0
        except Exception:
            traceback.print_exc()        	
    
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

    def motors_off_callback(self):  
        Admin_backend.button_callbacks.motors_off() 
        
    def Zero_current_callback(self):  
        Admin_backend.button_callbacks.Zero_current()	

    #funkcja uruchamiana przy starcie okna przypsiujaca wartosci oknu 
    #gui oraz deklarujaca callbacki
    def retranslateUi(self, MainWindow):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8",80))
            ip_adress=s.getsockname()[0]
        except Exception:    
            ip_adress="Check connection to switch"
            
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
        self.pushButton_12.setText(_translate("MainWindow", "Session Movement"))
        self.pushButton_12.clicked.connect(self.session_movement_callback)
        self.pushButton_13.setText(_translate("MainWindow", "motors off"))
        self.pushButton_13.clicked.connect(self.motors_off_callback)
        self.pushButton_14.setText(_translate("MainWindow", "Zero current point"))
        self.pushButton_14.clicked.connect(self.Zero_current_callback)
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
        self.label_4.setText(_translate("MainWindow", "Y Coordinate:"))
        self.label_5.setText(_translate("MainWindow", "X Coordinate:"))
        self.label_6.setText(_translate("MainWindow", "Message:"))
        self.label_7.setText(_translate("MainWindow", "Register Name:"))
        self.label_9.setText(_translate("MainWindow", " "))
        self.label_11.setText(_translate("MainWindow", "Position(inc):"))
        self.label_12.setText(_translate("MainWindow", "Acceleration(rp/s^2):"))
        self.label_13.setText(_translate("MainWindow", "Deceleration(rp/s^2):"))
        self.label_14.setText(_translate("MainWindow", "Velocity(rpm):"))
        self.label_15.setText(_translate("MainWindow", "Zero:"))
        self.label_16.setText(_translate("MainWindow", "Deafult:"))
        self.label_17.setText(_translate("MainWindow", "Current IP: %s"%(ip_adress)))
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

   
