# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:20:49 2019

@author: 萧墨离
"""
#https://blog.csdn.net/monotonomo/article/details/83342768
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import xlrd
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
sns.set_style('whitegrid')


worksheet=xlrd.open_workbook(u'D:\Desktop\合格表.xlsx')
sheet_names=worksheet.sheet_names()
for sheet_name in sheet_names:
    sheet=worksheet.sheet_by_name(sheet_name)
company_name=sheet.col_values(4)
company_sale=sheet.col_values(5)

#
name=[]
sale=[]  #计算机行业的销售
for i in range(0,len(company_name)):
    if company_name[i] == "计算机通信制造业":
        name.append(company_name[i])
        sale.append(company_sale[i])
color = cm.viridis(0.5)
f, ax = plt.subplots(1,1)
ax.plot(iter, sale, color=color)
ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
exp_dir = 'Plot/'
if not os.path.exists(exp_dir):    
    os.makedirs(exp_dir, exist_ok=True)
else:    
    os.makedirs(exp_dir, exist_ok=True)
f.savefig(os.path.join('Plot', 'reward' + '.png'), dpi=1000)
plt.show()