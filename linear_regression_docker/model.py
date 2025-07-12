# model.py

from sklearn.linear_model import LinearRegression
import numpy as np

# Sample training data (X: input, y: target)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 6, 9, 12, 15])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict a new value
new_data = np.array([[6]])
prediction = model.predict(new_data)

# Print the prediction
print(f"Prediction for input {new_data.flatten()[0]}: {prediction[0]}")
