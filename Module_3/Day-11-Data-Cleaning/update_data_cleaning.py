import pandas as pd

# Load uncleaned dataset
df = pd.read_csv("student_data_uncleaned.csv")

print("===== Original Dataset =====")
print(df)

# Check missing values
print("\n===== Missing Values Before Cleaning =====")
print(df.isnull().sum())

# Fill missing marks with average marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill missing attendance with average attendance
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

# Remove duplicate records
df = df.drop_duplicates()

print("\n===== Cleaned Dataset =====")
print(df)

print("\n===== Missing Values After Cleaning =====")
print(df.isnull().sum())

print("\n===== Duplicate Records After Cleaning =====")
print(df.duplicated().sum())

df.to_csv("student_data_cleaned.csv", index=False)