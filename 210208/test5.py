# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:57:25 2021

@author: user
test5.py
1부터 1000까지의 홀수의 합계 계산시 최초로 1000이 넘는 숫자를
구하는 프로그램을 작성하기
"""
hap,i=0,0
for i in range(1,101,2):
    hap+=i
    if hap >= 1000:
        break
print("1~100의 홀수의 합에서 최초로 1000이 넘는 위치: %d, 합계: %d" % (i,hap))
