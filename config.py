import ast
import os

# 换数据集记得改!!!!!!
DEBUG = False
MODEL_NAME = 'No10_unfreeze_1e-4_dev'
TEST_MODEL_NAME = 'best_50_8_0.0001_No10_unfreeze_1e-4_dev.pkl'
DEV = True
TEST_AFTER_TRAIN = True
TFX = True    # if using tensorboardX
FREEZE = False
CLASS_NUM = 12
BATCH_SIZE = 8
SAVE_SNAP = 5
STEP_SIZE = 5
SIZE = 224
EPOCH = 50
LR = 1e-4

if DEBUG:
    MODEL_NAME = 'debug'
    TFX = False
    EPOCH = 5
NO_LABEL_PRED = True
TRAIN_PATH = '/disk/unique/why/dataset/Tianchi_al/train2'
if DEV:
    DEV_PATH = '/disk/unique/why/dataset/Tianchi_al/dev'
MODEL_SAVE_PATH = './model'
TEST_PATH = '/disk/unique/why/dataset/Tianchi_al/test'
TEST_MODEL_PATH = '/disk/unique/why/code/Tianchi_al/model/' + TEST_MODEL_NAME

if DEBUG:
    TRAIN_PATH = '/disk/unique/why/dataset/Tianchi_al/sample_train'
    MODEL_SAVE_PATH = './model/debug_model'
    TEST_PATH = TRAIN_PATH
    if TEST_AFTER_TRAIN:
        TEST_MODEL_PATH = MODEL_SAVE_PATH

if os.getcwd()[:2] == '/d':
    with open('./cls2idx.txt', 'r') as f:
        tmp_str = f.read()
    CLS2IDX = ast.literal_eval(tmp_str)
    # CLS2IDX = {'凸粉': 0, '擦花': 1, '漏底': 2, '碰凹': 3}

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
