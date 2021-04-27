import numpy as np
import matplotlib.pyplot as plot


def euler_method(t1, t2, k):
    dt = 0.01
    time = 60

    def f(kof, temp_n):
        return -kof * (temp_n - t2)

    time_axis = np.arange(0, time + dt, dt)
    temperature_axis = np.zeros(len(time_axis))
    temperature_axis[0] = t1

    for i in range(len(time_axis) - 1):
        temperature_axis[i + 1] = temperature_axis[i] + f(k, temperature_axis[i]) * dt

    fig, ay = plot.subplots()
    ay.plot(time_axis, temperature_axis, lw=3)
    plot.title(f'coffee_cooling_Euler_method_k={k}')
    plot.xlabel('time')
    plot.ylabel('T')
    plot.grid(True)

    fig.set_size_inches(9, 8.5)
    plot.show()

    return [time_axis, temperature_axis]


def runge_cute(t1, t2, k):
    dt = 0.01
    time = 60

    def f(kof, temp_n):
        return -kof * (temp_n - t2)

    time_axis = np.arange(0, time + dt, dt)
    temperature_axis = np.zeros(len(time_axis))

    for i in range(len(time_axis)):
        k1 = f(time_axis[i], t1) * dt
        k2 = f(k, t1 + k1 / 2) * dt
        k3 = f(k, t1 + k2 / 2) * dt
        k4 = f(k, t1 + k3) * dt
        t1 = t1 + (k1 + k2 * 2 + k3 * 2 + k4) / 6
        temperature_axis[i] = t1

    fig, ay = plot.subplots()
    ay.plot(time_axis, temperature_axis, lw=3)
    plot.title(f'coffee_cooling_Runge-Cute_method_k={k}')
    plot.xlabel('time')
    plot.ylabel('T')
    plot.grid(True)

    fig.set_size_inches(9, 8.5)
    plot.show()

    return [time_axis, temperature_axis]



[time_axis_euler, temperature_axis_euler] = euler_method(100, 20, 0.12)


[time_axis_runge_cute, temperature_axis] = runge_cute(100, 20, 0.12)



fig, ay = plot.subplots()
ay.plot(time_axis_euler, temperature_axis_euler, lw=3)
ay.plot(time_axis_runge_cute, temperature_axis, 'g--', lw=3)
plot.legend(['euler`s_method', 'runge_cute`s_method'])
plot.title('coffee_cooling')
plot.xlabel('time')
plot.ylabel('T')
plot.grid(True)

fig.set_size_inches(9, 8.5)
plot.show()
