from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Iris dataset
iris = load_iris()

# Features and target
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train model
model.fit(X_train, y_train)

# Generate predictions
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("===== MODEL TESTING & PREDICTION =====")

print("\nTotal Samples:", len(X))
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

print("\nModel: K-Nearest Neighbors")

print("\nActual Values:")
print(y_test)

print("\nPredicted Values:")
print(predictions)

print("\nModel Accuracy:")
print(accuracy)

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    target_names=iris.target_names
))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nModel Testing Completed Successfully!")