import sqlite3
class check:
    con = sqlite3.connect('users.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS users;")



    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY ASC,
            level varchar(250) NOT NULL,
            user varchar(250) NOT NULL,
            password varchar(250) NOT NULL)""")
    cur.execute('INSERT INTO users VALUES(NULL,?, ?, ?);', ('Admin','admin', 'admin'))
    con.commit()



    def czytajdane():
        check.cur.execute(""" SELECT user,password FROM users """)
        users = check.cur.fetchall()



class Adress:
    con = sqlite3.connect('Adress.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS Adress (
                id INTEGER PRIMARY KEY ASC,
                class varchar(250) NOT NULL,
                name varchar(250) NOT NULL,
                adress varchar(250) NOT NULL,
                description varchar(250) NOT NULL,
                count varchar(250) NOT NULL
                )""")
   
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Machine_status', '0x3100','Use control word to change status of drive =>machine state','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RO', 'Drive_status', '0x3200','Status byte shows the status of drive','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('WO', 'Operation_modes', '0x3500','Allow to switch operation mode','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RO', 'Position', '0x3700','Actual position value','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RO', 'Velocity', '0x3b00 ','Actual velocity value','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RO', 'Current', '0x3E00','Actual current value','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RO', 'Digital_inputs', '0x6D00','Status words for digital inputs ','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Target_position', '0x4000','Target position in operation mode 1,range:0-x','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Max_velocity_trap', '0x4A00','Maximum velocity of trapezium profile in mode 1 range:0-x','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Max_Accelaration', '0x4B00','Acceleration of the trapezium profile D:610.352rps/s range:0-x','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Max_Decelaration', '0x4C00','Deceleration of the trapezium profile D：610.352rps/s range:0-x','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Target_velocity', '0x6F00','Target velocity in mode 3, -3, or 4 range:0-x','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Target_current', '0x3C00','Target current range:0-x','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Max_current', '0x3D00','Maximum current range:0-x','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Max_velocity', '0x4900','Maximum velocity range:0-x','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Homing_methods', '0x4D00','Homing methods range:0-x' ,'1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Homing_velocity', '0x5010','Velocity for searching limit switch range:0-x','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Homing_velocity_n', '0x5020','Velocity for searching phase-N signa range:0-x','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Homing_acceleration', '0x5200','Acceleration range:0-x','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Homing_offset', '0x4100','Home offset range:0-x','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RO', 'Error_code', '0x1F00','Current error code','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Max_fol_err', '0x3800','Maximum following error generates alarm','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Pos_reach_window', '0x3900','Position range for "target rached"','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Soft_pos_limit', '0x4410','Soft positive limit','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Soft_neg_limit', '0x4420','Soft negative limit','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Vel_loop_gain_prop', '0x6310','Proportional gain of velocity 50-soft 200-hard','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Vel_loop_gain_int', '0x6320','Integral gain of velocity','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Speed_filter', '0x6350','Speed feedback filter','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Pos_loop_val_prop', '0x6810','Proportional value of position loop','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Loop_velocity', '0x6820','Loop velocity feedworward','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Loop_acceleration', '0x6830','Loop acceleration feedworward','1'))         
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Smooth_filter', '0x6850','Loop smooth filter','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'EGR_numerator', '0x1310','Numerator of electric gain ratio','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'EGR_Denominator', '0x1320','Denominator of electric gain ratio','1'))  
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Pulse_mode_control', '0x1930','Pulse mode control','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Input_pulse', '0x1940','Input pulse amount before EG','2'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Exec_pulse', '0x1950','Execute pulse after EG','2')) 
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Pulse_filter', '0x1960','Filter for pulse input','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Pulse_speed_m', '0x19C0','Pulse speed of master','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Pulse_speed_s', '0x19D0','Pulse speed of slave','1'))         
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Storage_control_param', '0x2910','storage control parameters','1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('RW', 'Save_motor_pram', '0x2930','1 Save motor parametrs','1'))

       
    cur.execute("""
            CREATE TABLE IF NOT EXISTS Adress_multi (
                id INTEGER PRIMARY KEY ASC,
                class varchar(250) NOT NULL,
                name varchar(250) NOT NULL,
                adress varchar(250) NOT NULL,
                description varchar(250) NOT NULL)""")
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'POSITION_CONTROL0', '0x0C10', 'Multiple position control 0'))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'POSITION_CONTROL1', '0x0C20', 'Multiple position control 1'))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'POSITION_CONTROL2', '0x0C30', 'Multiple position control 2'))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'POSITION_CONTROL3', '0x0C40', 'Multiple position control 3'))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'POSITION_CONTROL4', '0x0D00', 'Multiple position control 4'))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'POSITION_CONTROL5', '0x0D10', 'Multiple position control 5'))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'POSITION_CONTROL6', '0x0D20', 'Multiple position control 6'))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'POSITION_CONTROL7', '0x0D30', 'Multiple position control 7'))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'SPEED_CONTROL0', '0x0C50 ', 'Multiple speed control0 '))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'SPEED_CONTROL1', '0x0C60', 'Multiple speed control1 '))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'SPEED_CONTROL2', '0x0C70', 'Multiple speed control2 '))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'SPEED_CONTROL3', '0x0C80', 'Multiple speed control3 '))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'SPEED_CONTROL4', '0x0D40', 'Multiple speed control4 '))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'SPEED_CONTROL5', '0x0D50', 'Multiple speed control5 '))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'SPEED_CONTROL6', '0x0D60', 'Multiple speed control6 '))
    cur.execute('INSERT INTO Adress_multi VALUES(NULL,?, ?, ?, ?);', ('RW', 'SPEED_CONTROL7', '0x0D70', 'Multiple speed control7 '))
    cur.execute("""
                CREATE TABLE IF NOT EXISTS functions (
                    id INTEGER PRIMARY KEY ASC,
                    name varchar(250) NOT NULL,
                    function varchar(250) NOT NULL,
                    description varchar(250) NOT NULL)""")
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x06', 'Motor power off'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x0F', 'Motor power on'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x0B', 'Quick stop, load tops-voltage switched off'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x01F', 'Start homing'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x2F', 'Start absolute positioning immediately'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x3F', 'Start absolute positioning immediately'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x4F', 'Start absolute positioning immediately'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x5F', 'Start relative positioning immediately'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x103F', 'Start absolute positioning while target position changes.'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x105F', 'Start relative positioning while target position changes'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0X80', 'Clear internal error'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x06', 'Motor power off'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Operation_modes', '1', 'Positioning with position loop'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Operation_modes', '3', 'Velocity with position loop'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Operation_modes', '-3', 'Velocity loop (immediate velocity mode)'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Operation_modes', '-4', 'Master/slave or pulse/direction control mode'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Operation_modes', '6', 'Homing'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Operation_modes', '7', 'CANOPEN based motion interpolation'))    
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Target_position', 'inc','Target coordinate range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Max_velocity_trap', 'RPM','Maximum velocity of trapezium profile range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Max_Accelaration', 'rp/s^2','Acceleration of the trapezium profile D：610.352 range:0-x' ))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Max_Decelaration', 'rp/s^2','Deceleration of the trapezium profile D：610.352 range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Target_velocity', 'RPM','Target velocity in mode 3, -3, or 4 range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Target_current', 'AMP','Target current range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Max_current', 'AMP','Maximum current range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Max_velocity', 'RPM','Maximum velocity range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Homing_methods', 'number','Homing methods range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Homing_velocity', 'RPM','Velocity for searching limit switch range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Homing_velocity_n', 'RPM','Velocity for searching phase-N signal range:0-x '))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Homing_acceleration', 'rp/s^2','Acceleration range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Homing_offset', 'inc','Home offset range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Max_fol_err', 'inc','Maximum following error generates alarm range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Pos_reach_window', 'inc','Position range for "target rached" range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Soft_pos_limit', 'inc','Soft positive limit range:0-x' ))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Soft_neg_limit', 'inc','Soft negative limit'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Vel_loop_gain_prop', 'inc','Proportional gain of velocity 50-soft 200-hard range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Vel_loop_gain_int', 'number','Integral gain of velocity range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Speed_filter', 'number','Speed feedback filter range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Pos_loop_val_prop', 'number','Proportional value of position loop range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Loop_velocity', 'number','Loop velocity feedworward range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Loop_acceleration', 'number','Loop acceleration feedworward range:0-x'))         
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Smooth_filter', 'number','Loop smooth filter range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('EGR_numerator', 'number','Numerator of electric gain ratio range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('EGR_Denominator', 'number','Denominator of electric gain ratio range:0-x'))  
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Pulse_mode_control', '0','CW/CCW'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Pulse_mode_control', '1','Pulse/direction'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Pulse_mode_control', '2','Incremental encoder'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Pulse_mode_control', '10','CW/CCW ,Rs 422 type'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Pulse_mode_control', '11','pulse/direction ,Rs 422 type'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Pulse_mode_control', '12','incremental encoder ,Rs 422 type'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Input_pulse', 'inc','Input pulse amount before EG range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Exec_pulse', 'inc','Execute pulse after EG range:0-x')) 
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Pulse_filter', 'number','Filter for pulse input range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Pulse_speed_m', 'number','Pulse speed of master range:0-x'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Pulse_speed_s', 'number','Pulse speed of slave range:0-x'))         
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Storage_control_param', '1','Save all parameters '))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Storage_control_param', '10','Initalize all param'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Save_motor_pram', '1','1 Save motor parametrs '))





    cur.execute("""
                CREATE TABLE IF NOT EXISTS interpretation (
                    id INTEGER PRIMARY KEY ASC,
                    name varchar(250) NOT NULL,
                    message varchar(250) NOT NULL,
                    description varchar(250) NOT NULL)""")
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Machine_status', 'number', 'do zrobienia'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x0001', 'ready to switch on'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x0002', 'switch on'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x0004', 'operation enable'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x0008', 'fault'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x0010', 'Voltage Disable'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x0020', 'Quick Stop'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x0040', 'switch on disable'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x0080', 'warning'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x0100', 'internal reserved'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x0200', 'reserved'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x0400', 'target reach'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x0800', 'internal limit active'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x1000', 'Step.Ach./V=0/Hom.att'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x2000', 'Foll.Err/Res.Hom.Err.'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x4000', 'Commutation Found'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Drive_status', '0x8000', 'Referene Found'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Position', 'inc', 'Actual position value'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Velocity', 'RPM', 'Actual velocity value'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Current', 'Amp', 'Actual current value'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Digital_inputs', '0x0001', 'Negative limit signal status'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Digital_inputs', '0x0002', 'Positive limit signal status'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Digital_inputs', '0x0004', 'Home signal status'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Digital_inputs', '0x0008', 'Hardware lock signal status'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Target_position', 'inc', 'target position value'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Max_velocity_trap', 'RPM', 'max velocity trapezium mode'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Max_Accelaration', 'rs','Acceleration of the trapezium profile Default value：610.352rps/s'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Max_Decelaration', 'rs','Deceleration of the trapezium profile Default value：610.352rps/s'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Target_velocity', 'RPM','Target velocity in mode 3, -3, or 4'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Target_current', 'Amp','Target current'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Max_current', 'Amp','Maximum current'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Max_velocity', 'RPM','Maximum velocity'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Homing_methods', 'number','Homing methods'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Homing_velocity', 'RPM','Velocity for searching limit switch'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Homing_velocity_n', 'RPM','Velocity for searching phase-N signa'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Homing_acceleration', 'rs','Acceleration'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Homing_offset', 'number','Home offset'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x0000','internal'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x0001','encoder ABZ'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x0002','encoder UVW'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x0004','encoder counting'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x0008','over temperature'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x0010','over voltage'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x0020','low voltage'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x0040','over current'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x0080','chop resistor'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x0100','following error'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x0200','logic voltage'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x0400','IIt error'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x0800','over frequency'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x1000','Reservd'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x2000','commutation'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x4000','eeprom'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Error_code', '0x8000',''))    
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Max_fol_err', 'inc','Maximum following error generates alarm'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Pos_reach_window', 'inc','Position range for "target rached"'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Soft_pos_limit', 'inc','Soft positive limit'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Soft_neg_limit', 'inc','Soft negative limit'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Vel_loop_gain_prop', 'inc/s','Proportional gain of velocity 50-soft 200-hard'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Vel_loop_gain_int', 'number','Integral gain of velocity'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Speed_filter', 'number','Speed feedback filter'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Pos_loop_val_prop', 'number','Proportional value of position loop'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Loop_velocity', 'number','Loop velocity feedworward'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Loop_acceleration', 'number','Loop acceleration feedworward'))         
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Smooth_filter', 'number','Loop smooth filter'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('EGR_numerator', 'number','Numerator of electric gain ratio'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('EGR_Denominator', 'number','Denominator of electric gain ratio'))  
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Pulse_mode_control', 'number','Pulse mode control'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Input_pulse', 'inc','Input pulse amount before EG'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Exec_pulse', 'inc','Execute pulse after EG')) 
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Pulse_filter', 'number','Filter for pulse input'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Pulse_speed_m', 'pulse/mS','Pulse speed of master'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Pulse_speed_s', 'pulse/mS','Pulse speed of slave'))         
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Storage_control_param', 'number','1 Save all parameters ,10 initalize all param'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Save_motor_pram', 'number','1 Save motor parametrs'))
    con.commit()



    cur.execute("""
            CREATE TABLE IF NOT EXISTS Limits (
                id INTEGER PRIMARY KEY ASC,
                name varchar(250) NOT NULL,
                type varchar(250) NOT NULL,
                min varchar(250) NOT NULL,
                max varchar(250) NOT NULL)""")
   
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Machine_status', 'locked','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Operation_modes', 'locked','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Target_position', 'int','-10000','10000'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Max_velocity_trap', 'int','0','140000'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Max_Accelaration', 'int','0','8193'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Max_Decelaration', 'int','0','8193'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Target_velocity', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Target_current', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Max_current', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Max_velocity', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Homing_methods', 'int','0' ,'0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Homing_velocity', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Homing_velocity_n', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Homing_acceleration', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Homing_offset', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Max_fol_err', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Pos_reach_window', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Soft_pos_limit', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Soft_neg_limit', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Vel_loop_gain_prop', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Vel_loop_gain_int', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Speed_filter', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Pos_loop_val_prop', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Loop_velocity', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Loop_acceleration', 'int','0','0'))         
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Smooth_filter', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('EGR_numerator', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('EGR_Denominator', 'int','0','0'))  
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Pulse_mode_control', 'locked','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Input_pulse', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Exec_pulse', 'int','0','0')) 
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Pulse_filter', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Pulse_speed_m', 'int','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Pulse_speed_s', 'int','0','0'))         
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Storage_control_param', 'locked','0','0'))
    cur.execute('INSERT INTO Limits VALUES(NULL,?, ?, ?, ?);', ('Save_motor_pram', 'locked','0s','0'))
    con.commit()

def czytajdane():
    Adress.cur.execute(""" SELECT id,name,function,description FROM functions """)
    func = Adress.cur.fetchall()
    list1=[]
    for f in func:
        print('s')
        list1.append(f['name'])
    print(list1)
czytajdane()