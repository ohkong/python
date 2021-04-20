# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:00:06 2021

@author: user
exam3.py : 가로 구구단 출력 하기
"""
i,j=0,0
for i in range(2,10):
    print("%6d단%5s" %(i," "),end="")
for j in range(2,10):
    for i in range(2,10):
        print("%2d X%2d =%3d " % (i,j,(i*j)), end="")
    print()

