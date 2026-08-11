# 🚀 Module 3 — Codomax Digital Solutions Internship

# 📊 Day 9 — 🐼 Pandas & NumPy 🔢

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

___

</p>

<p align="center">
  <b>Codomax Digital Solutions — AI & ML Internship</b>
</p>

---

## 📌 Overview

Day 9 is the first practical day of **Module 3 — Data Analysis & Visualization** in the Codomax Digital Solutions Internship.

The main focus of this task was to learn the fundamentals of **NumPy and Pandas**, two important Python libraries commonly used for numerical computing, dataset handling, and data analysis.

A simple student performance dataset was used to practice creating arrays, building DataFrames, exploring data, and performing basic statistical calculations.

## 🎯 Objective

The objectives of Day 9 were to:

- Understand the basic purpose of NumPy and Pandas.
- Learn how to work with datasets using Pandas and NumPy.
- Create and work with NumPy arrays.
- Perform basic numerical calculations using NumPy.
- Create a Pandas DataFrame.
- Explore structured data using Pandas.
- Access specific columns from a dataset.
- Perform basic statistical analysis.
- Build a foundation for the upcoming dataset cleaning and visualization tasks.

## 🔢 NumPy

**NumPy (Numerical Python)** is a Python library used for numerical operations and working with arrays.

In this task, NumPy was used to create an array containing student marks and perform basic calculations.

### NumPy Operations Practiced

- Creating a NumPy array
- Calculating total marks
- Calculating average marks
- Finding maximum marks
- Finding minimum marks

---

### Example

```python
import numpy as np

marks = np.array([80, 75, 90, 85, 70])

print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
````

## 🐼 Pandas

**Pandas** is a Python library designed for working with structured and tabular data.

A Pandas **DataFrame** was created to represent a simple student performance dataset.

### Pandas Operations Practiced

* Creating a DataFrame
* Displaying dataset records
* Viewing the first rows
* Checking dataset information
* Generating statistical summaries
* Selecting individual columns
* Calculating basic statistics

### Example

```python
import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Usman"],
    "Marks": [85, 92, 78, 88, 65],
    "Attendance": [90, 95, 80, 92, 75]
}

df = pd.DataFrame(data)

print(df)
print(df.head())
print(df.info())
print(df.describe())
```

## 📊 Dataset

A small student performance dataset was created for learning and practice.

| Name   | Marks | Attendance |
| ------ | ----: | ---------: |
| Ali    |    85 |         90 |
| Sara   |    92 |         95 |
| Ahmed  |    78 |         80 |
| Ayesha |    88 |         92 |
| Usman  |    65 |         75 |

The dataset contains three columns:

* **Name** — Student name
* **Marks** — Student marks
* **Attendance** — Student attendance percentage

## 📈 Basic Data Analysis

After creating the DataFrame, basic statistical calculations were performed.

```python
print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Total Marks:", df["Marks"].sum())
```

These calculations provide a quick understanding of the students' performance.

### Analysis Performed

* **Average Marks** — Determines the average student performance.
* **Highest Marks** — Identifies the highest score.
* **Lowest Marks** — Identifies the lowest score.
* **Total Marks** — Calculates the combined marks.

## 🔍 Data Exploration

The following Pandas functions were used to explore the dataset:

| Function        | Purpose                                |
| --------------- | -------------------------------------- |
| `df.head()`     | Displays the first rows                |
| `df.info()`     | Shows dataset structure and data types |
| `df.describe()` | Provides statistical summary           |
| `df["Marks"]`   | Selects the Marks column               |
| `df.mean()`     | Calculates average values              |
| `df.max()`      | Finds maximum value                    |
| `df.min()`      | Finds minimum value                    |
| `df.sum()`      | Calculates total                       |

## ⚙️ Methodology

```text
Start
  │
  ▼
Install Pandas & NumPy
  │
  ▼
Import Required Libraries
  │
  ▼
Create NumPy Array
  │
  ▼
Perform Numerical Calculations
  │
  ▼
Create Pandas DataFrame
  │
  ▼
Explore Dataset
  │
  ▼
Perform Basic Analysis
  │
  ▼
Display Output
  │
  ▼
Complete Day 9
```

## 🛠️ Tools & Technologies

* 🐍 Python 3.x
* 🔢 NumPy
* 🐼 Pandas
* 💻 Python IDLE
* 📝 Markdown
* 🔧 GitHub

## 💻 Development Environment

The program was developed and executed using **Python IDLE** on a Windows environment.

The required libraries were installed using Python's package manager:

```bash
py -m pip install pandas numpy matplotlib
```

The installation was verified before running the Day 9 program.

---

## ✨ Project Structure

```text
📁 Day-9-Pandas-NumPy
│
├── 📄 Pandas-NumPy.md
├── 🐍 code.py
└── 🖼️ output.png
```
---

## 📸 Output

The program was successfully executed and produced output for both NumPy calculations and Pandas DataFrame analysis.

The output demonstrates:

* NumPy array operations
* Total and average marks
* Highest and lowest marks
* Pandas DataFrame
* Dataset information
* Statistical summary
* Basic data analysis

___

## 💡 Key Takeaways

* NumPy is useful for numerical computing and array operations.
* Pandas is useful for handling and analyzing structured datasets.
* A DataFrame represents data in a table-like structure.
* Pandas provides simple functions for exploring datasets.
* Basic statistical calculations can be performed easily using Pandas.
* These libraries provide an important foundation for data analysis and visualization.

## 📈 Learning Outcome

After completing Day 9, I developed a basic practical understanding of **NumPy and Pandas**.

I learned how to create NumPy arrays, perform numerical calculations, create Pandas DataFrames, explore structured data, access columns, and perform basic statistical analysis.

This task provided the foundation required for the next stages of Module 3, including **dataset exploration, data cleaning, analysis, and visualization**.

## 📝 Conclusion

Day 9 successfully introduced the fundamental concepts of **Pandas and NumPy** through a simple student performance dataset.

The practical implementation helped strengthen my understanding of Python-based data analysis and prepared me for the upcoming tasks involving dataset exploration, cleaning, and visualization.

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
