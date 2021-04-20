# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:06:33 2021

@author: user

test3.py
파일 명을 입력받아 파일을 복사하는 프로그램 작성하기
[결과]
원본파일의 이름을 입력하세요 : test1.py
복사파일의 이름을 입력하세요 : test1.bak
복사완료
"""
inFp, outFp = None,None
inStr = ""
infile = input("원본파일의 이름을 입력하세요 : ")
outfile = input("복사본파일의 이름을 입력하세요 : ")
inFp = open(infile,"r",encoding='utf8')
outFp = open(outfile,"w",encoding='utf8')

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)
    
inFp.close()
outFp.close()
print("\n복사완료")