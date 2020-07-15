class Singleton1(object):
    _instance = None
    _is_first_inst = False

    def __new__(cls, name):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not self._is_first_inst:
            self.__name = name
            Singleton1._is_first_inst = True

    @property
    def name(self):
        return self.__name


if __name__ == '__main__':
    tony = Singleton1('Tony')
    karry = Singleton1('Karry')
    print(tony.name, karry.name)
    print(f'id(tony):{id(tony)}, id(karry):{id(karry)}')
    print('tony==karry:', tony == karry)
