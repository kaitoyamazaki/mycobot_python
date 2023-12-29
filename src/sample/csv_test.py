import csv
import pandas as pd

file_path = "../data/theta_data.csv"
df = pd.read_csv(file_path, header=None)

data = df.values

print(data[0])