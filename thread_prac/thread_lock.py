from threading import Thread, Lock

lock01 = Lock()
lock02 = Lock()
li = list(range(1, 101))


def worker01(name, lock_a, lock_b):
    global li
    with lock_a:
        item = li.pop()
        print(f'{name} : {item}')


def worker02(name, lock):
    pass


if __name__ == '__main__':
    wa = Thread(target=worker01, args=('Thread A', lock01,))
    wb = Thread(target=worker01, args=('Thread B', lock02,))
