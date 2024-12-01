import json
import re

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def transform_filename(filename):
    match = re.match(r"(\d+)_png", filename)
    if match:
        return f"{match.group(1)}.png"
    return None

def update_annotations(coco_file, combined_file):
    coco_data = load_json(coco_file)
    combined_data = load_json(combined_file)

    for image in coco_data['images']:
        transformed_filename = transform_filename(image['file_name'])
        if transformed_filename:
            print(f"Transformed filename: {transformed_filename}")
            for item in combined_data:
                if item['image'] == transformed_filename:
                    print(f"Found matching image: {transformed_filename}")
                    if 'matricule' in item['detections'] and item['detections']['matricule']:
                        for detection in item['detections']['matricule']:
                            if 'value' in detection:
                                image['matricule_class'] = detection['class_id']
                                image['matricule_value'] = detection['value']
                                print(f"Added matricule_class: {detection['class_id']}, matricule_value: {detection['value']}")
                            else:
                                print(f"No value found in detection for {transformed_filename}, skipping.")
                    else:
                        print(f"No matricule found for {transformed_filename}, skipping.")

    save_json(coco_data, coco_file)

if __name__ == "__main__":
    coco_file = '_annotations.coco.json'
    combined_file = 'combined.json'
    
    update_annotations(coco_file, combined_file)