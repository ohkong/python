# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:29:15 2021

@author: user

test6.py
컴퓨터가 임의의 서로다른 숫자 4개를 저장하고, 
화면에서 서로다른 4자리 숫자를 입력받아 
입력받은 숫자와 저장된 숫자를 비교하여 같은 숫자가 있는 경우 
자리수가 맞으면 strike, 자리수가 틀리면 
ball로 출력하는 프로그램 작성하기. 
컴퓨터가 저장한 숫자를 몇번만에 맞췄는지 입력횟수를 출력하기

컴퓨터 저장 숫자 : [0, 2, 6, 7]  인경우

서로다른 4자리 숫자를 입력하세요: 1234
Strike: 1 Ball: 0

서로다른 4자리 숫자를 입력하세요: 5678
Strike: 0 Ball: 2

서로다른 4자리 숫자를 입력하세요: 1678
Strike: 0 Ball: 2

서로다른 4자리 숫자를 입력하세요: 5278
Strike: 1 Ball: 1

서로다른 4자리 숫자를 입력하세요: 0267
5 번만에 맞췄습니다.
"""
import random

list1 = []
set = set(list1)
while len(set)<4 : #중복데이터 배제
    rnum = random.randrange(0,10) # 0-9까지의 임의의 수
    set.add(rnum)
list1 = list(set) #순서 유지
print(list1) #컴퓨터가 저장한 수
cnt = 0
while True :
    number = input("서로다른 4자리 숫자를 입력하세요: ")
    cnt += 1
    strike = 0
    ball = 0
    for n in number :
        num = int(n)
        if list1.count(num) == 1 : #list1 값에 num 값의 갯수. 존재
            if number.find(n) == list1.index(num): #위치 같은 경우
                strike += 1
            else :
                ball += 1
                
    if(strike == 4):
        break
    else : 
        print("Strike:",strike,"Ball",ball)

print(cnt,"번 만에 맞췄습니다.")