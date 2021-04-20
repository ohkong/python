# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:59:07 2021

@author: user

drinkdataex1.py : 전세계 음주 데이터 분석하기
"""
import pandas as pd
import seaborn as sns

file_path = 'drinks.csv'

drinks = pd.read_csv(file_path) 

print(drinks.info()) #요약
print(drinks.describe()) #통계를 위한 상세 요약본
"""
    corr : 상관계수
    pearson : 표준 상관계수 
    kendall
    spearman
"""
corr = drinks[['beer_servings','wine_servings']].corr(method='pearson')
print(corr)

#모든 컬럼의 상관계수
cols = ['beer_servings','spirit_servings',
        'wine_servings','total_litres_of_pure_alcohol']
corr = drinks[cols].corr(method="pearson")
print(corr)

cols_view = ["beer","spirit","wine","alcohol"]
sns.set(font_scale=1.5)
hm=sns.heatmap(corr.values,cbar=True,annot=True,square=True,
               fmt=".2f",annot_kws={'size':15},
               yticklabels=cols_view,
               xticklabels=cols_view)