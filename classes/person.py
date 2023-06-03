class Person:
    def __init__(self, id, firstname, lastname):
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = 24
        my_str = "New Person added: ID: {sid} Name: {first} {last}".format(sid = id, first=firstname, last=lastname)
        print(my_str)

    def __str__(self) -> str:
        return self.__firstname
    
    
        
    def get_name(self):
        str_output = self.__firstname + " " + self.__lastname
        return str_output
    
    def get_formatted_name(self) -> int:
        if len(self.__firstname)< 9:
            str_output = "\t" + str(self.__id) + "\t" + self.__firstname + "\t\t" + self.__lastname
        else:
            str_output = "\t" + str(self.__id) + "\t" + self.__firstname + "\t" + self.__lastname
        
        return str_output

    def print_name(self):
        if len(self.__firstname)< 9:
            print("\t" + str(self.__id) + "\t" + self.__firstname + "\t\t" + self.__lastname)
        else:
            print("\t" + str(self.__id) + "\t" + self.__firstname + "\t" + self.__lastname)
    
    def set_name(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname
        my_str = "{sid}'s name has been changed to: {first} {last}".format(sid = self.__id, 
                                                                                        first=self.__firstname, last=self.__lastname)
        
        print(my_str)
        
    def get_age(self):
        print("My age is " + str(self.__age))
    
    def set_age(self, newage):
        print("Age has been changed to: " + newage)
        self.__age = newage

    