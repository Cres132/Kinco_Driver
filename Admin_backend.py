import sys
import sqlite3
import datetime
import time
import serial
import traceback
import Interpretation
import Constants
import Current_position
import threading
import Check_move_Window
from PyQt5.QtCore import QDate, QTime,QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QComboBox,QStyleFactory,QMainWindow,QMessageBox ,QWidget,QVBoxLayout,QLabel,QCheckBox
from pymodbus.client.sync import ModbusSerialClient as modbusclient
from pymodbus.constants import Defaults
from timeit import default_timer as timer
import Admin_ui
import serwervxi

#zmienne uzywane do sprawdzania poprawnosci wysylanych widomosci
function_value = ''
register_name_value = ''
registers_names_list= []
message_name_value=''
message_names_list= []
#zmienna wykorzystywana do uzyskiwania textu podpowiedzi
label_text=[]
#zmienna przechowujaca odpowiedzi rejstrow
Register_respond=[]
#zmienna kontrolna do przechowujaca rejsestry
Register_respond_check=[]
#flaga bledu do okreslajaca wiadomosci wyswietlane wgui
#zmienna wykorzystywana w kontroli ruchu do okreslenia wartosci na ktorej
#skonczony byl poprzedni rcuh
ending_position=[0,0]
#zmienne okreslojace wybrana jednsotke
Unit=[0x001,0x002]
unit_choice=1
#zmienne informujaca czy obecnie jest wykonywany ruch
move_deafult_flag=[0]
#stala zawierajaca informacje o mozliwych wlasciwosciach ruchu
Positioning_values=["Absolute","Relative"]
#zmienna informujaca o tym czy mozna wykonac ruch
move_allowance=[0]
#zmienna mowiaca o wartosci poczatkowej ruchu
start_position=0
start=0
#tablica zapisujaca wspolrzedne do zapisania polozenia
Position_save_info=[]
Saved_points=[]
current_point=0
window1=0
currentPosition_ui=0
stop_thread=0
New_points=0
Points=[]
#klasa odpopwiadajaca za komunikacje sie z serwomechanizmami
class message_sending(Interpretation.interpretation):
    #okresla wartosc komunikacji po moodbusie dla funkcji
    Defaults.RetryOnEmpty = True
    Defaults.Timeout = 2
    Defaults.Retries = 2
    #tworznie zmienncy tymczasowych stosowanych do czytania z rejstrow
    Register=  ''
    count_r = 1
    message = ''

    
	
   #funkcja wczytujaca wartosci wszytskich resjestrow z bazy dancyh 
    def check_connection():
		#wczytaj wartosci z baz danych 
        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT class,name,adress,description,count  FROM Adress """)
        fun = Adress_cursor.fetchall()
        #stworz zmienne tymczasowe z informacja o klasie i adresie rejsestru
        Register_adress = ''
        Register_class = ''
        #wyzeruj wczesniej wczytane wartosci rejsestrow w klasie Interpretation
        Interpretation.Status_registers=[]
        Interpretation.Status_registers_status=[]
        #zdefiniuj wartosci polaczenia po modbasie i polacz sie z serwomechnizmem         
        client = modbusclient(method='rtu', port="/dev/ttyUSB0", timeout=1,stopbits=1, bytesize=8, parity='N', baudrate=19200)
        connectResult = client.connect()
        #wczytaj wartosc rejestru dla kazdego rejsestru znadjujacego sie w bazie danych
        for adr in fun:
            if (adr['class']=='RO' or adr['class']=='RW'):
                count_r=adr['count'] 
                print(adr['name'])           
                Register_adress=adr['adress']
                adresstemp=int(Register_adress, 16)
                try:
					#wczytaj zadany rejestr
                    hh = client.read_holding_registers(address=adresstemp, count=int(count_r), unit=Unit[0])
                    #jesli odpowie kodem bledu rzuc wyjatek
                    assert (hh.function_code < 0x80)                
                    print(hh.registers)
                    Interpretation.Status_registers.append([adr['name']])
                    Interpretation.Status_registers_status.append([hh.registers])              
                except Exception:
                    traceback.print_exc()
                    client.close()
                    return 1
                    print("error reading registers from servo")
        #wywolaj funkcje sprawdzajaca i przeksztalcajaca odczytane dane            
        Interpretation.interpretation.interpretcheck()
        #utworz z odczytanych rejstrow informacje o ich stanie
        iter2=0
        while(iter2<len(Interpretation.Status_registers)):
            Register_respond_check.append(str(Interpretation.Status_registers[iter2][0]+':'+Interpretation.Status_registers_message[iter2]))
            iter2=iter2+1
        #wyzeruj zmienne przechowujaca informacje o rejestrach
        print(Register_respond_check)
        Interpretation.Status_registers=[]
        Interpretation.Status_registers_status=[]
        #polacz sie z drugim serwomechanizmem
        client = modbusclient(method='rtu', port="/dev/ttyUSB0", timeout=1,stopbits=1, bytesize=8, parity='N', baudrate=19200)
        print(str(client))
        connectResult = client.connect()
        print(connectResult)
        #powtorz algorytm z kontatku z poprzednim serwomechanizmem
        for adr in fun:
            if (adr['class']=='RO' or adr['class']=='RW'):
                count_r=adr['count'] 
                print(adr['name'])	           
                Register_adress=adr['adress']
                adresstemp=int(Register_adress, 16)
                try:
                    hh = client.read_holding_registers(address=adresstemp, count=int(count_r), unit=Unit[1])
                    print(hh)
                    assert (hh.function_code < 0x80)                
                    print(hh.registers)
                    Interpretation.Status_registers.append([adr['name']])
                    Interpretation.Status_registers_status.append([hh.registers])              
                except Exception:
                    traceback.print_exc()
                    client.close()
                    return 1                           
        Interpretation.interpretation.interpretcheck()
        iter2=0
        while(iter2<len(Interpretation.Status_registers)):
            Register_respond_check[iter2]=Register_respond_check[iter2]+"   "+Interpretation.Status_registers_message[iter2]
            iter2=iter2+1    
        print(Register_respond_check)
        return 0
    
    #funkcja czytajaca podany przez uzytkownika rejestr            
    def read_register():
		#wyzeruj tablice tlumaczace dane na zrozumiale dla uzytkownika
        Interpretation.Status_registers=[]
        Interpretation.Status_registers_status=[]
        #wczytaj lokalna baze rejestrow
        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT class,name,adress,description,count FROM Adress """)
        fun = Adress_cursor.fetchall()
        Register_adress = ''
        Register_class = ''
        Register_name_temp=' '
        #jesli uzyskano pozwolenie na wczytywanie danych (do uzupelnienia
        #warunek wywolujacy w funkcje interpretread nie zostal okreslony)
        if(Interpretation.message_read_allowance==0):
			#wczytaj rejestry z bazy danych
            for adr in fun:
                if (message_sending.Register == adr['name']):
                    Register_adress=adr['adress']
                    Register_class=adr['class']
                    Register_name_temp=adr['name']
                    #print(Register_adress,Register_class)
                    count_r=adr['count']
            #rozpocznij transmisje przez modbus
            client=modbusclient(method='RTU',port='/dev/ttyUSB0',timeout=1,stopbits=1,bytesize=8,parity='N',baudrate=19200)
            connectResult=client.connect()
            try:
				#wczytaj zdefiniowane przez uzytkownika rejestry
                hh = client.read_holding_registers(address=int(Register_adress,16),count=int(count_r), unit=Unit[unit_choice])
                assert (hh.function_code < 0x80)                
                Interpretation.Status_registers_message=['']
                Interpretation.Status_registers.append([Register_name_temp])
                Interpretation.Status_registers_status.append([hh.registers])         
            except Exception:
                traceback.print_exc()
                serwervxi.connection_error=1
                Register_respond.append("connection error")
                client.close()
                return 1
            #przytlumacz wczytany rejestr
            Interpretation.interpretation.interpretcheck()
            Register_respond.append(str("Unit "+str(int(Unit[unit_choice]))+"  "+Register_name_temp +':'+Interpretation.Status_registers_message[0]))
        #zakoncz komunikacje prze modbus
        client.close()
        return 0

        
    #funkcja zajmujaca sie pisaniem do wyznaczonego przez uzytkownika 
    #rejestru    
    def write_register():
		#wczytaj rejestry z bazy danych
        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT class,name,adress,description,count  FROM Adress """)
        fun = Adress_cursor.fetchall()

        Register_adress = ''
        Register_class = ''
        Register_name_temp=' '
        #sprawdz czy podany rejestr znajduje sie w bazie danych
        for adr in fun:
            if (message_sending.Register == adr['name']):
                Register_adress=adr['adress']
                Register_class=adr['class']
                count_r=adr['count']
                Register_name_temp=adr['name']
              #  print(Register_adress,Register_class)
        #Wczytaj dane podane przez uzytkownika
        message_temp=message_sending.message   
                #wczytaj flage bledu 
 
        #print(Register_name_temp,message_temp)    
        send_allowance=Interpretation.interpretation.interpretsend(Register_name_temp,message_temp)
       # print(Interpretation.interpretation.interpretsend(Register_name_temp,message_temp))
        #wyczysc tablice tlumaczace wczytane rejestry
        Interpretation.Status_registers=[]
        Interpretation.Status_registers_status=[]
        #sprawdz czy wystapil wczesniej blad wczytywania jesli nie 
        # rozpocznij zapis do rejestru
        if(send_allowance == 0):
            client = modbusclient(method='RTU', port='/dev/ttyUSB0', timeout=1, stopbits=1, bytesize=8, parity='N',baudrate=19200)
            connectResult=client.connect()
            temp_register_adress=int(Register_adress,16)
            #mozliwosc podawania wartosci w postacji int i hex
            try:
                message_temp=int(message_temp)
                if message_temp<0:
                    message_temp=message_temp+2**32

            except:
                message_temp=int(message_temp,16)
            try:
				#wyzeruj zmienna z odczytana informacja
                rq=0
                #utworz tablice przechowujaca wiadomosc
                message_mutli_temp=[]
                #jesli dlugosc wiadomosci pisana jest do rejestru o dlugosc
                # rownej 1 komorce pamieci rejestru wyslij wiadomosc
                if(int(count_r)==1):			
                    rq = client.write_register(address=temp_register_adress,value=int(message_temp) , unit=Unit[unit_choice])
                #jesli dlugosc wiadomosci pisana jest do rejestru o dlugosc
                #rownej 2 komorkom pamieci rejestru dostosuj wartosci wysylane
                #do rejetru i wyslij wiadomosc		
                else:
					#jesli wartosc wiadomosci nie przekracza wartosci 
					#maksymalnej komorki pamieci						
                    if(int(message_temp)<65536):
						#wpisz do pierwszej komorki pamieci wartosc wcz
						#ytana od uzytkownika a do drugiej 0 i wyslij 
						#na adres rejestru
                        message_multi_temp=[int(message_temp),0]
                       
                        rq = client.write_registers(address=temp_register_adress,values=message_multi_temp , unit=Unit[unit_choice])
                    else:
						#jesli wartosc wiadomosci przekracza wartosc jednego rejestru
						#wylicz jaka czesc wiadomosci znajdzie sie w drugiej
						#komorce pamieci i wysllij wiadomosc
                        message_multi_temp=[int(int(message_temp)%65536),int(int(message_temp)//65536)]
                        rq = client.write_registers(address=temp_register_adress,values=message_multi_temp , unit=Unit[unit_choice])						

                assert (rq.function_code < 0x80)                
            except Exception:
                serwervxi.connection_error=1                
                traceback.print_exc()
                return 4
                
            #jesli mozna odczytac wartosc z rejsetru odczytaj nowo wpisana wartosc
            if(Register_class=='RW'):
                try:
                    hh = client.read_holding_registers(address=temp_register_adress,count=int(count_r), unit=Unit[unit_choice])
                    assert (hh.function_code < 0x80)
                    Interpretation.Status_registers_message=['']
                    Interpretation.Status_registers.append([Register_name_temp])
                    Interpretation.Status_registers_status.append([hh.registers])
                except Exception:
                    serwervxi.connection_error=1                
                    traceback.print_exc()
                    return 4
            client.close()
        else:
             return send_allowance
		#prztlumacz odczytana wiadomosc	
        Interpretation.interpretation.interpretcheck()
        Register_respond.append(str("Unit "+str(int(Unit[unit_choice]))+"  "+Register_name_temp +':'+Interpretation.Status_registers_message[0]))
        return 0

#klasa zajmujaca sie obsluga okien wczytywywania danych od uzytkownika
class comboboxes:
	#funkcja wywolywana po wczytaniu wartosci jednostki uzupelnia opcje
	#wyboru rejestru  
    def registers_names():
        if(function_value!=''):
            Adress_database = sqlite3.connect('Adress.db')
            Adress_database.row_factory = sqlite3.Row
            Adress_cursor = Adress_database.cursor()
            Adress_cursor.execute(""" SELECT class,name  FROM Adress """)
            fun = Adress_cursor.fetchall()
            for adresses in fun:
                if(function_value=='read'):
                    if adresses['class']=='RW' or adresses['class']=='RO':
                        registers_names_list.append(adresses['name'])
                else:
                    if adresses['class']=='RW' or adresses['class']=='WO':
                        registers_names_list.append(adresses['name'])
        return registers_names_list

	#funkcja wywolywana po wczytaniu nazwy rejestru uzupelnia opcje
	#wyboru wiadomosci dla rejetru i jego opis
    def messages_names():
        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT description,name  FROM Adress """)
        fun = Adress_cursor.fetchall()
        for adresses in fun:
            if(adresses['name']==register_name_value):
                label_text.append(adresses['description'])


        if(register_name_value!=''):
            Adress_database = sqlite3.connect('Adress.db')
            Adress_database.row_factory = sqlite3.Row
            Adress_cursor = Adress_database.cursor()
            Interpretation.allowed_messages_list=[]
            Adress_cursor.execute(""" SELECT name,function,description  FROM functions """)
            fun = Adress_cursor.fetchall()
            for functions in fun:
                if(register_name_value==functions['name']):
                    message_names_list.append(functions['function'])
                    Interpretation.allowed_messages_list.append(functions['function'])
        return message_names_list
    #funkcja wywolywana po wczytaniu wiadomosci uzupelnia opis wiadomosci
	#wyboranej przez uzytkownika  
    def message_description():
        if(register_name_value!=''):
            Adress_database = sqlite3.connect('Adress.db')
            Adress_database.row_factory = sqlite3.Row
            Adress_cursor = Adress_database.cursor()
            Adress_cursor.execute(""" SELECT name,function,description  FROM functions """)
            fun = Adress_cursor.fetchall()
            for functions in fun:
                if(register_name_value==functions['name']):
                    if(message_name_value==functions['function']):
                        print(functions['description'])
                        label_text.append(functions['description'])
    messages_names()
#klasa odpowidzialna za poruszanie serwomechanizmami
class moving(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    progress2 = pyqtSignal(int)
    progress3 = pyqtSignal(int)
    stop_current_thread = pyqtSignal()
	#zmienne dla domyslnego ruchu pobrane z pliku Constans    

    position_x=0
    acceleration_x=Constants.deafult_acceleration
    decceleration_x=Constants.deafult_decceleration
    velocity_x=Constants.deafult_velocity
    position_y=0
    acceleration_y=Constants.deafult_acceleration
    decceleration_y=Constants.deafult_decceleration
    velocity_y=Constants.deafult_velocity
    #print(position_x,acceleration_y,zero)
    #funkcja ktora powoduje przypisanie wartosci podanych przez uzytkownika
    # i uruchamia funkcje poruszajaca serwomechanizmami
    def do_move(self):
        print(self)  
        global currentPosition_ui          
        currentPosition_ui = Current_position.Ui_current_position_window()
        currentPosition_ui.setupUi(currentPosition_ui)      
        move_allowance[0]=0    
        position_x=self.position_x 
        acceleration_x=self.acceleration_x
        decceleration_x=self.decceleration_x
        velocity_x=self.velocity_x
        position_y=self.position_y
        acceleration_y=self.acceleration_y
        decceleration_y=self.decceleration_y
        velocity_y=self.velocity_y
        zero=self.zero
        print(zero)	
        if(move_deafult_flag[0]==1):             
            acceleration_x=Constants.deafult_acceleration
            decceleration_x=Constants.deafult_decceleration
            velocity_x=Constants.deafult_velocity
            acceleration_y=Constants.deafult_acceleration
            decceleration_y=Constants.deafult_decceleration
            velocity_y=Constants.deafult_velocity
            print(position_x,acceleration_y)
        #jesli serwomechanizm nie wykonuje ruchu wykonaj ruch najpierw
        #jednego serwomechanizmu nastepnie drugiego
        self.zero=zero
        if(move_allowance[0]==0 ):
            result=self.do_single_move(position_x,acceleration_x,decceleration_x,velocity_x,0,zero)
            if(result==0):           

                result2=self.execute_check(0,position_x,zero)
                if(result2!=0):
                    return result2
            else:
                print(result)
                return result 
        if(move_allowance[0]==0 ):
            result=self.do_single_move(position_y,acceleration_y,decceleration_y,velocity_y,1,zero)
            if(result==0):            
                result2=self.execute_check(1,position_y,zero)
                if(result2!=0):
                    return result2
            else:
                return result 
        self.progress.emit(result)
        self.finished.emit()	
        return 0
    
    #funkcja testujaca czy serwomechanizm porusza sie poprawnie        
    def do_test(self):  
		#wykorzystuje domyslne wartosci ruchu 
        position_x=0
        move_allowance[0]=0
        acceleration_x=Constants.deafult_acceleration
        decceleration_x=Constants.deafult_decceleration
        velocity_x=Constants.deafult_velocity
        position_y=0
        acceleration_y=Constants.deafult_acceleration
        decceleration_y=Constants.deafult_decceleration
        velocity_y=Constants.deafult_velocity
        zero=Constants.deafult_zero 
        #test polega na wykonaniu ruchu nastepnie wroceniu na miejsce 
        #pierwotne przez serwomechanizmy
        iter1=0
        iter2=0        
        iter1=0
        while iter1<=20:
            iter1=iter1+1;
            print(iter1)
            if(move_allowance[0]==0):        
                result=self.do_single_move("7400" ,acceleration_x,decceleration_x,velocity_x,0,zero)
                if(result==0):  
                    result2=self.execute_check(0,7400,zero)
                    if(result2!=0):
                        self.progress.emit(result2)
                        self.finished.emit()
                        return result2 
                else:
                    self.progress.emit(result)
                    self.finished.emit()					
                    return result
            else:
                print("error asd")       
              
            if(move_allowance[0]==0):        
                result=self.do_single_move("-7400" ,acceleration_x,decceleration_x,velocity_x,0,zero)
                if(result==0):                  
                    result2=self.execute_check(0,-7400,zero)
                    if(result2!=0):
                        self.progress.emit(result2)
                        self.finished.emit()					
                        return result2 
                else:
                    self.progress.emit(result)
                    self.finished.emit()                   
                    return result   
            else:
                print("error asd3")
                                  
        print("przetestowane",move_allowance)
        self.progress.emit(result)
        self.finished.emit()	
        return 0
    #funkcja wykonujaca ruch    
    def do_single_move(self,target,acceleration,decceleration,velocity,unit,zero):
        try:
            print(zero)			
			#wczytaj zmienne globalne dotyczace wyboru serwomechanizmu i
			#pozycji startowej
            global start
            global unit_choice
            unit_choice=int(unit)
            global start_position
            global stop_thread
            if stop_thread==1:
                move_allowance[0]=1
                self.progress.emit(5)
                self.finished.emit()
                return 5
				
            #wczytaj pozycje serwomechanizmu
            message_sending.Register="Position"
            message_sending.Unit=str(Unit)
            message_sending.read_register() 
            start_position=Interpretation.position_check[0] 

            #ustaw serwomechanizm stan operacyjny pozycjonowania
            message_sending.Register="Operation_modes"
            message_sending.Unit=str(unit) 
            message_sending.message="1"
            result=message_sending.write_register()
            if(result!=0):
                self.progress.emit(result)
                self.finished.emit()  
                return result
            #wlacz silniki serwomechanizmu
            message_sending.Register="Machine_status"        
            message_sending.Unit=str(unit) 

            message_sending.message="0x0F"
            result=message_sending.write_register()
            if(result!=0):
                self.progress.emit(result)
                self.finished.emit()				
                return result        
            #okresl pozycje docelowa   
            print(["aAa",str(target)])
            message_sending.Register="Target_position"
            message_sending.Unit=str(unit) 
            message_sending.message=str(target)
            result=message_sending.write_register()
            if(result!=0):
                self.progress.emit(result)
                self.finished.emit()
                return result
            #ustaw maksymalna predkosc
            message_sending.Register="Max_velocity_trap"
            message_sending.Unit=str(unit) 
            message_sending.message=str(velocity)            
            result=message_sending.write_register()
            if(result!=0):
                self.progress.emit(result)
                self.finished.emit()
                return result
            #ustaw maksymalne przyspieszenie
            message_sending.Register="Max_Accelaration"
            message_sending.Unit=str(unit) 
            message_sending.message=str(acceleration)
            result=message_sending.write_register()
            if(result!=0):
                self.progress.emit(result)
                self.finished.emit()
                return result
            #ustaw maksymalne przyspieszenie hamowania
            message_sending.Register="Max_Decelaration"
            message_sending.Unit=str(unit) 
            message_sending.message=str(decceleration)
            result=message_sending.write_register()
            if(result!=0):
                self.progress.emit(result)
                self.finished.emit()
                return result
                           
            message_sending.Register="Position"
            message_sending.Unit=str(unit)
            result=message_sending.read_register() 
            current_position=Interpretation.position_check[0]            
            if(result!=0):
                self.progress.emit(result)
                self.finished.emit()			
                return result
            
            if(zero=="Absolute"):
				#ustaw serwomechanizm w stan rozpoczecia pozycjonowania 
				#z zerem absolutnym
                print("tutaj")              
                message_sending.Register="Machine_status"
                message_sending.Unit=str(unit) 
                message_sending.message="0x2F"
                result=message_sending.write_register()

                if(result!=0):
                    self.progress.emit(result)
                    self.finished.emit()
                    return result
                # wykonaj pozycjonowanie
                message_sending.Register="Machine_status"
                message_sending.Unit=str(unit) 
                message_sending.message="0x3F"
                result=message_sending.write_register()
             
                if(result!=0):
                    self.progress.emit(result)
                    self.finished.emit()
                    return result
            else:
				#ustaw serwomechanizm w stan rozpoczecia pozycjonowania 
				#z zerem absolutnym relatywnym
                message_sending.Register="Machine_status"
                message_sending.Unit=str(unit) 
                message_sending.message="0x4F"
                result=message_sending.write_register()
                if(result!=0):
                   self.progress.emit(result)
                   self.finished.emit()					
                   return result
                # wykonaj pozycjonowanie
                message_sending.Register="Machine_status"
                message_sending.Unit=str(unit) 
                message_sending.message="0x5F"
                result=message_sending.write_register()               
               
                if(result!=0):
                    self.progress.emit(result)
                    self.finished.emit()					
                    return result
            #podnies flage wykonywania ruchu
            move_allowance[0]=1
            self.progress3.emit(unit)
            if unit!=1:                				
                if not Current_position.time1:
                    start=timer()
                    Current_position.time1.append(0)
                    Current_position.movement1.append(current_position)
                else:
                    start=timer()-Current_position.time1[-1]
                    Current_position.time1.append(Current_position.time1[-1])
                    Current_position.movement1.append(current_position)  
            else:
                if not Current_position.time2:
                    start=timer()
                    Current_position.time2.append(0)
                    Current_position.movement2.append(current_position)
                else:
                    start=timer()-Current_position.time2[-1]-1
                    Current_position.time2.append(Current_position.time2[-1])
                    Current_position.movement2.append(current_position)        					
        except Exception:
			#w wypadku bledu wylacz silnik i wyrzuc blad
            traceback.print_exc()
            message_sending.Register="Machine_status"
            message_sending.Unit=str(Unit) 
            message_sending.message="0x06"   
            message_sending.write_register()             
            ending_position[unit_choice]=start_position
            move_allowance[0]=1 
            print("error1")
            self.progress.emit(5)
            self.finished.emit()
            return 5
        return 0            
    #funkcja sprawdzajaca czy ruch wykonywany jest poprawnie    
        
    def execute_check(self,Unit,position,zero):
        print(self)
        try:
            global stop_thread
            if stop_thread==1:
                move_allowance[0]=1
                self.progress.emit(5)
                self.finished.emit()
                return 5 
            iter3=0			     
			#pobierz wartosc startowa i stworz zmienne tymczasowe
            global start_position
            check_moving=[0]
            positions_list=[]
            Interpretation.position_check=[0]
            target_positon=0
            #ustal pozycje docelowa       
            if(zero=='Relative'):
                target_position=position+start_position
            else:
                target_position=position
            #dopoki serwomechanizm nie poruszy sie do punktu docelowego
            #sprawdzaj jego polozenie co 100ms
            while(check_moving[0]==0):
                if stop_thread==1:
                     move_allowance[0]=1
                     self.progress.emit(5)
                     self.finished.emit()
                     return 5 
                message_sending.Register="Position"
                message_sending.Unit=str(Unit)
                result=message_sending.read_register() 
                current_position=Interpretation.position_check[0]
                print(current_position)
                self.progress2.emit(int(current_position))
                if Unit!=1:
                    end=timer()
                    Current_position.movement1.append(current_position)
                    Current_position.time1.append(end-start)
                else:
                    end=timer()					
                    Current_position.movement2.append(current_position) 
                    Current_position.time2.append(end-start) 


                #jesli polozenia zgadza sie z docelowym podnies flage
                #i zakoncz petle odpytywania.
                if(result!=0):
                    check_moving[0]=1               
                    ending_position[unit_choice]=current_position
                    move_allowance[0]=1                    
                    message_sending.Register="Machine_status"
                    message_sending.Unit=str(Unit) 
                    message_sending.message="0x06" 
                    message_sending.write_register()                    
                    print("error2") 
                    self.progress.emit(5)
                    self.finished.emit()                  
                    return 4               
							
                if(abs(current_position-target_position)<10): 
                 
                    message_sending.write_register()
                    print(current_position)
                    if Unit!=1:
                        end=timer()
                        Current_position.movement1.append(current_position)
                        Current_position.time1.append(end-start)
                    else:
                        end=timer()					
                        Current_position.movement2.append(current_position) 
                        Current_position.time2.append(end-start) 
                    

                    check_moving[0]=1                                 
                    ending_position[unit_choice]=current_position
                    if stop_thread==1:
                         move_allowance[0]=1
                         self.progress.emit(5)
                         self.finished.emit()
                         return 5 
                    move_allowance[0]=0
                    time.sleep(0.5)
                    return 0

                #jesli pozycja sie powtarza i dana pozycja nie jest docelowa 
                #czyli gdy serwomechanizm sie nie porusza wyrzuc blad    
                if(current_position in positions_list and current_position!=target_position): 
                    iter3=iter3+1
                    if iter3==50:
                        message_sending.Register="Machine_status"
                        message_sending.Unit=str(Unit) 
                        message_sending.message="0x06" 
                        message_sending.write_register()
                        check_moving[0]=1               
                        ending_position[unit_choice]=current_position
                        move_allowance[0]=1  
                        print("error3")                            
                        self.progress.emit(5)
                        self.finished.emit()
                        return 5
                #jesli uklad wykonuje ruch przez ponad 15 sekund program przerywa ruch i 
                #wyrzuca blad mozna usunac jeesli bedzie zbedne    
                elif(len(positions_list)>50000):				
                    message_sending.Register="Machine_status"
                    message_sending.Unit=str(Unit) 
                    message_sending.message="0x06"   
                    message_sending.write_register()             
                    ending_position[unit_choice]=current_position
                    move_allowance[0]=1 
                    self.progress.emit(5)
                    self.finished.emit()                   
                    return 5
                else:                    						
                    positions_list.append(current_position)  
                    time.sleep(0.01)
        except Exception:
			# W razie bledu wylacz silnik i wyrzuc blad
            traceback.print_exc()
            message_sending.Register="Machine_status"
            message_sending.Unit=str(Unit) 
            message_sending.message="0x06"   
            result=message_sending.write_register()             
            ending_position[unit_choice]=current_position
            move_allowance[0]=1 
            print("error4")
            self.progress.emit(5)
            self.finished.emit()           
            return 5
  
class button_callbacks:
    def error_reset():
        global unit_choice
        global Unit
        iter1=0
        for a in Unit:
            unit_choice=iter1
            iter1=iter1+1
            message_sending.Register="Sim_dig_in"
            message_sending.Unit=1 
            message_sending.message="2"   
            result=message_sending.write_register()        
            if result!=0:
                return result 
            message_sending.Register="Sim_dig_in"
            message_sending.Unit=1
            message_sending.message="0"   

            result=message_sending.write_register()        
            if result!=0:
                print(result)
                return result
       

		
			
    def savepoint_button_callback():
        global unit_choice
        global Position_save_info
        global current_point
        Interpretation.position_check=[0]
        Position_save_info=[]
        message_sending.Register="Position"
        unit_choice=0
        message_sending.read_register() 
        
        Position_save_info.append(Interpretation.position_check[0])
        Interpretation.position_check=[0]
        message_sending.Register="Position"
        
        unit_choice=1
        message_sending.read_register() 
        Position_save_info.append(Interpretation.position_check[0])
        Saved_points.append([Position_save_info[0],Position_save_info[1]]) 
        current_point=(len(Saved_points))-1
        time = QTime.currentTime()
        timet = time.toString('hh:mm:ss')
        now=QDate.currentDate()
        nowt=now.toString('yyyy:MM:dd')
        con = sqlite3.connect('Sessions.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()       
        cur.execute("""
              CREATE TABLE IF NOT EXISTS tempsession (
                id INTEGER PRIMARY KEY ASC,
                xcoordinate  varchar(250)  NOT NULL,
                ycoordinate varchar(250)  NOT NULL,
                name varchar(250)  NOT NULL,
                date date NOT NULL,
                time varchar(250) NOT NULL

                )""")
        cur.execute('INSERT INTO tempsession VALUES(NULL,?, ?, ?, ?, ?);', (str(Position_save_info[0]), str(Position_save_info[1]),"def",nowt,timet))
        con.commit()
        Interpretation.position_check=[0]           
    def previous_buttton_callback():
        global current_point
        if len(Saved_points)>0:
            if current_point>0:
     	        current_point=current_point-1
     	        return Saved_points[current_point]
            else:
     	        return Saved_points[0]

    def next_buttton_callback():
        global current_point
        if current_point<len(Saved_points)-1:
     	    current_point=current_point+1
     	    return Saved_points[current_point]
        else:
            return Saved_points[len(Saved_points)-1]	
    
    def Read_Session_callback(session_name):
        try:
            global New_points
            con = sqlite3.connect('Sessions.db')
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("""
              CREATE TABLE IF NOT EXISTS tempsession (
                id INTEGER PRIMARY KEY ASC,
                xcoordinate  varchar(250)  NOT NULL,
                ycoordinate varchar(250)  NOT NULL,
                name varchar(250)  NOT NULL,
                date date NOT NULL,
                time varchar(250) NOT NULL

                )""")
            print(session_name)         
            query='SELECT * FROM  %s'%session_name
            cur.execute(query)
            Points= cur.fetchall()
            New_points=Points            
            command="Delete from tempsession"   
            cur.execute(command)
            command="INSERT INTO tempsession SELECT * FROM %s"%session_name   
            cur.execute(command)            
            con.commit()      

        except Exception:
            traceback.print_exc()
    
    def savesession_buttton_callback(title):
        time = QTime.currentTime()
        timet = time.toString('hh:mm:ss')
        now=QDate.currentDate()
        nowt=now.toString('yyyy:MM:dd')
        con = sqlite3.connect('Sessions.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        time = QTime.currentTime()
        timet = time.toString('hh:mm:ss')
        now=QDate.currentDate()
        nowt=now.toString('yyyy:MM:dd')
        cur.execute("""
              CREATE TABLE IF NOT EXISTS tempsession (
                id INTEGER PRIMARY KEY ASC,
                xcoordinate  varchar(250)  NOT NULL,
                ycoordinate varchar(250)  NOT NULL,
                name varchar(250)  NOT NULL,
                date date NOT NULL,
                time varchar(250) NOT NULL

                )""")
        command="Delete from tempsession"   
        cur.execute(command)
        print(len(Points))
        print(Points)
        for i in range(len(Points)):
            print((Points[i][2]))
            cur.execute('INSERT INTO tempsession VALUES(NULL,?, ?, ?, ?, ?);', (str(Points[i][0]), str(Points[i][1]),str(Points[i][2]),nowt,timet))
        if title==" ":
            title=("session"+nowt+"_"+timet)
        title=title.replace(":","_")            
        command="ALTER TABLE tempsession RENAME TO %s"%title    
        cur.execute(command)

    
    def motors_off():
        global unit_choice
        global Unit
        iter1=0
        for a in Unit:            
            unit_choice=iter1
            iter1=iter1+1
            message_sending.Register="Machine_status"
            message_sending.Unit=iter1+1
            message_sending.message="0x06"  
            result=message_sending.write_register()        
       
    def Zero_current():
        global unit_choice
        global Unit
        global move_deafult_flag
        iter1=0
        for a in Unit:
            print(iter1)
            unit_choice=iter1
            
            message_sending.Register="Target_position"
            message_sending.message=str(0)
            result=message_sending.write_register()
            if(result!=0):
               return result   
                        
            message_sending.Register="Homing_acceleration"
            message_sending.message="10"
            result=message_sending.write_register()
            if(result!=0):
               return result                      
            
            message_sending.Register="Homing_velocity"
            message_sending.message="10"
            result=message_sending.write_register()
            if(result!=0):
               return result 
                    
            message_sending.Register="Operation_modes"
            message_sending.message="6"
            result=message_sending.write_register()
            if(result!=0):
               return result 

            message_sending.Register="Sim_dig_in"
            message_sending.Unit=1 
            message_sending.message="24"   
            result=message_sending.write_register()        
            if result!=0:
                return result 

            message_sending.Register="Machine_status"
            message_sending.Unit=1
            message_sending.message="0x01F"     
            result=message_sending.write_register()        
            if result!=0:
                return result  
            message_sending.Register="Sim_dig_in"
            message_sending.Unit=1
            message_sending.message="0"   
            result=message_sending.write_register()        
            if result!=0:
                return result         
      
            if result!=0:
                return result  
            iter1=iter1+1;
            
    def current_position_check():		 
        global unit_choice
        global Unit
        positions=[]
        i=0
        for a in Unit:
           unit_choice=i
           message_sending.Register="Position"
           message_sending.Unit=i
           result=message_sending.read_register() 
           positions.append(Interpretation.position_check[0])
           i=i+1
        return positions  
              
    def current_error_check():		 
        global unit_choice
        global Unit
        global Register_respond
        error_codes=[]
        i=0
        for a in Unit:
           unit_choice=i
           message_sending.Register="Error_code"
           message_sending.Unit=i
           result=message_sending.read_register() 
           error_codes.append(Interpretation.Status_registers_message[0])
           Register_respond=[]
           i=i+1
        return error_codes    
      
    def current_drive_status_check():		 
        global unit_choice
        global Unit
        global Register_respond
        status_codes=[]
        i=0
        for a in Unit:
           unit_choice=i
           message_sending.Register="Drive_status"
           message_sending.Unit=i
           result=message_sending.read_register() 
           status_codes.append(Interpretation.Status_registers_message[0])
           i=i+1
        return status_codes         
