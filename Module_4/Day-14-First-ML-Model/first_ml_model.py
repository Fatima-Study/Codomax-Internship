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