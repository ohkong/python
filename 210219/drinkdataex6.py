# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:41:46 2021

@author: user

drinkdataex6.py : 대한민국 순위 확인 
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = '../210218/drinks.csv'
drinks=pd.read_csv(file_path)
print(drinks.info())

#total_servings(총 주류 소비량) 컬럼을 생성
drinks['total_servings'] = drinks['beer_servings']\
        +drinks['wine_servings']+drinks['spirit_servings']

#술소비량 대비 알콜 비율 컬럼들 생성
drinks['alcohol_rate']=drinks['total_litres_of_pure_alcohol']\
                / drinks['total_servings']
print(drinks.info())
#fillna : null값인 경우 0으로 변경.
drinks['alcohol_rate'] = drinks['alcohol_rate'].fillna(0)

#순위 정보를 생성
country_with_rank = drinks[['country','alcohol_rate']]
country_with_rank = country_with_rank.sort_values\
        (by=['alcohol_rate'], ascending=0)
print(country_with_rank.head(5))

#국가별 순위 정보를 그래프로 시각화 합니다.
#country 컬럼만 리스트로 저장
country_list = country_with_rank.country.tolist()
x_pos = np.arange(len(country_list))
#alcohol_rate 컬럼만 리스트로 저장 막대그래프로 작성할 데이터
rank = country_with_rank.alcohol_rate.tolist()

bar_list = plt.bar(x_pos,rank) #막대그래프 그리기
#South Korea 에 해당되는 막대그래프의 색을 빨강색으로 설정.
bar_list[country_list.index("South Korea")].set_color('r')
plt.ylabel('alcohol rate')
plt.title('liquor drink rank by country')
plt.axis([0,200,0,0.3])

korea_rank = country_list.index("South Korea")
korea_alc_rate = country_with_rank[country_with_rank['country']==\
                                   'South Korea']['alcohol_rate'].values[0]
plt.annotate('South Korea : ' + str(korea_rank + 1),
              xy=(korea_rank, korea_alc_rate),
              xytext=(korea_rank+10, korea_alc_rate+0.05),
              arrowprops=dict(facecolor='red',shrink=0.05))
plt.show()