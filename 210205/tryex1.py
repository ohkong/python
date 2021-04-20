# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:12:55 2021

@author: user

tryex1.py : 예외 처리 예제
"""
mystr = "파이썬 공부 중입니다. 파이썬을 열심히 공부 합시다"
strops=[]
index=0
"""
while True:
    index = mystr.find("파이썬",index)
    if index == -1:
        break
    strops.append(index)
    index += 1
"""  
while True:
    try:
        index = mystr.index("파이썬",index)
        strops.append(index)
        index += 1
    except:
        break
    
print("파이썬 문자의 위치 :",strops,"문자의 갯수",len(strops))