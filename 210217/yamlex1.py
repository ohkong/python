# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:01:19 2021

@author: user

yamlex1.py : yaml 문서 예제 
"""
import yaml #pip install pyYAML
import json
yaml_str = """
   Date : 2021-02-17
   PriceList:
        -
            item_id: 1000
            name: banana
            color: yellow
            price: 800
        -
            item_id: 1001
            name: orange
            color: orange
            price: 1400
        -
            item_id: 1002
            name: Apple
            color: red
            price: 2400
"""
#yaml.load : yaml 문서를 파싱하여 dictionary 형 변경.
data = yaml.load(yaml_str,Loader=yaml.FullLoader)
print(type(data)) #dictionary 형
print(data["Date"],"과일 가격")
for item in data["PriceList"] :
    print(item["name"],item["price"])
#yaml_str 문서를 json형태의 문자열로 변경하고 위의 결과와 같은
# 결과가 나오도록 프로그램 구현하기
json_str = """
  { 
   "Date" : "2021-02-17",
   "PriceList":[
        {
            "item_id": 1000,
            "name": "banana",
            "color": "yellow",
            "price": 800
        },
        {
            "item_id": 1001,
            "name": "orange",
            "color": "orange",
            "price": 1400
        },
        { 
            "item_id": 1002,
            "name": "Apple",
            "color": "red",
            "price": 2400
        }
    ]
  }
"""
jsondata = json.loads(json_str)
print(jsondata["Date"],"과일 가격")
for item in jsondata["PriceList"] :
    print(item["name"],item["price"])