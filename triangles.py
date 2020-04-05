'''
杨辉三角，用生成器实现
'''


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def triange():
    L = [1]
    while True:
        yield L
        L = [L[x] + L[x + 1] for x in range(len(L) - 1)]
        L.insert(0, 1)
        L.append(1)
        if len(L) > 10:
            break


if __name__ == '__main__':
    g = triange()
    while True:
        try:
            x = next(g)
            print('g:', x)
        except StopIteration as e:
            print('Generator return value:')
            break
