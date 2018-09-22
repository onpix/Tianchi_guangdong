import ast
import os 

# 换数据集记得改!!!!!!
MODEL_NAME = 'unfreeze_1e-2'
DEBUG = False
TEST_AFTER_TRAIN = True
TFX = True      # if using tensorboardX
FREEZE = False
CLASS_NUM = 12
BATCH_SIZE = 8
SAVE_SNAP = 5
STEP_SIZE = 5
SIZE = 224
EPOCH = 50
LR = 1e-2

TRAIN_PATH = '/disk/unique/why/dataset/Tianchi_al/train2'
NO_LABEL_PRED = True
MODEL_SAVE_PATH = './model'
TEST_PATH = '/disk/unique/why/dataset/Tianchi_al/test'
TEST_MODEL_PATH = '/disk/unique/why/code/Tianchi_al/model/best_50_8_0.001_unfreeze.pkl'

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
