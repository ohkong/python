# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:37:49 2021

@author: user

guiex4.py : 섭씨를 화씨로 변경하기
"""
from tkinter import *

def fa() :
    ct = float(e1.get())
    ft = (9/5)*ct+32
    e2.insert(0,ft)
def ca() :
    ft = float(e2.get())
    ct = (ft-32)*5/9
    e1.insert(0,ct)
    
window = Tk()
window.title("섭씨를 화씨로 변경")
window.geometry("500x200")
window.resizable(False,False)

l1 = Label(window,text="섭씨")
l2 = Label(window,text="화씨")

l1.pack()
l2.pack()
l1.place(x=100,y=0)
l2.place(x=100,y=20)
e1 = Entry(window)
e2 = Entry(window)
e1.pack()
e2.pack()
b1=Button(window,text="섭씨->화씨",command=fa)
b1.pack()
b2=Button(window,text="화씨->섭씨",command=ca)
b2.pack()
window.mainloop()

