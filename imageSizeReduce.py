import os
from PIL import Image

def reduce_image_size(input_path, output_path, max_size):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for filename in os.listdir(input_path):
        file_path = os.path.join(input_path, filename)
        if os.path.isfile(file_path):
            try :
                with Image.open(file_path) as img:
                    img.thumbnail(img.size)
                    while True:
                        img.save(os.path.join(output_path, filename), optimize=True, quality=70)
                        file_size = os.path.getsize(os.path.join(output_path, filename)) / (1024 * 1024)
                        if file_size <= max_size:
                            print(f"File {filename} reduced to {file_size:.2f} MB")
                            break
                        img = img.resize((int(img.width * 0.8), int(img.height * 0.8)), Image.LANCZOS)
                        
            except Exception as e:
                print(e)

if __name__ == "__main__":
    input_path = "input"
    output_path = "output"
    max_size = 5 # in MB
    reduce_image_size(input_path, output_path, max_size)
    
