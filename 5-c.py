import numpy as np
import matplotlib.pyplot as plt

x = np.linspace ( 0, 4 * np.pi, 100 ) # 於 [-3, 3] 產生 100 個點
y = x*np.cos(x) + np.cos(x)

plt.plot ( x, y )
plt.xlabel ( 'x' )
plt.ylabel ( 'y' )
plt.title ( 'Plot of the Function dy/dy + tan(x)y = cosx' )
plt.text ( 4, -10, 'Copyright@10627109' ) # 請加上你的數位簽章
plt.show ( )
