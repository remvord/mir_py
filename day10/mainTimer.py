import threading
import time
import datetime
import queue
import random


def job():
    threading.current_thread().setName('job')

    def work():
        print('---work', datetime.datetime.now())
    while True:
        print('---job---', datetime.datetime.now())
        t = threading.Timer(1, work)
        t.setName('timer'+str(datetime.datetime.now()))
        t.start()
        t.join()


if __name__ == '__main__':
    pass
    print('---Start---', datetime.datetime.now())
    t = threading.Timer(3, job)
    t.start()
    t.join()
    print('---After---')
