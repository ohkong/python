# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:39:55 2021

@author: user

guiex5.py : 간단한 계산기 만들기
"""
import tkinter as tk

def calculate(event) :
    value = tk.Entry.get(display) #입력란에 등록된 값을 리턴
    if value != "":
        #eval: 자바스크립트와 같은 기능. 문자열 => 수식 : 결과 리턴
        result = eval(value) 
        display.delete(0,tk.END)
        display.insert(0,result)
        
def clear(event) :
    display.delete(0,tk.END)

window = tk.Tk()
window.title("계산기")
window.geometry("300x300")

display = tk.Entry(window,width=20)
display.pack()

b1 = tk.Button(window, text="=", width=5)
b1.bind("<Button-1>",calculate)
b1.pack()

b_c = tk.Button(window, text="C", width=5)
b_c.bind("<Button-1>",clear)
b_c.pack()

window.bind("<Return>",calculate)
window.bind("<Escape>",clear)

window.mainloop()