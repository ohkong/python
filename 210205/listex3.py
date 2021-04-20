# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:03:49 2021

@author: user

lietex3.py : 문자열 분리
"""
ss="2021/02/05"
print("10년 년도 출력하기")
list=ss.split("/")
print("10년전 : ",int(list[0])-10)

ss="(홍길동)" # 홍#길#동# 출력하기
for i in range(1,len(ss)-1):
    print(ss[i],end="#")
print()
#for문 사용 없이 동길홍 출력하기
print(ss[len(ss)-2:0:-1])

ss="홍길동"
if ss.startswith("(") ==False:
    print("(",end="")
print(ss,end="")
if ss.endswith(")") ==False:
    print(")")