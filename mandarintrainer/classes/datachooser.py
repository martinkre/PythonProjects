import csv
import codecs

# Specify the file path


def datachooser(data):
    if data == "numbers":
        file_path = "numdb.csv"
        dbchooser(file_path)
    elif data == "top100":
        file_path = "mandb.csv"
        dbchooser(file_path)
    else:
        print("choose either numbers or top100")
        
def dbchooser(file_path):
    # Open the CSV file with proper encoding
    with codecs.open(file_path, "r", encoding="utf-8-sig") as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        # Iterate over each row in the CSV file
        for row in reader:
            # Print each row
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[7]}")