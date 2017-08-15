import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

delta = 0.2
x = np.arange(-3, 3, delta)
y = np.arange(-3, 3, delta)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
x = X.flatten()
y = Y.flatten()
z = Z.flatten()

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.01)

fig = plt.figure()
plt.contour(X, Y, Z) #注意这里是大写X ,Y,Z

fig = plt.figure()
plt.contour(X, Y, Z,[1,2,3])

plt.show()
plt.waitforbuttonpress()