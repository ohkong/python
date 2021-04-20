# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:50:58 2021

@author: user

fileex4.py : 모듈을 이용하여 폴더 조회하기
"""
import os.path

print("폴더 목록 보기: os.walk 모듈 사용")
for dirName, subDirList, fnames in os.walk("D:\\20200914\\hadoophome\\bin"):
    for fname in fnames:
        print(os.path.join(dirName,fname))
    print(type(subDirList))
    print(subDirList)
