import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
dataset_dir = r'C:\Users\yessi\Desktop\Matricule\categories'
output_dir = r'C:\Users\yessi\Desktop\Datasetsplit'
categories = ['tunisia', 'nt']  # Subfolders

# Train-Test-Validation split ratios
train_ratio = 0.8
val_ratio = 0.2
test_ratio = 0.2

# Create output directories
for split in ['train', 'val', 'test']:
    for category in categories:
        os.makedirs(os.path.join(output_dir, split, category), exist_ok=True)

# Split each category
for category in categories:
    category_path = os.path.join(dataset_dir, category)
    images = os.listdir(category_path)

    train_val, test = train_test_split(images, test_size=test_ratio, random_state=42)
    train, val = train_test_split(train_val, test_size=val_ratio / (train_ratio + val_ratio), random_state=42)

    # Move files to respective directories
    for img in train:
        shutil.copy(os.path.join(category_path, img), os.path.join(output_dir, 'train', category, img))
    for img in val:
        shutil.copy(os.path.join(category_path, img), os.path.join(output_dir, 'val', category, img))
    for img in test:
        shutil.copy(os.path.join(category_path, img), os.path.join(output_dir, 'test', category, img))

print("Dataset split completed.")
