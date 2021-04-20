# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:04:12 2021

@author: user

excelex8.py : 폴더에 속한 excel 파일들을 읽어서 하나의 excel 파일로 생성
"""
import pandas as pd
import glob
import os
inpath="D:/20200914/pythonfile/excel"
outfile="sales_all.xlsx"
excels=glob.glob(os.path.join(inpath,"*.xls"))
print(type(excels))
rows=[]
for excel in excels :
    print(excel)
    dfs = pd.read_excel(excel,sheet_name=None,index_col=None)
    for sheet_name,df in dfs.items() :
        rows.append(df)

df_concat = pd.concat(rows,sort=False,axis=0,ignore_index=True)
writer = pd.ExcelWriter(outfile)
df_concat.to_excel(writer,sheet_name="all_data_all_worksheet",index=False)
writer.save()