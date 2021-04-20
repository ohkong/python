# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:17:01 2021

@author: user
test2.py
2. sales_2013.xlsx 파일의 january_2013 sheet의 중 
열이 "Customer Name", "Sale Amount" 컬럼만  
sales_2013_amt.xlsx 파일로 저장하기 
"""
import pandas as pd

infile="sales_2013.xlsx"
outfile="sales_2013_amt.xlsx"
df = pd.read_excel(infile,"january_2013",index_col=None)
df_value = df.loc[:,["Customer Name","Sale Amount"]]
writer = pd.ExcelWriter(outfile)
df_value.to_excel(writer,sheet_name="january_2013",index=False)
writer.save()
