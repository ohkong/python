# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:32:39 2021

@author: user

strex1.py : 문자열 처리하기
"""
print("안녕하세요")#문자열
print("안녕하세요"[0])#0번 인덱스 문자
print("안녕하세요"[4])
print("안녕하세요"[-1])#요. 뒤에서 첫번째 인덱스에 해당하는 문자
print("안녕하세요"[-2])#요. 뒤에서 두번째 인덱스에 해당하는 문자

#부분 문자열
print("안녕하세요"[1:3])#1번인덱스부터 2번인덱스까지의 부분문자열
print("안녕하세요"[:3])#0번인덱스부터 2번인덱스까지의 부분문자열
print("안녕하세요"[3:])#3번인덱스부터 끝까지 부분문자열
print("안녕하세요"[::2])#2칸씩 부분 문자열
print("안녕하세요"[::-1])#역순 문자
print("안녕하세요"[::-2])#역순 2칸씩 부분 문자열
print('"안녕하세요" 문자열의 길이:',len("안녕하세요"))
print(type(len("안녕하세요")))
print(type("안녕하세요"))

a="hello" #l문자의 갯수 출력하기
cnt=0
for i in range(0,len(a)):
    if(a[i]=='l'):
        cnt+=1
print("l문자의 갯수:",cnt)
print("l문자의 갯수:",a.count('l'))
print("h문자의 갯수:",a.count('h'))
print("a문자의 갯수:",a.count('a'))

print("l문자의 인덱스값:",a.find('l'))
print("a문자의 인덱스값:",a.find('a')) #-1 : 값없음

print("l문자의 인덱스값:",a.index('l'))
#print("a문자의 인덱스값:",a.index('a')) #오류 값없음

arr=[10,20,30,40,50,60,70] #리스트
print(arr[:2])#10,20
#첫번째값부터 1칸 건너씩 요소 출력하기
print(arr[::2])
#두번째값부터 1칸 건너씩 요소 출력하기
print(arr[1::2])
#역순으로 출력하기
print(arr[::-1])
#뒤부터 한칸 건너씩 출력하기
print(arr[::-2])
#[60,40,20] 출력하기
print(arr[-2::-2])
print(arr[5::-2])

#arr 요소의 전체 합과 평균 구하기
sum = 0
for i in range(0,len(arr)):
    sum += arr[i]
print("리스트 요소의 합",sum,"평균",sum/len(arr))

