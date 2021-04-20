# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:45:16 2021

@author: user

excelex2.py : xlsx 파일의 모든 sheet 읽기 
""" 
import openpyxl
filename="sales_2015.xlsx"
book = openpyxl.load_workbook(filename)
#book.worksheets : excel 파일의 모든 sheet를 리턴
for i,sheet in enumerate(book.worksheets) :
    print(book.sheetnames[i])#sheet 이름
    data=[]
    for r,row in enumerate(sheet.rows) : #해딩sheet의 행값들.
        line=[]
        for i,c in enumerate(row) :
            line.append(c.value)
        print(r+1,":",line)
        data.append(line)
