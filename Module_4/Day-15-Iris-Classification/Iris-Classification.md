# 🚀 Module 4 — Codomax Digital Solutions Internship

# 🌸 Day 15 — Iris Flower Classification 

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)](https://www.python.org/)
[![Iris Dataset](https://img.shields.io/badge/Dataset-Iris-green?style=for-the-badge)](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)
[![KNN](https://img.shields.io/badge/Model-KNN-purple?style=for-the-badge)](https://scikit-learn.org/stable/modules/neighbors.html)
[![Classification](https://img.shields.io/badge/Topic-Classification-red?style=for-the-badge)](https://scikit-learn.org/stable/supervised_learning.html)
[![Flower Prediction](https://img.shields.io/badge/Topic-Flower%20Prediction-pink?style=for-the-badge)](https://scikit-learn.org/stable/supervised_learning.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
---
---
<p align="center">
  <b>Codomax Digital Solutions — AI & ML Internship</b>
</p>

---

## 📌 Overview

Day 15 is the third practical task of **Module 4 — Machine Learning Fundamentals** in the Codomax Digital Solutions Internship.

The main focus of this task was to perform **Iris Flower Classification using Machine Learning**.

The Iris dataset provided by Scikit-learn was used with a **K-Nearest Neighbors (KNN)** classification model. The trained model was given new flower measurements and used to predict the corresponding Iris flower class.

---

## 🎯 Objective

The objectives of Day 15 were to:

- Understand the concept of classification in Machine Learning.
- Use the Iris Flower Dataset for classification.
- Load the dataset using Scikit-learn.
- Separate input features and target values.
- Split the dataset into training and testing data.
- Train a KNN classification model.
- Provide new flower measurements to the model.
- Predict the flower class.
- Understand how Machine Learning produces predictions.

---

## 🌸 Iris Flower Dataset

The Iris dataset contains measurements of Iris flowers.

The dataset includes four input features:

| Feature | Description |
|---|---|
| Sepal Length | Length of the flower sepal |
| Sepal Width | Width of the flower sepal |
| Petal Length | Length of the flower petal |
| Petal Width | Width of the flower petal |

The model predicts one of three flower classes:

| Target | Flower Class |
|---:|---|
| 0 | Setosa |
| 1 | Versicolor |
| 2 | Virginica |

---

## 🤖 Machine Learning Model

The **K-Nearest Neighbors (KNN)** algorithm was used for classification.

KNN predicts the class of a new data point by comparing it with nearby examples from the training dataset.

The model was created using:

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)
```
---

## 🔢 Features and Target

The Iris dataset was divided into input features and target values:

```python
X = iris.data
y = iris.target
```

Where:

* `X` contains the flower measurements.
* `y` contains the corresponding flower classes.

---

## 🔄 Train-Test Split

The dataset was divided into training and testing data:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

The split was:

```text
Total Dataset
     │
     ├── 80% → Training Data
     │
     └── 20% → Testing Data
```

The training data was used to train the model, while the testing data was reserved for evaluating the model.

---

## 🧠 Model Training

The KNN model was trained using the training dataset:

```python
model.fit(X_train, y_train)
```

During this stage, the model learned the relationship between flower measurements and their corresponding classes.

---

## 🔮 Flower Prediction

After training the model, a new flower was provided:

```python
new_flower = [[5.1, 3.5, 1.4, 0.2]]
```

The model was then used to predict its class:

```python
prediction = model.predict(new_flower)

predicted_class = iris.target_names[prediction[0]]
```

For the given measurements, the model predicts:

```text
Predicted Flower:
setosa
```

---

## 📊 Prediction Example

The input flower measurements were:

| Measurement  | Value |
| ------------ | ----: |
| Sepal Length |   5.1 |
| Sepal Width  |   3.5 |
| Petal Length |   1.4 |
| Petal Width  |   0.2 |

The resulting prediction was:

```text
Input Measurements
        ↓
KNN Classification Model
        ↓
Predicted Flower
        ↓
Setosa
```

---

## ⚙️ Methodology

```text
🚀 Start
   │
   ▼
🌸 Load Iris Dataset
   │
   ▼
📊 Separate Features & Target
   │
   ▼
✂️ Split Dataset
   │
   ▼
🤖 Create KNN Model
   │
   ▼
🧠 Train Model
   │
   ▼
🌱 Provide New Flower Measurements
   │
   ▼
🔮 Generate Prediction
   │
   ▼
📋 Display Flower Class
   │
   ▼
✅ Complete Day 15
```
---

## 🛠️ Tools & Technologies

* 🐍 Python 3.x
* 🤖 Scikit-learn
* 🌸 Iris Dataset
* 🧠 K-Nearest Neighbors
* 💻 Windows CMD
* 📝 Notepad
* 🔧 GitHub
* 📄 Markdown

---

## 💻 Development Environment

The Day 15 task was developed and executed using **Python on Windows**.

Scikit-learn was installed using:

```bash
py -m pip install scikit-learn
```

The program was executed using:

```bash
py iris_classification.py
```
---

## 📂 Project Structure

```text
Day-15-Iris-Classification
│
├── Iris-Classification.md
├── iris_classification.py
└── output.png
```
---

## 📸 Output

The program successfully loaded the Iris dataset, trained the KNN classification model, accepted new flower measurements, and generated a flower class prediction.

---

## 💡 Key Takeaways

* Iris Flower Classification is a simple Machine Learning classification problem.
* Scikit-learn provides ready-to-use datasets and Machine Learning algorithms.
* KNN can be used to classify new data based on nearby training examples.
* Input features describe the characteristics of the flower.
* The trained model can use new measurements to generate a prediction.
* Train-test splitting is an important part of the Machine Learning workflow.
* Machine Learning models can be used to classify previously unseen data.

---

## 📈 Learning Outcome

After completing Day 15, I gained practical experience in **Iris Flower Classification using Scikit-learn**.

I learned how to load the Iris dataset, prepare features and target values, split the dataset, train a KNN classification model, provide new flower measurements, and generate a prediction.

This task strengthened my understanding of Machine Learning classification and prepared me for the final testing and prediction task of Module 4.

---

## 📝 Conclusion

Day 15 successfully implemented an **Iris Flower Classification model using KNN and Scikit-learn**.

The practical implementation demonstrated how a trained Machine Learning model can use flower measurements to predict the corresponding Iris flower class.

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
