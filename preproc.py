import os 
from config import *
import shutil

file_list = os.listdir(TRAIN_PATH)
labels = set([x[:2] for x in file_list])
for x in labels:
    tmp = TRAIN_PATH + '/' + x
    if not os.path.exists(tmp):
        # new_dir.append(tmp)
        os.mkdir(tmp)

for x in file_list:
    path = TRAIN_PATH + '/' + x
    tar = x[:2]
    shutil.move(path, TRAIN_PATH+'/'+tar)