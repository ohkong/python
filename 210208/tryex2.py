# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:48:18 2021

@author: user

tryex2.py: 다중 예외 처리 

"""
num1 = input("문자1 입력: ") #문자 1 입력받기
num2 = input("문자2 입력: ") #문자 2 입력받기

try :
    num1 = int(num1) #정수형으로 변환
    num2 = int(num2)
    while True :
        res = num1 / num2
        print(res)
except ValueError as e : # e변수에 예외객체 저장
    print("문자를 숫자로 변환할 수 없습니다.")
    print(e)
except ZeroDivisionError as e :
    print("0으로 나눌 수 없습니다.")
    print(e)
except KeyboardInterrupt as e :
    print("Ctrl + c 가 눌렸습니다.")
    print(e)
finally : #정상, 오류발생 모두 실행되는 블럭
    print("프로그램 종료")