import unittest
from observer import Observer, Observable


class WaterHeater(Observable):
    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        print('当前水温：{}'.format(self.__temperature))
        self.notify_observers()


class WashingMode(Observer):
    def update(self, observable, obj):
        if isinstance(observable, WaterHeater) and 50 <= observable.get_temperature() <= 70:
            print('水已烧好！可以洗澡')


class DrinkingMode(Observer):
    def update(self, observable, obj):
        if isinstance(observable, WaterHeater) and 100 <= observable.get_temperature():
            print('水已烧开！可以喝水')


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
