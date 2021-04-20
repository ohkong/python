# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:27:16 2021

@author: user

test2.py
주어진 자연수 N에 대해 N이 짝수이면 N!을, 
홀수이면 ΣN을 구하는 코드를 작성하기
"""
def calculator(n) :
    if n % 2 == 0:
        result = 1
        for i in range(1,n+1):
            result = result * i
    else:
        result = 0
        for i in range(1, n+1):
            result = result + i
    return result

num = int(input("숫자를 입력하세요 : "))
print(calculator(num))