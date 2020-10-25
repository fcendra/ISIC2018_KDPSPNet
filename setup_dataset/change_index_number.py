from os import listdir
from os.path import isfile, join
from path import Path
import numpy as np
import cv2

# Dataset path
target_path = Path('ISIC2018_Task1_Training_GroundTruth/')
annotation_images_path = Path('D:\Machine Learning Projects\ISIC2018_KDNet\dataset\isic2018\ISIC2018_Task1_Training_GroundTruth').abspath()
dataset = [ f for f in listdir(annotation_images_path) if isfile(join(annotation_images_path,f))]
images = np.empty(len(dataset), dtype = object)
count = 1

# Iterate all Training Images
for n in range(0, len(dataset)):
    # Read image
    images[n] = cv2.imread(join(annotation_images_path,dataset[n]),-1)
 
    # Convert it to array
    array = np.asarray(images[n],dtype="uint8")

    # Conditions when the value equal less than 1, change it to 255. 
    # If it is >= 1, increment it by -1
    arr = np.where(array == 255, 1, array)
    #counter = np.count_nonzero(arr < 0)
    
    cv2.imwrite(target_path + dataset[n], arr)

    print(str(count) + ".png is printed")
    count += 1