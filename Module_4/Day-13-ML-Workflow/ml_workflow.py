from sklearn.datasets import load_iris

# Step 1: Load Dataset
iris = load_iris()

print("===== MACHINE LEARNING WORKFLOW =====")

# Dataset information
print("\nDataset Loaded Successfully")
print("Number of Samples:", len(iris.data))
print("Number of Features:", len(iris.feature_names))

# Step 2: Display Features
print("\nFeatures:")
for feature in iris.feature_names:
    print("-", feature)

# Step 3: Display Target Classes
print("\nTarget Classes:")
for target in iris.target_names:
    print("-", target)

# Step 4: Display first sample
print("\nFirst Sample:")
print(iris.data[0])

# Step 5: Display corresponding target
print("\nFirst Sample Class:")
print(iris.target_names[iris.target[0]])

print("\nMachine Learning Workflow Introduction Completed!")