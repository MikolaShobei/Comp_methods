import numpy as np
import matplotlib.pyplot as plt


s = [254, 1, 1, 1, 29, 1, 2, 11, 1, 1, 3, 1, 3, 2, 3, 1, 2, 3, 1]
s1 = set(s)
print(s1)
s2 = [s.count(i) for i in s1]
# print(s.count(1))
# print(set(s2))
fig, ay = plt.subplots()
ay.plot(list(s1), s2, lw=3)
# plt.legend(['euler`s_method', 'runge_cute`s_method'])
plt.title('coffee_cooling')
plt.xlabel('square')
plt.ylabel('N')
plt.grid(True)

fig.set_size_inches(9, 8.5)
plt.show()
