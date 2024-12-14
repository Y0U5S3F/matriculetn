from tensorflow.keras.preprocessing import image
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt


# Load the model
model = tf.keras.models.load_model('license_plate_classifier2.h5')

image_size = (128,128)

# Load and preprocess the new image
new_image_path = r'C:\Users\yessi\Downloads\tons.png'  # Change this to the path of your image
img = image.load_img(new_image_path, target_size=image_size, color_mode='grayscale')  # Load and resize the image
img_array = image.img_to_array(img)  # Convert image to array
img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
img_array = img_array / 255.0  # Normalize the image (same as training)

# Make a prediction
prediction = model.predict(img_array)

# Output the result
if prediction[0] > 0.5:
    print("Class 1: Image contains numbers")
else:
    print("Class 0: Image contains Tunisia")


