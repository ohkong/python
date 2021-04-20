# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:05:50 2021

@author: user

fileex1.py : 파일 읽기
"""
infp=None
inStr = ""
"""
    open("파일이름","파일모드",["인코딩방식"])
    파일모드
        "r" : 읽기 모드
        "w" : 쓰기 모드. 파일이 존재하지 않는 경우 생성.
              파일이 존재하는 경우 내용이 변경됨
        "a" : 쓰기 모드. append모드. 파일이 존재하지 않는 경우 생성.
              파일이 존재하는 경우 내용이 추가됨
        "t" : 텍스트 모드. 기본형
        "b" : 이진 모드 
"""
infp = open("regularex3.py","rt",encoding='UTF8')
while True : 
    inStr = infp.readline() #한줄 읽어서 inStr 변수 저장.
    if inStr == None or inStr=="": #EOF(End of File)
        break
    print(inStr,end="")
infp.close()