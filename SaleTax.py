# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:09:18 2019

@author: 萧墨离
"""

import matplotlib.pyplot as plt
import xlrd
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']


worksheet=xlrd.open_workbook(u'D:\Desktop\合格表.xlsx')
sheet_names=worksheet.sheet_names()
for sheet_name in sheet_names:
    sheet=worksheet.sheet_by_name(sheet_name)
company_name=sheet.col_values(4)
company_sale=sheet.col_values(5)
company_tax=sheet.col_values(6)
del company_name[0]
#company_name.append(0)
del company_sale[0]
#company_sale.append(0)
del company_tax[0]

#去掉极端值
x=sum(company_sale)/len(company_sale)
y=sum(company_tax)/len(company_sale)
for i in range(1,len(company_name)):
    if company_sale[i]>=x or company_tax[i]>=y :
        #company_name[i]=0
        company_sale[i]=0
        company_tax[i]=0
        


plt.xlabel('销售收入')   
plt.ylabel('交税额')  
plt.scatter(company_sale,company_tax,marker=".")
plt.plot([0,25000],[0,1000],'r',linestyle='--')
plt.show()

