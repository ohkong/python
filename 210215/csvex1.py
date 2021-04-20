# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:47:55 2021

@author: user

csvex1.py : csv 파일 읽기 => 파일 복사하기
    jeju1.csv 파일을 같은 폴더에 복사.
    메뉴 : run > configuration per file > command line options check
                                        jeju1.csv jeju1_bak.csv
    jeju1.csv : 원본파일
    jeju1_bak.csv : 복사파일
"""
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r', newline="", encoding="utf8") as filereader :
    with open(output_file, 'w', newline="", encoding="utf8") as filewriter :
        header = filereader.readline() # 한줄읽기
        print(type(header))
        header = header.strip() # 공백제거
        print(header)
        header_list = header.split(",") # , 기준으로 문자열 분리. csv파일은 , 기준으로 셀을 분리
        print(header_list)
        # map(str,header_list) : header_list 리스트의 요소들을  문자열로 변환
        filewriter.write(",".join(map(str,header_list))+"\r\n")
        for row_list in filereader : #입력 스트림에서 파일을 한줄씩 읽기
            filewriter.write(row_list)
