# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:06:34 2021

@author: user

test1.py : sales_2015.xlsx 파일을 읽어서 
   # 1월의 고객별 판매금액을 막대그래프로 출력하기
   
    sales_2015.xlsx 파일을 읽어서 
   Customer Name 별 Sale Amount를 막대그래프로 출력하
"""
import pandas as pd
import matplotlib.pyplot as plt

infile="../excel/sales_2015.xlsx"
df = pd.read_excel(infile,"january_2015",index_col=None)
df_value = df.loc[:,["Customer Name","Sale Amount"]]

plt.style.use("ggplot")
customers = list(df_value["Customer Name"])
print(customers)
customers_index = range(len(customers))
amounts = list(df_value["Sale Amount"])

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(customers_index,amounts,align="center",color="darkblue")
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")
plt.xticks(customers_index,customers,rotation=0,fontsize="small")
plt.xlabel("Customer")
plt.ylabel("Amount")
plt.title("Sales Amount")
plt.savefig("sales_amount1.png", dpi=400,bbox_inches="tight")