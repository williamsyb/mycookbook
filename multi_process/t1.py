# -*- coding UTF-8 -*-
# @project : mycookbook
# @Time    : 2020/7/17 15:07
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : t1.py
# @Software: PyCharm

from multiprocessing.pool import Pool
from itertools import chain


def mul(x):
    return x*x

def pow3(y):
    return [y**3]

if __name__ == '__main__':
    pool = Pool(4)
    A=[]
    # for i in range(10):
        # pool.apply_async(mul, args=(i,), callback=A.append)

    pool.map_async(pow3, range(100), callback=A.extend)
    pool.close()
    pool.join()
    print(A)
    print(list(chain.from_iterable(A)))