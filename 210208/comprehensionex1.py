# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:13:58 2021

@author: user

comprehensionex1.py : 컴프리헨션 예제
패턴이 있는 list, dictionary, set을 간편하게 작성할 수 있는 기능
"""
numbers = []
for n in range(1,11) :
    numbers.append(n)
print(numbers)
#컴프리헨션 표현
print([x for x in range(1,11)])
clist = [x for x in range(1,11)]
print(clist)

#1 ~ 10 까지의 짝수 리스트 작성하기. for 구문으로 작성하기
evenlist=[]
#for x in range (2,11,2):
#    evenlist.append(x)
for x in range (2,11):
    if(x%2==0):
        evenlist.append(x)
print(evenlist)
#컴프리헨션 표현
evenlist=[x for x in range (1,11) if x%2==0]
print(evenlist)

# 2의 배수이고, 3의 배수인 값만 리스트에 추가하기
list23=[x for x in range (1,11) if x%2==0 if x%3==0]
print(list23)

#중첩사용 컴프리헨션
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
# row : [1,2,3]
# x : 1
list1 = [x for row in matrix for x in row]
print(list1)

#컴프리헨션 표현식을 사용하지 않음
list1=[]
for row in matrix:
    for x in row:
        list1.append(x)
print(list1)

colorlist=['black','white','blue']
sizelist=["S","M","L"]
dresslist=((c,s) for c in colorlist for s in sizelist)
for d in dresslist :
    print(d)