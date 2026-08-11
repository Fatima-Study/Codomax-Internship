# 🚀 Module 3 — Codomax Digital Solutions Internship

# 🧹 Day 11 — Data Cleaning & Analysis 📊

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-purple?style=for-the-badge)
![Data Cleaning](https://img.shields.io/badge/Data%20Cleaning-Analysis-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

---

<p align="center">
  <b>Codomax Digital Solutions — AI & ML Internship</b>
</p>

---

## 📌 Overview

Day 11 is the third practical task of **Module 3 — Data Analysis & Visualization** in the Codomax Digital Solutions Internship.

The main focus of this task was to learn how to **perform simple data cleaning and analysis using Pandas**.

A student performance dataset containing missing values and a duplicate record was used for practical data cleaning. The dataset was cleaned by handling missing values and removing duplicate records. Basic statistical analysis was then performed on the cleaned dataset.

---

## 🎯 Objective

The objectives of Day 11 were to:

- Identify missing values in a dataset.
- Identify duplicate records.
- Handle missing marks and attendance values.
- Remove duplicate records.
- Create a cleaned dataset.
- Perform basic statistical analysis.
- Calculate average, highest, and lowest marks.
- Calculate average attendance.

---

## 📊 Dataset

A student performance dataset was used for this task.

The dataset contains the following columns:

| Column | Description |
|---|---|
| Name | Student name |
| Subject | Subject studied |
| Marks | Student marks |
| Attendance | Attendance percentage |

The original dataset intentionally contained some data quality issues for cleaning practice.

---

## ⚠️ Data Quality Issues

The original dataset contained:

- Missing marks values.
- Missing attendance values.
- A duplicate student record.

These issues were identified before cleaning.

---

## 🔍 Identifying Missing Values

Pandas `isnull().sum()` was used to identify missing values.

```python
print(df.isnull().sum())
```
---

## 🔄 Handling Missing Values

Missing marks were replaced using the average marks:

```python
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
```

Missing attendance values were replaced using the average attendance:

```python
df["Attendance"] = df["Attendance"].fillna(
    df["Attendance"].mean()
)
```

This allowed the dataset to retain all student records while removing empty numerical values.

---

## ♻️ Removing Duplicate Records

Duplicate records were identified using:

```python
print(df.duplicated().sum())
```

Duplicate records were removed using:

```python
df = df.drop_duplicates()
```

After cleaning, the duplicate count became:

```text
0
```

---

## ✨ Cleaned Dataset

After handling missing values and removing duplicates, the cleaned dataset was saved as:

```text
student_data_cleaned.csv
```

The cleaned dataset was generated using:

```python
df.to_csv("student_data_cleaned.csv", index=False)
```

---

## 📈 Basic Data Analysis

After cleaning the dataset, basic analysis was performed.

### Average Marks

```python
df["Marks"].mean()
```

### Highest Marks

```python
df["Marks"].max()
```

### Lowest Marks

```python
df["Marks"].min()
```

### Average Attendance

```python
df["Attendance"].mean()
```

These calculations provide a simple overview of student performance after data cleaning.

---

## 🧹 Before & After Cleaning

| Data Quality Check | Before Cleaning | After Cleaning |
| ------------------ | --------------: | -------------: |
| Missing Marks      |               2 |              0 |
| Missing Attendance |               1 |              0 |
| Duplicate Records  |               1 |              0 |

The cleaning process successfully improved the quality of the dataset.

---

## ⚙️ Methodology

```text
🚀 Start
   │
   ▼
📂 Load Uncleaned Dataset
   │
   ▼
🔍 Check Missing Values
   │
   ▼
♻️ Check Duplicate Records
   │
   ▼
🧹 Handle Missing Values
   │
   ▼
🗑️ Remove Duplicate Records
   │
   ▼
📊 Perform Basic Analysis
   │
   ▼
💾 Save Cleaned Dataset
   │
   ▼
📈 Review Results
   │
   ▼
✅ Complete Day 11
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

The Day 11 task was developed and executed in a **Windows environment**.

Pandas was used for dataset cleaning and analysis.

The required library can be installed using:

```bash
py -m pip install pandas
```

The Python program was executed through **Windows Command Prompt** using:

```bash
py data_cleaning.py
```

---

## ✨ Project Structure

```text
📁 Day-11-Data-Cleaning
|
├── student_data_uncleaned.csv
├── student_data_cleaned.csv
|
├── analysis_data_cleaning.py
├── data_cleaning.py
├── update_data_cleaning.py
├── final_data_cleaning.py
│
├── Output-1-data-unclean.png
├── Output-2-update-data.png
├── Output-3-final-data-cleaning.png
└── Output-4-analysis-data.png
```
---

## 📸 Output

The program successfully identified and cleaned the data quality issues in the student performance dataset.

---

## 💡 Key Takeaways

* Pandas provides useful functions for data cleaning.
* `isnull()` helps identify missing values.
* `fillna()` can be used to handle missing values.
* `duplicated()` helps identify duplicate records.
* `drop_duplicates()` removes duplicate records.
* Clean datasets produce more reliable analysis.
* Basic statistical functions can provide useful insights into data.

---

## 📈 Learning Outcome

After completing Day 11, I gained practical experience in **data cleaning and basic data analysis using Pandas**.

I learned how to identify missing values, handle incomplete numerical data, detect duplicate records, remove duplicates, save a cleaned dataset, and perform basic statistical calculations.

This task prepared me for the final stage of Module 3, **Data Visualization using Matplotlib**.

---

## 📝 Conclusion

Day 11 successfully completed the internship requirement of **performing simple data cleaning and analysis**.

The practical implementation demonstrated how raw data can be cleaned and prepared before performing further analysis and visualization.

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

