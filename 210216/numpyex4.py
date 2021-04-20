# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:49:21 2021

@author: user

numpyex4.py : 
"""
import numpy as np

x=np.arange(10)
print(x)
print(x[:5]) #0부터 4인덱스까지 부분 배열
print(x[5:]) #5부터 끝까지 부분 배열
print(x[4:7]) #4부터 6인덱스까지 부분 배열
print(x[:2]) #0부터 끝인덱스까지 2씩 증가한 부분배열
print(x[1::2]) #1부터 끝인덱스까지 2씩 증가한 부분배열
print(x[1:8:3]) #1부터 7인덱스까지 3씩 증가한 부분배열
print(x[::-1]) #끝부터 0인덱스까지 역순인 배열 

print("0부터 9까지의 난수를 4행 5열 배열로 생성")
#x = np.random.randint(0,10,(4,5))
x = np.random.randint(10,size=(4,5))
print(x)

#2개의 행과 3개의 열을 가진 부분배열
print()
print(x[:2,:3])

#모든 행을 한개씩 걸러서 열 조회하기
print()
print(x[:,::2])

#행과 열 모두 역으로 조회하기.
print()
print(x[::-1,::-1])