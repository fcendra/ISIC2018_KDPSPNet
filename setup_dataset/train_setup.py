import glob

list = glob.glob("*.jpg")

train_target_path = 'ISIC2018_Task1-2_Training_Input/'
ground_truth_path = 'ISIC2018_Task1_Training_GroundTruth/'

count = 0
f = open('fine_train.txt', 'a')
# Iterate all Training Images
for n in range(0, len(list)):
    gt = list[n][0:12]
    f.write('\n' + train_target_path + list[n] + " " + ground_truth_path + gt + '_segmentation' + ".png")
    print(str(count) + ".txt is appended")
    count += 1
f.close()
