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


def callback(future):
    print('send email to bobby')


if __name__ == '__main__':
    # 1.单任务
    # s = time.clock()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_html('http://www.baidu.com'))
    # print(time.clock() - s)
    #
    # print('-' * 30)

    # 2.任务列表
    # s = time.clock()
    # loop = asyncio.get_event_loop()
    # tasks = [get_html('http://www.baidu.com') for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))
    # print(time.clock() - s)

    # 3.获取协程的返回值
    s = time.clock()
    loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(get_html_with_ret('http://www.baidu.com'))
    # loop.run_until_complete(get_future)
    # print(get_future.result())
    # 或者使用task
    task = loop.create_task(get_html_with_ret('http://www.baidu.com'))
    task.add_done_callback(callback)  # 给task增加hook回调函数，任务完成后执行
    loop.run_until_complete(task)
    print(task.result())
    print(time.clock() - s)
