# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:48:46 2021

@author: user

mapex2.py
"""
mylist = [1,2,3,4,5]
add = lambda num:num+10
mylist = list(map(add,mylist))
print(mylist)

#num: mylist의 요소값 한개
mylist = list(map(lambda num:num-10,mylist))
print(mylist) # [1,2,3,4,5]
mylist = list(map(lambda num:num*10,mylist))
print(mylist)

list1=[1,2,3,4]
list2=[10,20,30,40]
hap=lambda n1,n2:n1+n2
haplist=list(map(hap,list1,list2))
print(haplist)

#haplist = mylist + list1 + list2
list1.append(0)
list2.append(0)
hap=lambda n1,n2,n3:n1+n2+n3
haplist=list(map(hap,list1,list2,mylist))
print(haplist)
