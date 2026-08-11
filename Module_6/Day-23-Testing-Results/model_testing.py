import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

print("=" * 60)
print("       STUDENT SCORE PREDICTION")
print("       MODEL TESTING & RESULTS")
print("=" * 60)

# Load dataset
df = pd.read_csv("student_data.csv")

# Features and target
X = df[["Hours_Studied", "Attendance", "Previous_Score"]]
y = df["Final_Score"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Results
results = pd.DataFrame({
    "Actual Score": y_test.values,
    "Predicted Score": predictions.round(2)
})

print("\nActual vs Predicted Scores:")
print(results)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Performance:")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))

# Sample predictions
samples = pd.DataFrame({
    "Hours_Studied": [5, 7, 9],
    "Attendance": [85, 90, 95],
    "Previous_Score": [70, 75, 82]
})

sample_predictions = model.predict(samples)

print("\nSample Predictions:")

for i, score in enumerate(sample_predictions):
    print(
        f"Student {i + 1}: "
        f"Predicted Final Score = {score:.2f}"
    )

print("\n" + "=" * 60)
print("       DAY 23 COMPLETED SUCCESSFULLY")
print("=" * 60)