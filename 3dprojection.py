# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 22:12:53 2019

@author: 萧墨离
"""
import matplotlib.pyplot as plt
import xlrd
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']

from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 
import numpy as np 

worksheet=xlrd.open_workbook(u'D:\Desktop\合格表.xlsx')
sheet_names=worksheet.sheet_names()
for sheet_name in sheet_names:
    sheet=worksheet.sheet_by_name(sheet_name)
name=sheet.col_values(0)
sale=sheet.col_values(5)
area=sheet.col_values(7)
del name[0]
del sale[0]
del area[0]

fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
x, y = np.random.rand(2, 100) * 4
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]]) 
  
# Construct arrays for the anchor positions of the 16 bars. 
# Note: np.meshgrid gives arrays in (ny, nx) so we use 'F' to flatten xpos, 
# ypos in column-major order. For numpy >= 1.7, we could instead call meshgrid 
# with indexing='ij'. 
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25) 
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos) 
  
# Construct arrays with the dimensions for the 16 bars. 
dx = 0.5 * np.ones_like(zpos) 
dy = dx.copy() 
dz = hist.flatten() 
  
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average') 
  
plt.show()