from abc import ABCMeta, abstractmethod
import unittest


class Water:
    def __init__(self, state):
        self.__state = state
        self.__temperature = 25

    def set_state(self, state):
        self.__state = state

    def change_state(self, state):
        if self.__state:
            print(f'由{self.__state.get_name()}转为{state.get_name()}')
        else:
            print(f'初始化为:{self.__state.get_name()}')
        self.__state = state

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        if self.__temperature < 0:
            self.change_state(SolidState('固态'))
        elif self.__temperature <= 100:
            self.change_state(LiquidState('液态'))
        else:
            self.change_state(GaseousState('气态'))

    def rise_temperature(self, step):
        self.set_temperature(self.__temperature + step)

    def reduce_temperature(self, step):
        self.set_temperature(self.__temperature - step)

    def behavior(self):
        self.__state.behavior(self)


class State(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def behavior(self, water):
        pass


class SolidState(State):
    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print(f'我是固体，当前{str(water.get_temperature())}, 我很刚~')


class LiquidState(State):
    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print(f'我是液体，当前{str(water.get_temperature())}, 我很水~')


class GaseousState(State):
    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print(f'我是气体，当前{str(water.get_temperature())}, 我很飘~')


class TestWater(unittest.TestCase):
    def test_water(self):
        water = Water(LiquidState('液态'))
        water.behavior()
        water.set_temperature(-4)
        water.rise_temperature(18)
        water.behavior()
        water.rise_temperature(110)
        water.behavior()


if __name__ == '__main__':
    unittest.main()
