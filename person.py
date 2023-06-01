class Person:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = 0
        my_str = "New Person added: ID: {sid} Name: {first} {last}".format(sid = id, first=firstname, last=lastname)
        print(my_str)
        
    def get_name(self):
        print("Hello my name is " + self.firstname + " " + self.lastname)
    
    def set_name_and_id(self,id, firstname, lastname):
        my_str = "Person's ID is {sid} Name has been changed to: {first} {last}".format(sid = id, first=firstname, last=lastname)
        print(my_str)
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        
    def get_age(self):
        print("My age is " + str(self.age))
    
    def set_age(self, newage):
        print("Age has been changed to: " + newage)
        self.age = newage

    