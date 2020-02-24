# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 22:16:12 2019

@author: 萧墨离
"""

import matplotlib.pyplot as plt
import numpy as np
import xlrd
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']


data=xlrd.open_workbook(u'D:\Desktop\合格表.xlsx')
table=data.sheets()[0]
start=112
end=247
rows=end-start

sheet=[]   #计算机行业所有的数据
for x in range(start,end):
    values=[]
    row=table.row_values(x)
    for i in range(0,20):
        values.append(row[i])
    sheet.append(values)
    
"""
#计算机行业的销售和税收图
a=[i[5] for i in sheet]
b=[i[6] for i in sheet]
a1=[]
b1=[]
for i in range(0,len(a)):
    if a[i]<=100000:
        a1.append(a[i])
        b1.append(b[i])
plt.title('计算机行业的销售分析')
plt.xlabel('销售收入')   
plt.ylabel('交税额')  
#plt.scatter(a,b,marker=".") #本来的图
plt.scatter(a1,b1,marker=".")
plt.plot([0,80000],[0,8000],'r',linestyle='--')
plt.show()
"""

row0=[i[0] for i in sheet]  #企业名称
row5=[i[5] for i in sheet]   #销售收入
row6=[i[6] for i in sheet]  #交税
row16=[i[16] for i in sheet]  #安全事故类型
row17=[i[17] for i in sheet]  #国家安全标准化级别
row18=[i[18] for i in sheet]  #立案处罚情况
#row=[i[] for i in sheet]
rows0=[]
rows5=[]
rows6=[]
rows16=[]
rows17=[]
rows18=[]
#处理掉所有销售额大于100000的企业
for i in range(0,len(row0)):
    if row5[i]<=100000:
        rows0.append(row0[i])
        rows5.append(row5[i])
        rows6.append(row6[i])
        rows16.append(row16[i])
        rows17.append(row17[i])
        rows18.append(row18[i])
s1=[]
color=[]
markers=[]

for i in range(0,len(rows0)-1):
    n=0
    if rows16[i] == '有亡人事故':
        n=1
        s1.append(300)
        color.append('#FF0000')
    if rows17[i] == '三级':
        n=1
        s1.append(50)
        color.append('#90EE90')
    if rows17[i] == '二级':
        n=1
        s1.append(80)
        color.append('#228B22')
    if rows18[i] =='立案有处罚':
        n=1
        s1.append(300)
        color.append('#8B0000')
    if n==0:
        s1.append(10)
        color.append('blue')
plt.title('计算机行业的销售分析')
plt.xlabel('销售收入')   
plt.ylabel('交税额')  
plt.scatter(rows5,rows6,s=s1,c=color,marker='o',label='安全三级')
plt.plot([0,80000],[0,8000],'r',linestyle='--')
plt.show()