from classes.person import Person
import string
from classes.database import Database


class Attendeelist:
    def __init__(self):
        self.attendees = []
        self.__db = Database()
        
    def check_for_string(input: string) -> bool:
            if not input.isalpha():
                return False
            else:
                return True
        
    def addAttendee(self, firstname, lastname):
        
        #new_person = person.Person(firstname, lastname)
        #new_person.set_name_and_id(self.index, firstname, lastname)
        #self.attendees.append(new_person) 
        self.__db.insert_attendee(firstname, lastname)
        
        #self.index = self.index + 1

    def listAttendees(self):
        self.__db.list_attendees()
        
    def initialize_db(self):
        self.__db.init_db()  

    def close_book(self):
        self.__db.close_conn()
        
    def changeAttendee(self, id):
        try:
            person_to_be_changed = self.attendees[int(id)]
            print("Enter new firstname")
            fname = input()
            print("Enter new last name")
            lname = input()
            person_to_be_changed.set_name(fname,lname)
            
        except IndexError:
            print("Attendee not found")
        
    def deleteAttendee(self, id):
        self.__db.delete_attendee(id)
            
    def open_database(self):
        self.__db.open_database()   

    def clearAttendees(self):
        self.__db.clear_table()
    

    def deletedatabase(self):
        self.__db.clear_db()
        
        

    