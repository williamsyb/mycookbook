import time
from threading import Thread, Lock


class WorkerA(Thread):
    def __init__(self, lock01, lock02):
        super(WorkerA, self).__init__()
        self.__lock01 = lock01
        self.__lock02 = lock02

    def run(self):
        for i in range(1, 52, 2):
            self.__lock02.acquire()
            print(f'{i}', end='')
            print(f'{i + 1}', end='')
            time.sleep(0.5)
            self.__lock01.release()


class WorkerB(Thread):
    def __init__(self, lock01, lock02):
        super(WorkerB, self).__init__()
        self.__lock01 = lock01
        self.__lock02 = lock02

    def run(self):
        for i in range(26):
            self.__lock01.acquire()
            print(chr(i + ord('A')))
            time.sleep(0.5)
            self.__lock02.release()


if __name__ == '__main__':
    lock01 = Lock()
    lock02 = Lock()

    wa = WorkerA(lock01, lock02)
    wb = WorkerB(lock01, lock02)

    lock01.acquire()
    wa.start()
    wb.start()
