import asyncio
import time


async def get_html(sleep_times):
    print('start get url')
    await asyncio.sleep(sleep_times)
    print('done after {}s'.format(sleep_times))


if __name__ == '__main__':
    task1=get_html(3)
    task2=get_html(4)
    task3=get_html(4)

    tasks = [task1,task2,task3]

    loop=asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:  # 中途 ctrl+c 打断协程
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print('cancel task')
            print(task.cancel())
        loop.stop()
        loop.run_forever() # stop之后一定要再run_forever不然会报错

    finally:
        loop.close()

