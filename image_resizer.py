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
