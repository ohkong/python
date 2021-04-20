# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:41:58 2021

@author: user

soupex4.com : 네이버 페이지의 환율 정보 조회 
"""
from bs4 import BeautifulSoup
import urllib.request as req

url="https://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser",from_encoding="euc-kr")
sel = lambda q : soup.select(q)
#class 속성이 head_info div태그들 . 환율, 상승/하락값,상승/하락
hlist = sel("div.head_info") 
#class 속성이 h_lst인 h3태그들 통화명
htitle = sel("h3.h_lst")

#zip함수 설명
a=[1,2,3,4,5]
b=["a","b","c","d","e"]
for x in zip(a,b) :
    print(x)

#zip : 두개의 리트스를 하나로 연결하는 함수
#tag : 환율 정보
#title : 통화명
for tag,title in zip(hlist,htitle):
    print(title.select_one("span.blind").string, end="\t") #통화명
    value=tag.select_one("span.value").string #환율정보 
    print(value,end=" ")
    change = tag.select_one("span.change").string #환율 변동값 
    print(change,end="\t")
    blinds = tag.select("span.blind") #상승 하락
    b=tag.select("span.blind")[-1].string #마지막 태그 선택 
    print(b,end="*******\n")
