# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:57:48 2021

@author: user

soupex3.py :
"""
from bs4 import BeautifulSoup

fp = open("books.html",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")
print(soup.select("li")[3].string) #li태그들 중 4번째 태그의 내용출력 
print(soup.find_all("li")[3].string) #li태그들 중 4번째 태그의 내용출력 
#id 속성이 nu인 태그의 값을 출력
print(soup.select_one("#nu").string)
print(soup.select("#nu")[0].string)
#id 속성이 nu인 li 태그의 값을 출력
print(soup.select_one("li#nu").string)
#ul태그의 하위 태그인 id 속성이 nu인 li 태그의 값을 출력
print(soup.select_one("ul > li#nu").string)
#ul태그의 하위 태그중 id 속성이 nu인 li 태그의 값을 출력
print(soup.select_one("ul li#nu").string)
#id 속성이 bible인 태그의 하위 태그 중 id 속성이 nu인 li 태그의 값을 출력
print(soup.select_one("#bible li#nu").string)

#람다식을 이용하여 출력하기
sel = lambda q : print(soup.select_one(q).string)
#id속성이 nu인 태그의 값을 출력
sel("#nu")
#id 속성이 nu인 li 태그의 값을 출력
sel("li#nu")
#ul태그의 하위 태그인 id 속성이 nu인 li 태그의 값을 출력
sel("ul > li#nu")
#ul태그의 하위 태그중 id 속성이 nu인 li 태그의 값을 출력
sel("ul li#nu")
#id 속성이 bible인 태그의 하위 태그 중 id 속성이 nu인 li 태그의 값을 출력
sel("#bible li#nu")

#li태그중 4번째 태그의 값을 출력 
sel("li:nth-of-type(4)")
#id속성이 nu인 li태그의 값을 출력
sel("li[id='nu']")