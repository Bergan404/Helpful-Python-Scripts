import os
import subprocess

def compress_gif(input_path, output_path, target_size_MB=5):
    try:
        # Run gifsicle to compress the GIF
        cmd = f"gifsicle --optimize=3 -o {output_path} {input_path}"
        subprocess.run(cmd, shell=True, check=True)

        # Check if the resulting file size meets the target size
        current_size = os.path.getsize(output_path)
        if current_size > target_size_MB * 1024 * 1024:
            print(f"Compression didn't meet the target size for {input_path} (current size: {current_size / (1024 * 1024):.2f} MB)")
    except Exception as e:
        # Handle any exceptions that occur during processing
        print(f"Error processing {input_path}: {str(e)}")

def compress_gifs_in_folder(input_folder, output_folder, target_size_MB=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".gif"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename)
            compress_gif(input_file, output_file, target_size_MB)

if __name__ == "__main__":
    input_folder = "uncompressed-gif"
    output_folder = "compressed-gif"
    target_size_MB = 5

    compress_gifs_in_folder(input_folder, output_folder, target_size_MB)
