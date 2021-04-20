# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:42:41 2021

@author: user

exam5.py : 삼각형의 높이를 입력받은후 삼각형을 출력하는 
            프로그램 작성
삼각형의 높이를 입력하세요 : 3
*
**
***
"""
star = int(input("삼각형의 높이를 입력하세요 : "))
for i in range(1,star+1):
    print("*"*i)
print()
for i in range(star,0,-1):
    print("*"*i)

