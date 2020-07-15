from abc import ABCMeta, abstractmethod
import unittest


class WaterHeater:
    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        print('当前温度是：' + str(self.__temperature))
        self.notifies()

    def add_observer(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, water_heater):
        pass


class WashingMode(Observer):
    def update(self, water_heater):
        if 70 > water_heater.get_temperature() > 50:
            print('水烧号了，可以洗澡了')


class DrinkingMode(Observer):
    def update(self, water_heater):
        if water_heater.get_temperature() >= 100:
            print('水烧开了，可以喝了')


class TestWaterHeater(unittest.TestCase):
    def test_observer(self):
        heater = WaterHeater()
        washing_observer = WashingMode()
        drinking_observer = DrinkingMode()
        heater.add_observer(washing_observer)
        heater.add_observer(drinking_observer)
        heater.set_temperature(40)
        heater.set_temperature(60)
        heater.set_temperature(100)


if __name__ == '__main__':
    unittest.main()
