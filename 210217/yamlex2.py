# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:46:01 2021

@author: user

yamlex2.py : list를 yaml 문서양식으로 변경하기
"""
import yaml
customer = [
    {"name":"Inseong","age":"24","gender":"man"},
    {"name":"Kildong","age":"22","gender":"man"},
    {"name":"ChunHang","age":"20","gender":"woman"},
    {"name":"HangDan","age":"25","gender":"woman"}  
]
#파이썬 데이터(List)를 yaml 문서양식으로 변경하기
# yaml문서 양식에 맞는 문자열 <= yaml.dump(리스트)
yaml_str = yaml.dump(customer)
print(type(yaml_str))
print(yaml_str)

#yaml_str 문서를 리스트형으로 변경하기
data = yaml.load(yaml_str,Loader=yaml.FullLoader)
print(type(data))
print(data)