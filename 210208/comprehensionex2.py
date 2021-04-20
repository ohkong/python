# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:56:23 2021

@author: user

comprehensionex2.py : 컴프리헨션을 이용한 set
"""
set1 = {x**2 for x in [1,1,2,2,3,3]}
print(set1)

list1 = [x**2 for x in [1,1,2,2,3,3]]
print(list1)

# 1부터 10까지의 수중 짝수의 제곱을 출력하기
set2 = {x**2 for x in range(1,11) if x % 2 == 0}
print(set2)
print(sorted(set2))