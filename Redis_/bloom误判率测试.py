"""
基于redis布隆过滤器的误判率的测试
"""
import time
from redisbloom.client import Client
# pip install redisbloom
rb = Client(host='node01', port=6379)


def insert(size, key='book'):
    """插入数据"""
    # 一条条插入速度太慢了
    # for i in range(size):
    #     rb.bfAdd(key, f'book{i}')
    s = time.time()
    step = 1000  # 每次插入1000条数据
    for start in range(0, size, step):
        stop = start + step
        if stop >= size:
            stop = size
        rb.bfMAdd(key, *range(start, stop))
    print('插入结束... 花费时间: {:.4f}s'.format(time.time() - s))


def select(size, key='book'):
    """查询数据"""
    # 统计误判个数
    count = 0

    s = time.time()

    # 单条查询速度太慢了。。。
    # for i in range(size, size * 2):
    #     count += rb.bfExists(key, i)

    step = 1000  # 每次查1000条数据
    for start in range(size, size * 2, step):
        stop = start + step
        if stop >= size * 2:
            stop = size * 2
        count += rb.bfMExists(key, *range(start, stop)).count(1)  # 返回值[1, 0, 1, ...]统计1的个数
    print('size: {}, 误判元素个数: {}, 误判率{:.4%}'.format(size, count, count / size))
    print('查询结束... 花费时间: {:.4f}s'.format(time.time() - s))
    print('*' * 30)


def _test1(size, key='book'):
    """测试size个不存在的"""
    rb.delete(key)  # 先清空原来的key
    insert(size, key)
    select(size, key)


def _test2(size, error=0.001, key='book'):
    """指定误差率和初始大小的布隆过滤器"""
    rb.delete(key)

    rb.bfCreate(key, error, size)  # 误差率为0.1%， 初始个数为size

    insert(size, key)
    select(size, key)


if __name__ == '__main__':
    # The default error rate is 0.01 and the default initial capacity is 100.
    # 这个是默认的配置， 初始大小为100， 误差率默认为0.01
    _test1(1000)
    _test1(10000)
    _test1(100000)
    _test2(500000)