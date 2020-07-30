import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2*np.pi,2*np.pi,np.pi)
y= np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
plt.show()