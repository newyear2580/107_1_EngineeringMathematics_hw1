import numpy as np
import matplotlib.pyplot as plt


def f(x):
    y = x**2
    return y

x = np.linspace( -1.5, 2.5, 100 )
y = f(x)
plt.plot( x, y )

x = 1
for i in range( 0, 11 ):
    print('(X',i,',','Y',i,')','(',x,',',x**2,')')

    d = 2*x             # x^2的微分
    plt.plot( x, x**2, 'ko-' )
    x = x - x**2/d      # x(n+1) = x(n) - f(x(n))/f'(x(n))
                        # x(n+1) = x(n) / 2
    

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of the Function f(x) = x**2')
plt.text( -1, 5, 'Copyright@10627109')

plt.show()
