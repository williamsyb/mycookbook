from threading import Thread, Lock


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class Car(metaclass=Singleton):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


if __name__ == '__main__':
    car01 = Car('01')
    car02 = Car('02')
    print(car01.name)
    print(car02.name)
    print(car01 is car02)
