# print('hello')
YES = 'YES'
__NO = 'NO'
_CANCEL = 'CANCEL'

count = 0


def f1(n):
    try:
        # n = n*1
        if type(n) is str:
            return 'concat ' + (n + n)
        if type(n) is int:
            return n + n
        raise TypeError

    except TypeError as e:
        print(e)
        raise e


def f2(k, n1=10, n2=100, n3=300):
    return k+n1+n2+n3


def f3(k):
    for r in k:
        print(r)


def f4(*k):
    for r in k:
        print(r)


def f5(**k):
    for r in k:
        print(f'{r}={k[r]}')


def add(a):
    x = 1
    print(f'x={x}')

    def add1():
        nonlocal x
        x = 10
        return a + x
    print(f'x={x}')
    return add1() + x
    add1()


def f6():
    global count
    count = count + 1


def NO():
    global __NO
    return __NO


if __name__ == '__main__':
    pass
