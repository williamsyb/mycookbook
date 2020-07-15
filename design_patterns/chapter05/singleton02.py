class Singleton(type):
    def __init__(cls, what, base=None, kwargs=None):
        super().__init__(what, base, kwargs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Custom(metaclass=Singleton):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


def delete_list(L, i):
    L_len = len(L)
    if i < L_len:
        del L[i]
        for k in range(i + 1, L_len - 1)[::1]:
            L[k] = L[k + 1]
    print(L)


if __name__ == '__main__':
    # tony = Custom('Tony')
    # karry = Custom('Karry')
    # print(tony.name, karry.name)
    # print(f'id(tony):{id(tony)}, id(karry):{id(karry)}')
    # print('tony==karry:', tony == karry)
    li = [1, 2, 3, 4, 5, 6]
    delete_list(li, 3)
