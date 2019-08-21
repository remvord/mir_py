import threading
import time, datetime, random


class Printer():
    __lock = threading.Lock()

    def render(self, text):
        # try:
        with self.__lock:
            # self.__lock.acquire()
            time.sleep(random.random())
            print('[' + threading.current_thread().getName())
            time.sleep(random.random())
            print(text, '   ' + threading.current_thread().getName())
            time.sleep(random.random())
            print(threading.current_thread().getName() + ']')
        # finally:
        #     self.__lock.release()


class Query(threading.Thread):
    def __init__(self, text, p):
        super(Query, self).__init__(name=text)
        self.__text = text
        self.__p = p

    def __report(self):
        time.sleep(random.random())
        self.__p.render(self.__text)

    def run(self) -> None:
        self.__report()


if __name__ == '__main__':
    pass
    print('---Start---')
    p = Printer()
    Query('One ', p).start()
    Query('Two ', p).start()
    Query('Three ', p).start()
    print(threading.active_count())
    print('---After---')
