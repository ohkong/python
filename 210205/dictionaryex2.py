# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:50:32 2021

@author: user
dictionaryex2.py : dictionary 예제 2
"""
foods={"떡볶이":"오뎅","짜장면":"단무지","라면":"김치","맥주":"치킨"}
for i in foods.keys():
    print("%s=>%s" % (i,foods[i]))

#화면에서 등록된 음식을 입력받아서 궁합음식을 출력하기
#food = input("음식을 입력하세요 : ")
#print("%s" % (foods[food]))

while True : 
    myfood = input(str(list(foods.keys()))+"중 음식이름을 입력하세요:")
    if myfood =="종료":
        break
    if myfood in foods:
        print("<%s> 궁합음식은 <%s>입니다." % (myfood,foods[myfood]))
    else :
        print("등록된 음식이 아닙니다.")
#음식 등록하기
        yn=input("종아하는 음식으로 등록하시겠습니까(y)")
        if yn =='Y' or yn =='y':
            f=input("궁합음식을 등록하세요")
            foods[myfood]=f