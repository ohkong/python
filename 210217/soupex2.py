# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:32:28 2021

@author: user

soupex2.py : 웹크롤링 예제
"""
from bs4 import BeautifulSoup
import urllib.request as req

url="https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
#res = url로 연결시 제공되는 문자열
res = req.urlopen(url) #url로 연결
#url이 제공하는 내용을 분석하여 DOM객체로 생성 후 최상단 노드저장.
soup = BeautifulSoup(res,"html.parser")
title = soup.find("title").string
wf = soup.find("wf").string

"""
    ![CDATA[....]]> : CDATA 섹션 => 순수한 문자열 영역 <br />
                      마크업언어로 파싱되지 않는 영역
"""

print(title)
print(wf)

for w in wf.split("<br />") :
    print(w)
