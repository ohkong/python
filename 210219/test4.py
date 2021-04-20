# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:40:21 2021

@author: user

test4
"""
import pymysql 
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',family="Malgun Gothic")

conn = pymysql.connect(host="localhost",port=3307,
                       user="scott",passwd="1234",
                       db="classdb",charset="utf8")
datelist =[]
date = []
tot = []
try:
    cur = conn.cursor()
    cur.execute("select date_format(regdate,'%Y-%m-%d') regdate, count(*) cnt"
			+ " from board"
			+ " group by date_format(regdate, '%Y-%m-%d')"
			+ " order by regdate desc LIMIT 0,7")
    for row in cur.fetchall():
        datelist += row
finally:
    cur.close()
    conn.close()
for i in range(len(datelist)):
    if i%2==0:
        date += datelist[i]
    if i%2==1:
        tot += str(datelist[i])
print(datelist)
print(date)
print(tot)


plt.style.use("ggplot")
subjects=['2021-01-26', '2021-01-21', '2021-01-20', '2020-12-29', '2020-12-22', '2020-12-08', '2020-12-04']
subjects_index=range(len(subjects))
scores=tot
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(subjects_index,scores,align="center",color="darkblue")
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")
plt.xticks(subjects_index,subjects,rotation=0,fontsize="small")
plt.xlabel("글작성일")
plt.ylabel("게시글 작성건수")
plt.title("최근 등록 게시물")
plt.show() 
