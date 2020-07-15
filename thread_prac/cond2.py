import time
from threading import Thread, Condition

li = list(range(1, 101))
cond = Condition()


class Consumer01(Thread):
    def __init__(self, name, nums, con):
        Thread.__init__(self)
        self.name = name
        self.nums = nums
        self.con: Condition = con

    def consumer(self):
        self.con.acquire()
        num = self.nums.pop()
        print(f'{self.name}: {num}')
        if num % 2 == 0:
            self.con.wait()
        self.con.notify()
        self.con.release()

    def run(self):
        while len(self.nums) > 0:
            time.sleep(1)
            self.consumer()


class Consumer02(Thread):
    def __init__(self, name, nums, con):
        Thread.__init__(self)
        self.name = name
        self.nums = nums
        self.con: Condition = con

    def consumer(self):
        self.con.acquire()
        num = self.nums.pop()
        print(f'{self.name}: {num}')
        if num % 2 == 1:
            self.con.wait()
        self.con.notify()
        self.con.release()

    def run(self):
        while len(self.nums) > 0:
            time.sleep(2)
            self.consumer()


if __name__ == '__main__':
    consumer01 = Consumer01('Thread01', li, cond)
    consumer02 = Consumer02('Thread02', li, cond)
    consumer01.start()
    consumer02.start()
    consumer01.join()
    consumer02.join()
