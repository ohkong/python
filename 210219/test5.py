# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:40:21 2021

@author: user

test5
"""
import pymysql 
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',family="Malgun Gothic")

conn = pymysql.connect(host="localhost",port=3307,
                       user="scott",passwd="1234",
                       db="classdb",charset="utf8")
people = None
name = []
tot = []
cur = conn.cursor()
cur.execute("select name, count(*) cnt from board group by name"
			+" having count(*) >1 order by cnt desc")
people = cur.fetchone()
print(people)
while people:
    name1 = str(people[0])
    print(name1)
    name+=name1
    tot += str(people[1])
    people = cur.fetchone()
    
print(name)
print(tot)


labels = ['테스트2','관리자','사과12','사진','사진2']
sizes = tot 
colors = ['yellowgreen','gold','lightskyblue','lightcoral','blue']
explode = (0.1,0,0,0,0)
plt.title("최다 글쓴이별 게시물 건수")
wedgeprops ={'width':0.7,'edgecolor':'w','linewidth':0}
plt.pie(sizes,explode=explode,labels=labels,colors=colors,
        autopct='%1.1f%%',shadow=True,startangle=90,wedgeprops=wedgeprops)
plt.show()
