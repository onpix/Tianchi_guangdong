import ast
import os

# ----------------Train Setting--------------------
# 换数据集记得改!!!!!!
DEBUG = False
MODEL_MODE = 'd'     # d: densenet, r: resnet
MODEL_NAME = 'No17_1e-2_BS=16'
TEST_MODEL_NAME = 'No15_DenseNet_1e-2_BS=16.pkl'
DEV = False
SAVE_MODEL_BY_DEV_ACC = False
TEST_AFTER_TRAIN = False
TFX = True    # if using tensorboardX
FREEZE = True
NO_LABEL_PRED = True
CLASS_NUM = 12
BATCH_SIZE = 16
SAVE_SNAP = 5
STEP_SIZE = 5
SIZE = 224
EPOCH = 50
LR = 1e-2

# ---------------------------------------
DATA_ROOT = '/disk/unique/why/dataset/Tianchi_al/'
CODE_ROOT = '/disk/unique/why/code/Tianchi_al/'
TRAIN_PATH = DATA_ROOT + 'train2'
DEV_PATH = DATA_ROOT + 'dev'
MODEL_SAVE_PATH = CODE_ROOT + 'model'
TEST_PATH = DATA_ROOT + 'test'
TEST_MODEL_PATH = CODE_ROOT + 'model/' + TEST_MODEL_NAME

# --------------------------------------
if DEBUG:
    MODEL_NAME = 'debug'
    TFX = False
    EPOCH = 5
    TRAIN_PATH = DATA_ROOT + 'sample_train'
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
