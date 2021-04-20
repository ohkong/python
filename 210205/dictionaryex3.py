# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:58:04 2021

@author: user
dictionaryex3.py : 정렬하기
"""
import operator
dic,list={},[]
dic={"Thomas":"토마스","Edward":"애드워드","Henry":"헨리",
     "Gothen":"고든","James":"제임스"}
list=sorted(dic.items(),key=operator.itemgetter(0),reverse=True)
print(list)
print("영문이름으로 정렬하기")
list=sorted(dic.items(),key=operator.itemgetter(0),reverse=False)
print(list)
print("한글이름으로 정렬하기")
list=sorted(dic.items(),key=operator.itemgetter(1))
print(list)
print("한글이름 역순으로 정렬하기")
list=sorted(dic.items(),key=operator.itemgetter(1),reverse=True)
print(list)

