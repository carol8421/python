# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:12:16 2019

@author: 萧墨离
"""

import matplotlib.pyplot as plt
import xlrd

worksheet=xlrd.open_workbook(u'D:\Desktop\合格表.xlsx')
sheet_names=worksheet.sheet_names()
for sheet_name in sheet_names:
    sheet=worksheet.sheet_by_name(sheet_name)
company_name=sheet.col_values(4)
del company_name[0]

k=0
j=1
c=[]  #行业数量占比
d=[]  #企业名称的代号
for i in range(0,len(company_name)):
    if company_name[i]==company_name[i-1]:
        k+=1
    else:
        c.append(k/len(company_name))
        d.append(company_name[i-1])
        k=0
        j+=1
c[0]=1-sum(c)
#开始画图
plt.pie(x=c,labels=d,radius=3,autopct='%.1f%%')
plt.show()