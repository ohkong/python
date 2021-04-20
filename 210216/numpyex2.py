# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:41:50 2021

@author: user

numpyex2.py : numpy 기본 연산 
"""
import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)

print(a-b) #[20 29 38 47]
print(b**2) #[0 1 4 9]
print(a<35)

c=np.array([[1,1],[0,1]])
d=np.array([[2,0],[3,4]])
print(c+d) #행열 합 
print(c*d) #행열 곱
print(c@d) #행열식 곱 
print(c.dot(d)) #행열식 곱 @ 표시와 같은 기능을 함

e=np.ones((2,3),dtype=int)
print(e)
e *=3 #e배열의 각 요소의 값에 *3을 하여 다시 e 배열에 저장
print(e)

f=np.ones(3,dtype=np.int32)
g=np.linspace(0,np.pi,3)
print(f.dtype,g.dtype)
h=f+g
print(h)
print(h.dtype)