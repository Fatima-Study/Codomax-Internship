import pandas as pd

# Load uncleaned dataset
df = pd.read_csv("student_data_uncleaned.csv")

print("===== Original Dataset =====")
print(df)

print("\n===== Missing Values =====")
print(df.isnull().sum())

print("\n===== Duplicate Records =====")
print(df.duplicated().sum())