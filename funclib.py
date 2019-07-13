# print('hello')
YES = 'Yes'
__NO = 'No'
_CANCEL = 'Finish'


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


if __name__ == '__main__':
    pass
