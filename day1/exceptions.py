import time
import sys


# try:
#     # [i for i in range(9999999999)]
#     s = []
#     for r in range(100000000):
#         s[r] = str(r)
#     # while (True):
#     #     i = input('Input q to quit ')
#     #     if i == 'q':
#     #         exit(100)
#
class MyException(BaseException):
    mess = 'Пользовательский выход'


if __name__ == '__main__':
    while (True):
        try:
            s = 10
            k = input('0 - error, 10 - exit ')
            r = s / int(k)
            print(r)
            if r < 2:
                exit()

            b = MyException
            raise b

        except SystemExit as e:
            print("Press key q {e.code}")
            exit(100)
        except KeyboardInterrupt as e:
            print('\nUser terminate {e}')
        except ZeroDivisionError as e:
            print('На ноль делить нельзя!!!  ')
        finally:
            print('Продолжение----')
