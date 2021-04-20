# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:04:54 2021

@author: user

lambdaex2.py : 람다식을 이용한 리스트 처리
"""
mylist=[1,2,3,4,5]

def add10(num):
    return num+10

for i in range(len(mylist)):
    mylist[i]=add10(mylist[i])
print(mylist)

add=lambda num:num+10
for i in range(len(mylist)):
#    mylist[i] = add(mylist[i])
    mylist[i] = (lambda num:num+10)(mylist[i])
print(mylist)