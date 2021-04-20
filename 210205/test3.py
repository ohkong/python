# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:28:08 2021

@author: user

test3.py
나라와 수도를 등록하고 화면에 나라이름을 
입력받아 해당 나라의 수도를 출력하기
등록된 나라가 아닌 경우 수도를 입력받아 등록하기.
나라 입력시 "종료" 입력되면 프로그램 종료.
종료시 등록된 모든 나라와 수도정보를 화면 출력하기. 
"""

country = {} #dictionary
while True :
    indata = input(str(list(country.keys()))+ " 수도를 알고 싶은 나라는?")
    if indata in country : #country의 dictionary의 키정보 
        print("<%s> 나라의 수도는 <%s> 입니다." 
              %(indata,country.get(indata)))            
    elif indata=="종료":
        for i in country.keys():
            print("%s => %s " %(i,country[i]))
        break
    else:
        print("등록된 나라가 아닙니다.")
        yn = input("수도를 등록하시겠습니까?(y/n)")
        if yn=='y':
            f = input("수도이름을 입력하세요")
            country[indata] = f