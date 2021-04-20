# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:09:21 2021

@author: user

graphex1.py : 그래프 그리기 
"""
import matplotlib.pyplot as plt #pip install ggplot
plt.style.use("ggplot")
subjects=["Java","JSP","SPRING","HADOOP","PYTHON"] #막대그래프의 x좌표의값
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
plt.xlabel("Subject")
plt.ylabel("Score") #y축 제목
plt.title("Class Score")
#메모리 저장된 이미지 파일로 생성
plt.savefig("bar_plot.png", dpi=400,bbox_inches="tight")
plt.show() #메모리에 있는 그래프 이미지를 화면에 보여줌.