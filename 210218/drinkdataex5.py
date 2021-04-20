# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:59:23 2021

@author: user

drinkdataex5.py : 
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'drinks.csv'
drinks=pd.read_csv(file_path)
#total_servings 컬럼 생성하기 
drinks['total_servings'] = drinks['beer_servings']\
        +drinks['wine_servings']+drinks['spirit_servings']
print(drinks)

#술소비량 대비 알콜 비율(alcohol_rate) 컬럼 생성 
#
#alcohol_rate = 
#total_litres_of_pure_alcohol / total_servings
drinks['alcohol_rate']=drinks['total_litres_of_pure_alcohol']\
                / drinks['total_servings']
print(drinks.info())

#alcohol_rate이 null 인 경우 0으로 변경
drinks['alcohol_rate'] =drinks['alcohol_rate'].fillna(0)
print(drinks.info())