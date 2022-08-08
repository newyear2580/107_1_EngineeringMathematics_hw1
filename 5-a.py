import numpy as np
import matplotlib.pyplot as plt

x = np.linspace ( -3, 3, 100 ) # 於 [-3, 3] 產生 100 個點
y = np.exp ( -x**2/2 ) 

plt.plot ( x, y )
plt.xlabel ( 'x' )
plt.ylabel ( 'y' )
plt.title ( 'Plot of the Function dy/dx = -xy' )
plt.text ( 0.5, 0.9, 'Copyright@10627109' ) # 請加上你的數位簽章
plt.show ( )
