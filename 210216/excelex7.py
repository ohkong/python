# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:57:05 2021

@author: user

excelex7.py : pandas를 이용하여 xls 파일 읽기.
            출력되는 excel 파일의 sheet를 여러개로 지정하기
"""
import pandas as pd
infile = "ssec1804.xls"
outfile = "ssec1804_bak.xls"
writer = pd.ExcelWriter(outfile)
df = pd.read_excel(infile,sheet_name=None,index_col=None)
for worksheet_name,data in df.items() :
    print("===",worksheet_name,"===")
    print(data)
    data.to_excel(writer,sheet_name=worksheet_name,index=False,header=False)
writer.save()
