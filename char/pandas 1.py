import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('9.1 supermarkets.xlsx')

print("Column headings:")
print(df.columns)