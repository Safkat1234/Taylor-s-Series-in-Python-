#Taylor's Series in Python!
import numpy as np
from math import factorial
import matplotlib.pyplot as plot

x = np.linspace(0, 10, 100)
y = np.zeros(len(x))

figure = plot.figure()

for n in range(0, 10):
    #cos(x)
    taylor_term = (-1)**n * x**(2*n) / factorial(2*n)
    
    y = np.add(y, taylor_term)
    
    figure.clear()
    
    axis = figure.subplots()
    axis.plot(x,y)
    axis.set_xlabel('x')
    axis.set_xlabel('cos(x)')
    axis.set_title('Terms:{}'.format(n+1))
    
    plot.xlim(min(x), max(x))
    plot.ylim(-2, 2)
    
    
    plot.grid()
    plot.draw()
    
    plot.pause(0.05)
    
print(y)
plot.show()