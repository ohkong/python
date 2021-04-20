# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:25:47 2021

@author: user
dbex6.py : mariadb와 연결하기
"""
import pymysql 

conn = pymysql.connect(host="localhost",port=3307,
                       user="scott",passwd="1234",
                       db="classdb",charset="utf8")
cur = conn.cursor()
cur.execute("drop table items")
cur.execute('''create table items(
            item_id integer primary key auto_increment,
            name varchar(300),
            price integer)
                ''')
data=[("바나나",3000),("망고",30000),("사과",10000)]
for i in data:
    cur.execute("insert into items (name,price) values (%s, %s)",i)
conn.commit()

cur.execute("select * from items")
for row in cur.fetchall():
    print(row)

#items 테이블에서 가격이 3000이상 10000이하인 레코드를 조회하기
print("itmes 테이블에서 3000이상 10000이하인 레코드를 조회")
cur.execute("select * from items where price between %s and %s",(3000,10000))
for row in cur.fetchall():
    print(row)
    
#items 테이블에서 가격기 30000원인 레코드 제거하기
print("items 테이블에서 가격기 30000원인 레코드 제거하기")
cur.execute("delete from items where price=%s",(30000))
conn.commit()

cur.execute("select * from items")
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()
