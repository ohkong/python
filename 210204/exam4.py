# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:18:44 2021

@author: user

exam4.py : 숫자를 입력받아 입력수까지 합을 출력하기
숫자를 입력받아 짝수합을 출력하기
"""
num = int(input("숫자를 입력하세요 : "))
sum1 = 0
sum2 = 0
for i in range(0,num+1):
   sum1 = sum1+i
   if i%2==0:
        sum2 = sum2+i
#for i in range(0,num+1,2):
#   sum2 = sum2 + i
print("1부터 num 까지의 총합 : ",sum1)
print("1부터 num 까지의 짝수합 : ",sum2)