from threading import Thread, Lock, Condition


class Worker(Thread):
    def __init__(self, name, items, lock, cond):
        super().__init__()
        self.name = name
        self.items = items
        self.cond = cond
        self.lock=lock

    def run(self):
        # self.lock.acquire()
        #
        with self.cond:
            self.cond.wait()
        print(f'{self.name}: {self.items.pop(0)}')

        # self.lock.release


def start04():
    li = list(range(1, 101))
    cond = Condition()
    lock = Lock()
    t1 = Worker("Thread1", li, lock, cond)
    t2 = Worker("Thread2", li, lock, cond)
    t1.start()
    t2.start()
    with cond:
        cond.notify(1)
    with cond:
        cond.notify(1)
    t1.join()
    t2.join()


start04()