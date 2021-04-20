# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:51:25 2021

@author: user

graphex4.py : 그래프 그리기 graphex1.py의 그래프 내용을 한글로 변경 
"""
import matplotlib.pyplot as plt #pip install ggplot

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties\
        (fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)

plt.style.use("ggplot")
subjects=["자바","JSP","스프링","하둡","파이썬"] #막대그래프의 x좌표의값
print(range(len(subjects)))
subjects_index=range(len(subjects)) #subjects_index : 0~4값을 저장
print(type(subjects))
scores=[65,90,85,60,95]#막대그래프로 표현할 값
#그래프 출력
fig = plt.figure()#그래프를 그릴수 있는 공간. 도화지.
#도화지 영역 분리. 하나의 도화지에 여러개의 그림가능.
#1행1열 분리 =>한개 그림. 분리안함.
# 1 : 1번째 그림.
# ax1 :  그래프가 그려지는 영역
ax1 = fig.add_subplot(1,1,1)
#ax1.bar : 막대그래프
#subjects_index : x좌표 내용 인덱스
#scores : 막대그래프로 표현할 데이터 값
ax1.bar(subjects_index,scores,align="center",color="darkblue")
#xaxis : x축. 위치.
#yaxis : y축. 위치.
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")
#xticks : x축
#rotation : x축에 표시되는 내용의 방량
plt.xticks(subjects_index,subjects,rotation=0,fontsize="small")
#x축제목
plt.xlabel("과목")
plt.ylabel("점수") #y축 제목
plt.title("과정 점수")
#메모리 저장된 이미지 파일로 생성
plt.savefig("bar_plot2.png", dpi=400,bbox_inches="tight")
plt.show() #메모리에 있는 그래프 이미지를 화면에 보여줌.

