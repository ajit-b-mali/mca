# Assignment 4: Anomaly Detection Using Autoencoder
# Write a program for Anomaly Detection Using Autoencoder.

# # Uses Autoencoder to reconstruct MNIST images.
# # Reconstruction error (MSE) used to detect anomalies.
# # Prints number of anomalies detected.

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

# # Load dataset (MNIST digits)
(x_train, _), (x_test, _) = keras.datasets.mnist.load_data()

# Normalize and flatten
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape(len(x_train), -1)
x_test = x_test.reshape(len(x_test), -1)

# Build Autoencoder model
input_dim = x_train.shape[1]
encoding_dim = 64

input_layer = keras.Input(shape=(input_dim,))
encoded = layers.Dense(encoding_dim, activation='relu')(input_layer)
decoded = layers.Dense(input_dim, activation='sigmoid')(encoded)

autoencoder = keras.Model(input_layer, decoded)
autoencoder.compile(optimizer='adam', loss='mse')

# Train Autoencoder
autoencoder.fit(x_train, x_train, epochs=5, batch_size=256, shuffle=True, verbose=1)

# Compute reconstruction error
reconstructions = autoencoder.predict(x_test)
mse = np.mean(np.power(x_test - reconstructions, 2), axis=1)

# Set anomaly threshold
threshold = np.mean(mse) + 3*np.std(mse)

# Detect anomalies
anomalies = mse > threshold
print(f"Number of anomalies detected: {np.sum(anomalies)}")

# Show original vs reconstructed for first 5 images
for i in range(5):
    plt.subplot(1,2,1)
    plt.title("Original")
    plt.imshow(x_test[i].reshape(28,28), cmap='gray')
    plt.subplot(1,2,2)
    plt.title("Reconstructed")
    plt.imshow(reconstructions[i].reshape(28,28), cmap='gray')
    plt.show()

