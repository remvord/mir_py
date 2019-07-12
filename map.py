if __name__ == '__main__':
    m = {'key1': 100, 'key2': 200}
    print(type(m))
    print(len(m))

    # m = None
    if m is None:
        print('None')
    else:
        print('Not None')
    # if m is True:
    #     print('Not Empty')
    # else:
    #     print('Empty')
    print(m.keys())
    for r in m.items():
        print(r[1])
