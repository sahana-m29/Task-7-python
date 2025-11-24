# Task-7-python
# Image Resizer Tool (Python + Pillow)

This project provides a simple **batch image resizer** using Python and
the Pillow library.

## ✅ Features

-   Resize all images inside a folder
-   Convert images to a chosen format (`JPEG`, `PNG`, etc.)
-   Automatically saves resized images to an output folder
-   Supports: `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`

------------------------------------------------------------------------

## 📂 Folder Structure

    ImageResizer/
     ├── image_resizer.py
     ├── images_input/      # Put your original images here
     └── images_output/     # Resized images will be saved here

------------------------------------------------------------------------

## ▶️ How to Use

### 1. Install Pillow

    pip install pillow

### 2. Place your images

Put all images you want to resize inside:

    images_input/

### 3. Run the Script

    python image_resizer.py

### 4. Output

Resized images will appear in:

    images_output/

------------------------------------------------------------------------

## 🧾 Python Script (Used in This Project)

``` python
import os
from PIL import Image

# -------- SETTINGS --------
input_folder = "images_input"     # Folder containing original images
output_folder = "images_output"   # Folder where resized images will be saved

new_width = 1000    # Output width
new_height = 200    # Output height
output_format = "JPEG"   # Options: "JPEG", "PNG", "WEBP"
# ---------------------------

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Supported image file types
valid_ext = [".jpg", ".jpeg", ".png", ".webp", ".bmp"]

# Loop through all files in the folder
for file in os.listdir(input_folder):
    if any(file.lower().endswith(ext) for ext in valid_ext):

        img_path = os.path.join(input_folder, file)
        img = Image.open(img_path)

        # Resize image
        resized = img.resize((new_width, new_height))

        # Output path
        file_name = os.path.splitext(file)[0] + "." + output_format.lower()
        save_path = os.path.join(output_folder, file_name)

        # Save image
        resized.save(save_path, output_format)

        print(f"Resized & Saved: {save_path}")

print("\nAll images resized successfully!")
```

------------------------------------------------------------------------

## 🎯 Outcome

You now have an automated image processing tool that resizes & converts
images in batch using Python.

------------------------------------------------------------------------

## 📌 Author

Generated automatically using ChatGPT.
