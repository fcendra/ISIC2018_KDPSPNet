train_target_path = 'ISIC2018_Task1-2_Training_Input/'
ground_truth_path = 'ISIC2018_Task1_Training_GroundTruth/'

count = 0
f = open('fine_train.txt', 'a')
# Iterate all Training Images
for n in range(0, 16073):
    
    if count < 10:
        f.write('\n' + train_target_path + 'ISIC_000000' + str(count) + ".jpg" + " " + ground_truth_path + 'ISIC_000000' + str(count) + '_segmentation' + ".png")
    elif count < 100 and count > 9:
        f.write('\n' + train_target_path + 'ISIC_00000' + str(count) + ".jpg" + " " + ground_truth_path + 'ISIC_00000' + str(count) + '_segmentation' + ".png")
    elif count < 1000 and count > 99:
        f.write('\n' + train_target_path + 'ISIC_0000' + str(count) + ".jpg" + " " + ground_truth_path + 'ISIC_0000'+ str(count) + '_segmentation' + ".png")
    elif count < 10000 and count > 999:
        f.write('\n' + train_target_path + 'ISIC_000' + str(count) + ".jpg" + " " + ground_truth_path + 'ISIC_000' + str(count) + '_segmentation' + ".png")
    else:
        f.write('\n' + train_target_path + 'ISIC_00' + str(count) + ".jpg" + " " + ground_truth_path + 'ISIC_00' + str(count) + '_segmentation' + ".png")

    print(str(count) + ".txt is appended")
    count += 1
f.close()