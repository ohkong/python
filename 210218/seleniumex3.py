# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:02:02 2021

@author: user

seleniumex3.py : 셀레니움을 이용하여 url연결
    url에서 제동되는 html의 내용을  BeautifulSoup 모듈로 파싱
    pandas 모듈을 이용하여 csv파일로 생성
"""
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("D:/20200914/setup/chromedriver")
driver.get('https://oscar.go.com/winners')

time.sleep(1)
html = driver.page_source #html 소스 리턴 
print(type(html))
soup = BeautifulSoup(html,'html.parser')
category = soup.select('bls-winners-list > ul > li > div.winners-list__info > a')
movie = soup.select('bls-winners-list > ul > li > div.winners-list__info > h3 > a')
producer = soup.select('bls-winners-list > ul > li > div.winners-list__info > p')
print("category :",type(category))
print("movie :",type(movie))
print("producer :",type(producer))

oscars_2020 = [] #dictionary 요소를 가진 리스트.
#zip : 리스트들을 합하여 하나의 리스트로 생성.
#       [(c1,m1,p1),(c2,m2,p2), ...]
for item in zip(category, movie, producer):
    #item : (c1,m1,p1) 튜플 객체
    oscars_2020.append(
        { #dictionary 
            'category' : item[0].text,
            'movie'    : item[1].text,
            'producer' : item[2].text
        }
    )
data = pd.DataFrame(oscars_2020) #판다스 객체로 생성
print(data)
#data
data.to_csv('oscars_win_2020.csv',index=False)
driver.quit()