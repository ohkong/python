# -*- coding: utf-8 -*-
"""
    여러줄 주석
    1. 변수 선언 필요 없음
    2. {} 블럭이 없음
        if, 반복문 {} 가 없다 => 공백으로 블록 표시
    3. 주석
        """ """ : 여러줄 주석
        # : 한줄 주석
"""

print("Hello world")
"""
    input(문자열):문자열이 화면에 표시되고, 콘솔에서 값 입력
"""
sel = int(input("입력 진수 결정(16/10/8/2) :"))
num = input("값 입력:")
if sel == 16:
    num10 = int(num,16)
if sel == 10:
    num10 = int(num,10)
if sel == 8:
    num10 = int(num,8)
if sel == 2:
    num10 = int(num,2)
print(num10)
print(type(num))
print(type(num10))
num = num10
print(num)
print(type(num))
#10 진수를 진법의 값으로 출력
print("16진수=>",hex(num10))
print("8진수=>",oct(num10))
print("2진수=>",bin(num10))