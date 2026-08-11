import pandas as pd

# Load dataset
df = pd.read_csv("student_performance.csv")

print("===== Student Performance Dataset =====")
print(df)

print("\n===== First 5 Rows =====")
print(df.head())

print("\n===== Last 5 Rows =====")
print(df.tail())

print("\n===== Dataset Shape =====")
print(df.shape)

print("\n===== Column Names =====")
print(df.columns)

print("\n===== Dataset Information =====")
df.info()

print("\n===== Statistical Summary =====")
print(df.describe())

print("\n===== Marks =====")
print(df["Marks"])

print("\n===== Attendance =====")
print(df["Attendance"])

print("\n===== Basic Analysis =====")
print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Average Attendance:", df["Attendance"].mean())