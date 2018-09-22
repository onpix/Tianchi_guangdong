import matplotlib.pyplot as plt 
import numpy as np 
ROOT = '/run/media/why/OS/AI_Lab/whyAI/Tianchi_al_local/'
PATH = './data/log.npz'
NAME = ''

def read_f(path):
    res = np.load(path)
    loss = res['loss']
    acc = res['acc']
    return loss, acc

def draw(array, name):
    plt.figure()
    x = list(range(len(array)))
    plt.scatter(x, array, c='navy', linewidths=0.1)
    plt.plot(x, array, label=name, c='navy')
    plt.grid()
    plt.savefig(ROOT+'plot/{}.jpg'.format(name))

def plot():
    loss, acc = read_f(ROOT+PATH)    
    draw(loss, 'Loss'+NAME)
    draw(acc, 'Acc'+NAME)


if __name__ == '__main__':
    plot()
