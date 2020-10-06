import sys
import sqlite3
import time
import serial
import traceback
import Interpretation
from pymodbus.client.sync import ModbusSerialClient as modbusclient
from pymodbus.constants import Defaults


function_value = ''
register_name_value = ''
registers_names_list= []
message_name_value=''
message_names_list= []
label_text=[]
Register_respond=[]
Register_respond_check=[]
error_flag=[]
Unit=[0x001,0x002]
unit_choice=1

class message_sending:
    Defaults.RetryOnEmpty = True
    Defaults.Timeout = 2
    Defaults.Retries = 2
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
        Interpretation.Status_registers=[]
        Interpretation.Status_registers_status=[]

        client = modbusclient(method='rtu', port="/dev/ttyUSB0", timeout=1,stopbits=1, bytesize=8, parity='N', baudrate=19200)
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
                    hh = client.read_holding_registers(address=adresstemp, count=int(count_r), unit=Unit[0])
                    print(hh)
                    assert (hh.function_code < 0x80,hh.function_code)                
                    print(hh.registers)
                    Interpretation.Status_registers.append([adr['name']])
                    Interpretation.Status_registers_status.append([hh.registers])              
                except:
                    print("error")
        Interpretation.interpretation.interpretcheck()
        iter2=0
        while(iter2<len(Interpretation.Status_registers)):
            Register_respond_check.append(str(Interpretation.Status_registers[iter2][0]+':'+Interpretation.Status_registers_message[iter2]))
            iter2=iter2+1
        print(Register_respond_check)
        Interpretation.Status_registers=[]
        Interpretation.Status_registers_status=[]
        client = modbusclient(method='rtu', port="/dev/ttyUSB0", timeout=1,stopbits=1, bytesize=8, parity='N', baudrate=19200)
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
                    hh = client.read_holding_registers(address=adresstemp, count=int(count_r), unit=Unit[1])
                    print(hh)
                    assert (hh.function_code < 0x80,hh.function_code)                
                    print(hh.registers)
                    Interpretation.Status_registers.append([adr['name']])
                    Interpretation.Status_registers_status.append([hh.registers])              
                except:
                    print("error")
        Interpretation.interpretation.interpretcheck()
        iter2=0
        while(iter2<len(Interpretation.Status_registers)):
            Register_respond_check[iter2]=Register_respond_check[iter2]+"   "+Interpretation.Status_registers_message[iter2]
            iter2=iter2+1    
        print(Register_respond_check)
    
                
    def read_register():
        Interpretation.Status_registers=[]
        Interpretation.Status_registers_status=[]
        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT class,name,adress,description,count FROM Adress """)
        fun = Adress_cursor.fetchall()
        Register_adress = ''
        Register_class = ''
        Register_name_temp=''
        if(Interpretation.message_read_allowance==0):
            for adr in fun:
                if (message_sending.Register == adr['name']):
                    Register_adress=adr['adress']
                    Register_class=adr['class']
                    Register_name_temp=adr['name']
                    print(Register_adress,Register_class)
                    count_r=adr['count']
            client=modbusclient(method='RTU',port='/dev/ttyUSB0',timeout=1,stopbits=1,bytesize=8,parity='N',baudrate=19200)
            connectResult=client.connect()
            try:
                hh = client.read_holding_registers(address=int(Register_adress,16),count=int(count_r), unit=Unit[unit_choice])
                print(unit_choice)
                assert (hh.function_code < 0x80)                
                Interpretation.Status_registers_message=['']
                Interpretation.Status_registers.append([Register_name_temp])
                Interpretation.Status_registers_status.append([hh.registers])
         
            except Exception:
                traceback.print_exc()
            Interpretation.interpretation.interpretcheck()
            Register_respond.append(str("Unit "+str(int(Unit[unit_choice]))+"  "+Register_name_temp+':'+Interpretation.Status_registers_message[0]))
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
                Interpretation.Status_register_send = adr['name']
                Register_adress=adr['adress']
                Register_class=adr['class']
                count_r=adr['count']
                Register_name_temp=adr['name']
                print(Register_adress,Register_class)
        message_temp=message_sending.message        
        Interpretation.Status_register_send_message=message_sending.message
        Interpretation.interpretation.interpretsend()
        if(len(error_flag)<1):
             error_flag.append(1)
        error_flag[0]=Interpretation.message_send_allowance[0]
        Interpretation.Status_registers=[]
        Interpretation.Status_registers_status=[]
        print(message_temp)
        if(Interpretation.message_send_allowance[0] == 0):
            client = modbusclient(method='RTU', port='/dev/ttyUSB0', timeout=1, stopbits=1, bytesize=8, parity='N',baudrate=19200)
            connectResult=client.connect()
            temp_register_adress=int(Register_adress,16)
            try:
                rq=0
                message_mutli_temp=[]
                if(int(count_r)==1):			
                    rq = client.write_register(address=temp_register_adress,value=int(message_temp,16) , unit=1)
                    print(rq)  
                else:					
                    if(int(message_temp)<65536):
                        message_multi_temp=[int(message_temp),0]
                        print('12',message_multi_temp)
                        rq = client.write_registers(address=temp_register_adress,values=message_multi_temp , unit=Unit[unit_choice])
                        print(rq)
                    else:
                        message_multi_temp=[int(int(message_temp)%65536),int(int(message_temp)//65536)]
                        rq = client.write_registers(address=temp_register_adress,values=message_multi_temp , unit=Unit[unit_choice])						
                        print(rq)
                print(message_mutli_temp)
                assert (rq.function_code < 0x80)
                
            except Exception:
                traceback.print_exc()
            if(Register_class=='RW'):
                hh = client.read_holding_registers(address=temp_register_adress,count=int(count_r), unit=Unit[unit_choice])
                assert (hh.function_code < 0x80)
                print(str(hh))
                Interpretation.Status_registers_message=['']
                Interpretation.Status_registers.append([Register_name_temp])
                Interpretation.Status_registers_status.append([hh.registers])
            client.close()
        else:
            print("allowance 1")
        Interpretation.interpretation.interpretcheck()
        Register_respond.append(str(Register_name_temp+':'+Interpretation.Status_registers_message[0]))




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
            Interpretation.allowed_messages_list=[]
            Adress_cursor.execute(""" SELECT name,function,description  FROM functions """)
            fun = Adress_cursor.fetchall()
            for functions in fun:
                if(register_name_value==functions['name']):
                    message_names_list.append(functions['function'])
                    Interpretation.allowed_messages_list.append(functions['function'])


        return message_names_list
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

