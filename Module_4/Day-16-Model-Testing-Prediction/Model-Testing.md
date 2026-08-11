# 🚀 Module 4 — Codomax Digital Solutions Internship

# 📊 Day 16 — Model Testing & Prediction 🤖

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=for-the-badge)
![Model Testing](https://img.shields.io/badge/Topic-Model%20Testing-purple?style=for-the-badge)
![Prediction](https://img.shields.io/badge/Task-Prediction-green?style=for-the-badge)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

---

<p align="center">
  <b>Codomax Digital Solutions — AI & ML Internship</b>
</p>

---

## 📌 Overview

Day 16 is the final practical task of **Module 4 — Machine Learning Fundamentals** in the Codomax Digital Solutions Internship.

The main focus of this task was to **test a trained Machine Learning model and understand its prediction results**.

The Iris Flower Dataset was used with a **K-Nearest Neighbors (KNN)** classification model. The trained model was evaluated using testing data, and its predictions were compared with the actual values.

---

## 🎯 Objective

The objectives of Day 16 were to:

- Test a trained Machine Learning model.
- Generate predictions using testing data.
- Compare actual and predicted values.
- Calculate model accuracy.
- Generate a classification report.
- Generate a confusion matrix.
- Understand Machine Learning model evaluation.
- Analyze the final prediction results.

---

## 🌸 Dataset Used

The **Iris Flower Dataset** provided by Scikit-learn was used for testing and evaluation.

The dataset contains:

- 150 total samples.
- 4 input features.
- 3 target classes.

### Input Features

| Feature | Description |
|---|---|
| Sepal Length | Length of the sepal |
| Sepal Width | Width of the sepal |
| Petal Length | Length of the petal |
| Petal Width | Width of the petal |

### Target Classes

| Target Value | Flower |
|---:|---|
| 0  | Setosa |
| 1  | Versicolor |
| 2  | Virginica |

---

## 🤖 Machine Learning Model

The **K-Nearest Neighbors (KNN)** algorithm was used for classification.

The model was created using:

```python
model = KNeighborsClassifier(n_neighbors=3)
```
---

## 🔄 Training and Testing Data

The dataset was divided into training and testing sets using:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

The dataset was divided as:

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

---

## 🔮 Generating Predictions

After training the model, predictions were generated using the testing dataset:

```python
predictions = model.predict(X_test)
```

The predictions were then compared with the actual target values.

---

## 📊 Actual vs Predicted Values

The actual values were displayed using:

```python
print(y_test)
```

The predicted values were displayed using:

```python
print(predictions)
```

This comparison helps determine how accurately the model classified the testing samples.

```text
Actual Values
      ↓
Compare
      ↑
Predicted Values
      ↓
Evaluate Model
```

---

## 📈 Model Accuracy

The accuracy of the model was calculated using:

```python
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)
```

Accuracy represents the proportion of correctly classified samples out of all testing samples.

The actual accuracy value should be taken directly from the program output.

---

## 📋 Classification Report

A classification report was generated using:

```python
print(classification_report(
    y_test,
    predictions,
    target_names=iris.target_names
))
```

The classification report provides important evaluation metrics including:

* Precision
* Recall
* F1-score
* Support

These metrics provide a more detailed understanding of the model's classification performance.

---

## 🔲 Confusion Matrix

A confusion matrix was generated using:

```python
print(confusion_matrix(y_test, predictions))
```

The confusion matrix shows how many samples were correctly and incorrectly classified for each Iris flower class.

It helps identify which classes the model predicts correctly and where classification errors may occur.

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
✂️ Split Training & Testing Data
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
📊 Compare Actual & Predicted Values
   │
   ▼
📈 Calculate Accuracy
   │
   ▼
📋 Generate Classification Report
   │
   ▼
🔲 Generate Confusion Matrix
   │
   ▼
✅ Evaluate Model
```
---

## 🛠️ Tools & Technologies

* Python 3.x
* Scikit-learn
* Iris Dataset
* K-Nearest Neighbors
* Windows CMD
* Notepad
* GitHub
* Markdown

---

## 💻 Development Environment

The Day 16 task was developed and executed using **Python on Windows**.

Scikit-learn was installed using:

```bash
py -m pip install scikit-learn
```

The program was executed using:

```bash
py model_testing.py
```
---

## 📂 Project Structure

```text
Day-16-Model-Testing
│
├── model_testing.py
├── Model-Testing.md
└── output.png 
```

---

## 📸 Output

The program successfully tested the trained KNN Machine Learning model.

The output includes:

* Total dataset samples.
* Training samples.
* Testing samples.
* Actual target values.
* Predicted target values.
* Model accuracy.
* Classification report.
* Confusion matrix.
* 
---

## 💡 Key Takeaways

* Testing is an important stage of the Machine Learning workflow.
* Testing data helps evaluate model performance on unseen data.
* Actual and predicted values can be compared to identify correct predictions.
* Accuracy provides a simple measure of classification performance.
* A classification report provides detailed evaluation metrics.
* A confusion matrix helps understand classification results for each class.
* Model evaluation helps determine whether a trained model performs effectively.

---

## 📈 Learning Outcome

After completing Day 16, I gained practical experience in **testing and evaluating a Machine Learning classification model**.

I learned how to generate predictions, compare actual and predicted values, calculate model accuracy, generate a classification report, and analyze a confusion matrix.

This task completed the practical **Machine Learning Fundamentals workflow** covered throughout Module 4.

---

## 📝 Conclusion

Day 16 successfully completed the **model testing and prediction** stage of the internship task.

The KNN model was tested using the Iris dataset, and its prediction performance was evaluated using accuracy, classification metrics, and a confusion matrix.

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
