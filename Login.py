
import sys
import sqlite3
from Admin_ui import *
from Guest_ui import *
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMessageBox,QLabel, QGridLayout ,QComboBox,\
    QMainWindow
#klasa wyswietlajaca startowe okno loginu
class window(QWidget):

    def __init__(self, parent=None):
        super(window,self).__init__(parent)
        self.interfejs()
    #funkcja otwierajaca okno admina 
    def new_window(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
   #funkcja otwierajaca okno goscia       
    def new_window2(self):
        self.window = QMainWindow()
        self.ui = Ui_GuestWindow()
        self.ui.setup_guest_Ui(self.window)
        self.window.show()
        
    #funkcja odpowiadajca za sprawdzenie loginu w bazie danych
    def login(self):
        nadawca = self.sender()
        try:
			#wczytaj wartosci podane przez uzytkownika w gui
            templist1=[]
            text1 = self.user.text()
            text2 = self.password.text()
            text3 = self.cb.currentText()
            #Jesli uzytkonik loguje sie jako gosc przejdz do okna goscia
            if text3=="Guest":
                self.close()
                self.new_window2()
            #jesli uzytkownik loguje sie jako admin sprawdx haslo
            else:
				#tworzenie okna informujacego czy haslo jest poprawne
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                #wczytywanie informacji z lokalnej bazy danych
                users_database = sqlite3.connect('users.db')
                users_database.row_factory = sqlite3.Row
                user_cursor = users_database.cursor()
                user_cursor.execute(""" SELECT * FROM users """)
                #uzyskanie kursora na informacje z bazy danych
                fun=user_cursor.fetchall()
                #petla sprawdzajaca poprawnosc hasla
                for f in fun:
                    usercheck=f['user']
                    passwordcheck=f['password']
                    #sprawdz czy w bazie jest dany uzytkownik
                    if usercheck==text1:
						#sprawdz haslo jest poprawne dla danego 
						#uzytkownika
                        if passwordcheck==text2:
							#jesli wybrane zostalo logowanie jako admin
							#i dane sa poprawne przejdz do okna admina
                            if text3 == "Admin":
                                self.close()
                                self.new_window()
                            # jesli dane wejsciowe sa niepoprawne 
                            #wyswietl na odpowiednim oknie    
                            else:
                                msg.setText("logujesz sie jako admin?")
                                msg.exec_()
                        else:
                            msg.setText("haslo niepoprawne")
                            msg.exec_()
                    else:
                        msg.setText("nie ma takiego uzytkownika")
                        msg.exec_()
        except ValueError:
            print(ValueError)
    # Działanie przycisków Esc i Enter       
    def keyPressEvent(self, event): 
        if event.key() == QtCore.Qt.Key_Escape:
            sys.exit()
        elif event.key() == QtCore.Qt.Key_Return:
            self.login()
    #tworzenie okna uzytkownika
    def interfejs(self):
        op1=QLabel("Użytkownik:")
        op2=QLabel("Hasło:")
        ukladT = QGridLayout()
        self.user = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password) # hasło nie jest widoczne przy wpisywaniu
        self.cb = QComboBox()
        self.cb.addItem("Admin")
        self.cb.addItem("Guest")
        ukladT.addWidget(op1, 1, 0)
        ukladT.addWidget(op2, 3, 0)
        ukladT.addWidget(self.user, 2, 0)
        ukladT.addWidget(self.password, 4, 0)
        ukladT.addWidget(self.cb, 0, 0)
        zaloguj = QPushButton("Zaloguj", self)
        anuluj = QPushButton("Anuluj", self)
        ukladT.addWidget(zaloguj,5,0)
        ukladT.addWidget(anuluj, 5, 1)
        self.setLayout(ukladT)
        self.resize(400, 200)
        self.setWindowTitle("Okno logowania")
        self.show()
        zaloguj.clicked.connect(self.login)
        anuluj.clicked.connect(sys.exit)

#konstruktor klasy uruchamiajacy okno
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    okno = window()
    sys.exit(app.exec_())
