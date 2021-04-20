# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:39:45 2021

@author: user

exam2.py : 대륙코드를 입력받아 대륙별 레코드만 파일로 저장힉;
    AF, AS, EU, OC, SA
"""
import pandas as pd

file_path = 'drinks.csv'
drinks=pd.read_csv(file_path)

con = input("대륙코드를 입력하세요:(AF, AS, EU, OC, SA)")
conts = drinks.loc[drinks['continent']==con]
print(conts)
conts.to_csv(con+".csv",index=False)