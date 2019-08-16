# -*- coding: utf8 -*-
# @author: Akai-#0001

entry = [1, 7, 5]
weight = [0.8, 0.1, 0]

def sumf(e, p):
    s = 0
    for i in range(3):
        s += e[i]*p[i]
    return s

s = sumf(entry, weight)

def stepFunction(sum):
    if (sum >= 1):
        return 1
    return 0

r = stepFunction(s)

print("R = {}".format(s))
print("S = {}".format(r))
