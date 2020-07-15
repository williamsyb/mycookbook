from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """接口"""

    @abstractmethod
    def update(self, observable, obj):
        """
        :param observable: 被观察者对象
        :param obj: 消息主题
        """
        pass


class Observable(metaclass=ABCMeta):
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, obj=0):
        for o in self.__observers:
            o.update(self, obj)
