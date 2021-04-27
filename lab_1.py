def list_func():
    m = []
    for i in range(1, 11):
        arr = []
        for j in range(1, 11):
            arr.append(j)
        m.append(arr)

    for n, i in enumerate(m):
        st = ''
        for n2, j in enumerate(i):
            if i[n] == 1 or n2 == 2 or n == n2:
                ch = str(j)
                st += f' *{ch}'
            else:
                st += f' {str(j)} '

        print(st, sep='', end='\n')


list_func()





def fact(n):
    fact1 = 1
    for i in range(1, n + 1):
        fact1 *= i
    return fact1


print(fact(5))
