# Assignment 3: Image Classification Model
# Write a program for Building an Image Classification model.

# Dataset: CIFAR-10 (10 image classes)
# Model: Simple CNN
# Output: Accuracy printed after training

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

# Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

# Normalize images
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Build simple CNN model
model = keras.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)),
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
class_names = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']
for i in range(5):
    plt.imshow(sample_images[i])
    plt.title(f"Predicted: {class_names[preds[i].argmax()]}, Actual: {class_names[y_test[i][0]]}")
    plt.show()

