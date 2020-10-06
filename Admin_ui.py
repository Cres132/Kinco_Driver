from digitalclock import DigitalClock
from PyQt5.QtWidgets import QComboBox,QStyleFactory,QMainWindow,QMessageBox ,QWidget,QVBoxLayout,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtGui import QFont
import Constants
import Admin_backend
import Home_window
import Register_window
class Ui_MainWindow(object):
    names_list=[]
    Readed_registers=[]
    Responded_messages_list=[]
    def quit(self):
        sys.exit(app.exec())

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
        self.pushButton_6.setGeometry(QtCore.QRect(500, 260, 50, 25))
        self.pushButton_6.setObjectName("pushButton_5")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 450, 100, 60))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(360, 290, 50, 25))
        self.pushButton_8.setObjectName("pushButton_7")
        
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 5, 120, 25))
        self.pushButton_9.setObjectName("pushButton_7")
        

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


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 5, 331, 25))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(125, 5, 361,25))
        self.label_2.setObjectName("label_2")
        # Date
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 530, 211, 25))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 260, 100, 25))
        self.label_4.setObjectName("label_3")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 260, 100, 25))
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

        self.label_10 = QtWidgets.QLabel(self.scrollArea2)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 500, 25))
        self.label_10.setObjectName("label_3")

        self.coordination_box_y = QtWidgets.QTextEdit(self.centralwidget)
        self.coordination_box_y.setGeometry(QtCore.QRect(250, 290, 100, 25))
               
        self.coordination_box_x = QtWidgets.QTextEdit(self.centralwidget)
        self.coordination_box_x.setGeometry(QtCore.QRect(100, 290, 100, 25))

        self.Message_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.Message_edit.setGeometry(QtCore.QRect(375, 55, 100, 25))
        
        self.Message_edit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Message_edit2.setGeometry(QtCore.QRect(125, 55, 100, 25))
        
        self.Message_edit3 = QtWidgets.QTextEdit(self.centralwidget)
        self.Message_edit3.setGeometry(QtCore.QRect(250, 55, 100, 25))

        self.unit_choice = QtWidgets.QComboBox(self.centralwidget)
        self.unit_choice.setGeometry(QtCore.QRect(50, 25, 50, 25))

        self.function_choice = QtWidgets.QComboBox(self.centralwidget)
        self.function_choice.setGeometry(QtCore.QRect(125, 25, 100, 25))

        self.register_choice = QtWidgets.QComboBox(self.centralwidget)
        self.register_choice.setGeometry(QtCore.QRect(250, 25, 100, 25))

        self.message_choice = QtWidgets.QComboBox(self.centralwidget)
        self.message_choice.setGeometry(QtCore.QRect(375, 25, 100, 25))
        
        self.responded_messages = QWidget()
        self.vbox = QVBoxLayout()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.DigitalClock = DigitalClock(self.centralwidget)
        self.DigitalClock.setGeometry(QtCore.QRect(570, 553, 130, 21))
        self.retranslateUi(MainWindow) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def send_message(self):
        function_choosed=self.function_choice.currentText()
        Admin_backend.message_sending.Register=self.register_choice.currentText()
        Admin_backend.message_sending.Unit=self.unit_choice.currentText()  
        Admin_backend.message_sending.message=self.Message_edit.toPlainText()
        print(function_choosed)
        if(function_choosed=='read'):			
            Admin_backend.message_sending.read_register()
            self.Responded_messages_list.append(Admin_backend.Register_respond[len(Admin_backend.Register_respond)-1])
            object = QLabel(self.Responded_messages_list[len(self.Responded_messages_list)-1])
            self.vbox.addWidget(object)	
            self.responded_messages.setLayout(self.vbox)			
            self.scrollArea.setWidget(self.responded_messages)
            Admin_backend.Register_respond=[]
        elif(function_choosed=='write'):
            Admin_backend.message_sending.write_register()
            print(Admin_backend.error_flag)
            
            if(Admin_backend.error_flag[0]!=0):
                self.msgbox = QMessageBox()
                self.msgbox.setIcon(QMessageBox.Critical)
                if(Admin_backend.error_flag[0]==1):
                    self.msgbox.setText("wrong type of message")
                if(Admin_backend.error_flag[0]==2):
                    self.msgbox.setText("value of message out of limit")
                if(Admin_backend.error_flag[0]==3):
                    self.msgbox.setText("value of message out of limit")
                self.msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                self.msgbox.show()
            self.Responded_messages_list.append(Admin_backend.Register_respond[len(Admin_backend.Register_respond)-1])
            object = QLabel(self.Responded_messages_list[len(self.Responded_messages_list)-1])
            self.vbox.addWidget(object)	
            self.responded_messages.setLayout(self.vbox)			
            self.scrollArea.setWidget(self.responded_messages)
            Admin_backend.Register_respond=[]
            Admin_backend.error_flag=[]
        
        
        
    def getDate(self):
        date = QDate.currentDate()
        return date.toString(Qt.DefaultLocaleLongDate)
    
    def unit_selected(self, value):
        if(int(value)==1):
            Admin_backend.unit_choice=0
        else:
            Admin_backend.unit_choice=1
            print("to dziala")

    def Function_selected(self, value):
        self.register_choice.clear()
        Admin_backend.function_value=value
        names_list=Admin_backend.comboboxes.registers_names()
        self.register_choice.addItems(names_list)
        Admin_backend.registers_names_list=[]
        self.Message_edit2.setText(value)
   
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
 
    def Home_window(self):
        self.window = QMainWindow()
        self.Home_ui = Home_window.Ui_Home_Window()
        self.Home_ui.setupUi(self.window)
        self.window.show()

    def Register_window(self):
        self.window = QMainWindow()
        self.Register_ui = Register_window.Ui_Register_Window()
        self.Register_ui.setupUi(self.window)
        self.window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kinco Driver"))
        self.pushButton.setText(_translate("MainWindow", "Home"))
        self.pushButton.clicked.connect(self.Home_window)
        self.pushButton_2.setText(_translate("MainWindow", "Save point"))
        self.pushButton_3.setText(_translate("MainWindow", "previous"))
        self.pushButton_4.setText(_translate("MainWindow", "next"))
        self.pushButton_5.setText(_translate("MainWindow", "Send"))
        self.pushButton_5.clicked.connect(self.send_message)
        self.pushButton_6.setText(_translate("MainWindow", "test"))

        self.pushButton_7.setText(_translate("MainWindow", "Save session"))
        self.pushButton_8.setText(_translate("MainWindow", "move"))
        self.pushButton_9.setText(_translate("MainWindow", "Registers_status"))
        self.pushButton_9.clicked.connect(self.Register_window)
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
        self.label_10.setText(_translate("MainWindow", "Register Name:"))
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

