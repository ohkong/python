# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:08:27 2021

@author: user

jsonex1.py : json예제 
"""
import json
import os.path
import urllib.request as req

url ="https://api.github.com/repositories"
savename = "repo.json"
if not os.path.exists(savename) :#repo.json 파일이 없으면 
    req.urlretrieve(url,savename) #url에서 전달된 애용을 파일로 저장
#파일에서 읽어서 json으로 파싱
items = json.load(open(savename,"r",encoding="utf-8"))
print(type(items))
for item in items :
    print(type(item))
    print(item["name"]+"-"+item["owner"]["login"])

#items 내용을 json_output.json 파일에 저장 
json.dump(items,open("json_output.json","w",encoding="utf-8"))
