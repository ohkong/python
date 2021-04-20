# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:34:27 2021

@author: user

yieldex1.py : 함수의 종료 없이, yield로 값 리턴
"""
def getFun(num) : 
    for i in range(10,num+10) : 
        yield i #i변수의 값을 전달. 리턴하지 않음
        print(i, "값 반환")
        
print(list(getFun(5)))

for data in getFun(5) :
    print("main에서 출력 : ",data)
