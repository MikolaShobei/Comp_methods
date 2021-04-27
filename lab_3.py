import numpy as np
import matplotlib.pyplot as plt


class Flying:
    def __init__(self, m, s, beta, k2: 0):
        self.beta = beta
        self.m = m
        self.S = s
        self.k2 = k2

    v0 = 15
    deg = np.pi / 180
    g = 9.81
    T = 10
    dt = 0.01
    n = int(T / dt)
    X = []
    Y = []
    VX = []
    VY = []
    x = 0
    y = 0

    def func(self):
        Vx = np.cos(self.beta * self.deg) * self.v0
        Vy = np.sin(self.beta * self.deg) * self.v0
        for i in range(self.n):
            self.v = (Vx ** 2 + Vy ** 2) ** 0.5
            self.Fg = self.m * self.g
            Vx = Vx + self.dt * (-self.k2 * Vx / self.v)
            Vy = Vy + self.dt * (-self.k2 * Vy / self.v - self.Fg)

            self.x = self.x + Vx * self.dt
            self.y = self.y + Vy * self.dt

            self.X = np.append(self.X, self.x)
            self.Y = np.append(self.Y, self.y)
            self.VX = np.append(self.VX, Vx)
            self.VY = np.append(self.VY, Vy)

            if self.y < 0:
                break

        fig, ax = plt.subplots()
        plt.subplot(221)
        plt.plot(self.X, self.Y, 'g--', lw=5)

        plt.title('graph1')
        plt.xlabel('x')
        plt.ylabel('y')

        time = np.arange(0, len(self.VY) * self.dt, self.dt)
        plt.subplot(222)
        plt.plot(time, self.X, 'b', lw=2)

        plt.title('graph2')
        plt.xlabel('X')
        plt.ylabel('t')

        plt.subplot(223)
        plt.plot(time, self.Y, 'b', lw=2.5)

        plt.title('graph3')
        plt.xlabel('Y')
        plt.ylabel('t')
        plt.grid(True)

        fig.set_size_inches(8, 5)
        plt.show()


f1 = Flying(m=1, s=0.2, k2=0, beta=26)
f1.func()
