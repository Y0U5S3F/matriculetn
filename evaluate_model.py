import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Load the model
model = load_model('license_plate_classifier.h5')

# Evaluate the model on test data
test_dir = r'C:\Users\yessi\Desktop\Dataset_split\test'  # Path to your test data
test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(128, 128),
    batch_size=32,
    class_mode='categorical'
)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(test_generator)
print(f"Test loss: {test_loss}")
print(f"Test accuracy: {test_accuracy}")

# Predict on a new image
new_image_path = r'C:\Users\yessi\Desktop\Dataset_split\test\tunisia\matricule29_1.png'
# Load the image with OpenCV for better control over resizin
img_cv = cv2.imread(new_image_path)
# Resize the image using high-quality interpolation
resized_img = cv2.resize(img_cv, (128, 128), interpolation=cv2.INTER_CUBIC)

# Normalize the image
resized_img_array = np.array(resized_img) / 255.0  # Normalize to [0, 1]
resized_img_array = np.expand_dims(resized_img_array, axis=0)  # Add batch dimension

# Make a prediction
predictions = model.predict(resized_img_array)
predicted_class = np.argmax(predictions)  # Get the class with the highest probability

# Map the predicted class to category names
categories = ['tunisia', 'nt', 'others']
predicted_category = categories[predicted_class]

# Display the result
print(f"Predicted class: {predicted_category}")
print(f"Prediction probabilities: {predictions}")

# Visualize the resized image and prediction
plt.imshow(resized_img)
plt.title(f"Predicted: {predicted_category}")
plt.axis('off')
plt.show()
