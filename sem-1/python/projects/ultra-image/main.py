import os
from PIL import Image

def resize_image(input_image_path, output_image_path, new_width, new_height):
    # Open the image file
    with Image.open(input_image_path) as img:
        # Resize the image
        resized_img = img.resize((new_width, new_height))
        
        # Save the resized image
        resized_img.save(output_image_path)
        print(f"Image saved to {output_image_path}")

def main():
    print("Welcome to Image processing application: now only supprt to resize")
    input_file = input("Enter path of image: ").strip()

    if not os.path.isfile(input_file):
        print("Input file does not exist")
        return
    
    output_file = input("Enter output file of image: ").strip()
    
    width = int(input("Enter new width: ").strip() or '0')
    height = int(input("Enter new height: ").strip() or '0')

    resize_image(input_file, output_file, width, height)


if __name__ == "__main__":
    main()