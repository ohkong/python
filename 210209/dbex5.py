# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:54:24 2021

@author: user

dbex5.py : mariadb
"""
#python -m pip install --upgrade pip
#외부 모듈 사용
import pymysql #pip3 install pymysql 실행하기

conn = pymysql.connect(host="localhost",port=3307,
                       user="scott",passwd="1234",
                       db="classdb",charset="utf8")
try:
    cur = conn.cursor()
    cur.execute("select * from item")
    for row in cur.fetchall():
        print(type(row),row)
finally:
    cur.close()
    conn.close()
