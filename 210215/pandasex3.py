# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:11:15 2021

@author: user

pandasex3.py : supplier_data.csv 파일을 
                pandas를 이용하여 읽고 화면에 출력하기
"""
import pandas as pd

infile = "supplier_data.csv"
df = pd.read_csv(infile)
print(df)

importdate = ["1/20/14","1/30/14"]
#isin : 주어진 값이 맞는지? boolean값으로 리턴.
print(df["Purchase Date"].isin(importdate))
df_inset = df.loc[df["Purchase Date"].isin(importdate),:]
print(df_inset)

print(df["Invoice Number"].str.startswith("920-"))
df_inset = df.loc[df["Invoice Number"].str.startswith("920-"),:]
print(df_inset)
print(type(df_inset))
#pandas 데이터를 csv 파일로 생성
df_inset.to_csv("pandas_out3.csv",index=False)