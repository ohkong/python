# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:11:20 2021

@author: user

numpyex5.py : 배열 사본 생성, 재구조화 예제 
"""
import numpy as np

x=np.random.randint(10,size=10)
x_sub=x[:2] #0,1인덱스를 가진 부분배열
print(x)
print(x_sub)
x_sub[0]=20 #부분배열을 변경시 원본배열도 변경됨
print(x)
print(x_sub)

#배열복사
x_cop = x.copy() #x배열 복사
x_cop[0]=100
print(x)
print(x_cop)

#배열의 재편성 : 재편성되는 배열의 요소의 수가 원본의 배열의 수와 같아야한다.
x2= x.reshape(5,2) #1차원 배열 => 2차원 배열로 재편성함.
print(x2)

#0부터 99까지의 임의의 수를 9개 가진 배열 a생성
#a 배열을 3행3열로 재편성한배열 b생성하기
a=np.random.randint(100,size=9)
print(a)
b=a.reshape(3,3)
print(b)