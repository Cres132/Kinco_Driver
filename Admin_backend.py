import sys
import sqlite3
import time
import serial
from pymodbus.client.sync import ModbusSerialClient as modbusclient
from pymodbus.constants import Defaults


function_value = ''
register_name_value = ''
registers_names_list= []
message_name_value=''
message_names_list= []
label_text=[]

class message_sending:
    Defaults.RetryOnEmpty = True
    Defaults.Timeout = 5
    Defaults.Retries = 5
    Unit = ''
    Register=  ''
    count_r = '1'
    message = ''
    def check_connection():
        client=modbusclient(method='RTU',port='/dev/ttyUSB0',timeout=1,stopbits=1,bytesize=8,parity='N',baudrate=19200)
        connectResult=client.connect()
        
        try:
            hh = client.read_holding_registers(address=Register,count=count_r, unit=Unit)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        client.close()
        
        
    def read_register():
        Message1=["1",message_sending.message,message_sending.count_r,message_sending.Register,message_sending.Unit]
        print(Message1)

        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT class,name,adress,description  FROM Adress """)
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
            hh = client.read_holding_registers(address=Register_adress,count=count_r, unit=Unit)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        client.close()

        
        
    def write_register():
        Message1=["21",message_sending.message,message_sending.count_r,message_sending.Register,message_sending.Unit]
        print(Message1)

        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT class,name,adress,description  FROM Adress """)
        fun = Adress_cursor.fetchall()
        Register_adress = ''
        Register_class = ''
        for adr in fun:
            if (message_sending.Register == adr['name']):
                Register_adress=adr['adress']
                Register_class=adr['class']
                print(Register_adress,Register_class)
        client = modbusclient(method='RTU', port='/dev/ttyUSB0', timeout=1, stopbits=1, bytesize=8, parity='N',baudrate=19200)
        connectResult=client.connect()
        try:
            rq = client.write_register(address=Register_adress,value=message_sending.message , unit=message_sending.Unit)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        if(Register_class=='RW'):
            hh = client.read_holding_registers(address=Register_adress,count=count_r, unit=Unit)
            assert (hh.function_code < 0x80)
            print(str(hh))

        client.close()




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
