import os 
from config import *
import shutil
DEV_PATH = '/run/media/why/OS/WHY/AI_Dataset/Tianchi_al/guangdong_round1_train2_20180916/dev/'
TRAIN_PATH = '/run/media/why/OS/WHY/AI_Dataset/Tianchi_al/guangdong_round1_train2_20180916/瑕疵样本/'

def mv_file():
    if not os.path.exists(DEV_PATH):
        os.mkdir(DEV_PATH)
    for x in os.listdir(TRAIN_PATH):
        sub_path = TRAIN_PATH + x
        l = os.listdir(sub_path)
        dev_files = l[:int(len(l)/10)]
        target = DEV_PATH + x
        if not os.path.exists(target):
            os.mkdir(target)
        for y in dev_files:
            path = sub_path + '/' + y
            shutil.move(path, target)
        
def mv_back():
    for x in os.listdir(DEV_PATH):
        sub_path = DEV_PATH + x
        for y in os.listdir(sub_path):
            f_path = sub_path + '/' + y
            shutil.move(f_path, TRAIN_PATH + x)

if __name__ =='__main__':
    # mv_file()
    mv_back()