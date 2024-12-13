import os
import json
import shutil

# Set the directory paths
image_dir = r'C:\Users\yessi\Desktop\Matricule\cropped_images'  # Adjust this to your image folder
json_dir = r'C:\Users\yessi\Desktop\Matricule\matricule_jsons'  # Adjust this to your JSON folder
categories_dir = r'C:\Users\yessi\Desktop\Matricule\categories'  # This folder will store categorized images

# Create subfolders for each category if not already created
categories = ['0', '1', '2']
for category in categories:
    category_path = os.path.join(categories_dir, category)
    os.makedirs(category_path, exist_ok=True)

# Process each JSON file and move images
for json_file in os.listdir(json_dir):
    if json_file.endswith('.json'):
        json_path = os.path.join(json_dir, json_file)
        with open(json_path, 'r') as f:
            data = json.load(f)

            # Get the class_id from the JSON
            class_id = data.get('class_id')

            # Define the category based on class_id
            if class_id == 0:
                category_folder = '0'
            elif class_id == 1:
                category_folder = '1'
            else:
                category_folder = '2'


            image_name = json_file.replace('.json', '.png')  # Image should be .png
            image_path = os.path.join(image_dir, image_name)
            if os.path.exists(image_path):
                # Move the .png image to the appropriate folder
                shutil.move(image_path, os.path.join(categories_dir, category_folder, image_name))
            else:
                print(f"Image not found: {image_path}")

