import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(z,t):
    x = z[0]
    y = z[1]
    if t<5:
        u = 0
    else:
        u = 2
    dxdt = (-x+u)/2.0
    dydt = (-y+x)/5.0
    return [dxdt, dydt]

z0 = [0,0]

t = np.linspace(0,15, 150)
z = odeint(model, z0, t)

x = z[:, 0]
y = z[:, 1]
plt.plot(t,x, 'r-')
plt.plot(t,y, 'b:')
plt.show()
