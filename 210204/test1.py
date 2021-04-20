# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:35:07 2021

@author: user

test1.py
삼각형의 높이를 입력받은 후 삼각형을 출력하는 프로그램을 작성

삼각형의 높이를 입력하세요 : 5

    *
   **
  ***
 ****
*****

    *  
   ***
  *****
 *******
*********
"""
star = int(input("삼각형의 높이를 입력하세요 : "))
"""
for i in range(star,0,-1):
    print(' '*(i),end='')
    print('*'*(star-(i-1)))

print()

for i in range(star ,0 ,-1):
    print("  " *i ,end='')
    print("* " *(star- i +1) ,end='')
    print("* " *(star -i) ,end='')
    print("  " *i)
"""
for i in range(1, star+1):
    print(" "*(star-i),end="")
    print("*"*i)

print()
for i in range(0,star+1):
    print(" "*(star-i),end="")
    print("*"*(i*2-1))
    
print()
for i in range(star,0,-1):
    print(" "*(star-i),end="")
    print("*"*i)