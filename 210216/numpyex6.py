# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:45:14 2021

@author: user

numpyex6.py : 배열의 연결 및 분할 
"""
import numpy as np

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[3,2,1],[6,5,4]])
print(x)
print(y)

#배열의 연결
print(np.concatenate([x,y],axis=0)) #수직연결 .행으로 연결
print(np.concatenate([x,y],axis=1)) #수평연결 .열로 연결

#형태가 다른 배열의 연결
x=np.array([[1,2,3],[4,5,6]])
y=np.array([[3,2,1],[6,5,4],[3,2,1]])
z=np.array([[7],[10]])
print(x)
print(y)
print(z)

#vstack : 수직연결. 행기준 연결
#hstack : 수평연결. 열기준 연결
print(np.vstack([x,y])) #열의 갯수가 동일해야함
print(np.hstack([x,z])) #행의 갯수가 동일해야함
#print(np.hstack([x,y])) #행의 갯수가 다름
#print(np.vstack([x,z])) #열의 갯수가 다름

#배열의 분리
#0~15까지의 값을 4행4열 배열로 생성
x = np.arange(16).reshape((4,4))
print(x)
upper,lower = np.vsplit(x,[2]) #2행분리
print(upper)
print(lower)

left,right = np.hsplit(x,[2]) #2열분리 
print(left)
print(right)