# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:49:43 2021

@author: user

classex6.py : 추상메서드
                부모클래스의 멤버 메서드를 자손 클래스에서 구현함 pass
"""
class SuperClass :
    # raise NotImplementedError : 오버라이딩안하면 예외 발생
    def method(self): #추상메서드
        raise NotImplementedError #반드시 오버라이딩 해야함
#Subclass1 클래스 생성하기. SuperClass의 하위클래스. 부모와 같은 멤버를 가진다.
class Subclass1(SuperClass) :
#    pass
    def method(self):
        print("SubClass1에서 method 함수를 오버라이딩 함.")

sub1 = Subclass1()
sub1.method()