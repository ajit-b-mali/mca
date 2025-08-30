# Assignment 5: Python program to build a simple neural network.
# We will use the Keras library (part of TensorFlow) for this task.
# This program will build a neural network to classify handwritten digits
# from the famous MNIST dataset.

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

print("TensorFlow version:", tf.__version__)

# --- 1. Load and Preprocess the Data ---

# The MNIST dataset is included in Keras. It contains 60,000 training images
# and 10,000 testing images of handwritten digits (0-9).
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# The images are 28x28 pixel grayscale images. Pixel values range from 0 to 255.
# We need to normalize these values to be between 0 and 1.
# Normalization helps the network train more efficiently.
x_train, x_test = x_train / 255.0, x_test / 255.0

# --- 2. Build the Neural Network Model ---

# We will use a `Sequential` model, which is a linear stack of layers.
# This is the simplest type of model for a feed-forward neural network.
model = keras.models.Sequential([
    # This layer flattens the 28x28 pixel image into a 1D array of 784 pixels.
    # It serves as the input layer to our network.
    keras.layers.Flatten(input_shape=(28, 28)),

    # This is our first hidden layer. It's a `Dense` layer, meaning every neuron
    # in this layer is connected to every neuron in the previous layer.
    # It has 128 neurons and uses the 'relu' (Rectified Linear Unit) activation function.
    keras.layers.Dense(128, activation='relu'),

    # This is an optional Dropout layer. It randomly sets 20% of the input units
    # to 0 at each update during training time, which helps prevent overfitting.
    keras.layers.Dropout(0.2),

    # This is the output layer. It is also a `Dense` layer.
    # It must have 10 neurons, one for each class (digits 0 through 9).
    # The 'softmax' activation function is used to output a probability distribution
    # over the 10 classes. The neuron with the highest probability is the model's prediction.
    keras.layers.Dense(10, activation='softmax')
])

# --- 3. Compile the Model ---

# Before training, we need to configure the learning process. This is done
# with the `compile` method.
model.compile(
    # The 'adam' optimizer is an efficient and popular choice for gradient descent.
    optimizer='adam',
    # The loss function measures how inaccurate the model is during training.
    # 'sparse_categorical_crossentropy' is used for multi-class classification
    # when the labels are integers (like 0, 1, 2...).
    loss='sparse_categorical_crossentropy',
    # We want to monitor the 'accuracy' of the model during training.
    metrics=['accuracy']
)

# We can print a summary of the model to see its architecture.
print("Model Architecture:")
model.summary()

# --- 4. Train the Model ---

print("\nStarting model training...")
# The `fit` method trains the model for a fixed number of epochs (iterations
# over the entire dataset).
history = model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))
print("Model training finished.")

# --- 5. Evaluate the Model ---

# After training, we evaluate the model's performance on the test set,
# which it has never seen before.
print("\nEvaluating model on the test dataset...")
test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=2)

print(f"\nTest accuracy: {test_acc*100:.2f}%")
print(f"Test loss: {test_loss:.4f}")


# --- 6. Make Predictions (Optional) ---

# You can use the trained model to make predictions on new data.
# Let's predict the class for the first 5 images in the test set.
predictions = model.predict(x_test[:5])
print("\nPredictions for the first 5 test images:")
# The output of softmax is an array of probabilities. np.argmax finds the index
# (the predicted digit) with the highest probability.
for i in range(5):
    predicted_digit = np.argmax(predictions[i])
    actual_digit = y_test[i]
    print(f"  Image {i+1}: Predicted digit = {predicted_digit}, Actual digit = {actual_digit}")
    # Display the image
    plt.imshow(x_test[i], cmap=plt.cm.binary)
    plt.title(f"Predicted: {predicted_digit} | Actual: {actual_digit}")
    plt.show()
