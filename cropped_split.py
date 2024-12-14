import os
import cv2
import shutil
from sklearn.model_selection import train_test_split

# Paths
dataset_dir = r'C:\Users\yessi\Desktop\Matricule\middle'  # Folder with cropped images (categories 0, 1)
output_dir = r'C:\Users\yessi\Desktop\Datasetsplit'           # Output folder for split datasets
categories = ['0', '1']  # Subfolders for classes

# Split ratios
train_ratio = 0.8
val_ratio = 0.2
test_ratio = 0.2

# Preprocessing Function
def preprocess_image(image_path):
    """Load, preprocess, and save the image."""
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Could not read image: {image_path}")
        return False

    try:
        # Upscale the image
        scale_factor = 2
        new_width = int(image.shape[1] * scale_factor)
        new_height = int(image.shape[0] * scale_factor)
        upscaled_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

        # Convert to grayscale
        gray_image = cv2.cvtColor(upscaled_image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

        # Save the transformed image (overwrite original)
        cv2.imwrite(image_path, blurred_image)
        return True

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return False

# Preprocess and Split Dataset
for category in categories:
    category_path = os.path.join(dataset_dir, category)

    # Check if category folder exists
    if not os.path.exists(category_path):
        print(f"Category folder not found: {category_path}")
        continue

    images = os.listdir(category_path)
    print(f"Category '{category}' has {len(images)} images")

    # Preprocess images
    for img in images:
        img_path = os.path.join(category_path, img)
        success = preprocess_image(img_path)
        if not success:
            print(f"Skipping {img_path} due to preprocessing error")

    # Split into train, val, test
    train_val, test = train_test_split(images, test_size=test_ratio, random_state=42)
    train, val = train_test_split(train_val, test_size=val_ratio / (train_ratio + val_ratio), random_state=42)

    # Create output directories
    for split, split_images in zip(['train', 'val', 'test'], [train, val, test]):
        split_dir = os.path.join(output_dir, split, category)
        os.makedirs(split_dir, exist_ok=True)
        for img in split_images:
            src = os.path.join(category_path, img)
            dst = os.path.join(split_dir, img)
            shutil.copy(src, dst)

print("Dataset preprocessing and splitting completed.")
