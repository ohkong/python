# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:50:41 2021

@author: user

pandasex4.py : pandas 파일의 행과열 선택
"""
import pandas as pd

infile = "supplier_data.csv"
df = pd.read_csv(infile)

df_col = df.iloc[:,[0,3]] # 모든행, 0번,3번열 조회
print("df.iloc[:[0,3]] => ")
print(df_col)

df_col = df.iloc[0:4,0:3] # 0~3인덱스행, 0~2인덱
print("df.iloc[0:4,0:3] => ")
print(df_col)

#Invoice Number값이 920- 시작하는 행의
#Invoice Number, Cost컬럼만 조회하기
#조건을 만족하는 데이터를 pandas_out4.csv 파일로 저장하기
df_col = df.loc[df["Invoice Number"].str.startswith("920-"),
                ["Invoice Number","Cost"]]
print(df_col)
df_col.to_csv("pandas_out4.csv",index=False)