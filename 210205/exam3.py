# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:54:31 2021

@author: user

exam3.py : 리스트의 값의 합과 평균을 구하는 함수 작성하기
"""
def getSum(l):
#    sum =0
#    for i in range(0,len(l)):
#        sum+=l[i]
    return sum(l)

def getMean(l):
#    sum =0
#    avg=0
#    for i in range(0,len(l)):
#        sum+=l[i]
#    avg=sum/len(l)
#    return avg
    if len(l)>0:
        return sum(l)/len(l)
    else :
        return 0
#    return sum(l)/len(l) if len(l)>0 else 0
list=[2,3,3,4,4,5,5,6,6,8,8]
print("list의 값의 합",getSum(list))
print("list의 값의 평균",getMean(list))

list2=[]
print("list2의 값의 합",getSum(list2))
print("list2의 값의 평균",getMean(list2))

tp=[2,3,3,4,4,5,5,6,6,8,8]
print("tp의 값의 합",getSum(tp))
print("tp의 값의 평균",getMean(tp))