# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:01:26 2021

@author: user

exam1.py : beer_servungs 대륙별, 평균, 최소, 최대,합계를 구하고,
        막대그래프로 출력허가 
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'drinks.csv'
drinks = pd.read_csv(file_path)

result = drinks.groupby('continent').\
    beer_servings.agg(['mean','min','max','sum'])
print(result)

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
#rects4 = plt.bar\
#    (index+bar_width*3,sums,bar_width,color='y',label='Sums')
    
plt.xticks(index,result.index.tolist())
plt.legend()
plt.title("beer_servings")
plt.show()