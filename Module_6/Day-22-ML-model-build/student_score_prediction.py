import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

print("=" * 55)
print("       STUDENT SCORE PREDICTION")
print("       MACHINE LEARNING MODEL")
print("=" * 55)

# Load dataset
df = pd.read_csv("student_data.csv")

print("\nDataset:")
print(df)

# Features
X = df[["Hours_Studied", "Attendance", "Previous_Score"]]

# Target
y = df["Final_Score"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# Create Machine Learning model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# Make predictions
predictions = model.predict(X_test)

print("\nActual Scores:")
print(y_test.values)

print("\nPredicted Scores:")
print(predictions.round(2))

# Evaluate model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Evaluation:")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))

# Sample prediction
sample = pd.DataFrame({
    "Hours_Studied": [7],
    "Attendance": [90],
    "Previous_Score": [75]
})

sample_prediction = model.predict(sample)

print("\nSample Prediction:")
print("Hours Studied: 7")
print("Attendance: 90%")
print("Previous Score: 75")
print("Predicted Final Score:", round(sample_prediction[0], 2))

print("\n" + "=" * 55)
print("       DAY 22 COMPLETED SUCCESSFULLY")
print("=" * 55)