from PIL import Image
import os
import sys
import shutil
 
def rotate(image, degrees_to_rotate):
    return image.rotate(degrees_to_rotate, resample=Image.BICUBIC, expand=True)

def flip_image(image):
    return image.transpose(Image.FLIP_TOP_BOTTOM)

def load_image(image_path):
    return Image.open(image_path)

def save_image(image, saved_location): 
    image.save(saved_location)

def create_destination_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    else:
        shutil.rmtree(directory_path)
        os.makedirs(directory_path)

def copy_to_directory(source_file_path, destination_file_path):
    shutil.copy2(source_file_path, destination_file_path)

def extract_path(file_path):
    return os.path.dirname(file_path)

def extract_filename(file_path):
    return os.path.basename(file_path)

def extract_fileextension(file_path):
    return os.path.splitext(file_path)[-1].lower()
 
if __name__ == '__main__':

    path_origin = sys.argv[1]
    
    # Extract filename and extension of original image.
    file_name = extract_filename(path_origin)
    file_extension = extract_fileextension(path_origin)
    file_name_without_extension = file_name.replace(file_extension, '')

    # Create atlas directory.
    file_path = extract_path(path_origin)
    destination_directory_path = os.path.join(file_path, file_name_without_extension + ".atlas")
    create_destination_directory(destination_directory_path)

    # Create paths for new files.
    path_shop_image = os.path.join(destination_directory_path, file_name_without_extension + "_shop" + file_extension)
    path_left_up = os.path.join(destination_directory_path, file_name_without_extension + "_left_up" + file_extension)
    path_right_up = os.path.join(destination_directory_path, file_name_without_extension + "_right_up" + file_extension)
    path_left_down = os.path.join(destination_directory_path, file_name_without_extension + "_left_down" + file_extension)
    path_right_down = os.path.join(destination_directory_path, file_name_without_extension + "_right_down" + file_extension)

    # Create rotated and fliped images.
    image = load_image(path_origin)
    image_right_up = rotate(image, 70)
    image_left_up = flip_image(image_right_up)
    image_left_down = rotate(image, 250)
    image_right_down = flip_image(image_left_down)

    # Copy original image as shop image to atlas directory.
    copy_to_directory(path_origin, path_shop_image)

    # Save new images to atlas directory.
    save_image(image_right_up, path_right_up)
    save_image(image_left_up, path_left_up)
    save_image(image_left_down, path_left_down)
    save_image(image_right_down, path_right_down)