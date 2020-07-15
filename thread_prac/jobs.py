from multiprocessing import Queue
from multiprocessing import JoinableQueue
from multiprocessing import Process
import time

def main():
    jobs = JoinableQueue()
    results = Queue()
    create_process(jobs, results)
    time.sleep(2)
    for i in range(50):
        print('生产开始：', i)
        jobs.put(str(i))
    try:
        jobs.join()
    except KeyboardInterrupt:
        exit()
    while not results.empty():
        print(results.get_nowait())


class Worker(Process):
    def __init__(self, name, jobs: JoinableQueue, results: Queue):
        super().__init__()
        self.name = name
        self.jobs: JoinableQueue = jobs
        self.results: Queue = results

    def run(self):
        while True:
            print(f'消费者 {self.name}  就绪')
            val: str = self.jobs.get()
            print(f'{self.name} 消费者得到数据')
            val = val + '.orientsec.com.cn'
            self.results.put(val)
            self.jobs.task_done()


def create_process(jobs, results, concurrency=4):
    for i in range(concurrency):
        worker = Worker(str(i) + " workder", jobs, results)
        worker.daemon = True
        worker.start()


if __name__ == '__main__':
    main()
