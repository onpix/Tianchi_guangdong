import numpy as np 
import os
import shutil
ROOT = ('/home/why/下载/train2/正常')

l = os.listdir(ROOT)
for x in l:
    path = ROOT + '/' + x
    sub_l = os.listdir(path)
    for y in sub_l:
        shutil.move(path + '/'+y, ROOT)