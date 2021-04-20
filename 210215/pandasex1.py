# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:40:18 2021

@author: user
pandasex1.py : pandas를 이용하여 csv파일 읽기 
"""
import pandas as pd

infile = "jeju1.csv"
df = pd.read_csv(infile)
print(df)
print(type(df))
#경도만 출력
print(df["LON"])
#위도만 출력
print(df["LAT"])
#장소만 출력
print(df["장소"])

#3행만 출력
print(df.iloc[3])