# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:29:16 2019

@author: 萧墨离
"""
import xlrd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn import metrics
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
import pygal
import heapq
from prettytable import PrettyTable

company=pd.read_csv(r'D:\Desktop\test.csv')
company.head()
"""
sns.lmplot(x='占地面积',y='销售收入',data=company,
           fit_reg=False,scatter_kws={'alpha':0.8,'color':'steelblue'})
plt.show()
"""
def k_SSE(X,clusters):  #拐点法
    K=range(1,clusters+1)
    TSSE=[]
    for k in K:
        SSE=[]
        kmeans=KMeans(n_clusters=k)
        kmeans.fit(X)
        labels=kmeans.labels_
        centers = kmeans.cluster_centers_
        for label in set(labels):
            SSE.append(np.sum((X.loc[labels==label,]-centers[label,:])**2))
        TSSE.append(np.sum(SSE))
    plt.rcParams['axes.unicode_minus']=False
    plt.style.use('ggplot')
    plt.plot(K,TSSE,'b*-')
    plt.xlabel('簇的个数')
    plt.ylabel('簇内离差平方和之和')
    plt.show()

def k_silhouette(X,clusters):   #轮廓系数法
    K=range(2,clusters+1)
    S=[]
    for k in K:
        kmeans=KMeans(n_clusters=k)
        kmeans.fit(X)
        labels=kmeans.labels_
        S.append(metrics.silhouette_score(X,labels,metric='euclidean'))
    plt.rcParams['axes.unicode_minus']=False
    plt.style.use('ggplot')
    plt.plot(K,S,'b*-')
    plt.xlabel('簇的个数')
    plt.ylabel('轮廓系数')
    plt.show()
    
def short_pair_wise_D(each_cluster):
    mu=each_cluster.mean(axis=0)
    Dk=sum(sum((each_cluster-mu)**2))*2.0*each_cluster.shape[0]
    return Dk

def compute_Wk(data,classfication_result):
    Wk=0
    label_set=set(classfication_result)
    for label in label_set:
        each_cluster=data[classfication_result==label,:]
        Wk=Wk+short_pair_wise_D(each_cluster)/(2.0*each_cluster.shape[0])
    return Wk

def gap_statistic(X,B=10,K=range(1,11),N_init=10):  #间隔统计量法
    X=np.array(X)
    shape=X.shape
    tops=X.max(axis=0)
    bots=X.min(axis=0)
    dists=np.matrix(np.diag(tops-bots))
    rands=np.random.random_sample(size=(B,shape[0],shape[1]))
    for i in range(B):
        rands[i,:,:]=rands[i,:,:]*dists+bots
    gaps=np.zeros(len(K))
    Wks=np.zeros(len(K))
    Wkbs=np.zeros((len(K),B))
    for idxk,k in enumerate(K):
        k_means=KMeans(n_clusters=k)
        k_means.fit(X)
        classfication_result=k_means.labels_
        Wks[idxk]=compute_Wk(X,classfication_result)
        for i in range(B):
            Xb=rands[i,:,:]
            k_means.fit(Xb)
            classfication_result_b=k_means.labels_
            Wkbs[idxk,i]=compute_Wk(Xb,classfication_result_b)
    gaps=(np.log(Wkbs).mean(axis=1)-np.log(Wks))
    sd_ks=np.std(np.log(Wkbs),axis=1)
    sk=sd_ks*np.sqrt(1+1.0/B)
    gapDiff=gaps[:-1]-gaps[1:]+sk[1:]
    plt.bar(np.arange(len(gapDiff))+1,gapDiff,color='steelblue')
    plt.xlabel('簇的个数')
    plt.ylabel('k的选择标准')
    plt.show()


X=preprocessing.minmax_scale(company[['销售收入','交税','占地面积']])
X=pd.DataFrame(X,columns=['销售收入','交税','占地面积'])
#k_SSE(X,15)     #拐点法
#k_silhouette(X,15)  
#gap_statistic(X)

"""              #处理之后的散点图
kmeans=KMeans(n_clusters=3)
kmeans.fit(X)
company['cluster']=kmeans.labels_
centers=[]
for i in company.cluster.unique():
    centers.append(company.ix[company.cluster==i,['销售收入','交税','占地面积']].mean())
centers=np.array(centers)

sns.lmplot(x='占地面积',y='销售收入',hue='cluster',data=company,markers=['^','+','s'],
           fit_reg=False,scatter_kws={'alpha':0.8,'color':'steelblue'},legend=False)
plt.xlabel('占地面积')
plt.ylabel('销售收入')
plt.show()
"""  
    
"""      雷达图   
centers_std=kmeans.cluster_centers_
radar_chart=pygal.Radar(fill=True)
radar_chart.x_labels=['销售收入','交税','占地面积']
radar_chart.add('C1',centers_std[0])
radar_chart.add('C2',centers_std[1])
radar_chart.add('C3',centers_std[2])
radar_chart.render_to_file('radar_chart.svg')
"""
    
#提出四个超常点
worksheet=xlrd.open_workbook(u'D:\Desktop\合格表.xlsx')
table=worksheet.sheets()[0]
c=table.col_values(8)
del c[0]

#找出四个亩均销售最大点
result=map(c.index,heapq.nlargest(4,c)) 
temp=[]
Inf=0
for i in range(4):
    temp.append(c.index(max(c))+1)
    c[c.index(max(c))]=Inf      #获得最大点的下标
    
r0=table.row_values(0)
r1=table.row_values(temp[0])
r2=table.row_values(temp[1])
r3=table.row_values(temp[2])
r4=table.row_values(temp[3])
mat="{:<20}{:<16}{:<16}{:<16}{:<16}"     #格式化输出
for i in range(0,len(r0)):
    if i is not 4:
        print(mat.format(r0[i]+":",r1[i],r2[i],r3[i],r4[i]))
    else:
        print("{:<12}{:<12}{:<12}{:<12}{:<12}".format(r0[i]+":",r1[i],r2[i],r3[i],r4[i]))