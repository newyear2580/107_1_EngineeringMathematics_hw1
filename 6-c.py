from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


X = np.linspace ( -2, 2, 100 ) # 於 [-2, 2] 產生 100 個點
Y = np.linspace ( -2, 2, 100 )
x, y = np.meshgrid ( X, Y ) # 產生網狀格點
z = np.log( np.abs( np.sin(x) ) ) + y + 2*np.log( np.abs( y ) ) # 函數 z = f (x, y)

# 3D Plot (Surface Plot)
fig = plt.figure ( 1 )
ax = fig.gca ( projection = '3d' )
ax.plot_surface ( x, y, z, cmap = cm.coolwarm, linewidth = 0, antialiased = False )
plt.xlabel ( 'x' )
plt.ylabel ( 'y' )
plt.title ( '3D Plot of f (x,y)' )

# Contour Plot
plt.figure ( 2 )
plt.contour ( x, y, z, 30 ) # 產生 30 個 Contours
plt.xlabel ( 'x' )
plt.ylabel ( 'y' )
plt.title ( 'Contour Plot of f (x,y)' )
plt.text ( 0.5, -1.9, 'Copyright@10627109' )
plt.show()
