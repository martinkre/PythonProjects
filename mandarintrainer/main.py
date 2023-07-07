import sys, csv, codecs
import classes.datachooser as dc
import classes.appWindow as app1


def main(args):
    try:
        if len(args) == 3:
            dc.datachooser(args[2])
        else:
            print("choose numbers top100 or weekdays")
    except IndexError as er:
        print(er.args[0])
        print("No args given")
#####################   
#   !! DEBUG !!     #
#####################
#                   #
#  DELETE BEFORE    #
#   MERGING TO      #
#     MAIN!         #
#                   #
#####################

if __name__ == "__main__":
    arr = sys.argv
    try:
        if arr[1] == "gui":
            print("GUI loading")
            app1.MyApp.call_loader()
        elif arr[1] == "cli":
            main(arr)
        else:
            print("Need to chose either gui or cli")
    except IndexError as er:
        print("No args given")