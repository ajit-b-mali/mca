# Assignment 6: LSTM Network Example

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

# Create simple time-series dataset (e.g., sine wave)
x = np.linspace(0, 100, 200)
y = np.sin(x)

# Prepare data for LSTM (use previous 5 values to predict next)
X, Y = [], []
for i in range(len(y) - 5):
    X.append(y[i:i+5])
    Y.append(y[i+5])
X = np.array(X)
Y = np.array(Y)

# Reshape for LSTM [samples, timesteps, features]
X = X.reshape((X.shape[0], X.shape[1], 1))

# Build LSTM model
model = Sequential([
    LSTM(50, activation='tanh', input_shape=(5, 1)),
    Dense(1)
])

# Compile and train
model.compile(optimizer='adam', loss='mse')
model.fit(X, Y, epochs=50, verbose=0)

# Predict
y_pred = model.predict(X, verbose=0)

# Plot actual vs predicted
plt.plot(Y, label='Actual')
plt.plot(y_pred, label='Predicted', color='red')
plt.title('LSTM Prediction on Sine Wave Data')
plt.legend()
plt.show()
