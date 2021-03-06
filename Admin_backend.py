import sys
import sqlite3
import time
import serial
import Interpretation
from pymodbus.client.sync import ModbusSerialClient as modbusclient
from pymodbus.constants import Defaults


function_value = ''
register_name_value = ''
registers_names_list= []
message_name_value=''
message_names_list= []
label_text=[]
error_flag=Interpretation.message_send_allowance

class message_sending:
    Defaults.RetryOnEmpty = True
    Defaults.Timeout = 1
    Defaults.Retries = 2
    Unit = 1
    Register=  ''
    count_r = 1
    message = ''

    
    def check_connection():
        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT class,name,adress,description,count  FROM Adress """)
        fun = Adress_cursor.fetchall()
        Register_adress = ''
        Register_class = ''
        client = modbusclient(method='rtu', port="/dev/ttyUSB0", timeout=1, stopbits=1, bytesize=8, parity='N', baudrate=19200)
        print(str(client))
        connectResult = client.connect()
        print(connectResult)
        for adr in fun:
            if (adr['class']=='RO' or adr['class']=='RW'):
                count_r=adr['count'] 
                print(adr['name'])	           
                Register_adress=adr['adress']
                adresstemp=int(Register_adress, 16)
                try:
                    hh = client.read_holding_registers(address=adresstemp, count=int(count_r), unit=1)
                    assert (hh.function_code < 0x80,hh.function_code)                
                    print(hh.registers)
                    Interpretation.Status_registers.append([adr['name']])
                    Interpretation.Status_registers_status.append([hh.registers])
                    

                except:
                    print("error")
        Interpretation.interpretation.interpretcheck()  
         
                
    def read_register():

        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT class,name,adress,description,count FROM Adress """)
        fun = Adress_cursor.fetchall()
        Register_adress = ''
        Register_class = ''
        for adr in fun:
            if (message_sending.Register == adr['name']):
                Register_adress=adr['adress']
                Register_class=adr['class']
                print(Register_adress,Register_class)
                
        client=modbusclient(method='RTU',port='/dev/ttyUSB0',timeout=1,stopbits=1,bytesize=8,parity='N',baudrate=19200)
        connectResult=client.connect()
        try:
            hh = client.read_holding_registers(address=int(Register_adress,16),count=count_r, unit=Unit)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except:
            print("error")
        client.close()

        
        
    def write_register():
        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT class,name,adress,description,count  FROM Adress """)
        fun = Adress_cursor.fetchall()
        Register_adress = ''
        Register_class = ''
        for adr in fun:
            if (message_sending.Register == adr['name']):
                Register_adress=adr['adress']
                Register_class=adr['class']
                count_r=adr['count']
                print(Register_adress,Register_class)
        Interpretation.interpretation.interpretsend()
        if(Interpretation.message_send_allowance == 0):
            Interpretation.message_send_allowance=1
            client = modbusclient(method='RTU', port='/dev/ttyUSB0', timeout=1, stopbits=1, bytesize=8, parity='N',baudrate=19200)
            connectResult=client.connect()
            try:
                rq = client.write_register(address=int(Register_adress,16),value=int(message_sending.message,16) , unit=int(message_sending.Unit))
                assert (hh.function_code < 0x80)
                print(str(hh))
            except:
                print("error")
            if(Register_class=='RW'):
                hh = client.read_holding_registers(address=int(Register_adress,16),count=count_r, unit=Unit)
                assert (hh.function_code < 0x80)
                print(str(hh))
            client.close()
        else:
            print("error")
			




class comboboxes:
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
            Adress_cursor.execute(""" SELECT name,function,description  FROM functions """)
            fun = Adress_cursor.fetchall()
            for functions in fun:
                if(register_name_value==functions['name']):
                    message_names_list.append(functions['function'])


        return message_names_list
    def message_description():
        if(register_name_value!=''):
            Adress_database = sqlite3.connect('Adress.db')
            Adress_database.row_factory = sqlite3.Row
            Adress_cursor = Adress_database.cursor()
            Adress_cursor.execute(""" SELECT name,function,description  FROM functions """)
            fun = Adress_cursor.fetchall()
            for functions in fun:
                if(message_name_value==functions['function']):
                    print(functions['description'])
                    label_text.append(functions['description'])



    messages_names()

