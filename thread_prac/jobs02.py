import time
from multiprocessing import Process
from multiprocessing import Queue, JoinableQueue


def main():
    jobs = JoinableQueue()
    results = Queue()
    create_process(jobs, results)
    time.sleep(2)
    for i in range(50):
        print(f'生产者{i} 生产任务：("sunyibin{i}", {i})')
        jobs.put((f'sunyibin{i}', i))
    try:
        jobs.join()
    except KeyboardInterrupt:
        exit()
    while not results.empty():
        print(results.get_nowait())


class Worker(Process):
    def __init__(self, name, jobs, results):
        super().__init__()
        self.name = name
        self.jobs = jobs
        self.results = results

    def run(self):
        while True:
            print(f'消费者 {self.name}  就绪')
            name, age = self.jobs.get()
            print(f'{self.name} 处理任务 :{name}, {age}')
            msg = f'{name} is now {str(age)} years old'
            self.results.put(msg)
            self.jobs.task_done()


def create_process(jobs, results, concurrency=4):
    for i in range(concurrency):
        worker = Worker(str(i) + ' worker', jobs, results)
        worker.daemon = True
        worker.start()


if __name__ == '__main__':
    main()
