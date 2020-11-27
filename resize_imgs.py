from PIL import Image
import os, sys

path ="sample_images/"
new_dir = "sample_images_resized/"
dirs= os.listdir(path)

def resize():
    for item in dirs:
        img = Image.open(os.path.join(path,item)).convert('LA')
        filename = os.path.splitext(item)[0]
        imResize = img.resize((1500,1152), Image.ANTIALIAS)
        imResize.save(os.path.join(new_dir,filename + '.png'),'PNG', quality=95)

resize()

