# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:13:11 2021

@author: user

listex2.py : 리스트 함수
"""
mylist=[30,10,20]
# %s : 문자열을 지정하는 형식지정문자
print("리스트:%s" % mylist)
mylist.append(40)
print("mylist.append(40) 리스트:%s" % mylist)

#pop : LIPO(stack) 관련함수.
print("pop() 메서드 결과:%s" % mylist.pop())
print("pop() 메서드 후 리스트:%s" % mylist)

mylist.sort()
print("mylist.sort() 후 리스트 : %s" % mylist)
mylist.reverse() #역순 재배치
print("mylist.reverse() 후 리스트 : %s" % mylist)

print("20값의 위치 : %d" % mylist.index(20)) #20값의 인덱스값 리턴
mylist.insert(2, 222)
print("mylist.insert(2, 222) 후 리스트 : %s" % mylist)
mylist.remove(222) #222 값을 제거
print("mylist.remove(222) 후 리스트 : %s" % mylist)
mylist.extend([77,77,99]) #리스트 추
print("mylist.extend([77,77,99]) 후 리스트 : %s" % mylist)
print("77값의 갯수 : %d " % mylist.count(77))