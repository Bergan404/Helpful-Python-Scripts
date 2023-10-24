from PIL import Image
import os

# Specify the input and output directories
input_directory = "unconverted-images"
output_directory = "webp-images"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# List all the files in the input directory
input_files = os.listdir(input_directory)

for filename in input_files:
    if filename.endswith((".jpg", ".jpeg", ".png")):
        # Construct the full input and output file paths
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, os.path.splitext(filename)[0] + ".webp")

        # Open and convert the image to WebP format
        with Image.open(input_path) as img:
            img.save(output_path, "webp")

print("Conversion completed.")
