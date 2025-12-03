# Assignment 5: House Price Prediction using Simple Linear Regression

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Create sample dataset
np.random.seed(42)
sqft = np.random.uniform(500, 3500, 100)  # Square footage
price = 50000 + (sqft * 120) + np.random.normal(0, 20000, 100)  # House price with noise

# Convert to DataFrame
df = pd.DataFrame({'SquareFootage': sqft, 'Price': price})

# Split features and target
X = df[['SquareFootage']]
y = df['Price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Evaluate
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("Mean Squared Error:", round(mse, 2))
print("R² Score:", round(r2, 2))

# Plot regression
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.xlabel('Square Footage')
plt.ylabel('House Price')
plt.title('House Price Prediction using Linear Regression')
plt.legend()
plt.show()
