import asyncio
import time


async def get_html(utl):
    print('start get url')
    await asyncio.sleep(2)
    print('end get url')


async def get_html_with_ret(utl):
    print('start get url')
    await asyncio.sleep(2)
    print('end get url')
    return 'bobby'


if __name__ == '__main__':
    # 1.单任务
    # s = time.clock()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_html('http://www.baidu.com'))
    # print(time.clock() - s)
    #
    # print('-' * 30)

    # 2.任务列表
    s = time.clock()
    loop = asyncio.get_event_loop()
    tasks = [get_html('http://www.baidu.com') for i in range(10)]

    group1 = [get_html('http://www.baidu.com') for i in range(2)]
    group2 = [get_html('http://www.google.com') for i in range(2)]
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    loop.run_until_complete(asyncio.gather(group1, group2))
    print(time.clock() - s)
