# -*- coding:utf-8 -*-
import glob

# imageList = glob.glob("/media/mym/My Passport/cj/MRI_data/GGZ202106/*/*/*/*")  # ͼƬ�����ļ��е�·��
imageList = glob.glob("./LEVIR/label/*")
imageList.sort()  #������������
f = open('./LEVIR/list/val.txt', 'a')  # ������ǩ�ļ����ͼƬ�ļ���
for item in imageList:

    # print(item)                                # images_test/m1_a_018_1.jpg
    img_name1 = item.split('/')[-1]  # ͼƬ�ļ���018.jpg
    # img_name = img_name1.split('.')[0]
    print(img_name1)
    f.write(img_name1 + '\n')  # ��ͼƬ�ļ�������д��txt

print('OK')