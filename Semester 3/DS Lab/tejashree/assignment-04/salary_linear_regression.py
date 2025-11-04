import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Generate synthetic data for 100 employees
np.random.seed(42)
years_experience = np.random.uniform(1, 20, 100)
# Assume salary = 3000 * years_experience + noise
salaries = 3000 * years_experience + np.random.normal(0, 5000, 100)

df = pd.DataFrame({'YearsExperience': years_experience, 'Salary': salaries})

# Split data into train and test sets
X = df[['YearsExperience']]
y = df['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Plot results
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line (Test)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs. Years of Experience (Linear Regression)')
plt.legend()
plt.show()

# Print model coefficients
print(f"Intercept: {model.intercept_:.2f}")
print(f"Coefficient: {model.coef_[0]:.2f}")
