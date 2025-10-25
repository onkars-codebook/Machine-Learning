from sklearn.linear_model import LinearRegression

# Step 2: Prepare the data
# X now has two features: Temperature and Hours Open
X = [
    [20, 10],
    [25, 9],
    [30, 7],
    [35, 6]
]

# Target variable (cups sold)
y = [400, 350, 250, 200]

# Step 3: Create and train the model
model = LinearRegression()
model.fit(X, y)

# Step 4: Check learned parameters
print("Slope (coefficients):", model.coef_)   # m1, m2
print("Intercept (b):", model.intercept_)

# Step 5: Make a prediction
# Suppose tomorrow it's 28°C and you plan to open for 8 hours
prediction = model.predict([[3, 9]])
print(f"Predicted cups sold = {prediction[0]}")
