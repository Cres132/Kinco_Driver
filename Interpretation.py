import sys
import sqlite3
import Constants
import traceback

Status_registers=[]
Status_registers_status=[]
Status_registers_status2=[]
Status_register_send=''
Status_register_send_message=' '
Status_registers_message=[]
Send_message_type=' '
allowed_messages_list=[]
message_send_allowance=[]
message_read_allowance=0
message_write_allowance=0
position_check=[]



Unit_to_change_name = ' '
Unit_to_change_value = ' '


class interpretation:	
    def interpretcheck():
        while(len(Status_registers_message)<80):
            Status_registers_message.append("")
            
        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT name,message,description  FROM interpretation """)
        fun = Adress_cursor.fetchall()
        iter_temp1=0
        while iter_temp1 < len(Status_registers):
            status_register_temp=Status_registers[iter_temp1]
            status_register_status_temp=Status_registers_status[iter_temp1]	
            iter_temp1=iter_temp1+1
            msg_temp=''
            for inter in fun:
                if ([inter['name']]==status_register_temp):
                    print(status_register_status_temp)
                    if(str(hex(status_register_status_temp[0][0]))==inter['message']):
                        print("1")
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
                            print(status_register_temp)
                            print(status_register_status_temp[0])
                            print(msg_temp)
                    elif(inter['message']=='rs'):
                        if(len(status_register_status_temp[0])<2):
                            if(status_register_status_temp[0][0]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536							
                            msg_temp=str(round(status_register_status_temp[0][0]/163.84,3))+'  '+'rp/s^2'
                        else:
                            if(status_register_status_temp[0][1]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536	
                                 status_register_status_temp[0][1]=status_register_status_temp[0][1]-65536
                            msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536)/163.84,3))+'  '+'rp/s^2'

                    elif(inter['message']=='inc'):
                        if(len(status_register_status_temp[0])<2):
                            if(status_register_status_temp[0][0]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536
                            msg_temp=str(round(status_register_status_temp[0][0],3))+'  '+'inc'
                            position_check.append(round(status_register_status_temp[0][0],3))
                        else:
                            if(status_register_status_temp[0][1]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536	
                                 status_register_status_temp[0][1]=status_register_status_temp[0][1]-65536
                            msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536),3))+'  '	+'inc'
                            position_check.append(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536),3))
                    elif(inter['message']=='Hz'):
                        if(len(status_register_status_temp[0])<2):
                            if(status_register_status_temp[0][0]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536
                            msg_temp=str(round(status_register_status_temp[0][0]/100,3))+'  '+'Hz'
                        else:
                            if(status_register_status_temp[0][1]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536	
                                 status_register_status_temp[0][1]=status_register_status_temp[0][1]-65536
                            msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536)/100,3))+'  '+'Hz'
                            
                    elif(inter['message']=='inc/s'):
                        if(len(status_register_status_temp[0])<2):
                            if(status_register_status_temp[0][0]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536
                            msg_temp=str(round(status_register_status_temp[0][0]))+'  '+'inc/s'
                        else:
                            if(status_register_status_temp[0][1]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536	
                                 status_register_status_temp[0][1]=status_register_status_temp[0][1]-65536
                            msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536),3))+'  '+'inc/s'
                            position_check.append(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536),3))
                    elif(inter['message']=='pulse/mS'):
                        if(len(status_register_status_temp[0])<2):
                            if(status_register_status_temp[0][0]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536
                            msg_temp=str(round(status_register_status_temp[0][0]))+'  '+'pulse/mS'
                        else:
                            if(status_register_status_temp[0][1]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536	
                                 status_register_status_temp[0][1]=status_register_status_temp[0][1]-65536
                            msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536),3))+'  '+'pulse/mS'                    
                            
                    elif(inter['message']=='number'):
                        print("7")

                        msg_temp=str(round(status_register_status_temp[0][0],3))+'  '
                    else:
                        msg_temp=str(bin(round(status_register_status_temp[0][0],3)))+'  '
            Status_registers_message[iter_temp1-1]=str(msg_temp)
    
    
    def interpretsend():         
        Adress_database = sqlite3.connect('Adress.db')
        Adress_database.row_factory = sqlite3.Row
        Adress_cursor = Adress_database.cursor()
        Adress_cursor.execute(""" SELECT name,type,min,max  FROM Limits""")
        fun = Adress_cursor.fetchall()
        if(len(message_send_allowance)<1):
            message_send_allowance.append(1)
        Min_limit=0
        Max_limit=0
        Send_message_type=''
        Status_register_send_message_temp=Status_register_send_message
        for register in fun:
            if (register['name']==Status_register_send):
                Send_message_type=register['type']
                Min_limit=register['min']
                Max_limit=register['max']
        if (Send_message_type=='locked'):
            print(allowed_messages_list,Status_register_send_message_temp)
            if(Status_register_send_message_temp in allowed_messages_list):
                message_send_allowance[0]=0
            else:
                message_send_allowance[0]=1
        elif(Send_message_type=='int'):
            try:
                send_message_temp=int(Status_register_send_message_temp)               
                if(int(Min_limit)>send_message_temp or int(Max_limit)<send_message_temp):
                    message_send_allowance[0]=2
                else:					
                    message_send_allowance[0]=0
            except Exception:
                traceback.print_exc()
                print("xd2")
                message_send_allowance[0]=1
            
        else:
            message_send_allowance[0]=1		
        print(type(Status_register_send_message))
        print(Send_message_type)        
        print(message_send_allowance) 
        print("send")
        
    def interpretread():		
        message_read_allowance=0
        print("read")          
    

	
            
                    


		
