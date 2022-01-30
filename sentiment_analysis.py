import numpy as np
import pandas as pd

read=pd.read_csv('E:/PY/NLP/fifa data.csv')

print(read)

print(read.shape)

print(read.columns)

print(read.head(5))

print(read.tail(4))

print(read.describe)

print(read.isnull().any())

print(read.isnull().sum())
