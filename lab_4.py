import random
import tkinter as Tk

import matplotlib.pyplot as plt


def percolation(p, l):
    n = l
    m = l

    r = [[0 for x in range(n)] for x in range(m)]
    s = [[0 for x in range(m)] for x in range(n)]

    for i in range(0, n):
        for j in range(0, m):
            r[i][j] = random.random()
            if r[i][j] < p:
                s[i][j] = 1
            else:
                s[i][j] = 0

    squares = []
    flag = False

    def find_cluster_squares(i, j, arr):
        cluster_indexes = [(i, j)]
        local_flag = False
        local_cluster_square = 0
        while not not cluster_indexes:
            index_1, index_2 = cluster_indexes[0]
            local_cluster_square += 1

            if index_2 > 0 and arr[index_1][index_2 - 1] == 1:
                cluster_indexes.append((index_1, index_2 - 1))

            if index_2 < len(arr[0]) - 1 and arr[index_1][index_2 + 1] == 1:
                cluster_indexes.append((index_1, index_2 + 1))

            if index_1 < len(arr) - 1 and arr[index_1 + 1][index_2] == 1:
                cluster_indexes.append((index_1 + 1, index_2))

            if (i == 0 and index_1 == len(arr[1]) - 1) or (j == 0 and index_2 == len(arr[1]) - 1):
                local_flag = True

            cluster_indexes.pop(0)
            arr[index_1][index_2] = 0

        return [local_cluster_square, local_flag]

    for index_i, i in enumerate(s):
        for index_j, j in enumerate(i):
            if j == 1:
                get_cluster_square, get_local_flag = find_cluster_squares(index_i, index_j, s)
                squares.append(get_cluster_square)
                if get_local_flag:
                    flag = get_local_flag

    if flag is True:
        x0 = 10
        y0 = 10
        dx = 20
        dy = 20
        x1 = 30
        y1 = 30

        root = Tk.Tk()

        can = Tk.Canvas(root, width=500, height=500)
        can.pack()
        can.pack(fill='both')
        for i in range(0, n):
            for j in range(0, m):
                if r[i][j] < p:
                    can.create_rectangle(x0, y0, x1, y1, fill="green")
                    can.create_text((x0 + x1) / 2, (y0 + y1) / 2, text="1", font=("Helvectica", "8"))

                else:
                    can.create_rectangle(x0, y0, x1, y1, fill="yellow")
                    can.create_text((x0 + x1) / 2, (y0 + y1) / 2, text="0", font=("Helvectica", "8"))
                y0 += dy
                y1 += dy
            y0 = 10
            y1 = 30
            x0 += dx
            x1 += dx

        print(p, '- Поріг протікання')
        print(len(squares), '- всього кластерів')

        unique_squares = list(set(list(squares)))
        unique_squares.sort()
        unique_squares_num = [squares.count(i) for i in unique_squares]

        fig, ay = plt.subplots()
        ay.plot(list(unique_squares), unique_squares_num, lw=3)
        plt.title('My graphic')
        plt.xlabel('Square')
        plt.ylabel('N')
        plt.grid(True)

        fig.set_size_inches(19, 8.5)
        plt.show()

        root.mainloop()

    return flag


def breakthrough_point(p, l):
    while True:
        local_flag = percolation(p, l)

        if local_flag:
            break
        p += 0.01


breakthrough_point(0.4, 16)
