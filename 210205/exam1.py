# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:43:16 2021

@author: user
exam1.py : 
    aa,bb리스트를 생성하고,
    aa리스트는 0부터 짝수 100개를 저장하고
    bb리스트는 aa리스트의 역순으로 값을 저장하기
    aa[0] - aa[9], bb[99] - bb[90] 값을 출력하기
"""
aa=[]
bb=[]
value=0
for i in range(0,100):
    aa.append(value)
    value+=2
for i in range(0,100):
    bb.append(aa[99-i])
for i in range(0,10):
    print("aa[%2d]=%2d" % (i,aa[i]),end=",")
print()
for i in range(99,89,-1):
    print("bb[%2d]=%2d" % (i,bb[i]),end=",")