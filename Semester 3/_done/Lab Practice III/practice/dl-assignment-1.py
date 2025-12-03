# Assignment 1: Simple Neural Network
# Write a Python program to build a simple neural network.

# Builds a 2-layer neural network
# Uses random dummy data just to demonstrate working
# Trains for a few epochs and prints accuracy

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# Create a simple Sequential model
model = keras.Sequential([
    layers.Input(shape=(4,)),
    layers.Dense(8, activation='relu'),
    layers.Dense(3, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Dummy data for training (4 features, 3 classes)
X = np.random.rand(100, 4)
y = np.random.randint(0, 3, 100)

# Train the model
model.fit(X, y, epochs=5, verbose=1)

# Evaluate
loss, acc = model.evaluate(X, y, verbose=0)
print(f"Training Accuracy: {acc:.2f}")

# Show some predictions
sample = X[:5]
preds = model.predict(sample)
print("Sample inputs:\n", sample)
print("Predicted classes:\n", preds.argmax(axis=1))
print("Actual classes:\n", y[:5])
