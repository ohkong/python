# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:55:51 2021

@author: user

test2.py
입력된 자연수가 홀수인지 짝수인지 판별해 
주는 함수를 람다식을 이용하여 작성해 보자.
"""
x = int(input("자연수를 입력하세요 : "))

if((lambda x : True if x % 2 == 1 else False)(x)):
    print(x,"숫자는 홀수 입니다")
else:
     print(x,"숫자는 짝수 입니다")