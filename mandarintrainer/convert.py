import pandas
import sys
def main(args):
    input_file = args[1]
    output_file = args[2]
    read_file = pandas.read_table (input_file)
    read_file.to_csv (output_file, index=None)
    print(f"successfully created csv at {output_file}")

if __name__ == "__main__":
    main(sys.argv)