# 🚀 Module 4 — Codomax Digital Solutions Internship

# 🤖 Day 13 — Machine Learning Workflow

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=for-the-badge)](https://scikit-learn.org/)
[![Machine Learning](https://img.shields.io/badge/Topic-Machine%20Learning-blue?style=for-the-badge)](https://scikit-learn.org/stable/getting_started.html)
[![Iris Dataset](https://img.shields.io/badge/Dataset-Iris-green?style=for-the-badge)](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

---

<p align="center">
  <b>Codomax Digital Solutions — AI & ML Internship</b>
</p>

---

## 📌 Overview

Day 13 is the first practical task of **Module 4 — Machine Learning Fundamentals** in the Codomax Digital Solutions Internship.

The main focus of this task was to understand the **basic Machine Learning workflow** and learn how a dataset is prepared before training and testing a Machine Learning model.

The **Iris Flower Dataset** available through Scikit-learn was used as a beginner-friendly dataset. The dataset was loaded and explored to understand its samples, features, and target classes.

---

## 🎯 Objective

The objectives of Day 13 were to:

- Understand the basic Machine Learning workflow.
- Load a beginner-friendly dataset using Scikit-learn.
- Explore the dataset and its basic information.
- Understand features and target classes.
- Understand the difference between training and testing data.
- Understand the basic process of making predictions.
- Understand how Machine Learning model performance is evaluated.

---

## 🤖 What is Machine Learning?

Machine Learning is a field of Artificial Intelligence in which computers learn patterns from data and use those patterns to make predictions or decisions.

For this task, the model will eventually learn from flower measurements and predict the type of Iris flower.

---

## 🌸 Dataset Used

The **Iris Flower Dataset** was used for this task.

The dataset contains:

- **150 samples**
- **4 features**
- **3 target classes**

### Features

| Feature | Description |
|---|---|
| Sepal Length | Length of the flower sepal |
| Sepal Width | Width of the flower sepal |
| Petal Length | Length of the flower petal |
| Petal Width | Width of the flower petal |

### Target Classes

| Class | Description |
|---|---|
| Setosa | Iris Setosa flower |
| Versicolor | Iris Versicolor flower |
| Virginica | Iris Virginica flower |

---

## 🔄 Machine Learning Workflow

The basic Machine Learning workflow studied in Day 13 is:

```text
Dataset
   │
   ▼
Load Data
   │
   ▼
Explore Data
   │
   ▼
Prepare Data
   │
   ▼
Split Data
   │
   ▼
Train Model
   │
   ▼
Test Model
   │
   ▼
Make Predictions
   │
   ▼
Evaluate Results
```
---

## 📥 Loading the Dataset

The Iris dataset was loaded using Scikit-learn:

```python
from sklearn.datasets import load_iris

iris = load_iris()
```

The dataset was successfully loaded into Python.

---

## 🔍 Dataset Exploration

Basic information about the dataset was displayed using Python.

```python
print("Number of Samples:", len(iris.data))
print("Number of Features:", len(iris.feature_names))
```

The program also displayed the available features:

```python
for feature in iris.feature_names:
    print("-", feature)
```

The target classes were displayed using:

```python
for target in iris.target_names:
    print("-", target)
```

---

## 📊 First Sample

The first sample from the dataset was displayed:

```python
print(iris.data[0])
```

The corresponding target class was also identified:

```python
print(iris.target_names[iris.target[0]])
```

This helped demonstrate how input features are associated with a target class.

---

## ⚙️ Workflow Steps

### 1. Load Dataset

The dataset is loaded into the Python environment.

### 2. Explore Dataset

The dataset is examined to understand its features, samples, and target classes.

### 3. Prepare Data

The input features and target values are prepared for Machine Learning.

```text
X = Features
y = Target
```

### 4. Split Data

The dataset is divided into training and testing data.

```text
Training Data → Used to learn patterns
Testing Data  → Used to evaluate the model
```

### 5. Train Model

A Machine Learning algorithm learns patterns from the training data.

### 6. Test Model

The trained model is tested using data that was not used during training.

### 7. Make Predictions

The model predicts the target class for new or unseen data.

### 8. Evaluate Results

The predictions are compared with the actual target values to understand model performance.

---

## 💻 Practical Implementation

The following Python program was created for understanding the initial Machine Learning workflow:

```python
from sklearn.datasets import load_iris

# Step 1: Load Dataset
iris = load_iris()

print("===== MACHINE LEARNING WORKFLOW =====")

# Dataset information
print("\nDataset Loaded Successfully")
print("Number of Samples:", len(iris.data))
print("Number of Features:", len(iris.feature_names))

# Display features
print("\nFeatures:")
for feature in iris.feature_names:
    print("-", feature)

# Display target classes
print("\nTarget Classes:")
for target in iris.target_names:
    print("-", target)

# Display first sample
print("\nFirst Sample:")
print(iris.data[0])

# Display corresponding target
print("\nFirst Sample Class:")
print(iris.target_names[iris.target[0]])

print("\nMachine Learning Workflow Introduction Completed!")
```

---

## 🛠️ Tools & Technologies

* Python 3.x
* Scikit-learn
* Iris Dataset
* Windows CMD
* Notepad
* GitHub
* Markdown

---

## 💻 Development Environment

The Day 13 task was developed and executed in a **Windows environment** using Python.

Scikit-learn was installed using:

```bash
py -m pip install scikit-learn
```

The Python program was executed using:

```bash
py ml_workflow.py
```

---

## 📂 Project Structure

```text
Day-13-ML-Workflow
│
├── ml_workflow.py
├── output.png
└── ML-Workflow.md
```
---

## 📸 Output

The program successfully loaded the Iris dataset and displayed its basic information.

The output demonstrates:

* Dataset loaded successfully
* Number of samples
* Number of features
* Dataset features
* Target classes
* First dataset sample
* Corresponding flower class

---

## 💡 Key Takeaways

* Machine Learning follows a structured workflow from data preparation to evaluation.
* A dataset contains input features and target values.
* Features are used by the model to learn patterns.
* Target values represent the expected prediction.
* Training data is used to teach the model.
* Testing data is used to evaluate the trained model.
* Predictions are generated from learned patterns.
* Evaluation helps determine how well a model performs.

---

## 📈 Learning Outcome

After completing Day 13, I gained a basic practical understanding of the **Machine Learning workflow**.

I learned how to load and explore the Iris dataset using Scikit-learn, identify features and target classes, and understand the steps involved in preparing, training, testing, predicting, and evaluating a Machine Learning model.

This task provided the foundation for training my first Machine Learning model in the upcoming days.

---

## 📝 Conclusion

Day 13 successfully introduced the fundamental **Machine Learning workflow** using the Iris Flower Dataset.

The practical implementation helped build an understanding of how data moves through different stages of a Machine Learning project, preparing for the next task of training and testing a Machine Learning model.

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
