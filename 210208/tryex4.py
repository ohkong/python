# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:10:08 2021

@author: user

tryex4.py : 
    1. try문 수행 중 오류가 발생하면 except 구문 실행됨.
        오류가 없는 경우느 else 구문 실행
    2. 오류 발생시 무시하고, 어떤 구문도 실행되지 않도록 할때
        pass 예약어 사용
    3. raise 예약어 : 예외 강제 발생예약어
"""
try :
    age = int(input("나이를 입력하세요:"))
except : 
    print("나이가 아닙니다. 정확히 입력하세요")
else :
    if age <= 19 :
        print("미성년자 입니다.")
    else : 
        print("성인입니다.")

try :
    f = open("없는 파일","r")
except FileNotFoundError :
 #   print("파일은 없어도 됩니다.")
     pass