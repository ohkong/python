# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:32:16 2021

@author: user

excelex5.py : pandas를 이용하여 excel 파일 읽고 쓰기 
"""
import pandas as pd

infile = "sales_2015.xlsx"
outfile = "sales_2015_pd.xlsx"
df = pd.read_excel(infile,"january_2015",index_col=None)
print(df)
df_value = df[df["Sale Amount"].astype(float)>500.0]
writer = pd.ExcelWriter(outfile, engine="openpyxl")
df_value.to_excel(writer,sheet_name="jan_15_out",index=False)
writer.save()