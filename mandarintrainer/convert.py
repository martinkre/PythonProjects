import pandas as pd

read_file = pd.read_table (r'numbers.txt')
read_file.to_csv (r'numdb.csv', index=None)