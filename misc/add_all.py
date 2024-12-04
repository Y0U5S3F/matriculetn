import os
import json

def read_json_files(directory):
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    combined_data = []

    for json_file in json_files:
        with open(os.path.join(directory, json_file), 'r') as f:
            data = json.load(f)
            combined_data.append(data)

    return combined_data

def write_combined_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    directory = '.'  # Current directory
    output_file = 'combined.json'
    
    combined_data = read_json_files(directory)
    write_combined_json(combined_data, output_file)
