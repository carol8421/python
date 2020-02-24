# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:07:03 2019

@author: 萧墨离
"""

import matplotlib.pyplot as plt
import numpy as np
import xlrd
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']


worksheet=xlrd.open_workbook(u'D:\Desktop\合格表.xlsx')
sheet_names=worksheet.sheet_names()
for sheet_name in sheet_names:
    sheet2=worksheet.sheet_by_name(sheet_name)
company_name=sheet2.col_values(4)
company_sale=sheet2.col_values(5)
del company_name[0]
company_name.append(0)
del company_sale[0]
company_sale.append(0)

temp=[]
name=[]
max_sale=[]  #销售最大值
min_sale=[]  #销售最小值
avg_sale=[]  #销售平均值

temp.append(company_sale[0])
for i in range(1,len(company_name)):
    if company_name[i]==company_name[i-1]:
        temp.append(company_sale[i])
    else:
        max_sale.append(max(temp))
        min_sale.append(min(temp))
        avg_sale.append(sum(temp)/len(temp))
        name.append(company_name[i-1])
        temp=[]
        
"""  最大值、最小值、平均值的分布图
bar_width=0.5
plt.figure(figsize = (8, 6),dpi = 120,facecolor = 'lightgray')  
plt.bar(x=np.arange(len(name)),height=max_sale,label='max',color='steelblue',width=bar_width)
for x,y in enumerate(max_sale):
    plt.text(x-0.5,y+0.2,'%.f' %round(y,1),va='bottom')
plt.xticks(np.arange(len(name)),name,rotation=270)
plt.legend()
plt.show()


plt.figure(figsize = (8, 6),dpi = 120,facecolor = 'lightgray')
plt.bar(x=np.arange(len(name)),height=min_sale,label='min',color='steelblue',width=bar_width)
for x,y in enumerate(min_sale):
    plt.text(x-0.1,y+0.2,'%.f' %round(y,1),va='bottom')
plt.xticks(np.arange(len(name)),name,rotation=270)
plt.legend()
plt.show()

plt.figure(figsize = (8, 6),dpi = 120,facecolor = 'lightgray')
plt.bar(x=np.arange(len(name)),height=avg_sale,label='avg',color='steelblue',width=bar_width)
for x,y in enumerate(avg_sale):
    plt.text(x-0.5,y+0.2,'%.f' %round(y,1),va='bottom')
plt.xticks(np.arange(len(name)),name,rotation=270)
plt.legend()
plt.show()
"""

#三表和一
x=np.arange(len(max_sale))
bar_width = 0.2
x_1 = [i for i in range(16)]
x_2 = [i+bar_width for i in x_1]
x_3 = [i+bar_width*2 for i in x_1]
max1_sale=[]
min1_sale=[]
m=sum(max_sale)/len(max_sale)
n=sum(min_sale)/len(max_sale)
for i in range(0,len(max_sale)):
    max1_sale.append(max_sale[i]/10)
    min1_sale.append(min_sale[i]*10)

plt.bar(x_1,max1_sale,bar_width,label="max/10")
plt.bar(x_2,avg_sale,bar_width,label="avg",color='#FFD700')
plt.bar(x_3,min1_sale,bar_width,label="min*10",color='#ADFF2F')
plt.legend(loc=5)
plt.xticks(np.arange(len(name)),name,rotation=270)
plt.ylabel("单位：（万元）")
plt.show()