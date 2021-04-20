# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:28:53 2021

@author: user

test5.py
화면에서 주민등록번호를 000000-0000000 형태로 입력받는다.
 주민등록번호 뒷자리의  첫 번째 숫자는 성별을 나타낸다. 
 주민등록번호에서 성별을 나타내는 숫자를 조회하여
성별을 나타내는 숫자가 1,3 이면 남자로 2,4면 여자로 출력한다.
 그외는 내국인아님으로 출력한다.
"""
jumin=input("000000-0000000 형태로 주민번호를 입력하세요")
try:
    index = jumin.index("-")
    gender = jumin[index+1:index+2]
    if(gender=='1' or gender=='3'):
        print("남자")
    elif (gender=='2' or gender=='4'):
        print("여자")
    else:
        print("내국인 아님")
except:
    print("주민번호입력오류")