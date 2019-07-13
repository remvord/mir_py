import time, datetime

if __name__ == '__main__':
    print(time.gmtime(0))
    print(type(time.time()))
    t = time.time()
    t1 = t+60*60*24*10
    print(t1)
    print(time.gmtime(t1))
    dd = datetime.datetime.fromtimestamp(t1)
    print(dd)