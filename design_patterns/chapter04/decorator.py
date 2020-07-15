from abc import ABCMeta, abstractmethod
import unittest


class Person(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def wear(self):
        pass


class Engineer(Person):
    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    @property
    def skill(self):
        return self.__skill

    def wear(self):
        print('着装:')


class Teacher(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    @property
    def title(self):
        return self.__title

    def wear(self):
        print('着装:')


class ClothingDecorator(Person):
    def __init__(self, person):
        self.__decorator = person

    def wear(self):
        self.__decorator.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class CasualPantDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print('休闲便装')


class TshirtDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print('T-shirt')


class TestDecorator(unittest.TestCase):
    def test_water(self):
        engineer = Engineer('william', 'python')
        casual = CasualPantDecorator(engineer)
        tshirt = TshirtDecorator(casual)
        tshirt.wear()


if __name__ == '__main__':
    unittest.main()
