import re
import numpy as np
import time
from config import TEST_MODEL_NAME
ROOT = '/run/media/why/OS/AI_Lab/whyAI/Tianchi_al_local'
FILE_NAME = '/data/pred.txt'
SAVE_WITH_TIME = False
LABELS2RES = {'正常': 'norm',
              '不导电': 'defect1',
              '擦花': 'defect2',
              '横条压凹': 'defect3',
              '桔皮': 'defect4',
              '漏底': 'defect5',
              '碰伤': 'defect6',
              '起坑': 'defect7',
              '凸粉': 'defect8',
              '涂层开裂': 'defect9',
              '脏点': 'defect10',
              '其他': 'defect11'}

res = np.loadtxt(ROOT + FILE_NAME, delimiter=', ', dtype='str')
num = len(res)

for i in range(num):
    res[i][0] = re.findall('\d*\.jpg', res[i][0])[0]

sorted_res = sorted(res, key=lambda x: int(x[0][:-4]))
names = np.array([[re.findall('\d*\.jpg', x[0])[0] for x in sorted_res]]).T
preds = np.array([[x[-1] for x in sorted_res]]).T

preds = [x[0] for x in preds]
for i in range(num):
    if preds[i] == '碰凹':
        preds[i] = '横条压凹'
    preds[i] = LABELS2RES[preds[i]]

preds = np.array([preds]).T
new = np.concatenate((names, preds), axis=1)

if SAVE_WITH_TIME:
    now = time.strftime('%H:%M', time.localtime())
    np.savetxt(ROOT+'/{}_{}.csv'.format(TEST_MODEL_NAME, now), new, fmt='%s,%s')
else:
    np.savetxt(ROOT+'/{}.csv'.format(TEST_MODEL_NAME), new, fmt='%s,%s')
print('Everything done!')
