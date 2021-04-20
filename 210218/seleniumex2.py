# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:10:19 2021

@author: user

seleniumex2.py : 네이버 로그인 하기
"""
import time
from selenium import webdriver
driver = webdriver.Chrome("D:/20200914/setup/chromedriver")
time.sleep(1)
#url 설정 : 네이버 로그인 화면
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
id=input("네이버 아이디를 입력하세요: ")
time.sleep(1)
#execute_script : driver에서 자바스크립트 명령 사용
driver.execute_script("document.getElementsByName('id')[0].value='"+id+"'")
time.sleep(1)
pw = input("네이버 비밀번호를 입력하세요: ")
time.sleep(1)
driver.execute_script("document.getElementsByName('pw')[0].value='"+pw+"'")
time.sleep(1)
#find_element_by_xpath : xpath를 이용하여 태그 선택
# // : 하위 태그들.
# / : 자식 태그들.
# @id : id속성이 log.login 값을 가진 태그
# click
driver.find_element_by_xpath('//*[@id="log.login"]').click()
