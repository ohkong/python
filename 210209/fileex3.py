# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:39:32 2021

@author: user

fileex3.py : 파일 존재 여부 확인하기
"""
import os.path

#file = 'C:\\Data\\Python\\nofile.txt'
file = "regularex3.py" #상대경로 
file = "D:\\20200914\\hadoophome" #절대경로
if os.path.isfile(file):
    print("Yes. it is a file")
elif os.path.isdir(file):
    print("Yes. it is a directory")
    
if os.path.exists(file):
    print("Somthing exist")
else :
    print("Nothing")
print(os.path.basename(file))