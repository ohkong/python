# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:47:23 2021

@author: user

listex1.py : 리스트예제(배열)
    자바 컬렉션          파이썬
     List               list : []
     Map                dictionary : {key,value}
     Set                set : {value}
                        touple : () 상수화(변경불가)된 리스트
"""
a=[0,0,0,0] #리스트
b=[] #리스
print(b,len(b))
suma,sumb=0,0 #변수 초기화
for i in range(0,len(a)): #i : 0~3
    #str(int) : 정수형을 문자열형으로 변환 함수
    a[i]=int(input(str(i+1)+"번째 값:"))
    suma+=a[i]
    b.append(a[i]) #리스트추가
    sumb+=b[i]
print(a)
print(b,len(b))
print("a 리스트 합계:",suma)
print("b 리스트 합계:",sumb)