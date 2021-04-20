# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:48:42 2021

@author: user

forex1.py : for 구문 연습. 구구단 출력하기
"""
i,j=0,0
#range(2,10) : 2 부터 9까지의 값
for i in range(2,10):
    print("%5d단" % i)
    for j in range(2,10):
        print("%2dX%2d=%3d" % (i,j,(i*j)))
    print()
