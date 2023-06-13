from classes.attendeelist import Attendeelist
import os

print("##############################")
print("#   Welcome to the program   #")
print("#                            #")
print("#   type help for options    #")
print("##############################")
b1 = Attendeelist()

def func_loop():
    global command
    command = input()
    if command=="clear":
        os.system('cls')
        func_loop()
    elif command=="initdb":
        b1.initialize_db()
        func_loop()
    elif command=="deldb":
        b1.deletedatabase()
        func_loop()
    elif command=="opendb":
        b1.open_database()
        func_loop()
    elif command=="del":
        print("Enter pos to delete:")
        id = input()
        b1.deleteAttendee(id)
        func_loop()
    elif command=="change":
        print("Enter pos to be changed")
        id = input()
        b1.changeAttendee(id)
        func_loop()
    elif command=="filllist":
        print("Automatically filling list")
        print("How many times?")
        amount = input()
        for s in range(int(amount)):
            b1.addAttendee("John", "Doe")
        print("Automatic filling complete") 
        func_loop()
    elif command=="add":
        firstname = input("Put in first name: ")
        while Attendeelist.check_for_string(firstname) == False:
            print("Name can not contain special characters or numbers! Please enter name again:")
            firstname = input()
        lastname = input("Put in last name: ")
        while Attendeelist.check_for_string(lastname) == False:
            print("Name can not contain special characters or numbers! Please enter name again:")
            lastname = input()
        b1.addAttendee(firstname, lastname)
        func_loop()
    elif command=="clearlist":
        b1.clearAttendees()
        func_loop()
    elif command=="listall":
        b1.listAttendees()
        func_loop()
    elif command=="exit":
        print("See ya later, homeboy")
        b1.close_book()
        exit()
    elif command=="help":
        print("############################################################################")
        print("#                                                                          #")
        print("#\thelp         shows this help message                               #")
        print("#\tclearlist    clear all entries                                     #")
        print("#\tadd          add a single attendee                                 #")
        print("#\tfilllist     automatically add a certain amount of attendees       #")
        print("#\topendb       open a database with file dialog                      #")
        print("#\tinitdb       initialize a new database with file dialog            #")
        print("#\tlistall      list all attendees                                    #")
        print("#\tdel          deletes an attende at row from listall                #")
        print("#\tclear        clear the screen                                      #")
        print("#\tchange       change an attendees attributes (not implemented)      #")
        print("#\texit         ends the program                                      #")
        print("#                                                                          #")
        print("############################################################################")

        func_loop()
    else:
        print("---unknown command---")
        func_loop()


func_loop()