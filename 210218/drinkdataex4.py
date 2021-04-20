# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:08:56 2021

@author: user

drinkdataex4.py : 대륙별 total_litres_of_pure_alcohol을 시각화
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'drinks.csv'
drinks = pd.read_csv(file_path)

total_mean = drinks.total_litres_of_pure_alcohol.mean()
continent_mean = drinks.groupby('continent')\
    ['total_litres_of_pure_alcohol'].mean()
#대륙명 코드
continents = continent_mean.index.tolist()
continents.append('mean')

x_pos = np.arange(len(continents)) #0~continents갯수
alcohol = continent_mean.tolist()
alcohol.append(total_mean)#전체평균
#alpha : 투명도 1:불투명

bar_list = plt.bar(x_pos,alcohol,align='center',alpha=0.5)

#마지막막대의 색을 빨강으로 설정
bar_list[len(continents)-1].set_color('r')
#선그래프 설정 total_mean값에 해당하는 부분에 선그래프 설정
plt.plot([0.,6],[total_mean,total_mean],"k--")
plt.xticks(x_pos,continents) # x축 이름 설정

plt.ylabel('total_litres_of_pure_alcohol')
plt.title('total_litres_of_pure_alcohol by Continent')

plt.show()