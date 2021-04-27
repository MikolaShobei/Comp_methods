from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

pi = np.pi
eps0 = 8.8541e-12
k = 8.99e9
q1 = 7e-9
q2 = 12e-9
a = 0.025  # 25mm


def phi(x, y):
    return 5 * x ** 2 - 3 * y ** 2


def potencial(x, y, Q, x0, y0):
    return (Q * k) / np.sqrt((x - x0) ** 2 + (y - y0) ** 2)


DX = 0.100
DY = 0.100  # 100mm

dx = .001
LX = np.arange(-DX / 2, DX / 2, dx) + 0.001
LY = np.arange(-DY / 2, DY / 2, dx) - 0.001
X, Y = np.meshgrid(LX, LY)

PHI1 = potencial(X, Y, q1, -a / 2, 0) + potencial(X, Y, q2, a / 2, 0)
PHI2 = phi(X, Y)

Fi = np.gradient(PHI1)

plt.rcParams.update({'font.size': 22})

fig, ay = plt.subplots()

CS = ay.contour(X, Y, PHI1, 50)
ay.clabel(CS, inline=1, fontsize=10)
plt.title('Варіант 6')
plt.xlabel('X, m')
plt.ylabel('Y, m')
plt.grid(True)
fig.set_size_inches(10.5, 9.5)

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
3
# Plot the surface.
surf = ax.plot_surface(X, Y, PHI1, linewidth=1, antialiased=True)

plt.title('Варіант 6')
plt.xlabel('X, m')
plt.ylabel('Y, m')
plt.ylabel('U, V')
plt.grid(True)
fig.set_size_inches(10.5, 9.5)

fig, ax = plt.subplots()

# vector field(every 9 element, aka every 81 point)
q = ax.quiver(X[::9, ::9], Y[::9, ::9], Fi[0][::9, ::9] / dx, Fi[1][::9, ::9] / dx)

plt.title('Варіант 6')
plt.xlabel('X, m')
plt.ylabel('Y, m')
plt.grid(True)
fig.set_size_inches(10.5, 9.5)

fig, ay = plt.subplots()

CS = ay.contour(X, Y, PHI2)
ay.clabel(CS, inline=1, fontsize=10)
plt.title('Варіант 6')
plt.xlabel('X, m')
plt.ylabel('Y, m')
plt.grid(True)
fig.set_size_inches(10.5, 9.5)

plt.show()
