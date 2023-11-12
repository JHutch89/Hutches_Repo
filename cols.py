
import pandas as pd

# Read CSV file with explicit encoding
epl = pd.read_csv('/Users/jasonhutches/Desktop/Jason Hutches/Hutches_Repo/CSVs/EPL_Data.csv')

cols = epl.columns.to_list()

print(cols)