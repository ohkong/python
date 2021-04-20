# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:06:55 2021

@author: user

drinkdataex3.py : 그룹단위 데이터 분석 
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'drinks.csv'
drinks = pd.read_csv(file_path)
"""
continent을 기준으로 그룹화. spirit_servings데이터 분석
mean(평균),min(최소값),max(최대값),sum(합계) => 집계
"""
result = drinks.groupby('continent').\
    spirit_servings.agg(['mean','min','max','sum'])
print(result)

#순수 알코올 평균
total_mean = drinks.total_litres_of_pure_alcohol.mean()
print(total_mean)

#대륙별 평균 알코올 섭취량 
continent_mean = drinks.groupby('continent').\
        total_litres_of_pure_alcohol.mean()
print(continent_mean)

#전체 평균보다 많은 알코올을 섭취하는 대륙
continent_over_mean=\
    continent_mean[continent_mean >= total_mean]
print(continent_over_mean)

#평균 beer_servings값이 가장 높은 대륙을 조회하기b
beer_continent = drinks.groupby('continent').beer_servings.\
        mean().idxmax()
print(beer_continent)

#대륙별 spirit_servings의 평균, 최소, 최대, 합계를 시각화합니다.
n_groups = len(result.index)
means = result['mean'].tolist()
mins = result['min'].tolist()
maxs = result['max'].tolist()
sums = result['sum'].tolist()

index = np.arange(n_groups)
bar_width = 0.1

rects1 = plt.bar\
    (index,means,bar_width,color='r',label='Mean')
rects2 = plt.bar\
    (index +bar_width, mins,bar_width,color='g',label='Min')
rects3 = plt.bar\
    (index + bar_width*2,maxs,bar_width,color='b',label='Max')
rects4 = plt.bar\
    (index+bar_width*3,sums,bar_width,color='y',label='Sums')
    
plt.xticks(index,result.index.tolist())
plt.legend()
plt.show()