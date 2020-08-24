import threading
import time


# 大致思路
# 获取对方的锁，运行一次后，释放自己的锁
def show1():
    for i in range(1, 52, 2):
        lock_show2.acquire()
        print(i, end='')
        print(i + 1, end=' ')
        time.sleep(0.2)
        lock_show1.release()


def show2():
    for i in range(26):
        lock_show1.acquire()
        print(chr(i + ord('A')))
        time.sleep(0.2)
        lock_show2.release()


lock_show1 = threading.Lock()
lock_show2 = threading.Lock()

show1_thread = threading.Thread(target=show1)
show2_thread = threading.Thread(target=show2)

lock_show1.acquire()  # 因为线程执行顺序是无序的，保证show1()先执行

show1_thread.start()

show2_thread.start()
