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
                description varchar(250) NOT NULL)""")
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Machine_status', '0x3100','Use control word to change status of drive =>machine state'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RO', 'Drive_status', '0x3200','Status byte shows the status of drive'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('WO', 'Operation_modes', '0x3500','Allow to switch operation mode'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RO', 'Position', '0x3700','Actual position value'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RO', 'Velocity', '0x3b00 ','Actual velocity value'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RO', 'Current', '0x3E00','Actual current value'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RO', 'Digital_outputs', '0x6D00','Status words for digital inputs'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Target_position', '0x4000','Target position in operation mode 1, shift to demand position if control word starts motion'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Max_velocity', '0x4A00','Maximum velocity of trapezium profile in mode 1'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Max_Accelarotion', '0x4B00','Acceleration of the trapezium profile Default value：610.352rps/s'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Max_Decelarotion', '0x4C00','Deceleration of the trapezium profile Default value：610.352rps/s'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Target_velocity', '0x6F00','Target velocity in mode 3, -3, or 4'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Target_current', '0x3C00','Target current'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Max_current', '0x3D00','Maximum current'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Max_velocity', '0x4900','Maximum velocity'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Homing_methods', '0x4D00','Homing methods'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Homing_velocity', '0x5010','Velocity for searching limit switch'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Homing_velocity_n', '0x5020','Velocity for searching phase-N signa'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Homing_acceleration', '0x5200','Acceleration'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RW', 'Homing_offset', '0x4100','Home offset'))
    cur.execute('INSERT INTO Adress VALUES(NULL,?, ?, ?, ?);', ('RO', 'Error_code', '0x1F00','Current error code'))



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
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Operation_modes', '1', 'Positioning with position loop'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Operation_modes', '3', 'Velocity with position loop'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Operation_modes', '-3', 'Velocity loop (immediate velocity mode)'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Operation_modes', '-4', 'Master/slave or pulse/direction control mode'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Operation_modes', '6', 'Homing'))
    cur.execute('INSERT INTO functions VALUES(NULL,?, ?, ?);', ('Operation_modes', '7', 'CANOPEN based motion interpolation'))




    cur.execute("""
                CREATE TABLE IF NOT EXISTS interpretation (
                    id INTEGER PRIMARY KEY ASC,
                    name varchar(250) NOT NULL,
                    message varchar(250) NOT NULL,
                    description varchar(250) NOT NULL)""")
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
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Velocity', 'DEC', 'Actual velocity value'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Current', 'number', 'Actual current value'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Digital_outputs', '0x0001', 'Negative limit signal status'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Digital_outputs', '0x0002', 'Positive limit signal status'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Digital_outputs', '0x0004', 'Home signal status'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('Digital_outputs', '0x0008', 'Hardware lock signal status'))
    cur.execute('INSERT INTO interpretation VALUES(NULL,?, ?, ?);', ('', '', ''))

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
