# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:35:01 2021

@author: user

test1.py :네이버 로그인 후 본인의 주문 상품 목록 페이지 조회하기
    
    https://order.pay.naver.com/home
"""
import time
from selenium import webdriver
driver = webdriver.Chrome("D:/20200914/setup/chromedriver")
time.sleep(1)
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
id=input("네이버 아이디를 입력하세요: ")
time.sleep(1)
driver.execute_script("document.getElementsByName('id')[0].value='"+id+"'")
time.sleep(1)
pw = input("네이버 비밀번호를 입력하세요: ")
time.sleep(1)
driver.execute_script("document.getElementsByName('pw')[0].value='"+pw+"'")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(1)
#쇼핑영역 클릭하기
driver.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[5]/a').click()
time.sleep(1)
#My 쇼핑영역 클릭하기
driver.find_element_by_xpath('//*[@id="_myPageWrapper"]/a').click()
time.sleep(1)
#주문 확인/배송 조회 클릭하기
driver.find_element_by_xpath('//*[@id="_myPageWrapper"]/div/div[3]/ul[2]/li[2]/a').click()
time.sleep(1)
#주문정보 보기
#find_elements_by_css_selector : 선택자로 태그 객체들 지정
products = driver.find_elements_by_css_selector(".goods_pay_section")
for product in products :
    print("-",product.text)
    