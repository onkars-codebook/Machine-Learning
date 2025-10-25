from sklearn.linear_model import LinearRegression

# Step 2: Prepare the data
X = [[20], [25], [30], [35]]  # Temperature
y = [40, 35, 25, 20]          # Tea Cups sold

# Step 3: Create and train the model
model = LinearRegression()
model.fit(X, y)
# Here’s the data (X) and the correct answers (y). Learn the relationship between them.
#here under the fit method finding the slope(m) and intercept(b) and then finding an next thing.

# Step 4: Get slope (m) and intercept (b)
m = model.coef_[0]         # slope
b = model.intercept_       # intercept

print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# Step 5: Make a prediction;
temp = 9
predicted_cups = model.predict([[temp]])[0]
print(f"At {temp}°C, predicted cups sold = {predicted_cups}")
