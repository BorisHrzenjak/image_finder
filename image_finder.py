import os
import cv2
from deepface import DeepFace
from shutil import copy2

# Path to the folder containing reference images
reference_image_folder = r'C:\Users\BorisH\Documents\Python\Python Scripts\Image_finder\data'
# Path to the output folder where identified images will be saved
output_folder = r'C:\Users\BorisH\Documents\Python\Python Scripts\Image_finder\output'

# Load the reference image
reference_images = []
for file_name in os.listdir(reference_image_folder):
    if file_name.endswith(('jpg', 'jpeg', 'png')):
        reference_image_path = os.path.join(reference_image_folder, file_name)
        reference_images.append(cv2.imread(reference_image_path))

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to scan and process images in a directory
def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('jpg', 'jpeg', 'png')):
                image_path = os.path.join(root, file)
                try:
                    target_img = cv2.imread(image_path)
                    for ref_img in reference_images:
                        # Use DeepFace to find if the image matches the reference
                        result = DeepFace.verify(target_img, ref_img, model_name='VGG-Face')
                        if result["verified"]:
                            # Copy the matching image to the output folder
                            output_path = os.path.join(output_folder, os.path.relpath(image_path, directory))
                            output_dir = os.path.dirname(output_path)
                            if not os.path.exists(output_dir):
                                os.makedirs(output_dir)
                            copy2(image_path, output_path)
                            print(f"Found and saved: {image_path}")
                            break
                except Exception as e:
                    print(f"Could not process {image_path}: {e}")

# Scan the PC
scan_directory(r'C:\Users\BorisH\Pictures\Mobilne slike 19.05.2024')  # For Windows
# scan_directory('/')  # For Linux or macOS
