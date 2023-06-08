import sqlite3
from sqlite3 import Error
from sqlite3 import OperationalError
import classes.filedialog as fd

class Database:
    __START_ID = 8008601
    __DB_FILEPATH = r"C:/sqlite/db/pythonsqlite.db"
    __conn = None
    __curs = None
    __id = None
    def __init__(self):
        print("Please choose database you want to open")
        self.__DB_FILEPATH = fd.open_file()
        self.__conn = sqlite3.connect(self.__DB_FILEPATH)
        self.__curs = self.__conn.cursor()
        
        print("Successfully connected to db")
        
        sql = "select max(id) from attendees;"
        try:
            self.__curs.execute(sql)
            fetched_id = self.__curs.fetchone()
            if fetched_id[0] == None:
                self.__id = self.__START_ID
            else:
                self.__id = fetched_id[0]
            print(self.__id)
        except OperationalError as er:
            print(er.args)
        
        
    def open_database(self):
        self.__DB_FILEPATH = fd.open_file()
        self.__conn = sqlite3.connect(self.__DB_FILEPATH)
        self.__curs = self.__conn.cursor()
        
        print("Successfully connected to db")
        
        sql = "select max(id) from attendees;"
        try:
            self.__curs.execute(sql)
            fetched_id = self.__curs.fetchone()
            if fetched_id[0] == None:
                self.__id = self.__START_ID
            else:
                self.__id = fetched_id[0]
            print(self.__id)
        except OperationalError as er:
            print(er.args)

        
    def close_conn(self):
        self.__conn.close()
        

    def connection_returner(self):
        """ create a database connection to a SQLite database """
        #self.conn = None
        try:
            conn = sqlite3.connect(self.__dbfile)
            #print("SQLite Version: " + sqlite3.version)
            return conn
        except Error as e:
            print(e)
        #finally:
            #if conn:
             #   conn.close()
            

    def clear_table(self):
        try:
            self.__curs.execute('''DELETE FROM ATTENDEES ''')
            self.__conn.commit()
            self.__id = self.__START_ID
        except OperationalError as er:
            print(er.args[0])
            print("Database not initialized")

    def clear_db(self):
        try:
            self.__curs.execute('''DROP TABLE ATTENDEES''')
            self.__conn.commit()
            self.__id = self.__START_ID
        except OperationalError as er:
            print(er.args[0])
            print("Database not initialized")


    def init_db(self):
        print("Initializing Database")
        print("Please choose location for db")
        self.__DB_FILEPATH = fd.save_file()
        self.__conn = sqlite3.connect(self.__DB_FILEPATH)
        self.__curs = self.__conn.cursor()
        try:
            sql = '''CREATE TABLE ATTENDEES
                    (ID INT PRIMARY KEY,
                    FNAME           VARCHAR(20)    NOT NULL,
                    LNAME           VARCHAR(20)     NOT NULL);'''
            self.__curs.execute(sql)
            print("Table created successfully")
        except OperationalError as er:
            print(er.args[0])
            print("Database already exists")


    def insert_attendee(self, fname, lname):
        #conn = sqlite3.connect(self.__dbfile)
        
        
        try:
            sql = "select max(id) from attendees;"
        
            self.__curs.execute(sql)
            fetched_id = self.__curs.fetchone()
            if fetched_id[0] == None:
                self.__id = self.__START_ID
            elif fetched_id[0] is not None:
                self.__id = fetched_id[0] + 1
            else:
                self.__id += 1

            self.__curs.execute("INSERT INTO ATTENDEES \
                            VALUES (?,?, ?)" , (self.__id, fname,lname))
            print(f"{fname} {lname} has been added to table with ID {self.__id}")
        except Error as er:
            print(er.args)
            print("No such table. Database may not be initialized")
        self.__conn.commit()


    def delete_attendee(self, id):
        print(f"Deleting Attendee: {id}")
        ID = int(id)
        cursor = self.__conn.cursor()
        sql = 'delete from ATTENDEES where ROWID=?'
        cursor.execute(sql, (ID,))
        
        print("executed")
        self.__conn.commit()



    def list_attendees(self):
        
        try:  
            sql = "select * from attendees"
            self.__curs.execute(sql)
            if  len(self.__curs.fetchall()) <= 0:
                print("Table is empty")
                
            else:
                
                print(len(self.__curs.fetchall()))
                print("Pos\tID\tFirst name\t\tLast name")
                sql = "SELECT ROWID, ID, FNAME, LNAME from ATTENDEES"
                for row in self.__curs.execute(sql):
                    rowid = row[0]
                    id = row[1]
                    fname = row[2]
                    lname = row[3]
                    if len(fname) >= 8:
                        my_string = f"{rowid}\t{id}\t{fname}\t\t{lname}"
                    else:
                        my_string = f"{rowid}\t{id}\t{fname}\t\t\t{lname}"
                    print(my_string)

                
        except Error as er:
            print(er.args)
            print("No Table called attendees. Database may not be initiliazed.")
            return

        