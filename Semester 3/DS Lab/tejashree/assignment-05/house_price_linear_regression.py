import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Generate synthetic data for house prices
np.random.seed(42)
sqft = np.random.uniform(500, 3500, 100)
# Assume price = 150 * sqft + noise
prices = 150 * sqft + np.random.normal(0, 50000, 100)

df = pd.DataFrame({'SquareFootage': sqft, 'Price': prices})

# Split data into train and test sets
X = df[['SquareFootage']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Plot results
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line (Test)')
plt.xlabel('Square Footage')
plt.ylabel('House Price')
plt.title('House Price vs. Square Footage (Linear Regression)')
plt.legend()
plt.show()

# Calculate MSE and R^2 score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R^2 Score: {r2:.4f}")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Coefficient: {model.coef_[0]:.2f}")
