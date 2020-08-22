from .bitset import BitSet


class MyHash(object):
    def __init__(self, cap, seed):
        self.__cap = cap
        self.__seed = seed

    def hash(self, value:str):
        result:int = 0
        length:int = len(value)
        for i in range(length):
            result = self.__seed*result

class BloomFilter:
    def __init__(self):
        self.__SIZE = 2 << 10
        self.__num = [5, 19, 23, 31, 47, 71]
        self.__bits=BitSet(self.__SIZE)
        self.__function=[]

    def init(self):
        for i in range(len(self.__num)):
            self.__function.append(MyHash(self.__SIZE,self.__num[i]))

