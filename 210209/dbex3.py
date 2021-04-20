# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:06:18 2021

@author: user

dbex3.py : usertable의 내용을 화면에 출력하기
"""
import sqlite3

'''
dbpath = "iddb" #데이터베이스파일
conn = sqlite3.connect(dbpath)
cur = conn.cursor()
cur.execute("select * from usertable") #sql 구문 실행 
id_list = cur.fetchall() #모든 레코드 조회 
for list_id,username,email,birthday in id_list:
    print(list_id,username,email,birthday)
'''

con,cur = None,None
row = None
con = sqlite3.connect("iddb")
cur = con.cursor()

cur.execute("select * from usertable")
id_list = cur.fetchall()
for it in id_list:
    print(it)
print()

cur.execute("select * from usertable")
while True:
    row = cur.fetchone()
    if row == None:
        break
    print("%5s %15s %15s %d" % (row[0],row[1],row[2],row[3]))
con.close()