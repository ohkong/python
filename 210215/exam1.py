# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:51:54 2021

@author: user

exam1.py : ssec1804.xls 파일에서 1.남자, 1.여자 sheet의 데이터를
            ssec1804mf.xls 파일에 남자, 여자 sheet의 데이터로 저장하기
"""
from xlrd import open_workbook 
from xlwt import Workbook


#강사님 
def makesheet(output_sheet) :
    for row_index in range(worksheet.nrows) :
        for column_index in range(worksheet.ncols) :
            output_sheet.write(row_index,column_index,
                    worksheet.cell_value(row_index,column_index))
            #print(worksheet.cell_value(rindex,cindex))

infile = "ssec1804.xls" 
outfile = "ssec1804mf2.xls" 
worksheet = None
outworkbook = Workbook() 
out_male_sheet = outworkbook.add_sheet("남자")
out_female_sheet = outworkbook.add_sheet("여자")
with open_workbook(infile) as workbook :
    worksheet = workbook.sheet_by_name("1.남자")
    makesheet(out_male_sheet)
    worksheet = workbook.sheet_by_name("1.여자")
    makesheet(out_female_sheet)
outworkbook.save(outfile)

"""
#내가한것
infile = "ssec1804.xls" 
outfile = "ssec1804mf.xls" 

outworkbook = Workbook() 

out_sheet = outworkbook.add_sheet("남자")

with open_workbook(infile) as workbook :
    worksheet = workbook.sheet_by_name("1.남자")
    for rindex in range(worksheet.nrows) :
        for cindex in range(worksheet.ncols) :
            out_sheet.write(rindex,cindex,
                    worksheet.cell_value(rindex,cindex))
            print(worksheet.cell_value(rindex,cindex))
            
out_sheet = outworkbook.add_sheet("여자")

with open_workbook(infile) as workbook :
    worksheet = workbook.sheet_by_name("1.여자")
    for rindex in range(worksheet.nrows) :
        for cindex in range(worksheet.ncols) :
            out_sheet.write(rindex,cindex,
                    worksheet.cell_value(rindex,cindex))
            print(worksheet.cell_value(rindex,cindex))
outworkbook.save(outfile)
"""