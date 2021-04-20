# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:54:58 2021

@author: user

test1.py
다음 코드를 실행 했을 경우 결과를 예측하시오.
     출력된 결과의 이유를 설명하시오
"""
a = "Life is too short, you need python"

if "wife" in a: #false
    print("wife")

elif "python" in a and "you" not in a: #true and false => false
    print("python")

elif "shirt" not in a: #true
    print("shirt")

elif "need" in a:  
    print("need")

else: 
    print("none")
