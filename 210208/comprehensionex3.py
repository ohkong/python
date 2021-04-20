# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:04:01 2021

@author: user

comprehensionex3.py : dictionary에서 컴프리헨션 사용하
"""
products = {"냉장고":220,"건조기":140,"TV":130,"세탁기":150,"오디오":50,"컴퓨터":250}
print(products)
product1={}
#200만원 미만의 제품만 product1에 저장하기
'''
for name in products.keys():
    if products.get(name) < 200:
        product1[name]=products.get(name)
'''
for p,v in products.items():
    if v < 200 :
        product1.update({p: v})
print(product1)

#컴프리헨션으로 구현하기
product2 = {p:v for p,v in products.items() if v < 200}
print(product2)