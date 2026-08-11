# 🚀 Module 6 — Final AI & ML Project

# 📊 Day 21 — Dataset Preparation & Exploration

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge)
![Dataset](https://img.shields.io/badge/Dataset-CSV-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

<p align="center">
  <b>Codomax Digital Solutions — AI & ML Internship</b>
</p>

---

## 📌 Overview

Day 21 is the first stage of the **Module 6 — Final AI & ML Project**.

The project focuses on **Student Score Prediction using Machine Learning**. Day 21 was dedicated to preparing and exploring the student dataset before building the Machine Learning model.

A CSV dataset containing study hours, attendance, previous scores, and final scores was created and loaded using Pandas.

---

## 🎯 Objective

The objectives of Day 21 were to:

- Prepare a student performance dataset.
- Store the dataset in CSV format.
- Load the dataset using Pandas.
- Explore the dataset structure.
- Check rows and columns.
- Review column names and data types.
- Generate a basic statistical summary.
- Prepare the dataset for the Machine Learning model.

---

## 📊 Dataset

The dataset contains the following columns:

| Column | Description |
|---|---|
| Hours_Studied | Number of hours studied |
| Attendance | Student attendance percentage |
| Previous_Score | Previous academic score |
| Final_Score | Final score |

The dataset contains **10 student records and 4 columns**.

---

## 🐼 Dataset Loading

The CSV file was loaded using Pandas:

```python
import pandas as pd

df = pd.read_csv("student_data.csv")

print(df)
```
---

## 🔍 Dataset Exploration

The following operations were performed:

```python
print(df.shape)
print(df.columns.tolist())
df.info()
print(df.describe())
```

These functions were used to understand:

* Dataset size
* Column names
* Data types
* Non-null values
* Statistical information

---

## ⚙️ Methodology

```text
Start
  │
  ▼
Create Student Dataset
  │
  ▼
Save Dataset as CSV
  │
  ▼
Import Pandas
  │
  ▼
Load CSV Dataset
  │
  ▼
Explore Dataset
  │
  ▼
Check Rows & Columns
  │
  ▼
Check Data Types
  │
  ▼
Generate Statistical Summary
  │
  ▼
Prepare Dataset for ML
  │
  ▼
Complete Day 21
```

---

## 🛠️ Tools & Technologies

* Python 3.x
* Pandas
* CSV
* Windows CMD
* GitHub

---

## 📂 Project Structure

```text
Day-21-Dataset-Preparation
│
├── student_data.csv
├── prepare_dataset.py
├── dataset-output-1.png
├── dataset-output-2.png
└── Dataset-Prepare.md
```

---

## 📸 Output

The dataset was successfully loaded and explored using Python and Pandas.

The output demonstrates:

* Complete dataset
* Dataset shape
* Column names
* Dataset information
* Statistical summary

---

## 💡 Key Takeaways

* Learned how to create and work with CSV datasets.
* Used Pandas to load structured data.
* Explored dataset dimensions and columns.
* Checked data types and dataset information.
* Generated a statistical summary.
* Prepared the dataset for the next Machine Learning stage.

---

## 📈 Learning Outcome

After completing Day 21, I gained practical experience in preparing and exploring a dataset for a Machine Learning project.

This task established the foundation for **model building, training, and prediction** in the upcoming stages of the final project.

---

## 📝 Conclusion

Day 21 successfully completed the dataset preparation and exploration stage of the **Student Score Prediction** project.

The prepared dataset will be used in the next stage to build and train the Machine Learning model.

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
