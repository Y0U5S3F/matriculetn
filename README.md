#YOLO Object Detection Pipeline with Filtered JSON and Bounding Box Visualization
This project implements a complete pipeline for object detection using the YOLOv3 model. The pipeline includes object detection, non-maximum suppression (NMS), filtered JSON output generation, and annotated image creation with bounding boxes and labels.

Features
YOLOv3 Integration: Detects objects in images using pretrained YOLOv3 weights and configurations.
Non-Maximum Suppression (NMS): Filters overlapping bounding boxes to retain only the most confident detections.
Filtered JSON Output: Saves detected object data, including class, confidence, and coordinates, as JSON files.
Bounding Box Visualization: Draws bounding boxes with class labels and confidence scores on the detected objects in images.
Batch Processing: Processes all images in a specified folder automatically.
Requirements
Python 3.x
Required libraries:
opencv-python-headless
moviepy
numpy
matplotlib
Usage
Install the required dependencies:
bash
Copy code
pip install opencv-python-headless moviepy
Place input images in the /content/originals/ directory.
Run the script to process the images:
Performs object detection.
Saves filtered results in /content/borders/ as JSON.
Saves annotated images in /content/outputs/.
Outputs
Filtered JSON: Contains object class, confidence, and bounding box coordinates for each detection.
Bordered Images: Visualizes detections with labeled bounding boxes.
Example Results
JSON file: /content/borders/example.json
Annotated image: /content/outputs/example_bordered.jpg
