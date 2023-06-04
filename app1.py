from classes.attendeelist import Attendeelist
import os
import classes.database as db

db.create_connection(r"C:\sqlite\db\pythonsqlite.db")



b1 = Attendeelist()


print("##############################")
print("#   Welcome to the program   #")
print("#                            #")
print("#   type help for options    #")
print("##############################")


def func_loop():
    global command
    command = input()
    if command=="clear":
        os.system('cls')
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
        print("Put in first name")
        firstname = input()
        while Attendeelist.check_for_string(firstname) == False:
            print("Name can not contain special characters or numbers! Please enter name again:")
            firstname = input()
        print("Put in last name")
        lastname = input()
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
        exit()
    elif command=="help":
        print("listall      list all attendees")
        print("clearlist    clear all entries")
        print("add          add a single attendee")
        print("filllist     automatically add a certain amount of attendees")
        print("help         shows this help message")
        print("exit         ends the program")
        print("#######################################")

        func_loop()
    else:
        print("---unknown command---")
        func_loop()


func_loop()