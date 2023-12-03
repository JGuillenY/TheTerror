from PIL import Image
import os
import sys

input_directory = sys.argv[1]
output_path = '/home/yasue/Proyects/TheTerror/Tools/ImageResizer/512/'
width = sys.argv[2]
height = sys.argv[3] if len(sys.argv) > 3 else width

def resize_image(dirname, file):
    outputdir = output_path + dirname
    print(outputdir)
    print(os.path.exists(outputdir))
    if not os.path.exists(outputdir): os.mkdir(outputdir)
    img = Image.open(input_directory + '/' + dirname + '/' + file)
    new_image = img.resize((int(width), int(height)))
    new_image.save(outputdir + '/' + file)

def process_directory(directory):
    files = [f for f in os.listdir(input_directory + '/' + directory)]
    
    for file in files:
        if(file.split('.')[1] == 'jpg'):
            resize_image(directory, file)

if not os.path.exists(input_directory):
    print("Path specified does not exist.")
    exit()

textures = os.listdir(input_directory)
for texture in textures:
    process_directory(texture)