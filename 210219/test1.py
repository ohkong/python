# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:33:28 2021

@author: user

test1
"""
num = int(input("삼각형의 높이를 입력하세요 => "))
for i in range(0, num):
    for j in range(0, i):
        print(' ', end = '')
    for k in range(0, (num*2-1) - i * 2):
        print('*', end = '')
    print()