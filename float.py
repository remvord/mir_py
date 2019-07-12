if __name__ == '__main__':
    f = 1.5153456
    print(dir(f))
    print(type(f))
    i = round(f, 2)
    print(type(i))
    print('-' * 20)
    i = 2.5
    i1 = int(i)
    print(i1)

    try:
        breakpoint()
        print('-' + str(20) + (1 == 1))
    except:
        print('Error')
    print(10 / 0)
