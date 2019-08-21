while (True):
    n = a.fetchmany()
    print(a.rowcount)
    if n :
        break