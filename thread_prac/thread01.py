from time import sleep, time
import threading
# from Queue import Queue
from queue import Queue
from threading import Thread


def process_num(num):
    num_add = num + 1
    sleep(3)
    print(str(threading.current_thread()) + ": " + str(num) + " → " + str(num_add))


class ProcessWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            num = self.queue.get()
            process_num(num)
            self.queue.task_done()


thread_arr = []


def main():
    ts = time()
    queue = Queue()
    for x in range(10):
        worker = ProcessWorker(queue)
        worker.daemon = True
        worker.start()
        thread_arr.append(worker)
    for num in range(10):
        queue.put(num)
    # queue.join()
    for _ in thread_arr:
        _.join(2)
    print("cost time is: {:.2f}s".format(time() - ts))


if __name__ == "__main__":
    main()
