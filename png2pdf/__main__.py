import sys
import os
import re
from PIL import Image

def natural_sort_key(s):
    """Extract numerical parts for natural sorting like Screenshot 1, 2, 10"""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def png_to_pdf(image_folder, output_pdf):
    png_files = [f for f in os.listdir(image_folder) if f.lower().endswith('.png')]
    png_files.sort(key=natural_sort_key)

    if not png_files:
        print("❌ No PNG files found in the folder.")
        return

    images = []
    for file in png_files:
        img_path = os.path.join(image_folder, file)
        img = Image.open(img_path).convert("RGB")
        images.append(img)

    first_image = images.pop(0)
    first_image.save(output_pdf, save_all=True, append_images=images)
    print(f"✅ Combined {len(png_files)} PNGs into {output_pdf}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m png2pdf <image_folder> [output_pdf]")
        sys.exit(1)

    image_folder = sys.argv[1]
    output_pdf = sys.argv[2] if len(sys.argv) > 2 else "combined.pdf"

    if not os.path.isdir(image_folder):
        print(f"❌ Folder not found: {image_folder}")
        sys.exit(1)

    png_to_pdf(image_folder, output_pdf)

if __name__ == "__main__":
    main()
