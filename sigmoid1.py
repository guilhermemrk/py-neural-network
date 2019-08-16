# -*- coding: utf8 -*-
# @author: Akai-#0001

import numpy as np

def sigmoid(sum):
    return 1/(1+np.exp(-sum))

print(sigmoid(0))
