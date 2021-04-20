# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 10:30:58 2021

@author: user

regularex3.py : 정규식 예제
"""
import re

str = "The quick brown fow jumps over the lazy dog Te Thhe Thhhe."
str_list = str.split()
print(str_list)
# T문자로 시작하고, 0 개이상의 h문자, e문자로 끝나는 패턴
pattern = re.compile("Th*e")
count =0
for word in str_list:
    if pattern.search(word):
        count += 1
print("결과 1 : {1:s}:{0:d} ".format(count, "갯수"))

#re.I : 대문자 구분 없이.
pattern = re.compile("Th*e",re.I)
count =0
for word in str_list:
    if pattern.search(word):
        count += 1
print("결과 2 : {1:s}:{0:d} ".format(count, "갯수"))

#결과2에 맞는 문자열 출력하기
print("결과 3 : ",end="")
for word in str_list:
    if pattern.search(word):
        print(word,end=",")
print()

#결과2에 맞는 문자열 출력하기
#(?P<match_word>Th*e) : 대소문자 구분없이 Th*e 패턴 match_word라는 패턴그룹으로 
pattern = re.compile("(?P<match_word>Th*e)",re.I)
print("결과 4 : ",end="")
for word in str_list:
    if pattern.search(word):
        print("{0}".format(pattern.search(word).group("match_word")), end=",")
print()

#pattern.sub : 값의 치환함.
#Th*e 패턴에 맞는 문장을 "a"로 치환하기
pattern = re.compile("Th*e")
#print("결과 5: {0}".format(pattern.sub("a", str)))
print("결과 5:",pattern.sub("a", str))
