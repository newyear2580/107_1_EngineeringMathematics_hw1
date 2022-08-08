import numpy as np
import matplotlib.pyplot as plt

x = np.linspace ( 0, 4 * np.pi, 100 ) 
y = np.tan( x ) - x - 1

plt.plot ( x, y )
plt.xlabel ( 'x' )
plt.ylabel ( 'y' )
plt.title ( 'Plot of the Function dy/dy = (x+y+1)^2' )
plt.text ( 0.2, -60.0, 'Copyright@10627109' ) # 請加上你的數位簽章
plt.show ( )
