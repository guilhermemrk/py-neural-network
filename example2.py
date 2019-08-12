# -*- coding: utf8 -*-
# @author: Akai-#0001

import numpy as np

entry = np.array([1, 7, 5])
weight = np.array([0.8, 0.1, 0])

def sumf(e, p):
    # Produto Escalar / Dot Product
    return e.dot(p)

def stepFunction(sum):
    if (sum >= 1):
        return 1
    return 0

s = sumf(entry, weight)
r = stepFunction(s)

print("Entry: {}".format(entry))
print("Weight: {}".format(weight))
print("R = {}".format(s))
print("S = {}".format(r))
