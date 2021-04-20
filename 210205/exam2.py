# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:33 2021

@author: user

exam2.py : 간단한 계산기 함수
"""
oper = input("연산자를 선택하세요:(+,-,*,/) =>")
var1 = int(input("첫번째 수=>"))
var2 = int(input("두번째 수=>"))
def calc(v1,v2,op):
    re = 0
    if op=='+':
        re = v1 + v2
    elif op=='-':
        re = v1 - v2
    elif op=='*':
        re = v1 * v2
    elif op=='/':
        re = v1 / v2
    return re
res = calc(var1,var2,oper)
#print("계산: %d %s %d = %f" % (var1,oper,var2,res))
print("계산:",var1,oper,var2,"=",res)
res = calc(10.5,3.4,"+")
print("계산",10.5,"+",3.4,"=",res)