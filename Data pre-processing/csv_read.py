import pandas as pd
import numpy as np

a=pd.read_csv("E:\PY\pandas\CSVS file - Copy.csv")

print(a.to_string())

#for json you should write read_json instead of read_csv.............

print(a.head(2))

print(a.tail(3))

print(a.columns)

print(a.info)

print(a.shape)

print(a.describe)