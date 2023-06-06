import sqlite3
from sqlite3 import Error
from sqlite3 import OperationalError

class Database:
    __DB_FILEPATH = r"C:/sqlite/db/pythonsqlite.db"
    __conn = None
    __curs = None
    __id = 8008601
    def __init__(self):
        self.__conn = sqlite3.connect(self.__DB_FILEPATH)
        self.__curs = self.__conn.cursor()
        
        print("Successfully connected to db")
        
        sql = "select max(id) from attendees;"
        try:
            self.__curs.execute(sql)

            self.__id = self.__curs.fetchone()
            print(self.__id[0])
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
            self.__curs.execute('''DELETE FROM ATTENDEES''')
            self.__conn.commit()
        except OperationalError as er:
            print(er.args[0])
            print("Database not initialized")

    def clear_db(self):
        try:
            self.__curs.execute('''DROP TABLE ATTENDEES''')
            self.__conn.commit()
        except OperationalError as er:
            print(er.args[0])
            print("Database not initialized")


    def init_db(self):
        print("Initializing Database")
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
            self.__curs.execute("INSERT INTO ATTENDEES \
                             VALUES (?,?, ?)" , (self.__id, fname,lname))
            print(f"{fname} {lname} has been added to table")
        except Error as er:
            print(er.args)
            print("No such table. Database may not be initialized")
        self.__conn.commit()


    def delete_attendee(self, id):
        print(f"Deleting Attendee: {id}")
        ID = int(id)
        cursor = self.__conn.cursor()
        sql = 'delete from ATTENDEES where ID=?'
        cursor.execute(sql, (ID,))

        print("executed")
        self.__conn.commit()



    def list_attendees(self):
        
        try:  
            if  len(self.__curs.fetchall()) < 0:
                print("Table is empty")
                
            else:
                
                print(self.__curs.rowcount)
                print("Pos\tID\tFirst name\t\tLast name")
                for row in self.__curs.execute("SELECT ROWID, ID, FNAME, LNAME from ATTENDEES"):
                    rowid = row[0]
                    id = row[1]
                    fname = row[2]
                    lname = row[3]
                    if len(fname) > 8:
                        my_string = f"{rowid}\t{id}\t{fname}\t\t{lname}"
                    else:
                        my_string = f"{rowid}\t{id}\t{fname}\t\t\t{lname}"
                    print(my_string)

                
        except Error as er:
            print(er.args)
            print("No Table called attendees. Database may not be initiliazed.")
            return

        