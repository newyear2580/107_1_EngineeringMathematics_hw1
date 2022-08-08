import numpy as np
import matplotlib.pyplot as plt
from sympy import *              # 導入sympy
x,y,z = symbols('x y z')         # 定義符號

def f(x):
    y = x**2
    return y

x = np.linspace(-1.5, 2.5, 100)
y = f(x)
plt.plot(x,y)


x = 1
for i in range( 0, 11 ):
    print('(x', i, ',', 'Y', i, ') =', '(', x, ',', x**2, ')' )
    
    d = 2*x
    plt.plot(x, x**2, 'ko-' )
    x = x - 0.1*d
    


plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of the Function f(x) = x**2')
plt.text( -1, 5, 'Copyright@10627109') 

plt.show()
