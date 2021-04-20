# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 14:56:34 2021

@author: user

classex5.py : 클래스에서 사용되는 특별한 메서드

    생성자   : __init__(self,...)
    소멸자   : __del__(self)
    문자열화 : __repr__(self)
    +       : __add__(self,other)
    -       : __sub__(self,other)
    <       : __lt__(self,other)
    >       : __gt__(self,other)
    ==      : __eq__(self,other)
"""
class Line : 
    length = 0
    def __init__(self,length) :
        self.length = length
    def __repr__(self):
        return "선의 길이:"+str(self.length)
    def __add__(self,other):
        print("+ 연산자 호출")
        return self.length + other.length
    def __lt__(self,other):
        return self.length < other.length
    def __gt__(self,other):
        return self.length > other.length
    def __eq__(self, other):
        return self.length == other.length
    #소멸자 : 객체 제거시 호출되는 메서드
    def __del__(self):
        print(self.length,"길이 선이 제거 되었습니다.")
        
myline1 = Line(200) # __init__ 호출. 생성자 : 객체생성시 호출되는 메서드 
myline2 = Line(100)
print(myline1) #__repr__(self) : 자바의 toString 메서드기능 
print(myline2)
print("두선의 길이의 합:",myline1+myline2) #__add__호출
print("두선의 길이의 합:",myline1.__add__(myline2)) 
if myline1 < myline2 : #__lt__호출
    print("mylien2 선이 더 깁니다.")
elif myline1 == myline2 :   #__eq__호출
    print("myline1과 mylien2 선의 길이는 같습니다.")
else :
    print("mylien1 선이 더 깁니다.")
    
if myline1.__lt__(myline2) : #__lt__호출
    print("mylien2 선이 더 깁니다.")
elif myline1.__eq__(myline2) :   #__eq__호출
    print("myline1과 mylien2 선의 길이는 같습니다.")
elif myline1.__gt__(myline2) :
    print("mylien1 선이 더 깁니다.")
    
print("프로그램 종료")
#생성된 모든 객체들이 제거됨. 소멸자 호출 