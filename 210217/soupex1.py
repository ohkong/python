# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:57:53 2021

@author: user

soupex1.py : 크롤링 예제
"""
from bs4 import BeautifulSoup #pip install beautifulsoup4
html='''
    <html><body>
        <div id="potal">
            <h1>포털 목록</h1>
            <ul class="items">
                <li><a href="http://www.naver.com">naver</a></li>
                <li><a href="http://www.daum.net">daum</a></li>
            </ul></div></body></html>
'''
#soup : html 문자열을 파싱하여 DOM의 최상단 문서노드 저장
soup = BeautifulSoup(html,"html.parser")
links = soup.find_all("a") #a태그들
for a in links : #a : <a href="http://www.naver.com">naver</a>
    href = a.attrs["href"] # href : http://www.naver.com
    text = a.string #text : naver
    print(text,">",href)
#select_one : 선택된 태그 1개
#div#potal : id속성값이 potal인 div태그
h1=soup.select_one("div#potal > h1").string
print("h1=",h1)
#select : 조건에 맞는 태그들
li_list = soup.select("div#potal > ul.items > li")
print(type(li_list)) #li : 
for li in li_list:
    print("li=",li.string)