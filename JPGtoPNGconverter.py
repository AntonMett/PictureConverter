import pathlib
import sys
import os
from PIL import Image

jpg_folder = pathlib.Path(sys.argv[1])
new_png_folder = pathlib.Path(f'{jpg_folder}\{sys.argv[2]}')
os.chdir(jpg_folder)
try:
    os.mkdir(new_png_folder)
    print('Your directory created! ')
except FileExistsError:
    print('Destination Folder Already Exists! ')
files = os.listdir(jpg_folder)
print(files)

for file in files:
    print(file)
    im = Image.open(f'{jpg_folder}\{file}')
    im.save(f'{new_png_folder}', "PNG")
