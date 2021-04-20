# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:32:43 2021

@author: user

seleniumex1.py
"""
from selenium import webdriver #pip install selenium
import time
#chromedriver.exe 파일 다운 로드:
#   https://chromedriver.chromium.org/downloads
#   크롬의 버전에 맞는 파일 다운받기. 크롬도움말 > 크롬 정보
#D:/20200914/setup/ => 위치에 chromedriver.exe 파일 복사
#dirver : 브라우저를 제어할 수 있는 객체
driver = webdriver.Chrome("D:/20200914/setup/chromedriver")
driver.get("http://python.org")
# #top 하위의 ul.menu 태그의 하위의 모든 li 태그들
menus = driver.find_elements_by_css_selector('#top ul.menu li')
print(type(menus))
pypi=None
for m in menus : # m : li태그
    if m.text == "PyPI" :
        pypi = m #저장된 문자열이 PyPI인 li태그
    print(m.tag_name,m.text)
pypi.click() #PyPI 태그 클릭
time.sleep(5) #5초 대기
driver.quit() #브라우저 종료