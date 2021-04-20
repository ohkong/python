# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:06:47 2021

@author: user

numpyex3.py : numpy 에서 사용되는 함수 
"""
import numpy as np

a = np.arange(12).reshape(3,4)
print(a)
print(a.sum(axis=0)) #합계. axis=0, 컬럼기준
print(a.sum(axis=1)) #합계. axis=0, 행기준
print(a.max(axis=0)) #최대값. axis=1. 컬럼기준
print(a.max(axis=1)) #최대값. axis=1. 행기준
print(a.min(axis=1)) #최소값. axis=1. 행기준
print(a.cumsum(axis=1)) #누적합 행기준

b=np.arange(3)
print(b)
print(np.exp(b)) #로그
print(np.sqrt(b)) #제곱근

c=np.array([2,-1,4])
print(c)
print(b+c)
print(np.add(b,c))

#평균 0, 표준편차 1인 정규 분포를 따르는 3행3열 난수
d = np.random.normal(10,1,(3,3))
print(d)

#0~10 구간의 임의의 정수를 가진 3행3열 배열 생성
e = np.random.randint(0,10,(3,3))
print(e)