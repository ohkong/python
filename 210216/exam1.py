# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:36:08 2021

@author: user

exam1.py :
"""
import numpy as np

arr = np.zeros(10,dtype=int)
print(arr)

arr = np.ones((3,5))
print(arr)

arr=np.arange(0,21,2)
print(arr)

arr=np.linspace(0,1,5)
print(arr)

#3행 5열의 배열의 값을 3.14로 채운 배열 생성
arr = np.full((3,5),3.14)
print(arr)