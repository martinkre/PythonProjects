import sys
import classes.datachooser as dc

def main(args):
    print(args)
    dc.datachooser(args[1])
    


if __name__ == "__main__":
    main(sys.argv)