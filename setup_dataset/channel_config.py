from os import listdir
from os.path import isfile, join
from path import Path
import numpy as np
import cv2

# Dataset path
annotation_images_path = Path('dataset/isic2018/ISIC2018_Task1-2_Training_Input/').abspath()
dataset = [ f for f in listdir(annotation_images_path) if isfile(join(annotation_images_path,f))]
images = np.empty(len(dataset), dtype = object)
count = 1

array = []

# Iterate all Training Images
# for n in range(0, len(dataset)):
for n in range(0, 10235):
    # Read image
    images[n] = cv2.imread(join(annotation_images_path,dataset[n]),-1)
    number_of_channel = len(images[n].shape)
    # Convert it to array
    array = np.asarray(images[n],dtype="uint8")
    print(array)
    print(number_of_channel)