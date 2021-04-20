# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:36:50 2021

@author: user

cctvex2.py : 서울시 구별 CCTV 현황 분석하
"""
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib import rc

rc('font', family="Malgun Gothic")
CCTV_Seoul = pd.read_csv('CCTV_in_Seoul.csv',encoding='utf-8')
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0]:'구별'},inplace=True)
pop_Seoul = pd.read_excel('population_in_Seoul.xls',
                          header=2,usecols='B,D,G,J,N')
pop_Seoul.rename(columns={pop_Seoul.columns[0]:'구별',
                          pop_Seoul.columns[1]:'인구수',
                          pop_Seoul.columns[2]:'한국인',
                          pop_Seoul.columns[3]:'외국인',
                          pop_Seoul.columns[4]:'고령자'},inplace=True)
pop_Seoul.drop([26],inplace=True)
#구별 컬럼을 이용하여 두개의 데이터를 합병하기
data_result = pd.merge(CCTV_Seoul, pop_Seoul,on='구별')
data_result.set_index('구별',inplace=True)

#1차원 함수.
fp1=np.polyfit(data_result['인구수'],data_result['소계'],1)
#함수 생성
f1 = np.poly1d(fp1)
#1차원 함수에 입력할 값
fx=np.linspace(100000,700000,100)
#실제 CCTV갯수 - 1차원함수로 계산된 cctv갯수
#오차가 큰경우는 1차원 함수로 계산된 갯수와 차이가 많다.
data_result['오차'] = \
    np.abs(data_result['인구수'] - data_result['소계'])
df_sort = data_result.sort_values(by='오차',ascending=False)
print(df_sort.head())
plt.figure(figsize=(14,10))
plt.scatter(data_result['인구수'],data_result['소계'],
            c=data_result['오차'],s=50)
plt.plot(fx,f1(fx),ls='dashed',lw=3,color='g')
for n in range(10):
    plt.text(df_sort['인구수'][n]*1.02,df_sort['소계'][n]*0.98,
             df_sort.index[n],fontsize=15)

plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.colorbar()
plt.grid()
plt.show()