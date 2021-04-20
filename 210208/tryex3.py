# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:02:29 2021

@author: user
tryex3.py : 다중처리를 하나의 변수로 묶기
"""
try : 
    a=[1,2]
    print(a[1])
#    4/0
    b=int("a")
except (ZeroDivisionError, IndexError) as e :
    print(e)
except ValueError :
    print("정수 값만 가능합니다.")