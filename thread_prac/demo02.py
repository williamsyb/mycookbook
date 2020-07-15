from threading import Thread
import time


class Test(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def start(self):
        print('start')
        time.sleep(2)
        print('end')


if __name__ == '__main__':
    t = Test('hello')
    start = time.time()
    t.start()
    print("test thread name is: {}".format(t.name))
    print("main thread end, all time is{}".format(time.time() - start))
