# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:28:31 2021

@author: user

test4.py
홍길동 씨의 주민등록번호는 881120-106234이다.
홍길동씨의 주민등록 번호를 연월일(YYYYMMDD) 
부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.
881120
1068234
"""
jumin="881120-106234"
print(jumin[:jumin.find('-')])
print(jumin[jumin.find('-')+1:])
