import pandas as pd

print("=" * 50)
print("     STUDENT SCORE PREDICTION PROJECT")
print("=" * 50)

df = pd.read_csv("student_data.csv")

print("\nComplete Dataset:")
print(df)

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nDataset preparation completed successfully.")