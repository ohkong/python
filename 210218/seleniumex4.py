# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:48:54 2021

@author: user

seleniumex4.py : 화면 이미지 저장하기.
"""
from selenium import webdriver
url = "http://www.naver.com/"
driver = webdriver.Chrome("D:/20200914/setup/chromedriver")
driver.get(url)
#open된 브라우저의 화면을 이미지로 저장하기
driver.save_screenshot("naverhome.png")
driver.quit()
