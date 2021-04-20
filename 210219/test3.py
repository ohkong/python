# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:40:20 2021

@author: user

test3
"""
word = {}
while True :
    indata = input(str("영어단어를 입력하세요(종료:종료)"))
    if indata in word : 
        print("%s의 한글 뜻 : %s" 
              %(indata,word.get(indata)))          
    elif indata=="종료":
        for i in word.keys():
            print("'%s': '%s' " %(i,word[i]))
        break
    else:
        print("등록된 단어가 아닙니다.")
        yn = input("단어를 등록하시겠습니까?(y/n)")
        if yn=='y':
            f = input("단어의 뜻을 입력하세요")
            word[indata] = f
