# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:57:04 2021

@author: user

yamlex3.py : yaml문서에서 alias, 주석 설정하기 
"""
import yaml
yaml_str = """
# 주석 부분 정의
# 정의
color_def :
    - &color1 "#FF0000"
    - &color2 "#00FF00"
    - &color3 "#0000FF"
#별칭 정하기
color :
    title: *color1
    body:  *color2
    link:  *color3
    div:   *color1
"""
#yaml.load : yaml 형태의 문자열 => 리스트, 딕셔너리 형태로 변경
data = yaml.load(yaml_str,Loader=yaml.FullLoader)
print("title=",data["color"]["title"])
print("body=",data["color"]["body"])
print("link=",data["color"]["link"])
print("div=",data["color"]["div"])

#yaml 형태의 파일로 저장하기 : color.yaml 파일로 data 저장하기.
yaml.dump(data,open("color.yaml","w"))