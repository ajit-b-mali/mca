# Assignment 4: Predict Salary using Simple Linear Regression

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Create sample data (100 employees)
np.random.seed(42)
experience = np.random.uniform(1, 10, 100)
salary = 30000 + (experience * 8000) + np.random.normal(0, 5000, 100)

# Convert to DataFrame
df = pd.DataFrame({'Experience': experience, 'Salary': salary})

# Split features and target
X = df[['Experience']]
y = df['Salary']

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Display results
print("Model Coefficient (Slope):", model.coef_[0])
print("Model Intercept:", model.intercept_)

# Plot
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary Prediction using Linear Regression')
plt.legend()
plt.show()
