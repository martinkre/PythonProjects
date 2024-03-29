from classes.attendeelist import Attendeelist
import os
import time

print("##############################")
print("#   Welcome to the program   #")
print("#                            #")
print("#   type help for options    #")
print("##############################")
b1 = Attendeelist()

def main():
    global command
    command = input("Command: ")
    if command=="clear":
        os.system('cls')
        main()
    elif command=="initdb":
        b1.initialize_db()
        main()
    elif command=="deldb":
        b1.deletedatabase()
        main()
    elif command=="opendb":
        b1.open_database()
        main()
    elif command=="del":
        print("Enter pos to delete:")
        id = input()
        b1.deleteAttendee(id)
        main()
    elif command=="change":
        print("Enter pos to be changed")
        id = input()
        b1.changeAttendee(id)
        main()
    elif command=="filllist":
        print("Automatically filling list")
        print("How many times?")
        amount = input()
        for s in range(int(amount)):
            b1.addAttendee("John", "Doe")
        print("Automatic filling complete") 
        main()
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
        main()
    elif command=="clearlist":
        b1.clearAttendees()
        main()
    elif command=="listall":
        b1.listAttendees()
        main()
    elif command=="exit":
        print("See ya later, homeboy")
        b1.close_book()
        time.sleep(3)
        exit()
    elif command=="help":
        print("""############################################################################
#                                                                          #
#       help         shows this help message                               #
#       clearlist    clear all entries                                     #
#       add          add a single attendee                                 #
#       filllist     automatically add a certain amount of attendees       #
#       opendb       open a database with file dialog                      #
#       initdb       initialize a new database with file dialog            #
#       deldb        Deletes the database                                  #
#       listall      list all attendees                                    #
#       del          deletes an attende at row from listall                #
#       clear        clear the screen                                      #
#       change       change an attendees attributes (not implemented)      #
#       exit         ends the program                                      #
#                                                                          #
############################################################################\n""")

        main()
    else:
        print("---unknown command---")
        main()


if __name__ == "__main__":

    main()