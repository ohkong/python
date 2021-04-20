# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:26:05 2021

@author: user

test1.py
피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) : 5
[0,1,1,2,3]

피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) : 10
[0,1,1,2,3,5,8,13,21,34]
"""

def fibo(n) :
    fibolist=[]
    num1 = 0
    num2 = 1
    num3 = num1+num2
    fibolist.append(num1)
    fibolist.append(num2)
    fibolist.append(num3)
    for i in range(3,n):
        num1 = num2
        num2 = num3
        num3 = num1 + num2
        fibolist.append(num3)
    return fibolist

num = int(input("피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) :"))
print("f(",num,")=",end="")
print(fibo(num))