# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:46:08 2021

@author: user

test1.py
콘솔에 sql 구문을 입력하면 mariadb의 테이블들을 
이용하여 결과를 출력할 수 있도록 프로그램 작성하기

[결과]
sql 구문을 입력하세요 : select * from student
.....
.....

"""
import pymysql 
"""
#내가한거
conn = pymysql.connect(host="localhost",port=3307,
                       user="scott",passwd="1234",
                       db="classdb",charset="utf8")
cur = conn.cursor()
sql = input("sql 구문을 입력하세요 : ")
cur.execute(sql)
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()
"""
#강사님
conn = pymysql.connect(host="localhost",port=3307,
                       user="scott",passwd="1234",
                       db="classdb",charset="utf8")
cur = conn.cursor()
try:
    while True:
        sql = input("sql 구문을 입력하세요 : \n")
        if sql=="":
            break
        cur.execute("select count(*) from ("+sql+") a")
        row=cur.fetchone()
        print("조회 레코드수:",row[0],",조회 컬럼수:",end="")
        cur.execute(sql)
        row = cur.fetchone()
        print(len(row))
        cur.execute(sql)
        for row in cur.fetchall():
            print(row)
finally:
    cur.close()
    conn.close()