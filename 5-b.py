import numpy as np
import matplotlib.pyplot as plt

x = np.linspace ( 0, 2 * np.pi, 100 ) # 於 [-3, 3] 產生 100 個點
y = np.sin( x**2 / 2  + np.pi / 2 )

plt.plot ( x, y )
plt.xlabel ( 'x' )
plt.ylabel ( 'y' )
plt.title ( 'Plot of the Function dy/dy = x√(1-y^2)' )
plt.text ( 0.2, -1.0, 'Copyright@10627109' ) # 請加上你的數位簽章
plt.show ( )

