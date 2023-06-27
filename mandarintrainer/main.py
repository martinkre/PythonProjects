import sys
import classes.datachooser as dc

def main(args):
    try:
        dc.datachooser(args[1])
    except IndexError as er:
        print(er.args[0])
        print("you need to run with numbers, top100 or weekdays")
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
    main(sys.argv)