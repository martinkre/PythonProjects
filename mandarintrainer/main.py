import csv
import codecs

# Specify the file path
file_path = "mandb.csv"

# Open the CSV file with proper encoding
with codecs.open(file_path, "r", encoding="utf-8-sig") as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in reader:
        # Print each row
        print(row)