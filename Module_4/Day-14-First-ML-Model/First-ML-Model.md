# 🚀 Module 4 — Codomax Digital Solutions Internship

# Day 14 — Train Your First Machine Learning Model

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-orange?style=for-the-badge)
![Model](https://img.shields.io/badge/Model-KNN-purple?style=for-the-badge)
![Dataset](https://img.shields.io/badge/Dataset-Iris-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

---

<p align="center">
  <b>Codomax Digital Solutions — AI & ML Internship</b>
</p>

---

## 📌 Overview

Day 14 is the second practical task of **Module 4 — Machine Learning Fundamentals** in the Codomax Digital Solutions Internship.

The main focus of this task was to train the **first Machine Learning model using Scikit-learn**.

The **Iris Flower Dataset** was used as a beginner-friendly dataset. The dataset was divided into training and testing sets, and a **K-Nearest Neighbors (KNN)** classification model was trained to predict Iris flower classes.

---

## 🎯 Objective

The objectives of Day 14 were to:

- Train a first Machine Learning model using Scikit-learn.
- Use the Iris Flower Dataset for classification.
- Separate input features and target values.
- Split the dataset into training and testing data.
- Create a K-Nearest Neighbors classification model.
- Train the model using training data.
- Generate predictions using testing data.
- Calculate the model accuracy.
- Understand the basic process of Machine Learning model training.

---

## 🌸 Dataset Used

The **Iris Flower Dataset** was used for this task.

The dataset contains:

- **150 samples**
- **4 input features**
- **3 target classes**

### Input Features

| Feature | Description |
|---|---|
| Sepal Length | Length of the sepal |
| Sepal Width | Width of the sepal |
| Petal Length | Length of the petal |
| Petal Width | Width of the petal |

### Target Classes

| Class | Target Value |
|---|---:|
| Setosa | 0 |
| Versicolor | 1 |
| Virginica | 2 |

---

## 🧠 Machine Learning Model

The **K-Nearest Neighbors (KNN)** algorithm was used for classification.

KNN predicts the class of a new data point by comparing it with nearby data points in the training dataset.

For this task, the model was created with:

```python
model = KNeighborsClassifier(n_neighbors=3)
```
---

## 🔢 Features and Target

The dataset was divided into:

```python
X = iris.data
y = iris.target
```

Where:

* `X` represents the input features.
* `y` represents the target classes.

---

## 🔄 Train-Test Split

The dataset was divided into training and testing data using `train_test_split()`.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

The dataset was divided as follows:

```text
Total Dataset
     │
     ├── 80% → Training Data
     │
     └── 20% → Testing Data
```

With 150 samples:

```text
Training Samples → 120
Testing Samples  → 30
```

Training data was used to teach the model, while testing data was used to evaluate its predictions.

---

## 🤖 Model Training

The KNN model was trained using:

```python
model.fit(X_train, y_train)
```

During training, the model learned patterns from the training dataset.

---

## 🔮 Making Predictions

After training, predictions were generated using the testing data:

```python
predictions = model.predict(X_test)
```

The predicted values were then compared with the actual target values.

---

## 📊 Model Evaluation

The model accuracy was calculated using `accuracy_score()`:

```python
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)
```

Accuracy represents the proportion of correct predictions made by the model on the testing dataset.

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
   ├── 80% Training Data
   │
   └── 20% Testing Data
   │
   ▼
🤖 Create KNN Model
   │
   ▼
🧠 Train Model
   │
   ▼
🔮 Generate Predictions
   │
   ▼
📈 Calculate Accuracy
   │
   ▼
✅ Complete Day 14
```

---

## 💻 Python Implementation

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()

# Features and target
X = iris.data
y = iris.target

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Machine Learning model
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("===== FIRST MACHINE LEARNING MODEL =====")

print("Total Samples:", len(X))
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

print("\nModel: K-Nearest Neighbors")

print("\nPredictions:")
print(predictions)

print("\nActual Values:")
print(y_test)

print("\nModel Accuracy:", accuracy)

print("\nMachine Learning Model Trained Successfully!")
```

---

## 🛠️ Tools & Technologies

* 🐍 Python 3.x
* 🤖 Scikit-learn
* 🌸 Iris Dataset
* 💻 Windows CMD
* 📝 Notepad
* 🔧 GitHub
* 📄 Markdown

---

## 💻 Development Environment

The Day 14 project was developed and executed using **Python on Windows**.

Scikit-learn was installed using:

```bash
py -m pip install scikit-learn
```

The program was executed using:

```bash
py first_ml_model.py
```
---

## 📂 Project Structure

```text
Day-14-First-ML-Model
│
├── ML-Model.md
├── first_ml_model.py
└── output.png
```

---

## 📸 Output

The program successfully:

* Loaded the Iris dataset.
* Divided the dataset into training and testing data.
* Created a KNN classification model.
* Trained the model.
* Generated predictions.
* Compared predictions with actual values.
* Calculated model accuracy.

---

## 💡 Key Takeaways

* Scikit-learn provides simple tools for Machine Learning.
* The Iris dataset is suitable for beginner-level classification.
* Features are used as inputs for the Machine Learning model.
* Target values represent the classes to be predicted.
* Training data is used to train the model.
* Testing data is used to evaluate the model.
* KNN can be used for classification tasks.
* Accuracy can be used to measure prediction performance.

---

## 📈 Learning Outcome

After completing Day 14, I gained practical experience in **training a Machine Learning classification model using Scikit-learn**.

I learned how to load a dataset, separate features and targets, split data into training and testing sets, create a KNN model, train the model, generate predictions, and calculate model accuracy.

This task provided practical experience with the Machine Learning training process and prepared me for further classification and prediction tasks.

---

## 📝 Conclusion

Day 14 successfully completed the internship requirement of **training a first Machine Learning model using Scikit-learn**.

The Iris dataset and KNN algorithm provided a simple practical example of how a Machine Learning model can learn from training data and make predictions on testing data.

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
