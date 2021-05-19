import pathlib
import sys
import os
from PIL import Image

jpg_folder = sys.argv[1]
new_png_folder = sys.argv[2]
os.chdir(jpg_folder)
current_working_dir = os.getcwd()
print("The current working directory is %s" % current_working_dir)
files_in_jpg_folder = os.listdir(jpg_folder)


try:
    os.mkdir(new_png_folder)
    print('Your directory created! ')
except FileExistsError:
    print('Folder you are trying to create already exists, try different name! ')


for item in files_in_jpg_folder:
    image = Image.open(f'{item}')
    image.save(pathlib.Path(f'{jpg_folder}\{new_png_folder}'), 'PNG')
