# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:13:57 2021

@author: user

excelex1.py : xlsx 파일 읽기

xlsx : import openpyxl
xls  :
"""
import openpyxl #pip install openpyxl
filename = "sales_2015.xlsx"
book = openpyxl.load_workbook(filename)
sheet = book.worksheets[0]
data=[]
for row in sheet.rows :
    line=[]
    for l,d in enumerate(row) :
        line.append(d.value)
    data.append(line)
#print(data)
#enumerate : 리스트에서 데이터와 index값을 제공함 
for i in range(0,len(data)) :
    print(i+1,":",data[i])
print("enumerate 함수 사용")
for i,d in enumerate(data) :
    print(i+1,":",d)


