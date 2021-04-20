# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:45:19 2021

@author: user

test1.py 
1.http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp 
   의 내용을 받아서 forcast.xml 파일로 저장하기.
   
2. 저장된 파일을 읽어서 다음 결과가 나오도록 프로그램 구현하시오. 
단 결과는 실시간 자료이므로 동일하게  나오지 않습니다.  
형태만 맞춰 주시면 됩니다.

[결과]
+ 구름많음
  |- 서울
  |- 인천
  |- 수원
  |- 파주
  |- 이천
  |- 평택
  |- 강릉
+ 흐림
  |- 춘천
  |- 원주
+ 맑음
  |- 대전
  |- 세종
  |- 홍성
  |- 청주
  |- 충주
  |- 영동
  |- 광주
  |- 목포
  |- 여수
  |- 순천
  |- 광양
  |- 나주
  |- 전주
  |- 군산
 ...
"""
from bs4 import BeautifulSoup
import urllib.request as req
import os.path

url="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
if not os.path.exists("forcast.xml") :
    req.urlretrieve(url,"forcast.xml")
    
xml = open("forcast.xml","r",encoding="utf-8").read()

info = {}
soup = BeautifulSoup(xml,"html.parser")
for location in soup.find_all("location") :
    name = location.find("city").string
    weather = location.find("wf").string
    if not (weather in info) :
        info[weather] = []
    info[weather].append(name)

for weather in info.keys() :
    print("+",weather)
    for name in info[weather] :
        print(" |- ",name)