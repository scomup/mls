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

ax.plot(x, y_noise, color='m', linestyle='', marker='.')


def W(d,x):
    s=abs(x)/d
    if (s<=0.5):
        return (2/3)-4*s**2+4*s**3
    elif(s<=1):
        return (4/3)-4*s+4*s**2-(4/3)*s**3
    else:
        return 0

def polynomial(x,a):
    y=0
    for i in range(len(a)):
        y+=a[i]*x**i
    return y


if __name__ == "__main__":
    d=0.2 
    s = 0.02
    r = np.arange(-d,d+0.001,s)

    order=2
    p=np.zeros((len(x),order))
    for i in range(order):
        p[:,i] = x**i
    y_estimate=[]
    x_estimate=np.arange(-1+d,1-d,0.05)

    for xx in x_estimate:
        w = [ W(d,i-xx) for i in x]
        w = np.array(w).reshape(-1,1)
        A = np.dot((w*p).T,p)
        B = np.dot((w*p).T,y_noise)
        a=np.linalg.solve(A,B)
        y_estimate.append(polynomial(xx,a))
    
ax.plot(x_estimate,y_estimate, color='g', linestyle='-',marker='')

plt.show()