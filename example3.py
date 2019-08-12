# -*- coding: utf8 -*-
# @author: Akai-#0001

import numpy as np

entry = np.array([[0,0],[0,1],[1,0],[1,1]])
end = np.array([0,0,0,1])
weight = np.array([0.0, 0.0])
lp = 0.1

def stepFunction(sum):
    if (sum >= 1):
        return 1
    return 0

def calcEnd(reg):
    s = reg.dot(weight)
    return stepFunction(s)

# w(n+1) = w(n)+(lp*entry*err)
def train():
    errt = 1
    while (errt != 0):
        errt = 0
        for i in range(len(end)):
            edc = calcEnd(np.asarray(entry[i]))
            err = abs(end[i] - edc)
            errt += err
            for j in range(len(weight)):
                weight[j] = weight[j] + (lp * entry[i][j] * err)
                print('>> [Log] Weight updated to {}'.format(weight[j]))
        print('>> [Log] Number of errors: {}'.format(errt))

train()

print("----------------------------------")
print(">> [Log] Neural Network trained!")

for i in range(len(entry)):
    print("----------------------------------")
    print(">> [Log] Nodes: {0}\n>> [Log] Weights: {1}\n>> [Log] Result: {2}".format(entry[i], weight, calcEnd(entry[i])))
print("----------------------------------")
