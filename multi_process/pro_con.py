import multiprocessing
import random
import time


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue: multiprocessing.Queue = queue

    def run(self) -> None:
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Process Producer: item {} appended to queue {}'.format(item, self.name))
            time.sleep(1)
            print('The size of the queue is {}'.format(self.queue.qsize()))


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super(Consumer, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):
                print('the queue is empty')
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print('Consumer :{} popped from {}'.format(item, self.name))

                time.sleep(1)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    producer = Producer(queue)
    consumer = Consumer(queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
