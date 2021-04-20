# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:58:44 2021

@author: user

guiex7.py : raw 파일을 이미지로 출력하기
"""
from tkinter import *
window = NONE
canvas = None
XSIZE,YSIZE = 256,256

window = Tk()
window.title("raw 파일출력하기")
canvas = Canvas(window,height=YSIZE,width=XSIZE)

paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2),image=paper,state="normal")
#raw : 이진파일을 이진수로 저장한 파일 
fp = open("flower.raw","rb")

for i in range(0,XSIZE) :
    for k in range(0,YSIZE) :
        #ord : 코드값
        data = int(ord(fp.read(1)))#1바이트읽기
        #색상표시 : #FFFFFF
        paper.put("#%02x%02x%02x" % (data,data,data),(k,i)) #점찍기
fp.close()
canvas.pack()
window.mainloop()