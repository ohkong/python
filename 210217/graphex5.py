# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:33:01 2021

@author: user

graphex5.py
"""
import matplotlib.pylab as plt #graphic 을 위한 모듈
from matplotlib import rc
rc('font',family="Malgun Gothic") #한글가능한 폰트설정

labels =['개구리','돼지','개','통나무'] #이름
sizes = [15,30,45,10] #데이터
colors = ['yellowgreen','gold','lightskyblue','lightcoral']
explode = (0,0.1,0,0)
plt.title("Pie Chart")
#wedgeprops : 부채꼴 설정
#width : 반지름 대비 비율
#linewidth : 구분선 굵기
wedgeprops ={'width':0.7,'edgecolor':'w','linewidth':0}
#그래프작성
#autopct : 부채꼴 내부에 표시되는 내용의 형식
#startangle : 시작되는 위치 각도 지정. 배치순서 반시계 방향.
plt.pie(sizes,explode=explode,labels=labels,colors=colors,
        autopct='%1.1f%%',shadow=True,startangle=90,wedgeprops=wedgeprops)
plt.show()
