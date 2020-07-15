import asyncio
import time


async def main1():
    print('hello')
    await asyncio.sleep(1)
    print('world')


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main2():
    print(f"started at {time.strftime('%X')}")

    await say_after(10, 'hello')
    print('------------')
    await say_after(10, 'world')

    print(f"finished at {time.strftime('%X')}")


async def main3():
    task1 = asyncio.create_task(
        say_after(10, 'hello'))
    print('------------')
    task2 = asyncio.create_task(
        say_after(10, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    print('+++++++++++++++++')
    await task2

    print(f"finished at {time.strftime('%X')}")


async def nested():
    print('nested start')
    return 42


async def main4():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    # nested()

    # Let's do it differently now and await it:
    print(await nested())


async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())
    print('-----1------')
    time.sleep(5)
    print('------2-----')
    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task
    print('------3-----')

if __name__ == '__main__':
    asyncio.run(main())
