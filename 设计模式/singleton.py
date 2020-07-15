import time
from threading import Thread, Lock


class Singleton(type):

    def __init__(cls, *args, **kwargs):

        super(Singleton, cls).__init__(*args, **kwargs)
        # time.sleep(1)
        cls.__instance = None
        cls.__lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class Car(metaclass=Singleton):
    def __init__(self, name):
        time.sleep(1)
        self.__name = name

    @property
    def name(self):
        return self.__name


def task(name):
    # time.sleep(1)
    car = Car(name)
    print(f'car name:{car.name}, obj:{car}')


if __name__ == '__main__':

    # bwm = Car('bmw')
    # audi = Car('audi')
    # print(bwm.name)
    # print(audi.name)
    workers = []
    for i in range(10):
        worker = Thread(target=task, args=(f'bmw{i}',))
        worker.start()
    #     workers.append(worker)
    # [worker.start() for worker in workers]
    # [worker.join() for worker in workers]
