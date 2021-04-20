# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:42:19 2021

@author: user

mapex1.py : 리스트의 각각의 요소를 변경함
"""
before = ["2021","02","08"]
print(type(before[0]))
print(before)
after = list(map(int,before))
print(type(after[0]))
print(after)
print(int("123"))