if __name__ == '__main__':
    s = 'Person  name {0} job {1} salary {2}'
    n = 'Ivanov'
    j = 'Director'
    sal = 1000
    s1 = f'Person  name {n} job {j} salary {sal}'
    print(s.format(n, j, sal))
    print(s1)

