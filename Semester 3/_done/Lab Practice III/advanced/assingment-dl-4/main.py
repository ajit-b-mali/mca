# Assignment 8: Write a program for Anomaly Detection Using Autoencoder.
# This program will build an autoencoder to detect anomalies in ECG (electrocardiogram)
# time-series data. The model will be trained only on "normal" heartbeats and will
# be used to identify "anomalous" ones.

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras import layers, losses
import matplotlib.pyplot as plt

print("TensorFlow version:", tf.__version__)

# --- 1. Load and Prepare the ECG Dataset ---

# We will use the ECG5000 dataset, which is available online.
# It contains 5000 ECG signals, each with 140 data points.
# The label '1' indicates an anomaly, and '2' indicates a normal heartbeat.
# For consistency, we will map '2' to 0 (normal) and '1' to 1 (anomaly).
url = "http://storage.googleapis.com/download.tensorflow.org/data/ecg.csv"
dataframe = pd.read_csv(url, header=None)
raw_data = dataframe.values

# The last column is the label.
labels = raw_data[:, -1]
# The other columns are the time-series data.
data = raw_data[:, 0:-1]

# Split the data into training and testing sets.
from sklearn.model_selection import train_test_split
train_data, test_data, train_labels, test_labels = train_test_split(
    data, labels, test_size=0.2, random_state=21
)

# Remap labels: Normal is 0, Anomaly is 1
train_labels = (train_labels == 1.0).astype(int)
test_labels = (test_labels == 1.0).astype(int)

# --- 2. Normalize and Prepare Training Data ---

# Normalize the data to be in the [0, 1] range.
min_val = tf.reduce_min(train_data)
max_val = tf.reduce_max(train_data)

train_data = (train_data - min_val) / (max_val - min_val)
test_data = (test_data - min_val) / (max_val - min_val)

train_data = tf.cast(train_data, tf.float32)
test_data = tf.cast(test_data, tf.float32)

# IMPORTANT: We train the autoencoder ONLY on the normal heartbeats.
# This is the core principle of this anomaly detection method.
normal_train_data = train_data[train_labels == 0]
normal_test_data = test_data[test_labels == 0]

# We will also need the anomalous data from the test set for evaluation.
anomalous_test_data = test_data[test_labels == 1]

print(f"Number of normal training examples: {len(normal_train_data)}")
print(f"Number of normal test examples: {len(normal_test_data)}")
print(f"Number of anomalous test examples: {len(anomalous_test_data)}")

# Plot a normal and an anomalous heartbeat to see the difference.
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.grid()
plt.plot(np.arange(140), normal_train_data[0])
plt.title("A Normal ECG")
plt.subplot(1, 2, 2)
plt.grid()
plt.plot(np.arange(140), anomalous_test_data[0])
plt.title("An Anomalous ECG")
plt.show()


# --- 3. Build the Autoencoder Model ---

class AnomalyDetector(keras.Model):
    def __init__(self):
        super(AnomalyDetector, self).__init__()
        self.encoder = tf.keras.Sequential([
            layers.Dense(32, activation="relu"),
            layers.Dense(16, activation="relu"),
            layers.Dense(8, activation="relu")]) # Bottleneck layer

        self.decoder = tf.keras.Sequential([
            layers.Dense(16, activation="relu"),
            layers.Dense(32, activation="relu"),
            layers.Dense(140, activation="sigmoid")]) # Output layer

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

autoencoder = AnomalyDetector()

autoencoder.compile(optimizer='adam', loss='mae') # Mean Absolute Error loss

# --- 4. Train the Model ---

# Train the autoencoder on the normal training data.
history = autoencoder.fit(normal_train_data, normal_train_data,
                          epochs=20,
                          batch_size=512,
                          validation_data=(test_data, test_data),
                          shuffle=True)

# Plot training loss
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.legend()
plt.title("Training and Validation Loss")
plt.show()

# --- 5. Determine the Anomaly Threshold ---

# Calculate the reconstruction error for the normal training data.
reconstructions = autoencoder.predict(normal_train_data)
train_loss = tf.keras.losses.mae(reconstructions, normal_train_data)

# Plot the distribution of the reconstruction loss.
plt.hist(train_loss, bins=50)
plt.xlabel("Train loss")
plt.ylabel("No of examples")
plt.title("Distribution of Reconstruction Error for Normal Data")
plt.show()

# We will set the threshold as the mean + 3 * standard deviation of the loss.
threshold = np.mean(train_loss) + 3 * np.std(train_loss)
print("Anomaly Threshold: ", threshold)

# --- 6. Evaluate the Model on Test Data ---

def predict(model, data, threshold):
    reconstructions = model(data)
    loss = tf.keras.losses.mae(reconstructions, data)
    return tf.math.less(loss, threshold)

# Helper function to plot original vs. reconstructed signal.
def plot_example(data, title):
    reconstruction = autoencoder.predict(np.array([data]))
    plt.plot(data, 'b')
    plt.plot(reconstruction[0], 'r')
    plt.fill_between(np.arange(140), data, reconstruction[0], color='lightcoral')
    plt.legend(labels=["Input", "Reconstruction", "Error"])
    plt.title(title)
    plt.show()

# Plot a normal ECG - the reconstruction error should be low.
plot_example(normal_test_data[0], "Normal ECG vs. Reconstruction")

# Plot an anomalous ECG - the reconstruction error should be high.
plot_example(anomalous_test_data[0], "Anomalous ECG vs. Reconstruction")

# Calculate reconstruction errors for normal and anomalous test data.
normal_reconstructions = autoencoder.predict(normal_test_data)
normal_loss = tf.keras.losses.mae(normal_reconstructions, normal_test_data)

anomalous_reconstructions = autoencoder.predict(anomalous_test_data)
anomalous_loss = tf.keras.losses.mae(anomalous_reconstructions, anomalous_test_data)

# Plot the losses to visually confirm that anomalies have higher errors.
plt.hist(normal_loss, bins=50, label='normal')
plt.hist(anomalous_loss, bins=50, label='anomalous')
plt.axvline(threshold, color='r', linewidth=3, linestyle='dashed', label='{:0.3f}'.format(threshold))
plt.legend(loc='upper right')
plt.title("Reconstruction Errors on Test Data")
plt.show()
 