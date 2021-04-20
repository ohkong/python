# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:40:06 2021

@author: user

numpyex1.py  : numpy 기본
"""
import numpy as np
#np.arange(15) : 0~14까지의 숫자
#reshape(3,5) : 3행 5열의 배열로 설정 
a=np.arange(15).reshape(3,5)
print(a)
print(a.shape) # (3,4) 리스트의 구조. 
print(a.ndim) # 2차원 
print(a.dtype.name) # a 리스트의 요소의 자료형 이름
print(a.itemsize) # a 리스트의 요소의 크기 바이트 단위
print(a.size) # a 리스트의 요소의 갯수
print(type(a))
#np.array 배열을 생성.
b=np.array([6,7,8])
print(b)
print(type(b))

print(b.dtype)

c=np.array([1.2,3.5,5.1])
#c 배열의 요소의 자료형 출력하기
print(c.dtype)

#튜플을 이용하여 배열 생성
d=np.array([(1.5,2,3),(4,5,6)])
print(d)
print(d.dtype)

#리스트를 이용하여 배열 생성
e=np.array([[1,2],[3,4]],dtype=complex)
print(e)
print(e.dtype)

#3행 4열 2차원 배열을 생성하고 0으로 초기화
f=np.zeros((3,4))
print(f)
print(f.dtype)

#3차원 배열 생성. 요소를 1로 초기화
g=np.ones((2,3,4),dtype=np.int16)
print(g)
print(g.dtype)

#arange 함수를 이용하여 10부터 29까지의 수중 5의 배수로만 이루어진 배열 생성하기 
h=np.arange(10,30,5)
print(h)
print(h.dtype)

#arange(s,e,d) : s부터 e앞까지 d만큼 증가한 수들의 목록
i=np.arange(0,2,0.3)
print(i)
print(i.dtype)

#linspace(s,e,d) : s부터 e까지의 수를 d등분하기
#                   0~2까지를 균등하게 9등분한 숫자들의 목록.
j=np.linspace(0,2,9)
print(j)
print(j.dtype)

print(np.pi) # 원주율
#0~2 pi까지의 수를 100개 가져오기

k=np.linspace(0,2*np.pi,100)
print(k)
print(k.dtype)

#출력되는양이 많아지면 ...표시됨.
print(np.arange(10000))

#0~9999까지의 수를 100행 100열 배열로 생성하여 출력하기
print(np.arange(10000).reshape(100,100))