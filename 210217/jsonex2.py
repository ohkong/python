# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:39:38 2021

@author: user

jsonex2.py :json내용에서 날짜와 과일의 과격을 화면에 출력하고,
                price.json 파일에 저장하기
"""
import json
price={
    "date" : "2021-02-17",
    "price" : {
        "Apple" : 800,
        "Orange" : 1000,
        "Banana" : 500
    }       
}

print("날짜:",price["date"])
for p in price["price"].keys() :
    print("%s => %s" % (p,price["price"][p]))
json.dump(price,open("price.json","w"))

str ="""{
    "date" : "2021-02-17",
    "price" : {
        "Apple" : 800,
        "Orange" : 1000,
        "Banana" : 500
    }       
}
"""

price2=json.loads(str)
print("날짜:",price2["date"])
for p in price2["price"].keys() :
    print("%s => %s" % (p,price2["price"][p]))
json.dump(price2,open("price2.json","w"))