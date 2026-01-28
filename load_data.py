import pandas as pd

# load dataset
df = pd.read_csv("../data/opd_data.csv")

# basic checks
print("First 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

