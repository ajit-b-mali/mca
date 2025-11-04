# Assignment 5: Feed Forward Neural Network

import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

# Create sample dataset (house size vs price example)
X = np.linspace(500, 3500, 100)
y = 50000 + (X * 120) + np.random.normal(0, 20000, 100)

# Normalize data
X = (X - X.min()) / (X.max() - X.min())
y = (y - y.min()) / (y.max() - y.min())

# Build feed forward network
model = keras.Sequential([
    layers.Dense(10, activation='relu', input_shape=(1,)),
    layers.Dense(8, activation='relu'),
    layers.Dense(1)
])

# Compile model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train model
history = model.fit(X, y, epochs=100, verbose=0)

# Predict
y_pred = model.predict(X)

# Plot results
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_pred, color='red', label='Predicted')
plt.title('Feed Forward Neural Network Prediction')
plt.xlabel('Normalized Input')
plt.ylabel('Normalized Output')
plt.legend()
plt.show()
