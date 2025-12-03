import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
import numpy as np

print("--- Starting Model Training with Dropout ---")

# 1. Load and Preprocess Data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Reshape, Normalize, and One-Hot Encode
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

print(f"Training data shape: {x_train.shape}")

# 2. Define CNN Architecture
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    
    Flatten(),
    
    # CRITICAL: Dropout layer added here to reduce confidence and improve grading variation
    Dropout(0.25), 
    
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# 3. Compile and Train Model
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Training will take a few minutes
model.fit(x_train, y_train, 
          epochs=10, # Increased epochs for better learning with Dropout
          batch_size=128, 
          validation_data=(x_test, y_test),
          verbose=1)

# 4. Save Model
model.save('drawing_grader_cnn.h5')
print("\n--- Model trained successfully and saved as 'drawing_grader_cnn.h5' ---")