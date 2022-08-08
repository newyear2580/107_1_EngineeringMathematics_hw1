import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = x**3 - x*3 + 3
    return y

x = np.linspace( -1.5, 2.5, 100 )
y = f(x)
plt.plot( x, y )

x = 2
for i in range( 0, 11 ):
    y = f(x)
    print('(X',i,',','Y',i,')','(',x,',',y,')')
    d = 3*x**2 -3
    y = f(x)
    plt.plot( x, y, 'ko-' )
    x = x - 0.1*d
    

plt.xlabel('x')
plt.ylabel('y')
plt.title( 'Plot of the Function f(x) = x**3 - 3*x + 3' )
plt.text( 0, 8, 'Copyright@10627109' )

plt.show()
