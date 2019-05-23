import os
import numpy as np
from datetime import datetime

#mean and std of cifar100 dataset
CIFAR100_TRAIN_MEAN = (0.5070751592371323, 0.48654887331495095, 0.4409178433670343)
CIFAR100_TRAIN_STD = (0.2673342858792401, 0.2564384629170883, 0.27615047132568404)

#CIFAR100_TEST_MEAN = (0.5088964127604166, 0.48739301317401956, 0.44194221124387256)
#CIFAR100_TEST_STD = (0.2682515741720801, 0.2573637364478126, 0.2770957707973042)

#directory to save weights file
CHECKPOINT_PATH = 'checkpoint'

#total training epoches
EPOCH = 100 
MILESTONES = [15, 30, 50, 75, 90]
#MILESTONES = list((np.array(range(49))+1)*2)
#initial learning rate
#INIT_LR = 0.1

#time of we run the script
TIME_NOW = datetime.now().isoformat()

#tensorboard log dir
LOG_DIR = 'runs'

#save weights file per SAVE_EPOCH epoch
SAVE_EPOCH = 10

USE_ZFNET = 1

CPU_ONLY = 1


