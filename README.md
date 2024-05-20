# Face Recognition Image Finder

This Python script uses the `DeepFace` library to search for images in a specified directory (or directories) that match one or more reference images. The matching images are then copied to an output folder.

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python 3.x
- OpenCV (`cv2`)
- DeepFace (`deepface`)

You can install the required Python packages using pip:

```
pip install opencv-python
pip install deepface
```

## Usage

1. Clone or download the repository containing the script.
2. Update the following paths in the script according to your file structure:
   - `reference_image_folder`: Path to the folder containing the reference images.
   - `output_folder`: Path to the folder where the identified images will be saved.
3. Place your reference image(s) in the `reference_image_folder`.
4. In the script, update the directory path(s) to scan for images in the `scan_directory()` function call. For example:

   ```python
   scan_directory(r'C:\Users\YourUsername\Pictures\YourFolderName')
   ```

   You can provide multiple paths by adding more `scan_directory()` calls.

5. Run the script using the following command:

   ```
   python script_name.py
   ```

   Replace `script_name.py` with the actual name of your Python script file.

The script will scan the specified directory (or directories) and compare each image against the reference image(s). If a match is found, the image will be copied to the `output_folder` while maintaining the original directory structure.

## How it Works

1. The script loads the reference image(s) from the `reference_image_folder`.
2. It creates the `output_folder` if it doesn't already exist.
3. The `scan_directory()` function is called with the path(s) to scan for images.
4. For each image found in the specified directory (or directories), the script performs the following steps:
   - Load the target image using OpenCV (`cv2.imread()`).
   - Compare the target image against each reference image using the `DeepFace.verify()` function from the `deepface` library.
   - If a match is found (i.e., `result["verified"]` is `True`), copy the matching image to the `output_folder` while preserving the original directory structure.
   - Print a message indicating the path of the saved image.
5. If an error occurs during the processing of an image, it prints an error message with the image path and the exception details.

Note: The script uses the `VGG-Face` model from DeepFace for face recognition. You can modify the `model_name` parameter in the `DeepFace.verify()` function to use a different model if desired.

## License

This project is licensed under the [MIT License](LICENSE).
