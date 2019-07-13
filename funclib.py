# print('hello')
YES = 'Yes'
__NO = 'No'
_CANCEL = 'Finish'


def f1(n):
    try:
        # n = n*1
        return n * n
    except TypeError as e:
        print(e)
        raise e


if __name__ == '__main__':
    pass