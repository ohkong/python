# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:06:19 2021

@author: user

test2.py : 동물선택하여 대표이미지 보기
"""
from tkinter import *
window = Tk()
window.geometry("400x400")
window.title("좋아하는 동물 사진 보기")

# 함수 정의 부분
def  myFunc() :
    if var.get() == 1 :
        labelImage.configure(image=photo1)
    elif var.get() == 2 :
        labelImage.configure(image=photo2)
    else :
        labelImage.configure(image=photo3)
    
# 메인 코드 부분
labelText = Label(window, text="좋아하는 동물 투표  ", fg="blue", font=("궁서체", 20))

var = IntVar() # 정수값
#variable : value값을 변수화.
rb1 = Radiobutton(window, text="강아지", variable=var, value=1)
rb2 = Radiobutton(window, text="고양이", variable=var, value=2)
rb3 = Radiobutton(window, text="토끼", variable=var, value=3)
buttonOk = Button(window, text="사진 보기", command=myFunc)

photo1 = PhotoImage(file="../210210/gif/dog4.gif")
photo2 = PhotoImage(file="../210210/gif/cat.gif")
photo3 = PhotoImage(file="../210210/gif/rabbit.gif")

labelImage = Label(window, width=200, height=200, bg="yellow", anchor=SE, image=None)

labelText.pack(padx=5, pady=5)
rb1.pack(padx=5, pady=5)
rb2.pack(padx=5, pady=5)
rb3.pack(padx=5, pady=5)
buttonOk.pack(padx=5, pady=5)
labelImage.pack(padx=5, pady=5)

window.mainloop()