# Assignment 7: Write a program for Building an Image Classification model.
# This program implements a powerful image classifier using the technique of
# Transfer Learning. We will use the MobileNetV2 model, pre-trained on ImageNet,
# and retrain it to classify 5 different types of flowers.

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds

from tensorflow import keras
from keras import layers

print("TensorFlow version:", tf.__version__)

# --- 1. Load and Prepare the Dataset ---

# We will use the `tf_flowers` dataset from TensorFlow Datasets.
# It contains images of 5 types of flowers.
(train_ds, validation_ds, test_ds), metadata = tfds.load(
    'tf_flowers',
    split=['train[:80%]', 'train[80%:90%]', 'train[90%:]'],
    with_info=True,
    as_supervised=True,
)

num_classes = metadata.features['label'].num_classes
print("Number of classes:", num_classes)

# Let's inspect some of the images
get_label_name = metadata.features['label'].int2str

plt.figure(figsize=(10, 10))
for i, (image, label) in enumerate(train_ds.take(9)):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(image)
    plt.title(get_label_name(label))
    plt.axis("off")
plt.suptitle("A Sample of the Flower Dataset")
plt.show()


# --- 2. Create an Efficient Data Pipeline ---

# We need to resize all images to the size expected by MobileNetV2 (160x160)
# and batch the data for efficient training.
IMG_SIZE = 160
BATCH_SIZE = 32

# Preprocessing function to resize and normalize images
def format_example(image, label):
    image = tf.cast(image, tf.float32)
    image = (image / 127.5) - 1 # Normalize pixels to [-1, 1]
    image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
    return image, label

# Apply the function to our datasets and create batches
train_batches = train_ds.map(format_example).shuffle(1000).batch(BATCH_SIZE).prefetch(buffer_size=tf.data.AUTOTUNE)
validation_batches = validation_ds.map(format_example).batch(BATCH_SIZE).prefetch(buffer_size=tf.data.AUTOTUNE)
test_batches = test_ds.map(format_example).batch(BATCH_SIZE)


# --- 3. Build the Model with a Pre-Trained Base ---

IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)

# Load the MobileNetV2 model, pre-trained on ImageNet.
# We specify `include_top=False` to discard the original classification layer.
base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                               include_top=False,
                                               weights='imagenet')

# Freeze the convolutional base to prevent its weights from being updated
# during initial training.
base_model.trainable = False

# Let's see the architecture of our base model
base_model.summary()

# --- 4. Add a New Classification Head ---

# We will build our new model using the Keras Functional API.
inputs = keras.Input(shape=IMG_SHAPE)
# The base model will act as a feature extractor.
x = base_model(inputs, training=False)
# Add a GlobalAveragePooling2D layer to average the spatial features.
x = layers.GlobalAveragePooling2D()(x)
# Add a Dropout layer for regularization to prevent overfitting.
x = layers.Dropout(0.2)(x)
# Add our final Dense layer for classification.
outputs = layers.Dense(num_classes, activation='softmax')(x)

# Create the final model.
model = keras.Model(inputs, outputs)


# --- 5. Compile and Train the Model ---

# We compile the model with a suitable optimizer, loss function, and metric.
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("\nModel Architecture (with new classification head):")
model.summary()

print("\nStarting initial training (only training the new head)...")
initial_epochs = 10
history = model.fit(train_batches,
                    epochs=initial_epochs,
                    validation_data=validation_batches)


# --- 6. (Optional but Recommended) Fine-Tuning ---

# For higher accuracy, we can "fine-tune" the model. This involves un-freezing
# the top layers of the base model and training the entire model on our data
# with a very low learning rate.

print("\nStarting fine-tuning...")
base_model.trainable = True # Un-freeze the base model

# Let's freeze the first 100 layers and fine-tune the rest
for layer in base_model.layers[:100]:
    layer.trainable = False

# We must re-compile the model for these changes to take effect.
# A very low learning rate is critical for fine-tuning.
model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.00001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Continue training from where we left off
fine_tune_epochs = 10
total_epochs = initial_epochs + fine_tune_epochs

history_fine = model.fit(train_batches,
                         epochs=total_epochs,
                         initial_epoch=history.epoch[-1],
                         validation_data=validation_batches)


# --- 7. Evaluate and Visualize ---

# Evaluate the final model on the test set
loss, accuracy = model.evaluate(test_batches)
print(f'\nTest accuracy: {accuracy*100:.2f}%')

# Plot the training history
acc = history.history['accuracy'] + history_fine.history['accuracy']
val_acc = history.history['val_accuracy'] + history_fine.history['val_accuracy']
loss = history.history['loss'] + history_fine.history['loss']
val_loss = history.history['val_loss'] + history_fine.history['val_loss']

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.plot([initial_epochs-1, initial_epochs-1], plt.ylim(), label='Start Fine Tuning')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(2, 1, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.plot([initial_epochs-1, initial_epochs-1], plt.ylim(), label='Start Fine Tuning')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.xlabel('epoch')
plt.show()
