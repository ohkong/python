# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:34:54 2021

@author: user

dbex4.py : usertable에 데이터 추가
"""
import sqlite3

data=[('test2','테스트2','test2@aaa.bbb',1991),
      ('test3','테스트3','test3@aaa.bbb',1993),
      ('test4','테스트4','test4@aaa.bbb',1994),
      ('test5','테스트5','test5@aaa.bbb',1995)
      ]

con = sqlite3.connect("iddb")
cur = con.cursor()
cur.executemany("""insert into usertable
    (id,username,email,birthday) values (?,?,?,?)
                """, data)
con.commit()

cur.execute("select * from usertable")
item_list = cur.fetchall()
for it in item_list:
    print(it)
print()

con.close()