# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:49:13 2021

@author: user

graphex8.py : 3D surface 그래프
"""
import matplotlib.pylab as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
XX,YY = np.meshgrid(X,Y)
RR = np.sqrt(XX**2 + YY**2)
ZZ = np.sin(RR)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_title("3D Surface Plot")
ax.plot_surface(XX,YY,ZZ,rstride=1,cstride=1,cmap='hot')
plt.show()