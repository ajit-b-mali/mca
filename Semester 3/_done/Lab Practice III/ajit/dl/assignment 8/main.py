import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Deep Learning Assignment 4: Write a program for Anomaly Detection Using Autoencoder

import matplotlib.pyplot as plt

# Generate synthetic normal data
np.random.seed(42)
normal_data = np.random.normal(loc=0.0, scale=1.0, size=(1000, 20))

# Generate synthetic anomalous data
anomaly_data = np.random.normal(loc=4.0, scale=1.0, size=(50, 20))

# Combine and create labels
X = np.vstack([normal_data, anomaly_data])
y = np.hstack([np.zeros(len(normal_data)), np.ones(len(anomaly_data))])

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build Autoencoder
input_dim = X_train.shape[1]
encoding_dim = 10

input_layer = Input(shape=(input_dim,))
encoder = Dense(encoding_dim, activation="relu")(input_layer)
decoder = Dense(input_dim, activation="linear")(encoder)
autoencoder = Model(inputs=input_layer, outputs=decoder)

autoencoder.compile(optimizer='adam', loss='mse')

# Train only on normal data
autoencoder.fit(X_train[y_train == 0], X_train[y_train == 0],
                epochs=50, batch_size=32, shuffle=True, validation_split=0.1, verbose=0)

# Compute reconstruction error
reconstructions = autoencoder.predict(X_test)
mse = np.mean(np.power(X_test - reconstructions, 2), axis=1)

# Set threshold for anomaly detection
threshold = np.percentile(mse, 95)

# Predict anomalies
y_pred = (mse > threshold).astype(int)

# Output results

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Plot reconstruction error
plt.figure(figsize=(8,4))
plt.hist(mse[y_test == 0], bins=30, alpha=0.6, label='Normal')
plt.hist(mse[y_test == 1], bins=30, alpha=0.6, label='Anomaly')
plt.axvline(threshold, color='r', linestyle='--', label='Threshold')
plt.xlabel("Reconstruction error")
plt.ylabel("Count")
plt.legend()
plt.title("Reconstruction Error Histogram")
plt.show()