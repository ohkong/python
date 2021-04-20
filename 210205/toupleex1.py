# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:35:20 2021

@author: user

toupleex1.py : 튜플예제 : 변경불가 리스트
"""
tp1=(10,20,30)
print(tp1)
#tp1.append(10) #tuple은 변경 할 수 없음
list1=list(tp1) #tuple을 list로 변경
list1.append(40) #list 객체에 요소 추가
tp1=tuple(list1) #list를 tuple로 변경
print(tp1)
print("tp1의 크기=",len(tp1))
print("tp[1:3]=",tp1[1:3])
print("tp[:3]=",tp1[:3])
print("tp[2:]=",tp1[2:])
print("tp[::2]=",tp1[::2])
print(tp1[0],tp1[1],tp1[2])

a,b,c,d=tp1
print(a,b,c,d)
