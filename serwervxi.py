import sys
import os
import signal
import time
import logging
import Admin_ui
import Admin_backend
import traceback
sys.path.append(os.path.abspath('..'))
import vxi11_server as Vxi11
message_received=""
connection_error=0
move_error=0

def signal_handler(signal, frame):
    logger.info('Handling Ctrl+C!')
    instr_server.close()
    sys.exit(0)
                                        
class ServiceDevice(Vxi11.InstrumentDevice):

    def device_init(self):
        print('ServiceDevice: device_init()')
        return
    
    def device_read(self, request_size, term_char, flags, io_timeout):        
        global message_received 
        global connection_error
        global move_error
        Move_list=Admin_backend.Saved_points
        error = Vxi11.Error.NO_ERROR
        reason = Vxi11.ReadRespReason.END
        data = ""
        command=message_received[0:5]
        try:
			
            if(str(command)=="reser"):
                Admin_backend.button_callbacks.error_reset()
                print("Reset Error")
                data = "Reset Error"
                
            elif(str(command)=="zeroc"):
                Admin_backend.button_callbacks.Zero_current()
                print("Zero current point")
                data = "Zero current point"
                
            elif(str(command)=="curin"):
                if len(Move_list)>0:				
                    print("current index")
                    data = "current index = %d"%(Admin_backend.current_point+1) 
                else:           
                    data ="Choose session first"  
                                              
            elif(str(command)=="reall"):
                Admin_backend.current_point=0		    
                Admin_backend.button_callbacks.error_reset()
                Admin_backend.button_callbacks.Zero_current()
                Admin_backend.button_callbacks.motors_off()
                print("Reset Device")
                data = "Device rested"

            elif(str(command)=="reade"):
                error_message=["",""]	
								
                if connection_error==0:					
                    if move_error==0:
                        error_codes=Admin_backend.button_callbacks.current_error_check()  

                        iter1=0
                        for code in error_codes:
                            arr=(bytes(code, 'utf-8'))
                            print(arr)							
                            if code == '0b0  '  :
                                error_message[iter1]="No error"                              
                               
                            else:
                                error_message[iter1]="Unknow error"
                            iter1=iter1+1
                        data = "%s  %s"%(error_message[0],error_message[1])								
                    else:
                        if(move_error==1):
                            data ="wrong type of message"
                        elif(move_error==2):
                            data ="one of value out of limit"
                        elif(move_error==3):
                            data ="one of value out of limit"
                        elif(move_error==4):
                            data ="Check connection"
                        elif(move_error==5):
                            data ="Move Error"
                        elif(move_error==6):
                            data ="Invalid input data"
                        move_error=0                    
                else:
                    data = "connection error"
                    connection_error=0					
                print("Read error")
                
                
            elif(str(command)=="readd"):				
                Drive_status=Admin_backend.button_callbacks.current_drive_status_check()  
                data = "%s  %s"%(Drive_status[0],Drive_status[1])           
			
                print("Read Drive status")                                
            else:
                data = "Wrong command :("
                
        except Exception:
           traceback.print_exc()
           data ="Error :("	
                
        opaque_data = data.encode("ascii") 

        return error, reason, opaque_data
			
    def device_write(self, opaque_data, flags, io_timeout): 
       
        global message_received
        error = Vxi11.Error.NO_ERROR
        message_received=bytes.decode(opaque_data)
        print( bytes.decode(opaque_data))           
        return error 

        return error, reason, opaque_data

class MoveDevice(Vxi11.InstrumentDevice):

    def device_init(self):
        print('MoveDevice: device_init()')
        return
    
    def device_read(self, request_size, term_char, flags, io_timeout):
        global message_received
        global move_error 
        error = Vxi11.Error.NO_ERROR
        reason = Vxi11.ReadRespReason.END
        # opaque_data is a bytes array, so encode correctly!
        data = ""
        command=message_received[0:4]
        coordinates=[]       
        Move_list=Admin_backend.Saved_points
        current_point=Admin_backend.current_point        
        if(str(command)=="move"):
            try:
                for word in message_received.split():
                    if word[0]=='-':
                        coordinates.append(word)
                    if word.isdigit():  
                        coordinates.append(word)
                print(coordinates)      
                result=Remote_control.move(int(coordinates[0]),int(coordinates[1]))
                print(result)
                move_error=result
                if result==0:
                    data = "moved with x=%d INC y=%d INC move"%(int(coordinates[0]),int(coordinates[1]))
                else:
                    data = "move error"
            except Exception:
                traceback.print_exc()
                data ="Error :("      
        #obsluga poruszenia do nastepnego punktu    
        elif(str(command)=="next"):
            if len(Move_list)>0:
                try:
                    current_coordinates=Move_list[current_point]
                    saved_coor=Admin_backend.button_callbacks.next_buttton_callback()
                    move_x=int(saved_coor[0])-int(current_coordinates[0])
                    move_y=int(saved_coor[1])-int(current_coordinates[1])
                    if (move_x==0 and move_y==0):
                        print("move not needed")
                    else:
                        result=Remote_control.move(move_x,move_y)
                        print("moving to next with x=%d INC y=%d INC move"%(move_x,move_y)) 
                    data ="moved to next with x=%d INC y=%d INC move"%(move_x,move_y)
                    if Admin_backend.current_point==current_point:
                        data ="it was last point"
                except Exception:
                    traceback.print_exc()
                    data ="Error :("
            else:           
                data ="Choose session first"
                		 	
        elif(str(command)=="mtoi"):
			          
            for word in message_received.split():
                if word[0]=='-':
                    coordinates.append(word)
                if word.isdigit():  
                    index=int(word)-1
                    
            if len(Move_list)>=abs(index):
				
                try:
                    current_coordinates=Move_list[current_point]
                    saved_coor=Move_list[index]
                    move_x=int(saved_coor[0])-int(current_coordinates[0])
                    move_y=int(saved_coor[1])-int(current_coordinates[1])
                    if (move_x==0 and move_y==0):
                        print("move not needed")
                    else:
                        result=Remote_control.move(move_x,move_y)
                        print("moving to next with x=%d INC y=%d INC move"%(move_x,move_y)) 
                    data ="moved to next with x=%d INC y=%d INC move"%(move_x,move_y)
                    Admin_backend.current_point=index
                except Exception:
                    traceback.print_exc()
                    data ="Error :("
            else:				
                if len(Move_list)>0:
                    data ="Index out of list"					
                else: 					      
                    data ="Choose session first"
                       
        elif(str(command)=="prev"):
            if len(Move_list)>0:
                try:
                    current_coordinates=Move_list[current_point]
                    saved_coor=Admin_backend.button_callbacks.previous_buttton_callback()
                    move_x=int(saved_coor[0])-int(current_coordinates[0])
                    move_y=int(saved_coor[1])-int(current_coordinates[1])
                    if (move_x==0 and move_y==0):
                        print("move not needed")
                    else:
                        result=Remote_control.move(move_x,move_y)
                        print("moving to previous with x=%d INC y=%d INC move"%(move_x,move_y)) 
                    data ="moved to previous x=%d INC y=%d INC move"%(move_x,move_y)
                    if Admin_backend.current_point==current_point:
                        data ="it was first point"
                except Exception:
                    traceback.print_exc()
                    data ="Error :("
            else:           
                data ="Choose session first"
         
        elif(str(command)=="moff"):
            try:
                print("motors off") 
                Admin_backend.button_callbacks.motors_off() 
                data = "motors are off"                      		 
            except Exception:
                traceback.print_exc()
                data ="Error :("

        elif(str(command)=="crpo"):
            try:
                print("motors off") 
                positions=Admin_backend.button_callbacks.current_position_check() 
                data = "Positon X=%d Y=%d"%(int(positions[0]),int(positions[1]))                      		 
            except Exception:
                traceback.print_exc()
                data ="Error :("
                                    
        elif(str(command)=="crpt"):            			
            if len(Move_list)>0:
                try:
                    current_coordinates=Move_list[current_point]
                    data ="Current point x=%d INC y=%d INC move"%(int(current_coordinates[0]),int(current_coordinates[1]))
                except Exception:
                    traceback.print_exc()
                    data ="Error :("		
            else:           
                data ="Choose session first"		               
        else:
            data = "Wrong command :("
        opaque_data = data.encode("ascii") 

        return error, reason, opaque_data
        
    def device_write(self, opaque_data, flags, io_timeout): 
        "The device_write RPC is used to write data to the specified device"
        global message_received
        error = Vxi11.Error.NO_ERROR
        message_received=bytes.decode(opaque_data)
        print( bytes.decode(opaque_data))           
        return error 

class Listen_connection():
    def listen():
        logging.basicConfig(level=logging.WARNING)
        logger = logging.getLogger(__name__)

        signal.signal(signal.SIGINT, signal_handler)
        print('Press Ctrl+C to exit')
        logger.info('starting time_device')
    
        # create a server, attach a device, and start a thread to listen for requests
        instr_server = Vxi11.InstrumentServer()
        print(instr_server)
        instr_server.add_device_handler(ServiceDevice, 'SERV')
        instr_server.add_device_handler(MoveDevice, 'MOVE')
        instr_server.listen()
    # sleep (or do foreground work) while the Instrument threads do their job


class Remote_control():    
    def move(xcor,ycor):
        try:
            moveclass=Admin_backend.moving()
            moveclass.position_x=xcor
            moveclass.position_y=ycor
            moveclass.zero="Relative" 
            Admin_backend.move_deafult_flag[0]=1
            result=moveclass.do_move()
        except Exception:
            traceback.print_exc()
            return 1  
        return result   
        
            
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C to exit')
    logger.info('starting time_device')
    
    # create a server, attach a device, and start a thread to listen for requests
    instr_server = Vxi11.InstrumentServer()
    print(instr_server)
    instr_server.add_device_handler(ServiceDevice, 'SERV')
    instr_server.add_device_handler(MoveDevice, 'MOVE')
    instr_server.listen()

    # sleep (or do foreground work) while the Instrument threads do their job
    while True:
        time.sleep(1)

        
