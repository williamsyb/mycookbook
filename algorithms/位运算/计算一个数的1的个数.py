# -*- coding UTF-8 -*-
# @project : mycookbook
# @Time    : 2020/8/21 12:28
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : 计算一个数的1的个数.py
# @Software: PyCharm


def count_bit(num: int) -> int:
    print(bin(num))
    count = 0
    while num:
        if num & 1 == 1:
            count += 1
        num = num >> 1
    return count


if __name__ == '__main__':
    print(count_bit(7))
