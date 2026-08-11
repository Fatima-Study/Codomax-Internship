# 🚀 Module 3 — Codomax Digital Solutions Internship

# 📊 Day 10 — Dataset Exploration 🔍📈

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge)
![Dataset](https://img.shields.io/badge/Dataset-CSV-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

</p>

<p align="center">
  <b>Codomax Digital Solutions — AI & ML Internship</b>
</p>

---

## 📌 Overview

Day 10 is the second practical task of **Module 3 — Data Analysis & Visualization** in the Codomax Digital Solutions Internship.

The main focus of this task was to learn how to **load and explore a sample dataset using Pandas**.

A student performance dataset in CSV format was created and loaded into Python. The dataset was then explored by checking its rows, columns, structure, data types, statistical information, and basic values.

---

## 🎯 Objective

The objectives of Day 10 were to:

- Load a sample CSV dataset using Pandas.
- Understand the structure of a dataset.
- Display and explore dataset records.
- Check the number of rows and columns.
- Identify dataset column names.
- Check data types and dataset information.
- Generate a basic statistical summary.
- Perform simple exploration of marks and attendance data.

---

## 📊 Sample Dataset

The dataset used in this task is a **Student Performance Dataset**.

| Name | Subject | Marks | Attendance |
|---|---|---:|---:|
| Ali | Python | 85 | 90 |
| Sara | Python | 92 | 95 |
| Ahmed | Python | 78 | 80 |
| Ayesha | Python | 88 | 92 |
| Usman | Python | 65 | 75 |
| Fatima | Python | 95 | 98 |
| Hassan | Python | 72 | 82 |
| Zainab | Python | 89 | 94 |

### Dataset Columns

- **Name** — Student name.
- **Subject** — Subject studied by the student.
- **Marks** — Marks obtained by the student.
- **Attendance** — Student attendance percentage.

---

## 🐼 Loading the Dataset with Pandas

The CSV dataset was loaded using the Pandas `read_csv()` function.

```python
import pandas as pd

df = pd.read_csv("student_performance.csv")

print(df)
```

The CSV file was successfully converted into a Pandas DataFrame for further exploration.

---

## 🔍 Dataset Exploration

Several Pandas functions were used to understand the dataset.

### First 5 Rows

```python
print(df.head())
```

The `head()` function displays the first five records of the dataset.

### Last 5 Rows

```python
print(df.tail())
```

The `tail()` function displays the last five records.

### Dataset Shape

```python
print(df.shape)
```

The dataset contains:

```text
8 Rows × 4 Columns
```

### Column Names

```python
print(df.columns)
```

The dataset contains:

```text
Name
Subject
Marks
Attendance
```

---

## 🧾 Dataset Information

The `info()` function was used to inspect the structure of the dataset.

```python
df.info()
```

It provides information about:

* Number of records
* Column names
* Non-null values
* Data types
* Memory usage

---

## 📈 Statistical Summary

The `describe()` function was used to generate a statistical summary of the numerical columns.

```python
print(df.describe())
```

The summary provides information such as:

* Count
* Mean
* Standard deviation
* Minimum value
* Maximum value

---

## 📊 Basic Data Exploration

Specific columns were accessed to explore student marks and attendance.

```python
print(df["Marks"])
print(df["Attendance"])
```

Basic calculations were also performed:

```python
print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Average Attendance:", df["Attendance"].mean())
```

These calculations provide a simple overview of student performance.

---

## ⚙️ Methodology

```text
🚀 Start
   │
   ▼
📊 Create Sample CSV Dataset
   │
   ▼
🐼 Import Pandas
   │
   ▼
📂 Load CSV Dataset
   │
   ▼
🔍 Display Dataset
   │
   ▼
📋 Explore Rows & Columns
   │
   ▼
🧾 Check Dataset Information
   │
   ▼
📈 Generate Statistical Summary
   │
   ▼
📊 Perform Basic Exploration
   │
   ▼
✅ Complete Day 10
```

---

## 🛠️ Tools & Technologies

* 🐍 Python 3.x
* 🐼 Pandas
* 📊 CSV Dataset
* 💻 Windows CMD
* 📝 Notepad
* 🔧 GitHub
* 📄 Markdown

---

## 💻 Development Environment

The Day 10 task was developed and executed in a **Windows environment**.

Pandas was installed using Python's package manager:

```bash
py -m pip install pandas
```

The Python program was executed through **Windows Command Prompt** using:

```bash
py dataset_exploration.py
```

---

## ✨ Project Structure

```text
📁 Day-10-Dataset-Exploration
│
├── Dataset-Exploration.md
├── student_performance.csv
├── dataset_exploration.py
|
├── Output 1.png
├── Output 2.png
└── Output 3.png
```
---

## 📸 Output

The program successfully loaded and explored the student performance dataset.

The output demonstrates:

* Complete dataset
* First five rows
* Last five rows
* Dataset shape
* Column names
* Dataset information
* Statistical summary
* Marks and attendance values
* Basic calculations

---

## 💡 Key Takeaways

* Pandas can load CSV files easily using `read_csv()`.
* A dataset can be represented as a Pandas DataFrame.
* `head()` and `tail()` help explore dataset records.
* `shape` provides the number of rows and columns.
* `info()` helps understand dataset structure and data types.
* `describe()` provides a statistical summary.
* Individual columns can be selected and analyzed using Pandas.

---

## 📈 Learning Outcome

After completing Day 10, I gained practical experience in **loading and exploring datasets using Pandas**.

I learned how to work with CSV files, create a DataFrame from a dataset, inspect rows and columns, check dataset information, generate statistical summaries, and perform basic data exploration.

This task prepared me for the next stage of Module 3, **Data Cleaning & Analysis**.

---

## 📝 Conclusion

Day 10 successfully completed the internship requirement of **loading and exploring a sample dataset**.

The practical task strengthened my understanding of Pandas and provided hands-on experience in examining structured data before performing data cleaning, analysis, and visualization.

---

## 👩‍💻 Author & Contact

<p align="center">
  <img src="https://github.com/Fatima-Study.png" width="120" alt="Fatima">
</p>

<p align="center">
  <strong>Fatima</strong><br>
  AI & ML | Codomax Digital Solutions | Internship (Aug 2026 Batch)
</p>

<p align="center">
  <a href="https://github.com/Fatima-Study">GitHub Profile</a> •
  <a href="https://www.linkedin.com/in/fatima-taufique-1313b633b/">LinkedIn</a>
</p>
