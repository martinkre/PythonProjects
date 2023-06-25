import pandas as pd

read_file = pd.read_table (r'sal.txt')
read_file.to_csv (r'mandb.csv', index=None)