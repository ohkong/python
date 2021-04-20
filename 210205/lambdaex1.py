# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:51:39 2021

@author: user

lambdaex1.py : 람다식으로 함수 구현
"""
def hap(num1,num2):
    res = num1 + num2
    return res

print(hap(10,20))

hap1 = lambda num1,num2:num1+num2 #람다식으로 작성된 함수
print(hap1(10,20))

#람다 방식으로 곱셈출력하기
mul = lambda num1,num2:num1*num2
print(mul(10,20))

#매개변수의 기본값 설정하기
hap2=lambda num1=0,num2=1:num1+num2
print(hap2())
print(hap2(100))
print(hap2(100,200))
