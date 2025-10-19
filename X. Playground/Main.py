from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
# Step 1: Load the Iris dataset
iris = load_iris()

# Step 2: Separate features and labels
X = iris.data       # features (sepal length, width, petal length, petal width)
print(X)
y = iris.target     # labels (species: 0,1,2)

# Step 3: Split into training and testing data
# test_size=0.2 means 20% of data will be for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
