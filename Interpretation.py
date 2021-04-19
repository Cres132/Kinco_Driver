import sys
import sqlite3
import Constants
import traceback

#zmienne wykorzystywane do interpretacji wczytywanych danych
Status_registers=[]
Status_registers_status=[]
Status_registers_status2=[]
Status_registers_message=[]
message_read_allowance=0
position_check=[0]
Unit_to_change_name = ' '
Unit_to_change_value = ' '
send_allowance=0

#klasa odpowiadajajaca za interpretacje wczytanych rejestrow
class interpretation:	
    def interpretcheck():
		#stworz tablice 100x1 pustych stringow
        while(len(Status_registers_message)<100):
            Status_registers_message.append("")
        #wczytaj rejestry z bazy danych    
        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT name,message,description  FROM interpretation """)
        fun = Adress_cursor.fetchall()
        #stworz zmienna tymczasowa sterujaca iteracja petli
        iter_temp1=0
        #jdopoki zmienna iterujaca jest mniejsza niz liczba podanych przez inna 
        #klase rejestrow
        while iter_temp1 < len(Status_registers):
			#wczytaj wartosci wczytane do zmiennej tymczasowej
            status_register_temp=Status_registers[iter_temp1]
            status_register_status_temp=Status_registers_status[iter_temp1]
            #zwieksz zmiennna iteracyjna	
            iter_temp1=iter_temp1+1
            msg_temp=''
            #sprawdz w bazie dancych czy wystepuje dany rejestr jesli tak 
            #przeksztalc jego wartosc na wartosc zrozumiala dla czlowieka
            for inter in fun:
                if ([inter['name']]==status_register_temp):
                    if(str(hex(status_register_status_temp[0][0]))==inter['message']):
                        if(len(status_register_status_temp[0])<2):
                            if(status_register_status_temp[0][0]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536
                            msg_temp=str(round(status_register_status_temp[0][0],3))
                        else:
                            if(status_register_status_temp[0][1]>10):
                                msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536),3))
                            else:
                                msg_temp=str(round((status_register_status_temp[0][0]+(status_register_status_temp[0][1]-65536)*65536),3))
                    elif(inter['message']=='Amp'):
                        if(len(status_register_status_temp[0])<2):                            
                            if(status_register_status_temp[0][0]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536
                            msg_temp=str(round(status_register_status_temp[0][0]/105*1.414,3))+'  '+'AMP'
                        else:
                            if(status_register_status_temp[0][1]>60000):
                                 status_register_status_temp[0][1]=status_register_status_temp[0][1]-65536
                            msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*6553)/105*1.414,3))+'  '+'AMP'

                    elif(inter['message']=='RPM'):
                        if(len(status_register_status_temp[0])<2):
                            if(status_register_status_temp[0][0]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536						
                            msg_temp=str(round(status_register_status_temp[0][0]/2730,3))+'  '+'rpm'
                        else:
                            if(status_register_status_temp[0][1]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536	
                                 status_register_status_temp[0][1]=status_register_status_temp[0][1]-65536
                            msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536)/2730,3))+'  '+'rpm'
                            #print(status_register_temp)
                            #print(status_register_status_temp[0])
                           # print(msg_temp)
                    elif(inter['message']=='rs'):
                        if(len(status_register_status_temp[0])<2):
                            if(status_register_status_temp[0][0]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536							
                            msg_temp=str(round(status_register_status_temp[0][0]/163.84,3))+'  '+'rp/s^2'
                        else:
                            if(status_register_status_temp[0][1]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536	
                                 status_register_status_temp[0][1]=status_register_status_temp[0][1]-65535
                            msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536)/163.84,3))+'  '+'rp/s^2'

                    elif(inter['message']=='inc'):
                        if(len(status_register_status_temp[0])<2):
                            if(status_register_status_temp[0][0]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536
                            msg_temp=str(round(status_register_status_temp[0][0],3))+'  '+'inc'
                            position_check[0]=round(status_register_status_temp[0][0],3)
                        else:
                            if(status_register_status_temp[0][1]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536	
                                 status_register_status_temp[0][1]=status_register_status_temp[0][1]-65535
                            msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536),3))+'  '	+'inc'
                            position_check[0]=(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536),3))
                    elif(inter['message']=='Hz'):
                        if(len(status_register_status_temp[0])<2):
                            if(status_register_status_temp[0][0]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536
                            msg_temp=str(round(status_register_status_temp[0][0]/100,3))+'  '+'Hz'
                        else:
                            if(status_register_status_temp[0][1]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536	
                                 status_register_status_temp[0][1]=status_register_status_temp[0][1]-65535
                            msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536)/100,3))+'  '+'Hz'
                            
                    elif(inter['message']=='inc/s'):
                        if(len(status_register_status_temp[0])<2):
                            if(status_register_status_temp[0][0]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536
                            msg_temp=str(round(status_register_status_temp[0][0]))+'  '+'inc/s'

                        else:
                            if(status_register_status_temp[0][1]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536	
                                 status_register_status_temp[0][1]=status_register_status_temp[0][1]-65535
                            msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536),3))+'  '+'inc/s'

                    elif(inter['message']=='pulse/mS'):
                        if(len(status_register_status_temp[0])<2):
                            if(status_register_status_temp[0][0]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536
                            msg_temp=str(round(status_register_status_temp[0][0]))+'  '+'pulse/mS'                    
                        else:
                            if(status_register_status_temp[0][1]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536	
                                 status_register_status_temp[0][1]=status_register_status_temp[0][1]-65535
                            msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536),3))+'  '+'pulse/mS'                    
                            
                    elif(inter['message']=='number'):
                        #print("7")

                        msg_temp=str(round(status_register_status_temp[0][0],3))+'  '
                    else:
                        msg_temp=str(bin(round(status_register_status_temp[0][0],3)))+'  '
            
            #zapisz uzyskane wiadomosci do tablicy             
            Status_registers_message[iter_temp1-1]=str(msg_temp)
    
    #funkcja interpretujaca czy wiadomosc wybrana przez uzytkownika nie 
    #przekracza wartosc i limitow okreslonych w bazie dancyh 
    
    def interpretsend(register_name,mess):  
		#wczytaj lokalna baze danych
        global send_allowance
        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT name,type,min,max  FROM Limits""")
        fun = Adress_cursor.fetchall()
        #utworzenie zmiennych tymaczaowych okreslajacych limity 
        Min_limit=0
        Max_limit=0
        Send_message_type=''
        #zmienna tymczasowa z wysylana wiadomoscia
        message_temp=mess
        if send_allowance==1:
            send_allowance=0
            return 1
        #print(register_name,"tutaj")
        #wczytaj wartosc limitu dla rejestru do ktorego wysylana jest 
        #wiadomosc
        for register in fun:
            if (register['name']==register_name):
                Send_message_type=register['type']
                Min_limit=register['min']
                Max_limit=register['max']
        #jesli typ wiadomosci ma predefiniowane wartosci ktore mozna 
        #wpisaywac porownaj wartosc wiadomosci podana przez uzytkownika 
        #jesli nie bedzie jej w wiadomosciach predefiniowanych wyrzuc blad        
        if (Send_message_type=='locked'):
            Adress_database = sqlite3.connect('Adress.db')
            Adress_database.row_factory = sqlite3.Row
            Adress_cursor = Adress_database.cursor()
            Adress_cursor.execute(""" SELECT name,function,description  FROM functions """)
            fun = Adress_cursor.fetchall()
            for functions in fun:
                if(register_name==functions['name'] and message_temp==functions['function']):
                    return 0
            return 1

        # jesli jest to wartosc liczbowa 
        elif(Send_message_type=='int'):
            try:
				# przeksztalc podana przez uzytkownika wartosc w stringu
				#na int
                send_message_temp=int(message_temp)   
                #sprawdz czy podana wartosc liczbowa miesci sie w okreslonych
                #w bazie danych granicach      
                if(int(eval(Min_limit))>send_message_temp or int(Max_limit)<send_message_temp):
                    return 2
                else:					
                    return 0
            except Exception:
                traceback.print_exc()
                return 1            
        else:
            return 1	
            
   #interpretacja wczytytania jeszcze nie zaimplementowana     
    def interpretread():		
        message_read_allowance=0
     
    

	
            
                    


		
