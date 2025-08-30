# Assignment 6: Design and implement a CNN model to classify an image dataset.
# We will use the Keras library to build a CNN to classify images from the
# CIFAR-10 dataset.

import tensorflow as tf
from tensorflow import keras
from keras import layers, models
import numpy as np
import matplotlib.pyplot as plt

print("TensorFlow version:", tf.__version__)

# --- 1. Load and Prepare the CIFAR-10 Data ---

# CIFAR-10 is a dataset of 60,000 32x32 color images in 10 classes,
# with 6,000 images per class.
cifar10 = keras.datasets.cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalize pixel values to be between 0 and 1.
# This is a crucial step for helping the training process converge faster.
x_train, x_test = x_train / 255.0, x_test / 255.0

# Define the names for the 10 classes
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# --- 2. Visualize the Data ---
# It's always a good idea to look at some of the images to understand the data.
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i])
    # The y_train labels are arrays, so we need to access the first element
    plt.xlabel(class_names[y_train[i][0]])
plt.suptitle("A Sample of the CIFAR-10 Training Data")
plt.show()


# --- 3. Build the Convolutional Neural Network (CNN) Model ---

model = models.Sequential()

# === The Convolutional Base ===
# Layer 1: First Convolutional Block
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))

# Layer 2: Second Convolutional Block
# We increase the number of filters to 64. This allows the model to learn more complex features.
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Layer 3: Third Convolutional Block
model.add(layers.Conv2D(64, (3, 3), activation='relu'))


# === The Dense Classifier Head ===
# Before feeding the data to the Dense layers, we must flatten the 3D output
# from the convolutional base into a 1D vector.
model.add(layers.Flatten())

# A dense layer for classification. 64 neurons is a good starting point.
model.add(layers.Dense(64, activation='relu'))

# The final output layer. It must have 10 neurons (one for each class) and
# a 'softmax' activation to produce a probability distribution.
model.add(layers.Dense(10, activation='softmax'))

# Print a summary of the model.
print("Model Architecture:")
model.summary()


# --- 4. Compile the Model ---

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# --- 5. Train the Model ---

print("\nStarting model training...")
# We train for 10 epochs. For better results, you could increase this number.
# We also pass the test data as validation_data to monitor the model's
# performance on unseen data at the end of each epoch.
history = model.fit(x_train, y_train, epochs=10,
                    validation_data=(x_test, y_test))
print("Model training finished.")


# --- 6. Evaluate the Model ---

print("\nEvaluating model on the test dataset...")
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"\nTest accuracy: {test_acc*100:.2f}%")


# --- 7. Plot Training History ---

# Plotting the training and validation accuracy/loss can give us insights
# into whether the model is overfitting.
plt.figure(figsize=(12, 4))

# Plot training & validation accuracy values
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

# Plot training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

plt.suptitle("Model Training History")
plt.show()
