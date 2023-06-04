import classes.person as person
import string
class Attendeelist:
    def __init__(self):
        self.attendees = []
        self.index = 8008601
        
    def check_for_string(input: string) -> bool:
            if not input.isalpha():
                return False
            else:
                return True
        
    def addAttendee(self, firstname, lastname):
        
        new_person = person.Person(self.index, firstname, lastname)
        #new_person.set_name_and_id(self.index, firstname, lastname)
        self.attendees.append(new_person) 
        self.index = self.index + 1

    def listAttendees(self):
        if self.attendees:
            print("Pos\tID\tFirst name\tLast name")
            counter = 0
            my_iterator = iter(self.attendees)
            for x in my_iterator:
                print(str(counter) + person.Person.get_formatted_name(x))
                counter +=1
  
        else:
            print("No entries in list")
        
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
        
        try:
            self.attendees.__delitem__(int(id))
            str_print = ("Removed Attendee {id}").format(id=id)
            print(str_print)
        except IndexError:
            print("Attendee not found")
            
            

    def clearAttendees(self):
        self.attendees.clear()
        print("List has been cleared")

    