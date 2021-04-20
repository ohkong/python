# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:17:17 2021

@author: user
test3.py
3. sales_2013.xlsx 파일의 모든 sheet의  열이 
"Customer Name", "Sale Amount" 컬럼만 
sales_2013_allamt.xlsx 파일로 저장하기 
"""
import pandas as pd

infile="sales_2013.xlsx"
outfile="sales_2013_oneamt.xlsx"
writer = pd.ExcelWriter(outfile)
df = pd.read_excel(infile,sheet_name=None,index_col=None)
row_output=[]
for worksheet_name,data in df.items() :
    print("===",worksheet_name,"===")
    data_value = data.loc[:,["Customer Name","Sale Amount"]]
    row_output.append(data_value)
filtered_row = pd.concat(row_output,axis=0,ignore_index=True)
filtered_row.to_excel(writer,sheet_name="sales_2013_allamt",index=False)
writer.save()

