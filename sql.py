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
   
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?,?);', ('RW', 'Machine_status', '0x3100','Use control word to change status of drive =>machine state','1'))
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
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?, ?);', ('', '', '','',''))


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
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x2F-3F', 'Start absolute positioning immediately'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x4F-5F', 'Start relative positioning immediately'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x103F', 'Start absolute positioning while target position changes.'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x105F', 'Start relative positioning while target position changes'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Machine_status', '0x0F-1F', 'Start homing'))
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
