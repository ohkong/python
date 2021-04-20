# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:48:44 2021

@author: user

pandasex2.py : pandas 이해하기
"""
import pandas as pd

df = pd.DataFrame({"A":[1,4,7],"B":[2,5,8],"C":[3,6,9]})
print(df)
print(df["A"])
# 행 선택
# iloc[인덱스] : 인덱스 기준으로 조회
# loc[이름기준] : 행의 이름 기준으로 조회
print("행의 인덱스값으로 조회하기")
print("df.iloc[0]=",df.iloc[0])
print("df.iloc[1]=",df.iloc[1])
print("df.iloc[2]=",df.iloc[2])

print()
print("df.loc[0]=",df.loc[0])
print("df.loc[1]=",df.loc[1])
print("df.loc[2]=",df.loc[2])

df = pd.DataFrame(data=([[1,2,3],[4,5,6],[7,8,9]]),
                  index=[2,"A",4],columns=[51,52,54])
print(df)
