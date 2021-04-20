# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:46:23 2021

@author: user

test2.py
 Thread를 이용하여 
1~10000까지의 합을 5개의 스레드로 나눠서 각각의 구간 합을 
스레드 1 : 1 ~ 2000까지의 합
스레드 2 : 2001 ~ 4000까지의 합
스레드 3 : 4001 ~ 6000까지의 합
스레드 4 : 6001 ~ 8000까지의 합
스레드 5 : 8001 ~ 10000까지의 합
main에서 더하여 총합을 구하는 프로그램 작성하기
"""
import threading

class Sum :
    startnum = 0
    endnum = 0
    sum = 0
    def __init__(self,snum,enum):
        self.startnum = snum
        self.endnum = enum
        
    def getSum(self):
        for i in range(self.startnum,self.endnum+1):
            self.sum += i
        return self.sum
    
if __name__=="__main__":
    sumlist =[]
    thlist=[]
    for i in range(0,5):
        sumlist.append(Sum((i*2000)+1,(i+1)*2000))
        thlist.append(threading.Thread(target=sumlist[i].getSum))
        thlist[i].start()
        
    for th in thlist:
        th.join()
        
    sum =0
    for s in sumlist:
        sum+=s.sum
        
    print (sum)