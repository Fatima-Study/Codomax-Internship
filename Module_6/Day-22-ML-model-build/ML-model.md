#  Module 6 — Final AI & ML Project

#  Day 22 — Machine Learning Model Building

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

<p align="center">
  <b>Codomax Digital Solutions — AI & ML Internship</b>
</p>

---

## 📌 Overview

Day 22 is the second stage of the **Module 6 — Final AI & ML Project**.

The project focuses on **Student Score Prediction using Machine Learning**.

In this stage, the dataset prepared during Day 21 was used to build and train a Machine Learning model using **Scikit-learn**.

A **Linear Regression** model was used to predict students' final scores based on study hours, attendance, and previous scores.

---

## 🎯 Objective

The objectives of Day 22 were to:

- Load the prepared student dataset.
- Select input features and target variable.
- Split the dataset into training and testing data.
- Create a Machine Learning model.
- Train the Linear Regression model.
- Generate predictions.
- Evaluate the model performance.
- Test the model with a sample student.

---

## 📊 Dataset

The project uses the `student_data.csv` dataset prepared during Day 21.

The dataset contains:

| Feature | Description |
|---|---|
| Hours_Studied | Number of hours studied |
| Attendance | Student attendance percentage |
| Previous_Score | Previous academic score |
| Final_Score | Final student score |

### Features

The following columns were used as input features:

```text
Hours_Studied
Attendance
Previous_Score
```
---

### Target

```text
Final_Score
```

The model learns the relationship between the input features and the final score.

---

## 🤖 Machine Learning Model

A **Linear Regression** model from Scikit-learn was used.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

The model was trained using the training portion of the dataset.

---

## 🔀 Train-Test Split

The dataset was divided into training and testing sets using Scikit-learn:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The training data was used to train the model, while the testing data was used to evaluate its predictions.

---

## 📈 Prediction

After training the model, predictions were generated using the test data:

```python
predictions = model.predict(X_test)
```

A sample student was also used to demonstrate how the trained model can predict a final score.

---

## 📊 Model Evaluation

The model was evaluated using:

### Mean Absolute Error (MAE)

MAE measures the average difference between the actual and predicted values.

```python
mean_absolute_error(y_test, predictions)
```

### R² Score

The R² score indicates how well the model explains the variation in the target values.

```python
r2_score(y_test, predictions)
```

The actual values produced by the program are shown in the Day 22 output screenshot.

---

## ⚙️ Methodology

```text
Start
  │
  ▼
Load Student Dataset
  │
  ▼
Select Features
  │
  ▼
Select Target Variable
  │
  ▼
Split Dataset
  │
  ▼
Create Linear Regression Model
  │
  ▼
Train Model
  │
  ▼
Generate Predictions
  │
  ▼
Evaluate Model
  │
  ▼
Make Sample Prediction
  │
  ▼
Complete Day 22
```

---

## 🛠️ Tools & Technologies

* Python 3.x
* Pandas
* NumPy
* Scikit-learn
* Windows CMD
* GitHub

---

## 📂 Project Structure

```text
Day-22-ML-model-build
│
├── student_data.csv
├── student_score_prediction.py
├── output.png
└── ML-model.md
```

---

## 📸 Output

The program successfully:

* Loaded the student dataset.
* Split the data into training and testing sets.
* Trained the Linear Regression model.
* Generated predictions.
* Calculated model evaluation metrics.
* Generated a sample student score prediction.

---

## 💡 Key Takeaways

* Learned the basic workflow of building a Machine Learning model.
* Practiced feature and target selection.
* Learned how to split data into training and testing sets.
* Built a Linear Regression model using Scikit-learn.
* Trained the model using prepared data.
* Generated predictions from the trained model.
* Learned basic model evaluation using MAE and R² Score.

---

## 📈 Learning Outcome

After completing Day 22, I gained practical experience in building and training a Machine Learning model using **Scikit-learn**.

I learned how to prepare input features, define a target variable, split a dataset, train a Linear Regression model, generate predictions, and evaluate model performance.

---

## 📝 Conclusion

Day 22 successfully completed the **Machine Learning model building and training stage** of the Student Score Prediction project.

The trained model will be further reviewed and analyzed during the next stage of the final project.

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
