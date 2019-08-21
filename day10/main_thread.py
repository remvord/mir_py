import threading
import time, datetime


def work():
    c = 0
    while True:
        time.sleep(1)
        print(f'{datetime.datetime.now()} ThreaDer {threading.current_thread()}')
        c += 1
        if c == 5:
            break


if __name__ == '__main__':
    print('---Start---')
    t = threading.current_thread()
    t.setName('- My thread')
    print('nameThread', t.getName())
    print('isdaemon', t.daemon)
    print(threading.active_count())
    print(t.is_alive())
    tWork = threading.Thread(target=work, name='Work threader')
    # work()
    print(tWork.is_alive())
    tWork.start()
    tWork.join(1)
    print('---After ' + t.getName() + ' ---')
