import threading
import time
import datetime
import queue
import random


def producer(q):
    c = 0
    while True:
        c += 1
        time.sleep(random.random())
        print(threading.current_thread().getName() +
              '-->put--->' + str(c))
        evnt = threading.Event()
        q.put((c, evnt))
        evnt.wait()


def consumer(q):
    while True:
        data = q.get()
        time.sleep(random.random())
        print(data[0], threading.current_thread().getName())
        data[1].set()


if __name__ == '__main__':
    pass
    print('---Start---')
    a = [1, 2, 3, 4, 5]
    q = queue.Queue()
    tp = threading.Thread(target=producer, args=(q,), name='prod1')
    tc1 = threading.Thread(target=consumer, args=(q,), name='consum1')
    # tc2 = threading.Thread(target=consumer, args=(q,), name='consum2')
    tc1.start()
    # tc2.start()
    tp.start()
    tp.join()
    tc1.join()
    # tc2.join()
    print('---After---')
