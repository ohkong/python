# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:06:39 2021

@author: user

test5.py
년도를 입력받아 윤년인지 평년인지 출력하기

년도를 입력하세요 : 2100
2100 : 평년

년도를 입력하세요 : 2000
2000 : 윤년

년도를 입력하세요 : 2020
2020 : 윤년

년도를 입력하세요 : 2021
2021 : 평년
"""
year = int(input("년도를 입력하세요 : "))
if(year%400==0) or ((year%4==0)and(year%100!=0)):
    print(year," : 윤년")
else:
    print(year," : 평년")
