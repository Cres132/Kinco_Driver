import sys
import sqlite3
import Constants

Status_registers=[]
Status_registers_status=[]
Status_registers_message=[]
message_send_allowance=1
while(len(Status_registers_message)<22):
   Status_registers_message.append("")



Unit_to_change_name = ' '
Unit_to_change_value = ' '


class interpretation:	
    def interpretcheck():

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
                        else:
                            if(status_register_status_temp[0][1]>60000):
                                 status_register_status_temp[0][0]=status_register_status_temp[0][0]-65536	
                                 status_register_status_temp[0][1]=status_register_status_temp[0][1]-65536
                            msg_temp=str(round((status_register_status_temp[0][0]+status_register_status_temp[0][1]*65536),3))+'  '	+'inc'

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
                    elif(inter['message']=='number'):
                        print("7")

                        msg_temp=str(round(status_register_status_temp[0][0],3))+'  '
                    else:
                        msg_temp=str(round(status_register_status_temp[0][0],3))+'  '
            print(msg_temp)
            Status_registers_message[iter_temp1-1]=str(msg_temp)
    def interpretsend():
        message_send_allowance=1
        print("send")
    def interpretread():
        print("read")                  
                    


		
