from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load Iris dataset
iris = load_iris()

# Features and target
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

print("===== IRIS FLOWER CLASSIFICATION =====")

# Display available classes
print("\nFlower Classes:")
for i, name in enumerate(iris.target_names):
    print(i, "=", name)

# New flower measurements
new_flower = [[5.1, 3.5, 1.4, 0.2]]

# Predict flower
prediction = model.predict(new_flower)

# Display prediction
predicted_class = iris.target_names[prediction[0]]

print("\nNew Flower Measurements:")
print(new_flower[0])

print("\nPredicted Flower:")
print(predicted_class)

print("\nIris Flower Classification Completed Successfully!")