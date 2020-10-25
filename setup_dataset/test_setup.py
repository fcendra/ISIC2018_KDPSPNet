import glob

list = glob.glob("*.jpg")
test_target_path = 'ISIC2018_Task1-2_Test_Input/'
print(len(list))
# Iterate all Test Images file directory'
f = open('fine_test.txt', 'a')
for n in range(0, len(list)):
    f.write('\n' + test_target_path + list[n])
    print(str(n) + '.jpg is already append')
f.close()