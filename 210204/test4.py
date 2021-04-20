# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:00:58 2021

@author: user

test4.py 
16진수를 입력하면 16진수 인지 아닌지 판단하여 16진수가 
        맞으면 10진수로 변경하는 프로그램을 작성하시오.
16진수가 아닌 경우 16진수 아님을 출력하기

16진수 입력 : ff
ff = 255
​
16진수 입력 : qw
qw 문자는 16진수 문자가 아닙니다
"""
num16 = input("16진수를 입력하세요 : ")
able16=True
for i in range(0,len(num16)):
    num = num16[i]
    if ('0' <= num and num <='9') or ('a' <= num and num <='f') or ('A' <= num and num <='F'):
        print(end="")
    else : 
        print(num16,"문자는 16진수 문자가 아닙니다")
        able16=False
        break
if able16:
    print(num16,"=",int(num16,16))
    