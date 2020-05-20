#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import random

fig = plt.figure()
ax = fig.add_subplot(111)

x = np.arange(-1,1,0.02)
y = [((a*a-1)*(a*a-1)*(a*a-1)+0.5)*np.sin(a*2) for a in x]
y_noise = y+np.random.normal(0, 0.05, len(y))

def polynomial(x,a):
    y=0
    for i in range(len(a)):
        y+=a[i]*x**i
    return y

if __name__ == "__main__":
    order=9
    A = np.zeros((len(x),order+1))
    for j in range(0,order+1):
        A[:,j] = x**j
    AA = np.dot(A.T,A)
    BB = np.dot(A.T,y_noise.reshape(-1,1))
    a=np.linalg.solve(AA,BB)

    x_estimate=np.arange(-1,1,0.05)
    y_estimate = [polynomial(x,a) for x in x_estimate]

    ax.plot(x_estimate,y_estimate,color='g',linestyle='-',marker='')
    ax.plot(x, y_noise, color='m', linestyle='', marker='.')

    plt.show()

