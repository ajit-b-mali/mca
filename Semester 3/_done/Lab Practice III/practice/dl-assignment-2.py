# Assignment 2: Simple CNN for Image Classification
# Design and implement a CNN model to classify image dataset.

# Uses MNIST dataset (built-in image dataset)
# Basic CNN (Conv + Pool + Dense layers)
# Trains quickly and shows accuracy

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Preprocess data
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0

# Build CNN model
model = keras.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train
model.fit(x_train, y_train, epochs=3, batch_size=64, verbose=1)

# Evaluate
loss, acc = model.evaluate(x_test, y_test, verbose=0)
print(f"Test Accuracy: {acc:.2f}")

# Show sample predictions
sample_images = x_test[:5]
preds = model.predict(sample_images)
for i in range(5):
    plt.imshow(sample_images[i].reshape(28,28), cmap='gray')
    plt.title(f"Predicted: {preds[i].argmax()}, Actual: {y_test[i]}")
    plt.show()
