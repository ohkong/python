# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:01:24 2021

@author: user

dbex1.py : sqlite db 사용하기
    sqlite : 파이썬 내부에 존재하는 dbms
"""
import sqlite3

dbpath = "test.sqlite" #데이터베이스파일
conn = sqlite3.connect(dbpath)
cur = conn.cursor() #sql 구문 실행하기 위한 객체
#sql구문 들(;) 실행
cur.executescript('''
    drop table if exists items;
    create table items (item_id integer primary key,
        name text unique,
        price integer);
    insert into items (name,price) values ('Apple',800);
    insert into items (name,price) values ('Orange',500);
    insert into items (name,price) values ('Banana',300);
''')
conn.commit() #물리적으로 데이터 저장.
#sql 구문을 실행하기 위한 객체 
cur = conn.cursor()
cur.execute("select * from items") #sql 구문 실행 
item_list = cur.fetchall() #모든 레코드 조회 
#for it in item_list:
#    print(it)
for  item_id,name,price in item_list:
    print(item_id,name,price)
print()
for it in item_list:
    print(it[0],it[1],it[2])