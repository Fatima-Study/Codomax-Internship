# 🚀 Module 3 — Codomax Digital Solutions Internship

# Day 12 — Data Visualization 📈📊

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![Charts](https://img.shields.io/badge/Charts-Bar%20%7C%20Line%20%7C%20Pie-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

---

<p align="center">
  <b>Codomax Digital Solutions — AI & ML Internship</b>
</p>

---

## 📌 Overview

Day 12 is the final practical task of **Module 3 — Data Analysis & Visualization** in the Codomax Digital Solutions Internship.

The main focus of this task was to learn how to **visualize data using Matplotlib**.

The cleaned student performance dataset from Day 11 was used to create different types of charts. Bar, line, and pie charts were generated to present student marks and attendance data in a simple and visual form.

---

## 🎯 Objective

The objectives of Day 12 were to:

- Use Matplotlib for data visualization.
- Load a cleaned dataset using Pandas.
- Create a bar chart to compare student marks.
- Create a line chart to show the marks trend.
- Create a pie chart to visualize attendance distribution.
- Save the generated charts as image files.
- Understand how visualization makes data easier to interpret.

---

## 📊 Dataset

The **cleaned student performance dataset** created during Day 11 was used for visualization.

The dataset contains:

| Column | Description |
|---|---|
| Name | Student name |
| Subject | Subject studied |
| Marks | Marks obtained by the student |
| Attendance | Attendance percentage |

The dataset was loaded using Pandas:

```python
import pandas as pd

df = pd.read_csv("student_data_cleaned.csv")
```
---

## 📊 Bar Chart

A **bar chart** was created to compare the marks of different students.

```python
plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
```

The bar chart makes it easy to identify differences between student marks.

---

## 📈 Line Chart

A **line chart** was created to show the trend of student marks.

```python
plt.plot(df["Name"], df["Marks"], marker="o")

plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
```

The line chart helps visualize how the marks change from one student to another.

---

## 🥧 Pie Chart

A **pie chart** was created to visualize the distribution of student attendance.

```python
plt.pie(
    df["Attendance"],
    labels=df["Name"],
    autopct="%1.1f%%"
)

plt.title("Student Attendance Distribution")
```

The pie chart represents each student's attendance as a percentage of the total.

---

## 🔄 Visualization Process

```text
🚀 Start
   │
   ▼
📂 Load Cleaned Dataset
   │
   ▼
🐼 Import Pandas
   │
   ▼
📊 Import Matplotlib
   │
   ▼
📈 Create Bar Chart
   │
   ▼
📉 Create Line Chart
   │
   ▼
🥧 Create Pie Chart
   │
   ▼
💾 Save Charts as PNG
   │
   ▼
🔍 Review Visualizations
   │
   ▼
✅ Complete Day 12
```

---

## 🛠️ Tools & Technologies

* 🐍 Python 3.x
* 🐼 Pandas
* 📊 Matplotlib
* 📄 CSV Dataset
* 💻 Windows CMD
* 📝 Notepad
* 🔧 GitHub
* 📄 Markdown

---

## 💻 Development Environment

The Day 12 task was developed and executed using **Python on Windows**.

Matplotlib was installed using:

```bash
py -m pip install matplotlib
```

The Python program was executed using:

```bash
py data_visualization.py
```

---

## ✨ Project Structure

```text
Day-12-Data-Visualization
│
├── data_visualization.md
|
├── data_visualization.py
├── student_data_cleaned.csv
│
├── output-1-bar-chart.png
├── output-2-line-chart.png
├── output-3-pie-chart.png
└── output-4-dataset.png
```

---

## 📸 Output

The program successfully generated three different visualizations from the cleaned student dataset.

---

## 💡 Key Takeaways

* Matplotlib is useful for creating data visualizations.
* Bar charts are useful for comparing values.
* Line charts help show trends and changes.
* Pie charts represent data as proportions or percentages.
* Pandas can be combined with Matplotlib for effective data visualization.
* Visual representations make datasets easier to understand.

---

## 📈 Learning Outcome

After completing Day 12, I gained practical experience in **visualizing datasets using Python, Pandas, and Matplotlib**.

I learned how to load a cleaned dataset, create bar charts, line charts, and pie charts, customize basic chart labels and titles, and save visualizations as image files.

This task completed the **Data Analysis & Visualization** requirements of Module 3.

---

## 📝 Conclusion

Day 12 successfully completed the internship requirement of creating **bar, line, and pie charts using Matplotlib**.

The practical implementation demonstrated how cleaned data can be transformed into meaningful visual representations for easier comparison, interpretation, and understanding.

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
