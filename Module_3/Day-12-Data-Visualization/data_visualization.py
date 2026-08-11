import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("student_data_cleaned.csv")

print("===== Cleaned Dataset =====")
print(df)

# -----------------------------
# Bar Chart
# -----------------------------

plt.figure(figsize=(8, 5))

plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Bar-Chart.png")
plt.show()


# -----------------------------
# Line Chart
# -----------------------------

plt.figure(figsize=(8, 5))

plt.plot(df["Name"], df["Marks"], marker="o")

plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Line-Chart.png")
plt.show()


# -----------------------------
# Pie Chart
# -----------------------------

plt.figure(figsize=(7, 7))

plt.pie(
    df["Attendance"],
    labels=df["Name"],
    autopct="%1.1f%%"
)

plt.title("Student Attendance Distribution")

plt.tight_layout()
plt.savefig("Pie-Chart.png")
plt.show()

print("\nAll charts created successfully!")